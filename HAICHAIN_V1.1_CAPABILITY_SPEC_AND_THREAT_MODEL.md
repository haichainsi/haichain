# HAICHAIN v1.1 Architecture Specification & Formal Threat Model
**Universal Autonomous Machine Financial Operating System**  
*Document Version: 1.1-Hardened (Post-Audit Remediation Standard)*  
*Target Blockchain: Solana L1 (High-Throughput SVM) with High-Frequency State Channels*  
*Authors: HAICHAIN Architecture Council & Core Engineering Working Group*

---

## 1. Executive Summary & Remediation Ledger

This document serves as the formal architectural specification for HAICHAIN v1.1, incorporating all forensic due-diligence findings from independent review (including external competitive analyses and threat modeling).

### Key Architectural Resolutions:
1. **Competitive Landscape Integration**: Formally positions HAICHAIN as the **Programmable Policy & Non-Custodial Vault Layer** operating on top of standard machine rails, seamlessly complementary to **HTTP x402** (Coinbase / Linux Foundation) and **Solana Pay.sh** (Solana Foundation x Google Cloud).
2. **Cryptographic Merchant ATA Recipient Binding**: Eliminates the "unbound recipient" vulnerability. Merkle capability leaves strictly bind the spending authority to a designated whitelisted merchant token account.
3. **Domain-Separated Micro-Voucher Protocol**: Mitigates cross-cluster, cross-contract, and cross-session replay attacks.
4. **SEC Howey Test De-risking**: Eliminates passive dividend ("Real Yield") claims in marketing and pre-seed collateral, standardizing strictly on **50% Programmatic Buyback & Burn + 50% Protocol Reserves (CHGB - Cryptographic Hardware Gas Bond)**.
5. **Multi-Vault Concurrency**: Clarifies that Solana Sealevel transaction parallelization operates across independent user Vault PDAs, completely avoiding global single-account lock contention.

---

## 2. Formal Cryptographic Capability Leaf Grammar

### 2.1 The 5-Tuple Capability Grammar
An autonomous AI sub-agent does not hold unfettered custody of user stablecoins. Spending authority is delegated strictly through a deterministic **5-Tuple Composite Capability Leaf** $\mathcal{L}$:

$$\text{InnerCapability} = \text{Keccak256}\Big(\text{SubAgentPubkey} \parallel \text{MaxSpendAmount}_{\text{LE64}} \parallel \text{ExpirySlot}_{\text{LE64}} \parallel \text{Nonce}_{\text{LE64}}\Big)$$

$$\mathcal{L} = \text{Keccak256}\Big(\text{InnerCapability} \parallel \text{WhitelistedMerchantATA}_{\text{Pubkey}}\Big)$$

### 2.2 Mathematical Security Guarantees
- **Signer Identity Binding**: Only the ephemeral keypair corresponding to $\text{SubAgentPubkey}$ can sign the capability execution transaction.
- **Strict Recipient Whitelist Binding**: Even if an LLM is hijacked via jailbreak prompt injection or indirect memory poisoning (e.g. ElizaOS framework exploits) to alter the recipient wallet address, the modified $\text{MerchantATA}$ produces an entirely different leaf hash:
  $$\mathcal{L}_{\text{Attacker}} \neq \mathcal{L}_{\text{Legitimate}}$$
  The Anchor program verification:
  ```rust
  let computed_leaf = anchor_lang::solana_program::keccak::hashv(&[
      &leaf_capability,
      ctx.accounts.service_provider_ata.key().as_ref(),
  ]).0;
  ```
  causes the Merkle path verification to immediately fail with `HaiChainMasterError::InvalidCapabilityProof`.

---

## 3. Comprehensive Threat Model & Loss Containment Bounds

### 3.1 Clarified System-Level Loss Bound (Beyond Single-Leaf)
In any decentralized capability architecture, evaluating security solely per-leaf understates total systemic exposure. We define the **Global Bounded Loss Guarantee**:

$$\text{WorstCaseSystemicLoss} \le \min\left(\text{VaultConfirmedBalance},\, \sum_{i \in \mathcal{U}} \text{MaxAuthorizedAmount}_i\right)$$

Where $\mathcal{U}$ represents the set of currently valid, unexpired, un-nullified capability tickets.

### 3.2 Dual-Layer Instant Revocation
1. **$O(1)$ Atomic Nonce Invalidation (`advance_min_valid_nonce`)**:
   When a user suspects key compromise across a swarm of sub-agents, the Master Owner invokes:
   $$\text{advance\_min\_valid\_nonce}(\text{NewMinNonce})$$
   The on-chain constraint:
   $$\text{require}!\left(\text{ticket.nonce} \ge \text{vault.min\_valid\_nonce},\, \text{NonceAlreadyReclaimed}\right)$$
   instantly renders all previous unspent tickets invalid in a single $O(1)$ transaction without requiring the regeneration or re-uploading of the Merkle tree.
