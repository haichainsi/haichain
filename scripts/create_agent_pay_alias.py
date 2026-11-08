import os

os.makedirs('packages/agent-pay-python/haichain_agent_pay', exist_ok=True)

content = '''"""
HAICHAIN Agent Pay Python SDK (haichain_agent_pay alias)
Universal HTTP 402 Fast-Path Paywall & CapLeaf State Channel SDK for AI Agents and MCP Servers.
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
'''

with open('packages/agent-pay-python/haichain_agent_pay/__init__.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created packages/agent-pay-python/haichain_agent_pay/__init__.py")
