with open('sdk/typescript/src/policy-engine.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update PaymentIntent interface
old_intent = """export interface PaymentIntent {
  resource: string;
  maxAmount: bigint;
  merchant: PublicKey;
  mint: PublicKey;
  scopeClass: number;
}"""

new_intent = """export interface PaymentIntent {
  resource: string;
  maxAmount: bigint;
  merchant: PublicKey;
  mint: PublicKey;
  scopeClass: number;
  cosignerSignature?: Uint8Array;
  cosignerPublicKey?: PublicKey;
}"""

content = content.replace(old_intent, new_intent)

# 2. Add buildCosignPayload helper
old_method = """  public static buildVoucherPayload("""
new_methods = """  public static buildCosignPayload(
    potPubkey: PublicKey,
    merchantPubkey: PublicKey,
    channelId: bigint,
    amount: bigint,
    nonce: bigint
  ): Buffer {
    const channelBuf = Buffer.alloc(8);
    const amountBuf = Buffer.alloc(8);
    const nonceBuf = Buffer.alloc(8);
    channelBuf.writeBigUInt64LE(channelId);
    amountBuf.writeBigUInt64LE(amount);
    nonceBuf.writeBigUInt64LE(nonce);

    return crypto.createHash("sha256")
      .update(Buffer.from("HAICHAIN-TEE-COSIGN-V1"))
      .update(potPubkey.toBuffer())
      .update(merchantPubkey.toBuffer())
      .update(channelBuf)
      .update(amountBuf)
      .update(nonceBuf)
      .digest();
  }

  public static buildVoucherPayload("""

content = content.replace(old_method, new_methods)

# 3. Add TEE Co-Signer check inside evaluateAndAuthorize
# Look for where domain rate limit is enforced or amount check
target_insertion = """    // 5. Amount check
    const currentCumulative = this.cumulativeSpendPerChannel.get(channelId.toString()) || 0n;"""

new_cosign_check = """    // 4b. TEE Co-Signer Invariant Enforcement (bit REQUIRE_COSIGN)
    if ((grant.flags & CapLeafFlags.REQUIRE_COSIGN) !== 0) {
      if (!intent.cosignerSignature || !intent.cosignerPublicKey) {
        throw new Error("SECURITY ALERT: CapLeaf requires TEE Co-Signer attestation, but no co-signature was provided");
      }
      const cosignPayload = PolicyEngine.buildCosignPayload(grant.pot, grant.merchant, channelId, intent.maxAmount, grant.nonce);
      const isCosignValid = nacl.sign.detached.verify(
        cosignPayload,
        intent.cosignerSignature,
        intent.cosignerPublicKey.toBytes()
      );
      if (!isCosignValid) {
        throw new Error("SECURITY ALERT: TEE Co-Signer cryptographic verification failed");
      }
    }

    // 5. Amount check
    const currentCumulative = this.cumulativeSpendPerChannel.get(channelId.toString()) || 0n;"""

content = content.replace(target_insertion, new_cosign_check)

with open('sdk/typescript/src/policy-engine.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sdk/typescript/src/policy-engine.ts with TEE Co-Signer enforcement.")
