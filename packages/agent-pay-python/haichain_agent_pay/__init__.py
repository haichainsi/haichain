"""
HAICHAIN Agent Pay Python SDK (Package Alias)
Re-exports haichain_pay for developer convenience.
"""

from haichain_pay import (
    HaichainPaywall,
    haichain_paywall,
    HaichainASGIMiddleware,
    HaichainClient,
    AgentResponse,
    compute_voucher_hash,
    compute_x402_canonical_hash,
    verify_ed25519_signature,
    b58decode,
    b58encode,
)

__version__ = "0.1.0"
__all__ = [
    "HaichainPaywall",
    "haichain_paywall",
    "HaichainASGIMiddleware",
    "HaichainClient",
    "AgentResponse",
    "compute_voucher_hash",
    "compute_x402_canonical_hash",
    "verify_ed25519_signature",
    "b58decode",
    "b58encode",
]
