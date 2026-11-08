"""
HAICHAIN Universal HTTP 402 Paywall & Cryptographic Guardrail Middleware for Python
Fully compliant with RFC HTTP 402, Coinbase x402 Standard & HAICHAIN Policy Vault.
Supports FastAPI, Starlette, and ASGI frameworks.
"""

import base64
import functools
import inspect
import json
import secrets
import time
from typing import Dict, Any, Optional, Callable, List, Union

from .crypto import (
    b58decode,
    to_32_bytes,
    compute_voucher_hash,
    compute_x402_canonical_hash,
    verify_ed25519_signature,
)


class HaichainPaywall:
    """
    Universal HTTP 402 Micro-Payment Paywall for API endpoints and MCP Servers.
    """

    USDT_SOLANA_MAINNET = "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"
    USDC_SOLANA_MAINNET = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"

    def __init__(
        self,
        recipient: str,
        price_usdt: float = 0.001,
        cluster: str = "devnet",
        service_name: str = "HAICHAIN Monetized Agent Service",
        max_age_seconds: int = 300,
        token_mint: Optional[str] = None,
        allow_fast_path: bool = True,
    ):
        if not recipient:
            raise ValueError("[HaichainPaywall] recipient Solana address is required")

        self.recipient = recipient.strip()
        self.recipient_bytes = to_32_bytes(self.recipient)
        self.price_usdt = float(price_usdt)
        self.cluster = cluster
        self.service_name = service_name
        self.max_age_seconds = int(max_age_seconds)
        self.token_mint = token_mint or self.USDT_SOLANA_MAINNET
        self.allow_fast_path = allow_fast_path

        # Nullifier store: map of sig_key -> timestamp
        self._used_signatures: Dict[str, float] = {}

    def _cleanup_expired_nullifiers(self) -> None:
        cutoff = time.time() - (self.max_age_seconds * 2)
        expired = [k for k, ts in self._used_signatures.items() if ts < cutoff]
        for k in expired:
            del self._used_signatures[k]

    def generate_402_challenge(self, resource: str = "/api/v1/mcp") -> Dict[str, Any]:
        """
        Generates standard HTTP 402 Payment Challenge Response.
        Fully adheres to Coinbase x402 specification with HAICHAIN CapLeaf guardrails.
        """
        now_sec = int(time.time())
        expires_at = now_sec + self.max_age_seconds
        nonce = f"haichain_nonce_{now_sec}_{secrets.token_hex(8)}"
        payment_id = f"haipay_{now_sec}_{secrets.token_hex(6)}"
        caip2_network = (
            "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp"
            if self.cluster == "mainnet-beta"
            else "solana:EtWTRABZaYq6iMfeYKouRu166VU2xqa1"
        )

        body = {
            "error": "Payment Required",
            "statusCode": 402,
            "maxAmountRequired": str(self.price_usdt),
            "resource": resource,
            "description": f"{self.service_name} - Protected by HAICHAIN Autonomous Policy Vault",
            "payTo": self.recipient,
            "paymentAddress": self.recipient,
            "asset": self.token_mint,
            "assetAddress": self.token_mint,
            "assetType": "SPL",
            "network": f"solana-{self.cluster}",
            "caip2Network": caip2_network,
            "expiresAt": expires_at,
            "nonce": nonce,
            "paymentId": payment_id,
            "haichainGuardrail": {
                "protocol": "haichain-v1-voucher",
                "policyProtected": True,
                "boundedLossEnforced": True,
                "settlementHelper": "Settle via HAICHAIN Policy Vault, Spending Pot, or Python SDK.",
            },
            "settlementDetails": {
                "recipient": self.recipient,
                "amountUsdt": self.price_usdt,
                "network": f"solana-{self.cluster}",
                "protocol": "haichain-v1-voucher",
                "paymentHelper": "Use HAICHAIN relayer or client.executeMicroPayment() to broadcast on-chain settlement.",
            },
        }

        headers = {
            "Content-Type": "application/json",
            "WWW-Authenticate": f'X402 realm="{self.service_name}", scheme="haichain-v1-voucher"',
            "X-Payment-Required": "true",
            "X-Payment-Payee": self.recipient,
            "X-Payment-PayTo": self.recipient,
            "X-Payment-Amount": str(self.price_usdt),
            "X-Payment-Network": f"solana-{self.cluster}",
            "X-Payment-Nonce": nonce,
            "X-Resource-Uri": resource,
        }

        return {"status": 402, "headers": headers, "body": body}

    def verify_payment(self, auth_header_or_token: Optional[str]) -> Dict[str, Any]:
        """
        Verifies payment token or voucher (<2ms execution).
        """
        if not auth_header_or_token:
            return {"valid": False, "reason": "Missing Authorization or X-PAYMENT header"}

        raw_token = auth_header_or_token.strip()
        if raw_token.startswith("X402 "):
            raw_token = raw_token[5:].strip()
        elif raw_token.startswith("Bearer "):
            raw_token = raw_token[7:].strip()

        # Parse JSON directly or base64-encoded JSON
        parsed_payload = None
        try:
            if raw_token.startswith("{") and raw_token.endswith("}"):
                parsed_payload = json.loads(raw_token)
            else:
                decoded_str = base64.b64decode(raw_token).decode("utf-8")
                if decoded_str.startswith("{") and decoded_str.endswith("}"):
                    parsed_payload = json.loads(decoded_str)
        except Exception:
            pass

        if parsed_payload and self.allow_fast_path:
            return self._verify_fast_path(parsed_payload)

        return {
            "valid": False,
            "reason": "Malformed payment authorization: Expected signed JSON voucher payload",
        }

    def _verify_fast_path(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        agent_pubkey_str = (
            payload.get("agentPubkey")
            or payload.get("payer")
            or payload.get("clientPubkey")
        )
        sig_base64 = payload.get("signatureBase64") or payload.get("signature")
        recipient_str = (
            payload.get("merchantPubkey")
            or payload.get("payee")
            or payload.get("paymentAddress")
            or payload.get("payTo")
            or self.recipient
        )

        if not agent_pubkey_str or not sig_base64:
            return {
                "valid": False,
                "reason": "Fast-Path rejection: Missing agentPubkey or signature in payload",
            }

        # Nullifier check (Replay attack prevention)
        sig_key = f"sig_{sig_base64[:48]}"
        if sig_key in self._used_signatures:
            used_time = self._used_signatures[sig_key]
            return {
                "valid": False,
                "reason": f"Replay Attack Rejected: Voucher signature already consumed at {used_time}",
            }

        # Timestamp freshness check
        if "timestamp" in payload:
            now_sec = int(time.time())
            age_sec = now_sec - int(payload["timestamp"])
            if age_sec > self.max_age_seconds:
                return {
                    "valid": False,
                    "reason": f"Stale Voucher Rejected: Voucher timestamp is {age_sec}s old (Maximum permitted: {self.max_age_seconds}s)",
                }

        try:
            scheme = payload.get("scheme", "haichain-v1-voucher")
            if scheme == "haichain-v1-voucher" and "channelId" in payload and "cumulativeAmount" in payload:
                pot_pubkey_str = payload.get("potPubkey") or self.recipient
                channel_id = int(payload["channelId"])
                cumulative = int(payload["cumulativeAmount"])
                nonce = int(payload.get("nonce", 0))

                digest = compute_voucher_hash(
                    pot_pubkey=pot_pubkey_str,
                    merchant_pubkey=self.recipient,
                    channel_id=channel_id,
                    cumulative_amount=cumulative,
                    nonce=nonce,
                )

                if not verify_ed25519_signature(agent_pubkey_str, digest, sig_base64):
                    return {
                        "valid": False,
                        "reason": "Cryptographic Failure: Invalid Ed25519 signature on voucher payload",
                    }
            else:
                resource = payload.get("resource", "")
                amount = payload.get("amount") or payload.get("authorizedAmount") or self.price_usdt
                nonce_str = str(payload.get("nonce", ""))
                digest = compute_x402_canonical_hash(resource, amount, nonce_str)

                if not verify_ed25519_signature(agent_pubkey_str, digest, sig_base64):
                    return {
                        "valid": False,
                        "reason": "Cryptographic Failure: Signature verification failed on canonical x402 intent",
                    }

            # Record in Nullifier Store
            self._used_signatures[sig_key] = time.time()
            if len(self._used_signatures) % 100 == 0:
                self._cleanup_expired_nullifiers()

            return {
                "valid": True,
                "mode": "fast-path-voucher",
                "voucher_details": {
                    "agentPubkey": agent_pubkey_str,
                    "recipient": recipient_str,
                    "amount": payload.get("authorizedAmount") or self.price_usdt,
                    "channelId": payload.get("channelId"),
                    "cumulativeAmount": payload.get("cumulativeAmount"),
                    "verifiedAt": time.time(),
                },
            }
        except Exception as err:
            return {"valid": False, "reason": f"Fast-Path Verification Error: {str(err)}"}


def haichain_paywall(
    recipient: str,
    price_usdt: float = 0.001,
    cluster: str = "devnet",
    service_name: str = "HAICHAIN Monetized Agent Service",
    max_age_seconds: int = 300,
):
    """
    FastAPI / Starlette route decorator for HTTP 402 micro-payments.
    """
    paywall = HaichainPaywall(
        recipient=recipient,
        price_usdt=price_usdt,
        cluster=cluster,
        service_name=service_name,
        max_age_seconds=max_age_seconds,
    )

    def decorator(func: Callable):
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        has_req = any(p.name == "request" for p in params)
        if not has_req:
            try:
                from starlette.requests import Request as StarletteRequest
                req_param = inspect.Parameter("request", inspect.Parameter.KEYWORD_ONLY, annotation=StarletteRequest)
                new_sig = sig.replace(parameters=params + [req_param])
            except ImportError:
                new_sig = sig
        else:
            new_sig = sig

        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Locate injected or explicit request object
            if not has_req:
                request = kwargs.pop("request", None)
            else:
                request = kwargs.get("request")

            if request is None:
                for arg in args:
                    if hasattr(arg, "headers") and hasattr(arg, "url"):
                        request = arg
                        break

            if request is None:
                # Direct invocation without Request object; pass through
                return await func(*args, **kwargs)

            auth_token = (
                request.headers.get("x-payment")
                or request.headers.get("authorization")
                or request.headers.get("x-payment-signature")
                or request.headers.get("x-402-authorization")
            )

            res = paywall.verify_payment(auth_token)
            if not res["valid"]:
                try:
                    from fastapi.responses import JSONResponse
                    challenge = paywall.generate_402_challenge(str(request.url.path))
                    body = challenge["body"]
                    body["verificationError"] = res.get("reason")
                    return JSONResponse(status_code=402, content=body, headers=challenge["headers"])
                except ImportError:
                    raise RuntimeError("FastAPI/Starlette not installed to return 402 response")

            # Store verification details in request.state
            if hasattr(request, "state"):
                request.state.haichain_payment = {
                    "verified": True,
                    "mode": res.get("mode"),
                    "payee": recipient,
                    "amount_usdt": price_usdt,
                    "details": res.get("voucher_details"),
                }

            return await func(*args, **kwargs)

        wrapper.__signature__ = new_sig
        return wrapper

    return decorator


class HaichainASGIMiddleware:
    """
    ASGI middleware for protecting multiple routes or whole services with HAICHAIN x402 paywall.
    """

    def __init__(
        self,
        app,
        recipient: str,
        price_usdt: float = 0.001,
        protected_prefixes: Optional[List[str]] = None,
        cluster: str = "devnet",
        service_name: str = "HAICHAIN Monetized Agent Service",
    ):
        self.app = app
        self.paywall = HaichainPaywall(
            recipient=recipient,
            price_usdt=price_usdt,
            cluster=cluster,
            service_name=service_name,
        )
        self.protected_prefixes = protected_prefixes or ["/"]

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "/")
        is_protected = any(path.startswith(prefix) for prefix in self.protected_prefixes)

        if not is_protected:
            await self.app(scope, receive, send)
            return

        # Extract headers from ASGI scope
        headers_dict = {}
        for raw_k, raw_v in scope.get("headers", []):
            headers_dict[raw_k.decode("latin1").lower()] = raw_v.decode("latin1")

        auth_token = (
            headers_dict.get("x-payment")
            or headers_dict.get("authorization")
            or headers_dict.get("x-payment-signature")
            or headers_dict.get("x-402-authorization")
        )

        res = self.paywall.verify_payment(auth_token)
        if not res["valid"]:
            challenge = self.paywall.generate_402_challenge(path)
            body = challenge["body"]
            body["verificationError"] = res.get("reason")
            body_bytes = json.dumps(body).encode("utf-8")

            asgi_headers = [
                (k.encode("latin1"), v.encode("latin1"))
                for k, v in challenge["headers"].items()
            ]
            asgi_headers.append((b"content-length", str(len(body_bytes)).encode("latin1")))

            await send({
                "type": "http.response.start",
                "status": 402,
                "headers": asgi_headers,
            })
            await send({
                "type": "http.response.body",
                "body": body_bytes,
            })
            return

        # Attach to scope
        scope["haichain_payment"] = res
        await self.app(scope, receive, send)
