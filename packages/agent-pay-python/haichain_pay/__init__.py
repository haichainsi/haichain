"""
HAICHAIN Agent Pay Python SDK
Universal HTTP 402 Fast-Path Paywall & CapLeaf State Channel SDK for AI Agents and MCP Servers.
"""

from .crypto import (
    b58decode,
    b58encode,
    compute_voucher_hash,
    compute_x402_canonical_hash,
    verify_ed25519_signature,
)
from .client import HaichainClient
from .paywall import HaichainPaywall, haichain_paywall, HaichainASGIMiddleware

__version__ = "0.1.0"
__all__ = [
    "HaichainPaywall",
    "haichain_paywall",
    "HaichainASGIMiddleware",
    "HaichainClient",
    "compute_voucher_hash",
    "compute_x402_canonical_hash",
    "verify_ed25519_signature",
    "b58decode",
    "b58encode",
]
