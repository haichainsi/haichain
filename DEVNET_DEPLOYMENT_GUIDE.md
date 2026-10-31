# HAICHAIN: Solana Devnet Deployment & Operations Manual
**Universal Autonomous Machine Financial Operating System (Kernel v6.9.3)**

---

## 1. Generated Devnet Infrastructure

The automated orchestrator (`npm run deploy:devnet`) has prepared the official Devnet environment:

| Entity | Address / Identifier | Link / File |
| :--- | :--- | :--- |
| **Deployer Wallet** | `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | [View on Solana Explorer](https://explorer.solana.com/address/HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW?cluster=devnet) |
| **Program ID** | `DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk` | [View on Solana Explorer](https://explorer.solana.com/address/DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk?cluster=devnet) |
| **Master Vault PDA** | `FtqZDVdogfFweQxBwoXjZ62XQzbKeAs32umRVNQt4t8F` | Seeds: `[b"vault", deployerPubkey]` |
| **Sample Nullifier PDA** | `CyfEH4kT1TDK9wR2GhgMxWA9mhz8BPQqATLaDQVpNUz6` | Seeds: `[b"nullifier", vaultPda, nonce_1]` |
| **Deployer Keypair File** | `devnet-deployer.json` | Local private key (DO NOT COMMIT) |
| **Program Keypair File** | `devnet-program-keypair.json` | Local private key for program ID |
| **Deployment Manifest** | `devnet-deployment.json` | Complete cryptographic configuration |
| **Environment Profile** | `.env.devnet` | System variables for MCP & SDK |

---

## 2. Step-by-Step Deployment Instructions

### Step 1: Fund the Deployer Wallet with Devnet SOL
Solana Devnet requires ~1.5 to 2.5 SOL to cover bytecode account rent and transaction fees.
Because public RPC faucets are often closed or rate-limited, request free Devnet SOL from the official web faucet:

1. Open: **[https://faucet.solana.com](https://faucet.solana.com)** (or [https://solfaucet.com](https://solfaucet.com))
2. Enter Deployer Address: `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW`
3. Request **2 SOL**.

*(Alternatively, if you already have a funded Solana CLI wallet, run:*
`solana transfer HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW 2 --url devnet`)

---

### Step 2: Build sBPF Bytecode
Compile the Rust Anchor kernel into an optimized Solana BPF `.so` binary:

```bash
# Using standard Solana tools
cargo build-sbf

# Or using Anchor
anchor build
```

The compiled binary will be placed at:
`target/deploy/haichain_core.so`

---

### Step 3: Broadcast & Deploy to Solana Devnet
Deploy the contract to Devnet using the generated Program ID and Deployer Keypair:

```bash
solana program deploy \
  --program-id devnet-program-keypair.json \
  target/deploy/haichain_core.so \
  --url devnet \
  --keypair devnet-deployer.json
```

Once executed, Solana Explorer will confirm the active status:
`https://explorer.solana.com/address/DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk?cluster=devnet`

---

### Step 4: Run Post-Deployment Verification
Re-run the automated verification suite to confirm that the on-chain program and PDAs are active:

```bash
npm run deploy:devnet
```

---

## 3. Connecting SDK and MCP Server to Devnet

To connect your Claude Desktop, Cursor, or AI Agent to the newly deployed Devnet contract, update `.env` or your MCP server configuration:

```bash
SOLANA_RPC_URL="https://api.devnet.solana.com"
HAICHAIN_PROGRAM_ID="DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk"
```

All agent micro-escrows, Merkle tickets, and instant kill-switches will now settle directly on Solana Devnet.
