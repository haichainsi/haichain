# @haichainsi/mcp-server

Official **Model Context Protocol (MCP)** Server for **HAICHAIN**: The Universal Autonomous Machine Financial & Cognitive Operating System on Solana.

Connect your AI agents in **Claude Desktop**, **Cursor IDE**, and custom agent frameworks directly to on-chain Solana settlement vaults, autonomous spending pots, and emergency panic-retraction circuits.

---

## 🚀 Features

- **On-Chain Balance Inspection (`get_agent_spending_pot_balance`):** Inspect verified real-time balances in the Agent's Spending Pot (USDT & SOL on Solana).
- **Atomic Micro-Payments (`execute_micro_payment`):** Empower autonomous AI agents to execute fractional micro-payments for downstream APIs, inference tokens, and sub-agent task compensation.
- **Hardware-Speed Panic Kill-Switch (`trigger_emergency_panic`):** Instantly trip the emergency circuit breaker on Solana, freezing agent capabilities upon detecting prompt injections or anomalous behaviors.
- **Cross-Platform Zero-Config Keypair Resolution:** Automatically uses your existing Solana CLI keypair (`~/.config/solana/id.json`), custom `HAICHAIN_PRIVATE_KEY`, or generates a persistent local agent wallet in your user config directory.

---

## 📦 Installation & Quick Start

### Option 1: Run with `npx` (No installation needed)

Add the server to your MCP client configuration (Claude Desktop or Cursor) using `npx`:

```json
{
  "mcpServers": {
    "haichain": {
      "command": "npx",
      "args": ["-y", "@haichainsi/mcp-server"]
    }
  }
}
```

### Option 2: Run from Local Source (Developers)

```bash
# Clone the repository
git clone https://github.com/haichainsi/haichain.git
cd haichain/mcp-server

# Install dependencies & build
npm install
npm run build

# Start the server
npm start
```

---

## ⚙️ Configuration & Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `HAICHAIN_CLUSTER` | Solana cluster: `devnet` or `mainnet-beta` | `devnet` |
| `SOLANA_RPC_URL` | Custom Solana RPC endpoint | `https://api.devnet.solana.com` |
| `HAICHAIN_PRIVATE_KEY` | Agent Private Key (Base58, JSON array, or file path) | Auto-resolved from `~/.config/solana/id.json` or persistent agent wallet |

---

## 🖥️ Setup Guide

### 1. Claude Desktop Setup

Open your Claude Desktop configuration file:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the `haichain` server:

```json
{
  "mcpServers": {
    "haichain": {
      "command": "npx",
      "args": ["-y", "@haichainsi/mcp-server"],
      "env": {
        "HAICHAIN_CLUSTER": "devnet"
      }
    }
  }
}
```

Restart Claude Desktop. You will see the hammer icon 🔨 with HAICHAIN tools available!

---

### 2. Cursor IDE Setup

In your project root, create or edit `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "haichain": {
      "command": "npx",
      "args": ["-y", "@haichainsi/mcp-server"],
      "env": {
        "HAICHAIN_CLUSTER": "devnet"
      }
    }
  }
}
```

---

## 🛠️ Available MCP Tools

### 1. `get_agent_spending_pot_balance`
Inspects the live verified on-chain balance of the agent's spending pot.
* **Inputs:** `vaultAddress` (optional string)
* **Returns:** JSON object containing USDT balance, SOL balance, agent public key, status, and Solana Explorer link.

### 2. `execute_micro_payment`
Executes an atomic micro-payment on Solana for API consumption or sub-agent compensation.
* **Inputs:**
  * `amountUsdt` (number, required): Amount in USDT (e.g. `0.002` for $0.002).
  * `actionDescription` (string): Description of the task/inference.
  * `merchantRecipient` (string, optional): Merchant public key.
* **Returns:** Transaction signature, latency in ms, network fee, and Solana Explorer URL.

### 3. `trigger_emergency_panic`
Trips the emergency circuit breaker, freezing all agent spending capabilities.
* **Inputs:** `reason` (string, optional)
* **Returns:** Confirmed on-chain revocation memo and state status.

---

## 📄 License

Apache-2.0 © HAICHAIN Autonomous Machine Foundation.
