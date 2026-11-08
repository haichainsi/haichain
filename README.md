# HAICHAIN (v0.1.0-prototype)
### High-Velocity Autonomous Machine Financial Operating System (Solana Devnet Prototype)

> [!WARNING]
> **⚠️ DEVNET PROTOTYPE — UN-AUDITED — DO NOT DEPOSIT REAL FUNDS**
> This repository contains experimental software under active security research, protocol hardening, and developer preview. It has **NOT** completed an independent third-party audit. Do **NOT** deposit real funds on Solana mainnet. All token allocations, smart contracts, and settlement flows currently operate in test mode on **Solana Devnet**.

HAICHAIN is an open protocol providing fine-grained cryptographic spending firewalls and micro-payment state channels for Autonomous AI Agents and Model Context Protocol (MCP) servers built on **Solana L1**.

---

## 1. Core Capabilities & Architecture

1. **HTTP x402 Native Protocol Support:** Dual-path interoperability supporting standard Coinbase x402 JSON challenge/response alongside sub-2ms fast-path off-chain state channel vouchers with cryptographic ed25519 signatures.
2. **Deterministic Capability Tickets (CapLeaf v1):** 223-byte compact binary tickets enforcing strict per-merchant allowlists, per-transaction spend limits, sliding-window velocity caps, and scope restrictions to prevent prompt-injection drainage.
3. **Emergency Panic Kill-Switch & Epoch Invalidation:** Pot freeze mechanisms increment panic epoch on-chain, rendering all pre-panic off-chain vouchers immediately invalid against MEV searchers or rogue agents.
4. **Dispute Window & Nonce Replay Defense:** Unilateral channel close requires dispute window countdown, while deterministic PDA nullifiers prevent double-spend replay attacks.
5. **Zero-Commingling Dedicated ATAs:** Insulates against token-level blacklist freeze contagion by maintaining segregated token accounts per vault/channel.

---

## 2. Official Devnet Token Standard

* **Primary Settlement Asset:** **USDT (Tether SPL Token on Solana)**
* **Official Solana USDT Mint (Mainnet Reference):** `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`
* **Precision:** 6 Decimals (`1 USDT = 1,000,000 micro-units`)
* **Devnet Testing Program ID:** `DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk`

---

## 3. Repository Architecture

```
c:\Users\Surface\Documents\8. HAICHAIN\
├── app/
│   ├── index.html                  # Landing Page (Devnet Prototype)
│   └── dashboard.html              # Web3 Agent & Channel Dashboard
├── programs/
│   └── haichain-core/              # Solana Anchor Smart Contract (Rust)
│       ├── Cargo.toml
│       └── src/lib.rs              # Pot, CapLeaf, Channel Escrow, Panic & Dispute Invariants
├── packages/
│   └── agent-pay/                  # Dual-Path x402 Payment Interop Package
│       ├── src/index.ts
│       └── package.json
├── sdk/
│   ├── typescript/                 # Global Client SDK (x402 Protocol, PolicyEngine, CapLeaf)
│   │   ├── src/index.ts
│   │   └── package.json
│   └── c-edge/                     # Bare-Metal C-SDK (< 200KB RAM) for Robotics & IoT
│       ├── haichain_flash.h
│       └── haichain_flash.c
├── mcp-server/                     # Model Context Protocol Server (Claude & Cursor)
│   ├── src/index.ts
│   └── package.json
├── server/
│   └── production-agent-relayer.js # Relayer with Anti-SSRF Guard & Rate Limiting
├── tests/
│   ├── haichain-claude-audit-negative.test.ts # Negative Test Suite (Test Âm)
│   ├── haichain-x402-interoperability.test.ts # RFC-compliant x402 interop suite
│   ├── haichain-capleaf-v1-verification.test.ts # CapLeaf v1 wire verification
│   └── haichain-phase2-ai-gateway.test.ts     # AI Gateway & Policy Engine tests
├── Anchor.toml                     # Anchor Deployment Configuration
└── Cargo.toml                      # Workspace Cargo Configuration
```

---

## 4. Key Security Invariants

1. **Agent Authorization Invariant:** Channel reservations and child probation grant activations strictly require `agent == grant.agent`.
2. **Revocation & Panic Invariant:** Revoked grants or panicked pots (`frozen == true`, epoch mismatch) immediately invalidate pending vouchers.
3. **Dispute Window Invariant:** Unilateral channel close requires a 24-hour dispute countdown window (`dispute_secs`) before unspent funds can be reclaimed.
4. **Wormhole Sysvar Check Defense:** Canonical `sysvar::instructions` ID verification prevents instruction sysvar forgery.
5. **Anti-SSRF Guard:** Relayer strictly enforces HTTPS and blocks loopback (`127.0.0.1`, `localhost`), link-local, cloud metadata (`169.254.169.254`), and private RFC 1918 subnets (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
6. **Double-Spend Replay Defense:** Deterministic Nullifier PDAs ensure no nonce can ever be spent twice.

---

## 5. Verification & Test Execution

### Build Solana Anchor Smart Contract:
```bash
cd programs/haichain-core
cargo check
cargo test
```

### Run Full Test Suite (Unit, Interoperability, Negative Tests):
```bash
npm test
# Or run individual test suites:
npx ts-mocha tests/haichain-claude-audit-negative.test.ts
npx ts-mocha tests/haichain-x402-interoperability.test.ts
```

### Build Client SDKs:
```bash
cd sdk/typescript && npm run build
cd packages/agent-pay && npm run build
```

---
*Status: Devnet Testing Prototype (`v0.1.0-prototype`). Audit pending.*
