# @haichainsi/agent-pay

> **Universal HTTP 402 Paywall & Solana Micro-Escrow Middleware for AI Agents on Smithery, Fetch.ai, and MCP Servers.**

Monetize any AI Agent or MCP Server in 3 lines of code. Enable autonomous agents on the internet to pay your bot directly via Solana Devnet / Mainnet USDT micro-payments without credit cards or centralized payment processors.

---

## ⚡ 1-Minute Quick Start

```bash
npm install @haichainsi/agent-pay @solana/web3.js
```

### In Express / Node.js HTTP Server:

```javascript
const express = require('express');
const { haichainPaywall } = require('@haichainsi/agent-pay');

const app = express();

// Protect your agent's capability behind a $0.003 USDT micro-paywall
app.use('/api/extract', haichainPaywall({
  recipient: 'YOUR_SOLANA_WALLET_ADDRESS',
  priceUsdt: 0.003,
  cluster: 'devnet'
}));

app.post('/api/extract', (req, res) => {
  // Only executes AFTER client settles payment on Solana
  res.json({
    success: true,
    data: "High-value crawled web data or specialized AI inference"
  });
});

app.listen(3000);
```

### In Cloudflare Worker / Hono:

```javascript
import { HaichainPaywall } from '@haichainsi/agent-pay';

const paywall = new HaichainPaywall({
  recipient: 'YOUR_SOLANA_WALLET_ADDRESS',
  priceUsdt: 0.005,
  cluster: 'devnet'
});

export default {
  async fetch(request) {
    return await paywall.handleFetch(request, async () => {
      return new Response(JSON.stringify({ result: "Task completed" }), {
        headers: { 'Content-Type': 'application/json' }
      });
    });
  }
};
```

---

## 🔒 How It Works (HTTP 402 Flow)

```
1. Caller Agent ─── GET /api/extract ─────────────────► Monetized Agent Server
2. Caller Agent ◄── HTTP 402 Payment Required ──────── Monetized Agent Server
                    (X-Payment-Payee, X-Payment-Amount)
3. Caller Agent ─── Settle 0.003 USDT on Solana ──────► Solana L1 Escrow
4. Caller Agent ─── GET /api/extract + TxSig ─────────► Monetized Agent Server
5. Caller Agent ◄── HTTP 200 OK + Data ─────────────── Monetized Agent Server
```