2. **Sub-Second Hardware Panic Button (`trigger_emergency_panic`)**:
   Under an active attack, the Master Owner signs an emergency panic transaction:
   - Sets `vault.panic_kill_switch_tripped = true`.
   - Zeros `vault.confirmed_balance = 0`.
   - Executes an atomic CPI SPL transfer sweeping 100% of remaining USDT/USDC directly to the cold storage `user_safe_destination_ata`.
   - Reverts all future payment execution attempts with `HaiChainMasterError::VaultUnderPanicState`.

---

## 4. Off-Chain State Channel & Domain Separation Protocol

### 4.1 Micro-Voucher Structure
For high-frequency streaming payments (e.g., SSE token-by-token LLM inference @ $0.000004/token), off-chain micro-vouchers are signed by the agent:

$$\text{Payload} = \text{"haichain-v1-channel-settlement"} \parallel \text{ClusterID} \parallel \text{ProgramID} \parallel \text{VaultPDA} \parallel \text{ProviderPubkey} \parallel \text{SessionID} \parallel \text{Nonce} \parallel \text{CumulativeAmount}$$

$$\text{Signature} = \text{Ed25519Sign}_{\text{AgentKey}}(\text{SHA256}(\text{Payload}))$$

### 4.2 Anti-Replay Matrix
| Vector | Defense Mechanism | Invariant Check |
| :--- | :--- | :--- |
| **Cross-Cluster Replay** (Devnet $\to$ Mainnet) | `ClusterID` in payload (`"mainnet-beta"` vs `"devnet"`) | SHA256 digest divergence |
| **Cross-Provider Replay** (Merchant A $\to$ Merchant B) | `ProviderPubkey` in payload | Recipient public key mismatch |
| **Cross-Session Replay** (Session 1 $\to$ Session 2) | Unique monotonic `SessionID` | Ephemeral nullifier PDA uniqueness |
| **Cross-Program Replay** (Fake Contract Spoofing) | `ProgramID` in payload | Program address binding |
| **Concurrent Double-Spend** | Ephemeral Nullifier PDA initialized per nonce | `AccountAlreadyInitialized` on-chain collision |

---

## 5. Solana SVM Parallelism & Scalability Reality

### 5.1 Account Lock Contention Analysis
- **Myth**: Concurrent Merkle trees or multi-agent spending causes Sealevel parallel execution bottlenecks on Solana.
- **Reality in HAICHAIN**:
  - Each human master user owns an independent **`MasterAgentVault` PDA** derived from `[b"agent-vault", master_owner]`.
  - When Agent Swarm A (User 1) and Agent Swarm B (User 2) make payments, Solana Sealevel schedules them on **parallel CPU threads simultaneously**, because their respective account read/write sets are completely disjoint.
  - Serialization occurs only *within* a single user's vault, where atomic balance integrity is required.
  - Off-chain state channels compress 1,000 to 10,000 sub-cent interactions into a single net-settlement transaction, reducing L1 transaction frequency by 99.9%.

---

## 6. Howey Test Compliance & Sustainable Tokenomics

```
+----------------------------------------------------------------------------------------------------+
| INCOMING PROTOCOL MICRO-FEES (0.05% - 0.10% TAKE-RATE ON NET STATE CHANNEL SETTLEMENTS)            |
+----------------------------------------------------------------------------------------------------+
                                      |
                   +------------------+------------------+
                   |                                     |
                   v                                     v
       [50% PROGRAMMATIC BUYBACK & BURN]     [50% PROTOCOL TREASURY & CHGB BOND]
       * Automated AMM token retirement     * Underwrites Relayer gas insurance
       * Deflationary circulating supply    * Dispute resolution staking reserves
       * ZERO passive dividend payout       * Network security bounties
```

### Legal Assessment (US SEC & Global Regulatory Standard):
- **Prong 1 (Investment of Money)**: Tokens purchased on public DEX/CEX.
- **Prong 2 (Common Enterprise)**: Protocol is fully open-source and governed by decentralized ve-governance.
- **Prong 3 & 4 (Expectation of Profits Solely from Efforts of Others)**:
  - **Negated**: Token holders **receive zero passive dividends or cash-flow yield**.
  - Token value accrues strictly through deflationary supply reductions and utility necessity (relayer bonding, dispute arbitration, and fee discount tiers).
