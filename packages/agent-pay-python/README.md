# @haichainsi/agent-pay-python (haichain-agent-pay)

> **High-Velocity HTTP x402 Fast-Path Payment & CapLeaf State Channel SDK for Python AI Agents, FastAPI & MCP Servers**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Latency: Sub-millisecond](https://img.shields.io/badge/Voucher%20Verification-%3C0.3ms-brightgreen.svg)]()

## 🌟 Overview

`haichain-agent-pay` provides instantaneous off-chain payment authorization (<0.3ms) and dual-path settlement for autonomous AI agents, Anthropic Model Context Protocol (MCP) servers, LangChain tools, and DePIN API providers.

- **Fast-Path Verification (<0.3ms):** Validates Ed25519 cryptographic signatures on vouchers without waiting for Solana L1 slot confirmations.
- **Nullifier Store Replay Immunity:** Prevents replay attacks by invalidating already consumed vouchers.
- **FastAPI / Starlette Native:** Monetize endpoints in 3 lines of code using `@haichain_paywall`.
- **RFC HTTP 402 & Coinbase x402 Compliant:** Interoperable with autonomous agent wallets and MCP client inspectors.

---

## 📦 Installation

```bash
pip install haichain-agent-pay
# Or with FastAPI support:
pip install "haichain-agent-pay[fastapi]"
```

---

## 🚀 Quickstart: Monetize a FastAPI MCP Endpoint

```python
from fastapi import FastAPI, Request
from haichain_pay import haichain_paywall

app = FastAPI(title="Monetized Agent API")

MERCHANT_ADDRESS = "FiArjiLPRvU5wMEXeGwKTQfVSQiSTcxhmQwsEe2SzFRR"

@app.post("/api/v1/tools/search")
@haichain_paywall(
    recipient=MERCHANT_ADDRESS,
    price_usdt=0.003, # 0.003 USDT per invocation
    service_name="Deep Web Research MCP Tool"
)
async def research_tool(request: Request):
    payment_info = getattr(request.state, "haichain_payment", {})
    return {
        "status": "success",
        "result": "Research report generated...",
        "paid_by": payment_info.get("details", {}).get("agentPubkey")
    }
```

If a client calls `/api/v1/tools/search` without payment, the endpoint returns **HTTP 402 Payment Required** with standard x402 headers and settlement parameters.

---

## 🤖 Agent Client: Instant Micro-Payment Signing

```python
from haichain_pay import HaichainClient
import httpx

# Initialize client with local agent private key
client = HaichainClient()

# Generate signed voucher header
auth_header = client.build_auth_header(
    merchant_pubkey=MERCHANT_ADDRESS,
    amount_microunit=3000, # 0.003 USDT
    channel_id=1
)

# Make authenticated request
response = httpx.post(
    "http://localhost:8000/api/v1/tools/search",
    headers={"Authorization": auth_header}
)
print("Response:", response.json())
```

---

## 🛡️ Architecture & Security Model

```
+-------------------------------------------------------------+
|                      Autonomous AI Agent                    |
+-------------------------------------------------------------+
                               |
                   HTTP POST + Voucher Signature (<0.3ms)
                               v
+-------------------------------------------------------------+
|          FastAPI / Starlette Endpoint (@haichain_paywall)    |
|   1. Verify Ed25519 signature in-memory (< 0.3ms)            |
|   2. Check Nullifier Store against Replay Attack             |
|   3. Enforce 300s Freshness Window                           |
+-------------------------------------------------------------+
                               |
                  Periodic On-Chain Settlement
                               v
+-------------------------------------------------------------+
|          HAICHAIN Anchor Smart Contract on Solana L1         |
|   Instruction: settle_voucher / extend_channel_reserve      |
+-------------------------------------------------------------+
```

---

## 🧪 Running Tests

```bash
pytest packages/agent-pay-python/tests/
```
