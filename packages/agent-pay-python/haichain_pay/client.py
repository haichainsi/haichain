"""
HAICHAIN Autonomous Agent Client SDK
Enables AI Agents and MCP Clients to generate fast-path cryptographic micro-vouchers (< 1ms).
"""

import base64
import json
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


class HaichainClient:
    """
    Client for autonomous AI agents paying for APIs, MCP tools, and compute services.
    Manages local Ed25519 signing keys, channel nonces, and cumulative voucher balances.
    """

    def __init__(
        self,
        private_key: Optional[Union[str, bytes, nacl.signing.SigningKey]] = None,
        pot_pubkey: Optional[str] = None,
        default_channel_id: int = 1,
    ):
        if private_key is None:
            self._signing_key = nacl.signing.SigningKey.generate()
        elif isinstance(private_key, nacl.signing.SigningKey):
            self._signing_key = private_key
        elif isinstance(private_key, (bytes, bytearray)):
            self._signing_key = nacl.signing.SigningKey(bytes(private_key)[:32])
        elif isinstance(private_key, str):
            # Try base58 first, then base64
            try:
                raw = b58decode(private_key)
                self._signing_key = nacl.signing.SigningKey(raw[:32])
            except Exception:
                raw = base64.b64decode(private_key)
                self._signing_key = nacl.signing.SigningKey(raw[:32])
        else:
            raise TypeError("Unsupported private_key format")

        self.verify_key = self._signing_key.verify_key
        self.agent_pubkey_bytes = self.verify_key.encode()
        self.agent_pubkey = b58encode(self.agent_pubkey_bytes)

        self.pot_pubkey = pot_pubkey or self.agent_pubkey
        self.channel_id = default_channel_id
        self._channel_balances: Dict[str, int] = {}
        self._nonce_counter: int = 0

    def create_voucher(
        self,
        merchant_pubkey: str,
        amount_microunit: int,
        channel_id: Optional[int] = None,
        scheme: str = "haichain-v1-voucher",
        resource: str = "/api/v1/mcp",
    ) -> Dict[str, Any]:
        """
        Creates and cryptographically signs a micro-payment voucher.
        Returns a dictionary suitable for JSON serialization into an HTTP header.
        """
        cid = channel_id if channel_id is not None else self.channel_id
        chan_key = f"{cid}_{merchant_pubkey}"
        current_cumulative = self._channel_balances.get(chan_key, 0)
        new_cumulative = current_cumulative + int(amount_microunit)
        self._channel_balances[chan_key] = new_cumulative

        self._nonce_counter += 1
        nonce = int(time.time()) * 1000 + (self._nonce_counter % 1000)

        if scheme == "haichain-v1-voucher":
            voucher_hash = compute_voucher_hash(
                pot_pubkey=self.pot_pubkey,
                merchant_pubkey=merchant_pubkey,
                channel_id=cid,
                cumulative_amount=new_cumulative,
                nonce=nonce,
            )
            sig = self._signing_key.sign(voucher_hash).signature
            sig_b64 = base64.b64encode(sig).decode("ascii")

            payload = {
                "scheme": "haichain-v1-voucher",
                "agentPubkey": self.agent_pubkey,
                "merchantPubkey": merchant_pubkey,
                "potPubkey": self.pot_pubkey,
                "channelId": str(cid),
                "cumulativeAmount": str(new_cumulative),
                "authorizedAmount": amount_microunit,
                "nonce": str(nonce),
                "signatureBase64": sig_b64,
                "timestamp": int(time.time()),
            }
        else:
            # Coinbase x402 fallback detached format
            canonical_hash = compute_x402_canonical_hash(resource, amount_microunit, str(nonce))
            sig = self._signing_key.sign(canonical_hash).signature
            sig_b64 = base64.b64encode(sig).decode("ascii")

            payload = {
                "scheme": "x402-detached",
                "agentPubkey": self.agent_pubkey,
                "merchantPubkey": merchant_pubkey,
                "resource": resource,
                "authorizedAmount": amount_microunit,
                "nonce": str(nonce),
                "signatureBase64": sig_b64,
                "timestamp": int(time.time()),
            }

        return payload

    def build_auth_header(
        self,
        merchant_pubkey: str,
        amount_microunit: int,
        channel_id: Optional[int] = None,
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
        json_bytes = json.dumps(payload).encode("utf-8")
        encoded = base64.b64encode(json_bytes).decode("ascii")
        return f"X402 {encoded}"
