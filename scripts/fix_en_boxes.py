import unicodedata, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def display_width(s):
    w = 0
    for c in s:
        ea = unicodedata.east_asian_width(c)
        if ea in ('W', 'F'):
            w += 2
        else:
            w += 1
    return w

def fix_en():
    with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Box 2 (Line ~198): Billing Philosophy line has w=103
    old_b2 = '|  Billing Philosophy   Pay-to-Access (Forced Fixed Month)   Pay-per-Execution (Fractional Nano-cents)|'
    new_b2 = '|  Billing Philosophy   Pay-to-Access (Forced Fixed Month)  Pay-per-Execution (Fractional Nano-cents) |'
    text = text.replace(old_b2, new_b2)

    # 2. Box 4 (Mom-Test, Line ~321): lines are w=83 instead of 86
    old_b4 = """   |   [ 1. BIOMETRIC PASSKEY ] ───► [ 2. UNIVERSAL ON-RAMP ] ───► [ 3. SAFE POT ]   |
   |  - Apple FaceID / TouchID     - Apple Pay / Google Pay     - Isolated $10.00 |
   |  - WebAuthn Secure Enclave    - Instant QR / SEPA / Card   - Anti-Drain PDA  |
   |  - Zero Seed Phrases          - Zero Crypto Exchange KYC   - Circuit Breaker |"""
    
    new_b4 = """   |   [ 1. BIOMETRIC PASSKEY ] ───► [ 2. UNIVERSAL ON-RAMP ] ───► [ 3. SAFE POT ]   |
   |  - Apple FaceID / TouchID     - Apple Pay / Google Pay     - Isolated $10.00    |
   |  - WebAuthn Secure Enclave    - Instant QR / SEPA / Card   - Anti-Drain PDA     |
   |  - Zero Seed Phrases          - Zero Crypto Exchange KYC   - Circuit Breaker    |"""
    text = text.replace(old_b4, new_b4)

    # 3. Box 5 (Six Invariants, Line ~411): Make box 102 chars wide
    old_b5_pattern = r'\+---------------------------------------------------------------------------------\+\n\|               HAICHAIN v6\.9\.3 SIX INVARIANTS EXPLOIT DEFENSE MATRIX             \|\n\+---------------------------------------------------------------------------------\+\n.*?\+---------------------------------------------------------------------------------\+'
    new_b5 = """+----------------------------------------------------------------------------------------------------+
|                         HAICHAIN v6.9.3 SIX INVARIANTS EXPLOIT DEFENSE MATRIX                      |
+----------------------------------------------------------------------------------------------------+
| 1. INSTRUCTION SYSVAR INTROSPECTION (CVE-2022-24300 PREVENTION):                                   |
|   - Hardcoded Sysvar Instructions Pubkey: Sysvar1nstructions1111111111111111111111111             |
|   - Rejects spoofed sysvar addresses passed via arbitrary context accounts.                        |
|                                                                                                    |
| 2. NON-ZERO MERKLE ROOT & UNINITIALIZED PDA DEFENSE:                                               |
|   - Non-Zero Root Invariant: require!(composite_root != [0u8; 32])                                 |
|   - Eliminates vulnerabilities allowing execution against uninitialized roots.                     |
|                                                                                                    |
| 3. ELIZAOS PROMPT INJECTION DEFENSE:                                                               |
|   - 4-Tuple Bound Capability Leaf: Hash(Pubkey || MaxSpend || Expiry || Nonce)                     |
|   - Forbids poisoned agents from diverting funds to attacker wallets.                              |
|                                                                                                    |
| 4. LIVE SPL ATA BALANCE INTROSPECTION & ANTI-DRIFT GUARD:                                          |
|   - Strict ATA Balance Reload: require!(actual_ata_balance >= spend_amount)                        |
|   - Prevents internal accounting drift and donation-based exchange rate bugs.                      |
|                                                                                                    |
| 5. MULTI-SLOT FLASH-LOAN LIQUIDITY QUARANTINE:                                                     |
|   - Multi-Slot Quarantine: require!(slot >= last_deposit_slot + 2)                                 |
|   - Prevents flash-loan deposit-and-drain manipulation in the same block.                          |
|                                                                                                    |
| 6. TETHER USDT FREEZE DEFENSE:                                                                     |
|   - Segregated Vault ATAs: Each user vault maintains an isolated SPL ATA.                         |
|   - Zero cross-user contagion if third-party wallets face regulatory freeze.                       |
+----------------------------------------------------------------------------------------------------+"""
    text = re.sub(old_b5_pattern, new_b5, text, flags=re.DOTALL)

    # 4. Box 7 (Line ~1125): HAICHAIN SOVEREIGN MACHINE CONSENSUS L1
    old_b7 = """  +-------------------------------------------------------------------------+
  |             HAICHAIN SOVEREIGN MACHINE CONSENSUS L1 (HAI-VM)            |
  | - Bare-Metal OP_402_PAY Opcode: Frictionless Sub-cent Value Transfer   |
  | - Unified Human-Agent Soulbound DIDs: Cryptographic Accountability     |
  | - Sub-Second Deterministic Panic Retraction (< 400ms Emergency Vault)  |
  +-------------------------------------------------------------------------+"""
    new_b7 = """  +-------------------------------------------------------------------------+
  |             HAICHAIN SOVEREIGN MACHINE CONSENSUS L1 (HAI-VM)            |
  | - Bare-Metal OP_402_PAY Opcode: Frictionless Sub-cent Value Transfer    |
  | - Unified Human-Agent Soulbound DIDs: Cryptographic Accountability      |
  | - Sub-Second Deterministic Panic Retraction (< 400ms Emergency Vault)   |
  +-------------------------------------------------------------------------+"""
    text = text.replace(old_b7, new_b7)

    # 5. Box 8 (Roadmap, Line ~1269): Wrap long lines to fit exactly 102 chars
    old_b8_chunk = """|  Phase 1: Q4 2026  Solana L1 Mainnet Commercial Launch       v6.9.3 Hardened Kernel Deployment     |
|                    (Market Penetration & PMF)                Biometric WebAuthn Passkeys & On-Ramp |
|                                                              MCP Server for Cursor, Claude, LangChain|
|                                                              Formal Verification Completed; OtterSec & Neodyme Audits Scheduled Q4 2026|
|                                                                                                    |
|  Phase 2: Q2 2027  High-Throughput SVM App-Rollup            Dedicated SVM Sequencer Testnet       |
|                    (Ecosystem Expansion)                     Celestia / EigenDA DA Integration     |
|                                                              Symbiotic Knowledge Marketplace Launch|
|                                                              Reverse Micro-Tasking Protocol Active |
|                                                                                                    |
|  Phase 3: Q4 2027  HAICHAIN Sovereign Machine L1             HAI-VM Bare-Metal Testnet             |
|                    (The Superintelligence Endgame)           Native OP_402_PAY Opcode Engine       |
|                                                              Dual-Tier PoAW + PoAI Consensus       |
|                                                              1:1 SPL-to-Native $HAISI Teleport Bridge|
|                                                              100,000+ Machine TPS Verified         |"""

    new_b8_chunk = """|  Phase 1: Q4 2026  Solana L1 Mainnet Commercial Launch       v6.9.3 Hardened Kernel Deployment     |
|                    (Market Penetration & PMF)                Biometric WebAuthn Passkeys & On-Ramp |
|                                                              MCP Server for Cursor, Claude         |
|                                                              Formal Verification Completed         |
|                                                              OtterSec & Neodyme Audits (Q4 2026)   |
|                                                                                                    |
|  Phase 2: Q2 2027  High-Throughput SVM App-Rollup            Dedicated SVM Sequencer Testnet       |
|                    (Ecosystem Expansion)                     Celestia / EigenDA DA Integration     |
|                                                              Symbiotic Knowledge Marketplace Launch|
|                                                              Reverse Micro-Tasking Protocol Active |
|                                                                                                    |
|  Phase 3: Q4 2027  HAICHAIN Sovereign Machine L1             HAI-VM Bare-Metal Testnet             |
|                    (The Superintelligence Endgame)           Native OP_402_PAY Opcode Engine       |
|                                                              Dual-Tier PoAW + PoAI Consensus       |
|                                                              1:1 SPL-to-Native $HAISI Teleport     |
|                                                              100,000+ Machine TPS Verified         |"""
    text = text.replace(old_b8_chunk, new_b8_chunk)

    # 6. 3-Stage Evolutionary Trajectory (Line ~1020):
    old_traj = """   | - Micro-settlement Net |             | - Sequencer: HAICHAIN  |             | - Native OP_402_PAY    |
   | - 100k Agents / PMF    |             | - Gas Fee: $HAISI        |             | - Native DID & Credit  |
   | - Projected: $700k-1.4M ARR  |             | - 50,000+ Machine TPS  |             | - True Decentralized SI|"""
    new_traj = """   | - Micro-settlement Net |             | - Sequencer: HAICHAIN  |             | - Native OP_402_PAY    |
   | - 100k Agents / PMF    |             | - Gas Fee: $HAISI      |             | - Native DID & Credit  |
   | - Projected: $1.4M ARR |             | - 50,000+ Machine TPS  |             | - True Decentralized SI|"""
    text = text.replace(old_traj, new_traj)

    # 7. Box 3 (Competitor Matrix, Line ~250): fix lines that are 116, 118, 119, 125 chars
    old_b3_lines = [
        "|                       copycat mining; Closed-loop Model Autophagy      (PoAI) ingesting unpoisoned human ground    |",
        "| Virtuals Protocol     Single-threaded EVM write-lock contention on    Sealevel 32-partitioned ingestion ATAs;    |",
        "|                       $0.50); Speculative meme bonding curves         compression (771-byte datagram); Real utility|",
        "| Legacy Web2 Rails     $0.30 + 2.9% fixed fee floor (150,000% fee      Pure micro-utility ($0.000001 netted / $0.001 base);|",
        "| (Tools for Humanity)  passive UBI token distribution; Zero machine    integrated directly into the economic loop   |",
        "| (Coinbase / Linux Fdn/token limitation on Solana; Unconstrained client companion); Multi-delegate Merkle capability;|",
        "| Solana x Google Cloud)spending limits (V12 audit CVEs); Lacks on-chain Isolated PDA spending pots; Panic Circuit    |",
        "|                       circuit breakers & provider slashing mechanisms.Breaker sweeping in < 400ms; Bounded Loss.   |"
    ]
    new_b3_lines = [
        "|                       copycat mining; Closed-loop Model Autophagy     (PoAI) ingesting unpoisoned human ground     |",
        "| Virtuals Protocol     Single-threaded EVM write-lock contention on    Sealevel 32-partitioned ingestion ATAs;     |",
        "|                       $0.50); Speculative meme bonding curves         compression (771-byte datagram); Utility USDT|",
        "| Legacy Web2 Rails     $0.30 + 2.9% fixed fee floor (150,000% fee      Pure micro-utility ($0.000001 netted);       |",
        "| (Tools for Humanity)  passive UBI token distribution; Zero machine    integrated directly into the economic loop    |",
        "| (Coinbase / Linux Fdn/token limitation on Solana; Unconstrained client companion); Multi-delegate Merkle capability;|",
        "| Solana x Google Cloud)spending limits (V12 audit CVEs); Lacks on-chain Isolated PDA spending pots; Panic Circuit   |",
        "|                       circuit breakers & provider slashing mechanisms.Breaker sweeping in < 400ms; Bounded Loss.  |"
    ]
    for old_l, new_l in zip(old_b3_lines, new_b3_lines):
        text = text.replace(old_l, new_l)

    with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Applied all fixes to EN!")

if __name__ == '__main__':
    fix_en()
