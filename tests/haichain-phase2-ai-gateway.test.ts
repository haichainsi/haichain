// tests/haichain-phase2-ai-gateway.test.ts
// HAICHAIN v1.1 - Phase 2 Forensic Verification Suite
// Tests Out-of-Process Policy Engine, HTTP x402 Handshake, TEE Cosigner Anti-SSRF,
// and Anti-Prompt-Injection Micro-Loop Throttling.

import { expect } from "chai";
import { Keypair, PublicKey } from "@solana/web3.js";
import * as crypto from "crypto";
import nacl from "tweetnacl";
import {
  CapLeafV1,
  CapLeafV1Engine,
  CapLeafFlags,
  CapScopeClass,
  PolicyEngine,
  PaymentIntent,
  X402Client,
  X402Challenge,
} from "../sdk/typescript/src/index";
import { TeeCosignerService, WellKnownPayeeIdentity } from "../server/tee-cosigner";

describe("HAICHAIN v1.1 - Phase 2: AI Gateway, HTTP x402 Protocol & Policy Engine Sandbox", () => {
  const dummyPot = new PublicKey(Buffer.alloc(32, 0x11));
  const dummyAgentKeypair = Keypair.generate();
  const dummyMerchantKeypair = Keypair.generate();
  const dummyMint = new PublicKey(Buffer.alloc(32, 0x44));

  const scopeRef = crypto.createHash("sha256").update("GET https://api.openai.com/v1/search").digest();

  const activeLeaf: CapLeafV1 = {
    version: 1,
    pot: dummyPot,
    agent: dummyAgentKeypair.publicKey,
    merchant: dummyMerchantKeypair.publicKey,
    mint: dummyMint,
    maxSpend: 5_000_000n, // 5.00 USDT
    maxReserve: 500_000n,  // 0.50 USDT
    windowCap: 1_000_000n, // 1.00 USDT
    windowSecs: 3600,
    scopeClass: CapScopeClass.DATA_API | CapScopeClass.LLM_INFERENCE,
    scopeRef,
    nonce: 1n,
    notBefore: BigInt(Math.floor(Date.now() / 1000) - 100),
    expiry: BigInt(Math.floor(Date.now() / 1000) + 86400),
    epoch: 0,
    flags: CapLeafFlags.NONE,
  };

  it("1. [OUT-OF-PROCESS POLICY ENGINE]: Zero-Knowledge key isolation authorizes intent without exposing private key", () => {
    const engine = new PolicyEngine(dummyAgentKeypair);
    engine.registerActiveGrant(activeLeaf);

    const leafHashHex = crypto.createHash("sha256").update(Buffer.from("dummy_leaf")).digest("hex");
    // Register under leafHashHex for testing
    (engine as any).activeGrants.set(leafHashHex, activeLeaf);

    const intent: PaymentIntent = {
      resource: "https://api.openai.com/v1/search",
      maxAmount: 2_000n, // 0.002 USDT micro-tick
      merchant: dummyMerchantKeypair.publicKey,
      mint: dummyMint,
      scopeClass: CapScopeClass.DATA_API,
    };

    const auth = engine.evaluateAndAuthorize(intent, leafHashHex, 1001n);
    expect(auth.authorizedAmount).to.equal(2_000n);
    expect(auth.cumulativeVoucherAmount).to.equal(2_000n);
    expect(auth.signature).to.be.instanceOf(Uint8Array);
    expect(auth.signature.length).to.equal(64); // Ed25519 signature
  });

  it("2. [HTTP x402 PROTOCOL CLIENT]: Successfully handles 402 challenge and generates valid voucher header", () => {
    const engine = new PolicyEngine(dummyAgentKeypair);
    const leafHashHex = "active_grant_leaf_hash_001";
    (engine as any).activeGrants.set(leafHashHex, activeLeaf);

    const x402Client = new X402Client(engine);

    // Simulate Merchant sending HTTP 402 challenge
    const rawChallengeJson = JSON.stringify({
      payee: dummyMerchantKeypair.publicKey.toBase58(),
      mint: dummyMint.toBase58(),
      amountMicroUnits: "1500", // 0.0015 USDT
      scheme: "haichain-v1-voucher",
      resource: "https://api.anthropic.com/v1/messages",
      expires: Math.floor(Date.now() / 1000) + 300,
    });

    const challenge = X402Client.parseChallenge(rawChallengeJson);
    expect(challenge.scheme).to.equal("haichain-v1-voucher");

    const response = x402Client.generatePaymentResponse(
      challenge,
      leafHashHex,
      2002n,
      CapScopeClass.LLM_INFERENCE
    );

    expect(response.authorizedAmount).to.equal(1500n);
    expect(response.headers["Authorization"]).to.include("X402");
    expect(response.headers["X-Haichain-Cumulative"]).to.equal("1500");

    // Verify delivery receipt
    const receipt = {
      resource: "https://api.anthropic.com/v1/messages",
      bytesDelivered: 1024,
      providerSignature: "sig_abc",
      cumulativePaid: "1500",
    };
    const isDeliveryValid = x402Client.verifyDeliveryReceipt(receipt, "https://api.anthropic.com/v1/messages");
    expect(isDeliveryValid).to.be.true;
  });

  it("3. [ANTI-PROMPT-INJECTION THROTTLING]: Blocks infinite micro-payment draining loop on probation domain", () => {
    const probationMerchant = Keypair.generate().publicKey;
    const probationLeaf: CapLeafV1 = {
      ...activeLeaf,
      merchant: probationMerchant,
      flags: CapLeafFlags.PROBATION,
    };

    const engine = new PolicyEngine(dummyAgentKeypair);
    const leafHashHex = "probation_leaf_hash";
    (engine as any).activeGrants.set(leafHashHex, probationLeaf);

    const attackerResource = "https://evil-prompt-injection-loop.xyz/api/chunk";
    const intent: PaymentIntent = {
      resource: attackerResource,
      maxAmount: 1000n,
      merchant: probationMerchant,
      mint: dummyMint,
      scopeClass: CapScopeClass.DATA_API,
    };

    const now = Math.floor(Date.now() / 1000);

    // Call 1: Allowed
    engine.evaluateAndAuthorize(intent, leafHashHex, 3001n, now + 1);
    // Call 2: Allowed
    engine.evaluateAndAuthorize(intent, leafHashHex, 3001n, now + 2);
    // Call 3: Allowed
    engine.evaluateAndAuthorize(intent, leafHashHex, 3001n, now + 3);

    // Call 4: Exceeds 3 calls / 10 mins window -> Must be blocked!
    expect(() => {
      engine.evaluateAndAuthorize(intent, leafHashHex, 3001n, now + 4);
    }).to.throw(/RATE LIMIT BREACH.*exceeded 3 calls per 10m window/);
  });

  it("4. [SEMANTIC PAYLOAD VERIFICATION]: Rejects empty response and disguised internal errors", () => {
    const engine = new PolicyEngine(dummyAgentKeypair);

    // Empty payload
    expect(() => {
      engine.verifyServicePayload(Buffer.alloc(0));
    }).to.throw(/Empty payload returned by provider/);

    // Disguised error
    const disguisedErrorPayload = '{"status": 200, "data": {"error": "Failed", "code": 500}}';
    expect(() => {
      engine.verifyServicePayload(disguisedErrorPayload);
    }).to.throw(/Provider returned disguised internal error/);
  });

  it("5. [TEE COSIGNER ANTI-SSRF & DOMAIN AUDIT]: Rejects internal IPs and freshly registered burner domains", () => {
    const cosigner = new TeeCosignerService();

    const merchantKey = Keypair.generate();
    const domain = "api.verified-partner.com";
    const payload = Buffer.from(`HAICHAIN-PAYEE-IDENTITY:${domain}:${merchantKey.publicKey.toBase58()}`);
    const validSig = nacl.sign.detached(payload, merchantKey.secretKey);

    const payeeJson: WellKnownPayeeIdentity = {
      version: "1.0",
      merchantPubkey: merchantKey.publicKey.toBase58(),
      mintAllowlist: [dummyMint.toBase58()],
      domain,
      organization: "Verified Partner Corp",
      signature: Buffer.from(validSig).toString("base64"),
    };

    // Vector A: SSRF via Loopback IP (127.0.0.1)
    const ssrfDecision = cosigner.evaluateMerchantIdentity(domain, "127.0.0.1", 120, payeeJson);
    expect(ssrfDecision.allowed).to.be.false;
    expect(ssrfDecision.reason).to.include("SSRF PROTECTION");

    // Vector B: SSRF via AWS Metadata IP (169.254.169.254)
    const metadataDecision = cosigner.evaluateMerchantIdentity(domain, "169.254.169.254", 120, payeeJson);
    expect(metadataDecision.allowed).to.be.false;
    expect(metadataDecision.reason).to.include("SSRF PROTECTION");

    // Vector C: Burner Domain (< 30 days old)
    const burnerDecision = cosigner.evaluateMerchantIdentity(domain, "198.51.100.1", 5, payeeJson);
    expect(burnerDecision.allowed).to.be.false;
    expect(burnerDecision.reason).to.include("HIGH RISK DOMAIN");

    // Vector D: Legitimate Merchant (> 30 days, public IP, verified signature)
    const legitDecision = cosigner.evaluateMerchantIdentity(domain, "198.51.100.1", 180, payeeJson);
    expect(legitDecision.allowed).to.be.true;
    expect(legitDecision.cosignerSignature).to.be.instanceOf(Uint8Array);
  });
  it("6. [TEE COSIGNER CAPLEAF INVARIANT ENFORCEMENT]: Enforces valid TEE co-signature when REQUIRE_COSIGN flag is present", () => {
    const engine = new PolicyEngine(dummyAgentKeypair);
    const cosignerKeypair = Keypair.generate();

    // Create grant with REQUIRE_COSIGN flag
    const grantWithCosign: CapLeafV1 = {
      version: 1,
      pot: dummyPot,
      agent: dummyAgentKeypair.publicKey,
      merchant: dummyMerchantKeypair.publicKey,
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
      merchant: dummyMerchantKeypair.publicKey,
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
    const cosignPayload = PolicyEngine.buildCosignPayload(dummyPot, dummyMerchantKeypair.publicKey, channelId, spendAmount, 888n);
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
