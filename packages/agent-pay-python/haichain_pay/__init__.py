"""
HAICHAIN Agent Pay Python SDK
Universal HTTP 402 Fast-Path Paywall, CapLeaf State Channels & 1-Click Financial Firewall for AI Agents.
"""

from .crypto import (
    b58decode,
    b58encode,
    compute_voucher_hash,
    compute_x402_canonical_hash,
    verify_ed25519_signature,
)
from .client import HaichainClient, AgentResponse
from .paywall import HaichainPaywall, haichain_paywall, HaichainASGIMiddleware
from .firewall import (
    HaiChainFirewall,
    firewall,
    haichain_firewall,
    BudgetExceededException,
    PromptInjectionAnomalyException,
)

__version__ = "0.2.0"
__all__ = [
    "HaiChainFirewall",
    "firewall",
    "haichain_firewall",
    "BudgetExceededException",
    "PromptInjectionAnomalyException",
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
