# @haichainsi/sdk

> **HAICHAIN**: Universal Autonomous Machine Financial Operating System Client SDK for TypeScript / Node.js.

[![npm version](https://img.shields.io/npm/v/@haichainsi/sdk.svg)](https://www.npmjs.com/package/@haichainsi/sdk)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Solana Devnet](https://img.shields.io/badge/Solana-Devnet-green.svg)](https://explorer.solana.com/address/DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk?cluster=devnet)

Official TypeScript SDK for interacting with the **HAICHAIN Protocol** on Solana. Provides high-level abstractions for autonomous AI agents, programmatic micro-escrow streams, x402 payment headers, SLA bonded providers, and cross-chain intent settlement.

---

## 📦 Installation

```bash
npm install @haichainsi/sdk @solana/web3.js @coral-xyz/anchor
```

Or using `yarn` / `pnpm`:

```bash
pnpm add @haichainsi/sdk @solana/web3.js @coral-xyz/anchor
```

---

## 🚀 Quick Start

### 1. Initialize Client

```typescript
import { Connection, PublicKey } from "@solana/web3.js";
import { HaiChainClient } from "@haichainsi/sdk";

const connection = new Connection("https://api.devnet.solana.com", "confirmed");
const programId = new PublicKey("DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk");

const client = new HaiChainClient(connection, programId);
console.log("HAICHAIN SDK initialized successfully!");
```

### 2. Create Fiat / Crypto Deposit Session

```typescript
const session = await client.createUsdtDepositSession({
  userUid: "user_agent_001",
  amountUsdt: 5.0,
  preferredRail: "apple_pay"
});

console.log("Deposit Address (Solana SPL):", session.depositAddressSolanaSpl);
console.log("Checkout URL:", session.checkoutUrlFiat);
```

### 3. HTTP x402 Micropayment Header Generator

Easily integrate autonomous agent payments into API calls:

```typescript
// Construct standard X-402 challenge headers
const paymentHeaders = {
  "X-402-PayTo": "provider_ata_address_here",
  "X-402-Amount": "1000", // 0.001 USDT (1 Action Credit)
  "X-402-Nonce": "random_crypto_nonce"
};
```

---

## 🏛️ Core Architectural Pillars

1. **SLA Staked Provider Bonds & Slashing Invariants:** Cryptographic proof verification and penalty slashing for faulty data.
2. **Hybrid Web2 to DePIN Fallback Router:** Seamless failover to decentralized compute/data when Web2 providers deplatform.
3. **Cross-Chain Intent-based Solver Mesh:** Gasless, instant execution across Base/EVM and Solana with zero bridge delay.
4. **Dynamic Spot Tickets & Micro-Auctions:** Real-time capacity pricing based on network saturation.
5. **Enterprise Rollup Invoicing:** Big 4 audit-ready VAT/GST invoices backed by Merkle roots.

---

## 🔗 Resources

- **Official Website:** [haichain.si](https://haichain.si)
- **Developer Documentation:** [haichain.si/dashboard?tab=mcp](https://haichain.si/dashboard?tab=mcp)
- **Model Context Protocol Server:** [@haichainsi/mcp-server](https://www.npmjs.com/package/@haichainsi/mcp-server)
- **Whitepaper:** [haichain.si/whitepaper.html](https://haichain.si/whitepaper.html)

---

## 📄 License

Apache-2.0 © HAICHAIN Foundation
