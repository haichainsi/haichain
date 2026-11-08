#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

sdk_path = 'sdk/typescript/src/index.ts'
with open(sdk_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """  public async handleX402Challenge(
    headers: X402PaymentRequestHeaders,
    agentPrivateKey: Uint8Array,
    whitelistedProviders: PublicKey[]
  ): Promise<X402PaymentAuthorizationHeaders> {
    const payTo = new PublicKey(headers["X-402-PayTo"]);
    const isWhitelisted = whitelistedProviders.some(p => p.equals(payTo));
    
    if (!isWhitelisted) {
      throw new Error("SECURITY ALERT: Destination provider is not whitelisted. ElizaOS Memory Poisoning blocked!");
    }

    const authSignature = `x402_sig_${Buffer.from(agentPrivateKey.slice(0, 16)).toString("hex")}_${headers["X-402-Nonce"]}`;

    return {
      "X-402-Authorization": authSignature,
      "X-402-Payer-Vault": "AgentVaultPda11111111111111111111111111111111",
      "X-402-Timestamp": new Date().toISOString(),
    };
  }"""

new_block = """  /**
   * Handles HTTP x402 Payment Challenge with strict destination whitelist verification
   * and dynamically derived Payer Vault PDA.
   */
  public async handleX402Challenge(
    headers: X402PaymentRequestHeaders,
    agentPrivateKey: Uint8Array,
    whitelistedProviders: PublicKey[],
    vaultOwner?: PublicKey
  ): Promise<X402PaymentAuthorizationHeaders> {
    const payTo = new PublicKey(headers["X-402-PayTo"]);
    const isWhitelisted = whitelistedProviders.some(p => p.equals(payTo));
    
    if (!isWhitelisted) {
      throw new Error("SECURITY ALERT: Destination provider is not whitelisted. ElizaOS Memory Poisoning blocked!");
    }

    const authSignature = `x402_sig_${Buffer.from(agentPrivateKey.slice(0, 16)).toString("hex")}_${headers["X-402-Nonce"]}`;

    // Derive canonical Agent Vault PDA from vaultOwner, or fallback to Keypair public key
    let payerVaultStr: string;
    if (vaultOwner) {
      payerVaultStr = this.getAgentVaultPda(vaultOwner)[0].toBase58();
    } else {
      const derivedPubkey = Keypair.fromSecretKey(agentPrivateKey).publicKey;
      payerVaultStr = this.getAgentVaultPda(derivedPubkey)[0].toBase58();
    }

    return {
      "X-402-Authorization": authSignature,
      "X-402-Payer-Vault": payerVaultStr,
      "X-402-Timestamp": new Date().toISOString(),
    };
  }

  /**
   * Computes the 5-Tuple Cryptographic Composite Capability Leaf.
   * Cryptographically binds the authorized Sub-Agent to a specific Whitelisted Merchant Token Account (ATA).
   * Enforced on-chain by haichain-core Anchor smart contract to eliminate prompt injection / memory poisoning theft.
   */
  public static computeCompositeCapabilityLeaf(
    subAgentSigner: PublicKey,
    whitelistedMerchantAta: PublicKey,
    maxAuthorizedAmount: bigint | number,
    expirySlot: bigint | number,
    nonce: bigint | number
  ): Buffer {
    const amountBuf = Buffer.alloc(8);
    const expiryBuf = Buffer.alloc(8);
    const nonceBuf = Buffer.alloc(8);

    amountBuf.writeBigUInt64LE(BigInt(maxAuthorizedAmount));
    expiryBuf.writeBigUInt64LE(BigInt(expirySlot));
    nonceBuf.writeBigUInt64LE(BigInt(nonce));

    const capPayload = Buffer.concat([
      subAgentSigner.toBuffer(),
      amountBuf,
      expiryBuf,
      nonceBuf,
    ]);
    const leafCapability = crypto.createHash("sha256").update(capPayload).digest();

    return crypto.createHash("sha256").update(
      Buffer.concat([leafCapability, whitelistedMerchantAta.toBuffer()])
    ).digest();
  }

  /**
   * Generates cryptographic payload for State Channel Micro-Voucher signing with full Domain Separation.
   * Prevents cross-cluster, cross-contract, cross-provider, and cross-session replay attacks.
   */
  public static buildVoucherSigningPayload(
    clusterId: "mainnet-beta" | "devnet" | "testnet",
    programId: PublicKey,
    vaultPda: PublicKey,
    providerPubkey: PublicKey,
    sessionId: string,
    nonce: number | bigint,
    cumulativeAmount: number | bigint
  ): Buffer {
    const DOMAIN_SEPARATOR = "haichain-v1-channel-settlement";
    const payloadStr = `${DOMAIN_SEPARATOR}:${clusterId}:${programId.toBase58()}:${vaultPda.toBase58()}:${providerPubkey.toBase58()}:${sessionId}:${nonce.toString()}:${cumulativeAmount.toString()}`;
    return crypto.createHash("sha256").update(payloadStr).digest();
  }"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(sdk_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated sdk/typescript/src/index.ts successfully")
else:
    print("Old block not found in sdk/typescript/src/index.ts")
