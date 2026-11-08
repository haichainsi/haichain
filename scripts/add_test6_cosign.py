with open('tests/haichain-phase2-ai-gateway.test.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the closing "  });\n});" with test 6
test6_code = """  it("6. [TEE COSIGNER CAPLEAF INVARIANT ENFORCEMENT]: Enforces valid TEE co-signature when REQUIRE_COSIGN flag is present", () => {
    const engine = new PolicyEngine(dummyAgentKeypair);
    const cosignerKeypair = Keypair.generate();

    // Create grant with REQUIRE_COSIGN flag
    const grantWithCosign: CapLeafV1 = {
      version: 1,
      pot: dummyPot,
      agent: dummyAgentKeypair.publicKey,
      merchant: dummyMerchant,
      mint: dummyMint,
      maxSpend: 10_000_000n,
      maxReserve: 2_000_000n,
      windowCap: 5_000_000n,
      windowSecs: 3600,
      scopeClass: CapScopeClass.DATA_API,
      scopeRef: Buffer.alloc(32, 0xaa),
      nonce: 888n,
      notBefore: 1_700_000_000n,
      expiry: 1_800_000_000n,
      epoch: 1,
      flags: CapLeafFlags.REQUIRE_COSIGN,
    };

    engine.registerActiveGrant(grantWithCosign);
    const leafBytes = CapLeafV1Engine.serialize(grantWithCosign);
    const leafHashHex = crypto.createHash("sha256").update(leafBytes).digest("hex");

    const channelId = 555n;
    const spendAmount = 100_000n;

    // Vector A: Attempt spend WITHOUT co-signature -> MUST FAIL CLOSED
    const intentWithoutCosign: PaymentIntent = {
      resource: "https://api.verified-partner.com/v1/search",
      maxAmount: spendAmount,
      merchant: dummyMerchant,
      mint: dummyMint,
      scopeClass: CapScopeClass.DATA_API,
    };

    expect(() => {
      engine.evaluateAndAuthorize(intentWithoutCosign, leafHashHex, channelId, 1_700_000_100);
    }).to.throw(/CapLeaf requires TEE Co-Signer attestation/);

    // Vector B: Attempt spend WITH FORGED co-signature -> MUST BE REJECTED
    const forgedCosignIntent: PaymentIntent = {
      ...intentWithoutCosign,
      cosignerPublicKey: cosignerKeypair.publicKey,
      cosignerSignature: new Uint8Array(64).fill(0xfe),
    };

    expect(() => {
      engine.evaluateAndAuthorize(forgedCosignIntent, leafHashHex, channelId, 1_700_000_100);
    }).to.throw(/TEE Co-Signer cryptographic verification failed/);

    // Vector C: Valid TEE Hardware Co-signature -> AUTHORIZED
    const cosignPayload = PolicyEngine.buildCosignPayload(dummyPot, dummyMerchant, channelId, spendAmount, 888n);
    const validCosig = nacl.sign.detached(cosignPayload, cosignerKeypair.secretKey);

    const validCosignIntent: PaymentIntent = {
      ...intentWithoutCosign,
      cosignerPublicKey: cosignerKeypair.publicKey,
      cosignerSignature: validCosig,
    };

    const authResult = engine.evaluateAndAuthorize(validCosignIntent, leafHashHex, channelId, 1_700_000_100);
    expect(authResult.authorizedAmount).to.equal(spendAmount);
    expect(authResult.signature).to.be.instanceOf(Uint8Array);
  });
});
"""

# Replace last closing "});"
idx = content.rfind("});")
content = content[:idx] + test6_code

with open('tests/haichain-phase2-ai-gateway.test.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added test 6 to tests/haichain-phase2-ai-gateway.test.ts")
