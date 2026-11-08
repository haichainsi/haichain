"""
HAICHAIN Autonomous Agent Client SDK
Enables AI Agents and MCP Clients to generate fast-path cryptographic micro-vouchers (< 1ms).
"""

from __future__ import annotations
import base64
import json as _json
import secrets
import time
from typing import Dict, Any, Optional, Union
import nacl.signing

from .crypto import (
    b58encode,
    b58decode,
    to_32_bytes,
    compute_voucher_hash,
    compute_x402_canonical_hash,
)


class AgentResponse:
    """
    HTTP Response wrapper returned by HaichainClient.call_paid_agent.
    """

    def __init__(
        self,
        status_code: int,
        content: bytes,
        headers: Dict[str, str],
        voucher_used: Optional[Dict[str, Any]] = None,
    ):
        self.status_code = status_code
        self.content = content
        self.headers = headers
        self.voucher_used = voucher_used

    def json(self) -> Any:
        return _json.loads(self.content.decode("utf-8"))

    @property
    def text(self) -> str:
        return self.content.decode("utf-8")

    def __repr__(self) -> str:
        return f"<AgentResponse [{self.status_code}]>"


class HaichainClient:
    """
    Client for autonomous AI agents paying for APIs, MCP tools, and compute services.
    Manages local Ed25519 signing keys, channel nonces, and cumulative voucher balances.
    """

    def __init__(
        self,
        private_key: Optional[Union[str, bytes, nacl.signing.SigningKey]] = None,
        pot_pubkey: Optional[str] = None,
        cluster: str = "devnet",
    ):
        """
        Initializes the agent client.
        :param private_key: Base58 or 32/64-byte raw private key. Generates a new keypair if None.
        :param pot_pubkey: Optional on-chain Pot (Vault) public key.
        :param cluster: 'devnet' or 'mainnet-beta'.
        """
        self.cluster = cluster
        if private_key is None:
            self.signing_key = nacl.signing.SigningKey.generate()
        elif isinstance(private_key, nacl.signing.SigningKey):
            self.signing_key = private_key
        elif isinstance(private_key, str):
            seed = to_32_bytes(b58decode(private_key))
            self.signing_key = nacl.signing.SigningKey(seed)
        elif isinstance(private_key, (bytes, bytearray)):
            seed = to_32_bytes(bytes(private_key))
            self.signing_key = nacl.signing.SigningKey(seed)
        else:
            raise TypeError("Unsupported private_key format")

        self.verify_key = self.signing_key.verify_key
        self.agent_pubkey = b58encode(bytes(self.verify_key))
        self.pot_pubkey = pot_pubkey or self.agent_pubkey
        self._nonces: Dict[str, int] = {}
        self._cumulative_balances: Dict[str, int] = {}

    def get_next_nonce(self, merchant_pubkey: str) -> int:
        cur = self._nonces.get(merchant_pubkey, 0)
        self._nonces[merchant_pubkey] = cur + 1
        return cur + 1

    def create_voucher(
        self,
        merchant_pubkey: str,
        amount_microunit: int,
        channel_id: int = 1,
        scheme: str = "haichain-v1-voucher",
        resource: str = "/api/v1/mcp",
    ) -> Dict[str, Any]:
        """
        Creates and signs a cryptographically verifiable Haichain fast-path micro-voucher.
        Execution takes < 0.2ms.
        """
        prev_balance = self._cumulative_balances.get(merchant_pubkey, 0)
        new_balance = prev_balance + amount_microunit
        self._cumulative_balances[merchant_pubkey] = new_balance

        nonce = self.get_next_nonce(merchant_pubkey)
        now = int(time.time())

        # 32-byte digest
        voucher_digest = compute_voucher_hash(
            pot_pubkey=self.pot_pubkey,
            merchant_pubkey=merchant_pubkey,
            channel_id=channel_id,
            cumulative_amount=new_balance,
            nonce=nonce,
        )

        signed_payload = self.signing_key.sign(voucher_digest)
        sig_raw = signed_payload.signature
        sig_b58 = b58encode(sig_raw)
        sig_b64 = base64.b64encode(sig_raw).decode("ascii")

        return {
            "scheme": scheme,
            "version": "1.0",
            "cluster": self.cluster,
            "potPubkey": self.pot_pubkey,
            "merchantPubkey": merchant_pubkey,
            "agentPubkey": self.agent_pubkey,
            "channelId": channel_id,
            "cumulativeAmount": str(new_balance),
            "amountMicrounit": amount_microunit,
            "nonce": nonce,
            "timestamp": now,
            "resource": resource,
            "signature": sig_b58,
            "signatureBase64": sig_b64,
            "signer": self.agent_pubkey,
        }

    def build_auth_header(
        self,
        merchant_pubkey: str,
        amount_microunit: int,
        channel_id: int = 1,
        scheme: str = "haichain-v1-voucher",
        resource: str = "/api/v1/mcp",
    ) -> str:
        """
        Generates standard 'X402 <base64_payload>' HTTP Authorization header.
        """
        payload = self.create_voucher(
            merchant_pubkey=merchant_pubkey,
            amount_microunit=amount_microunit,
            channel_id=channel_id,
            scheme=scheme,
            resource=resource,
        )
        json_bytes = _json.dumps(payload).encode("utf-8")
        encoded = base64.b64encode(json_bytes).decode("ascii")
        return f"X402 {encoded}"

    def call_paid_agent(
        self,
        url: str,
        method: str = "POST",
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Union[bytes, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: float = 30.0,
    ) -> AgentResponse:
        """
        Autonomously invokes a monetized agent endpoint.
        If the endpoint returns HTTP 402 Payment Required, this method automatically:
        1. Parses the RFC 402 challenge details (payTo recipient, price).
        2. Signs an Ed25519 fast-path micro-voucher locally.
        3. Attaches the cryptographic voucher and re-submits the request.
        """
        import urllib.request
        import urllib.error

        req_headers = {
            "User-Agent": "HAICHAIN-Agent-Client/1.0",
            "Accept": "application/json",
        }
        if headers:
            req_headers.update(headers)

        body_bytes = None
        if json is not None:
            body_bytes = _json.dumps(json).encode("utf-8")
            req_headers["Content-Type"] = "application/json"
        elif data is not None:
            body_bytes = data.encode("utf-8") if isinstance(data, str) else data

        req = urllib.request.Request(url, data=body_bytes, headers=req_headers, method=method)

        voucher_used = None
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                resp_bytes = resp.read()
                resp_headers = dict(resp.headers)
                return AgentResponse(resp.status, resp_bytes, resp_headers)
        except urllib.error.HTTPError as http_err:
            if http_err.code == 402:
                # 402 Challenge received -> auto-resolve
                challenge_bytes = http_err.read()
                challenge_headers = {k.lower(): v for k, v in dict(http_err.headers).items()}
                challenge_data = {}
                try:
                    challenge_data = _json.loads(challenge_bytes.decode("utf-8"))
                except Exception:
                    pass

                recipient = (
                    challenge_data.get("payTo")
                    or challenge_data.get("paymentAddress")
                    or challenge_data.get("recipient")
                    or (challenge_data.get("settlementDetails") or {}).get("recipient")
                    or challenge_headers.get("x-payment-payee")
                    or challenge_headers.get("x-payment-payto")
                )
                if not recipient:
                    raise RuntimeError(
                        f"HTTP 402 received but unable to parse recipient address from challenge: {challenge_data}"
                    )

                price_raw = (
                    challenge_data.get("maxAmountRequired")
                    or challenge_data.get("amountUsdt")
                    or challenge_data.get("priceUsdt")
                    or (challenge_data.get("settlementDetails") or {}).get("amountUsdt")
                    or challenge_headers.get("x-payment-amount")
                    or 0.003
                )
                try:
                    amount_microunit = int(float(price_raw) * 1_000_000)
                except Exception:
                    amount_microunit = 3_000

                # Sign voucher
                auth_header = self.build_auth_header(
                    merchant_pubkey=recipient,
                    amount_microunit=amount_microunit,
                    resource=url,
                )
                voucher_used = {
                    "merchant": recipient,
                    "amountMicrounit": amount_microunit,
                    "agent": self.agent_pubkey,
                }

                # Retry request with signed voucher
                req_headers["Authorization"] = auth_header
                retry_req = urllib.request.Request(url, data=body_bytes, headers=req_headers, method=method)
                try:
                    with urllib.request.urlopen(retry_req, timeout=timeout) as retry_resp:
                        return AgentResponse(
                            retry_resp.status,
                            retry_resp.read(),
                            dict(retry_resp.headers),
                            voucher_used,
                        )
                except urllib.error.HTTPError as retry_err:
                    return AgentResponse(
                        retry_err.code,
                        retry_err.read(),
                        dict(retry_err.headers),
                        voucher_used,
                    )
            else:
                return AgentResponse(http_err.code, http_err.read(), dict(http_err.headers))
