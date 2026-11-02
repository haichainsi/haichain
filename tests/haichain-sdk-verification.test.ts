// tests/haichain-sdk-verification.test.ts
import { expect } from "chai";
import { Keypair, PublicKey } from "@solana/web3.js";
import { HaiChainClient, PROTOCOL_CONSTANTS, SOLANA_USDT_MINT, SOLANA_USDC_MINT } from "../sdk/typescript/src/index";
import { keccak_256 } from "@noble/hashes/sha3";

describe("HAICHAIN Phase 1 Audit: Cryptographic Leaf & Voucher Payload Verification", () => {
  it("1. [KECCAK LEAF PARITY]: computeCompositeCapabilityLeaf strictly matches on-chain Anchor keccak logic", () => {
    const subAgent = Keypair.generate().publicKey;
    const merchantAta = Keypair.generate().publicKey;
    const maxAmount = 5_000_000n; // 5.00 USDT
    const expirySlot = 120_000n;
    const nonce = 1n;

    // SDK calculation
    const sdkLeaf = HaiChainClient.computeCompositeCapabilityLeaf(
      subAgent,
      merchantAta,
      maxAmount,
      expirySlot,
      nonce
    );

    // Independent manual calculation simulating Anchor solana_program::keccak::hashv
    const amountBuf = Buffer.alloc(8);
    const expiryBuf = Buffer.alloc(8);
    const nonceBuf = Buffer.alloc(8);
    amountBuf.writeBigUInt64LE(maxAmount);
    expiryBuf.writeBigUInt64LE(expirySlot);
    nonceBuf.writeBigUInt64LE(nonce);

    const manualInnerHash = Buffer.from(
      keccak_256(Buffer.concat([subAgent.toBuffer(), amountBuf, expiryBuf, nonceBuf]))
    );
    const manualCompositeLeaf = Buffer.from(
      keccak_256(Buffer.concat([manualInnerHash, merchantAta.toBuffer()]))
    );

    expect(sdkLeaf.equals(manualCompositeLeaf)).to.be.true;
    expect(sdkLeaf.length).to.equal(32);
  });

  it("2. [RECIPIENT BINDING]: Substituting merchant ATA changes the leaf hash completely", () => {
    const subAgent = Keypair.generate().publicKey;
    const legitimateMerchant = Keypair.generate().publicKey;
    const attackerMerchant = Keypair.generate().publicKey;

    const leaf1 = HaiChainClient.computeCompositeCapabilityLeaf(subAgent, legitimateMerchant, 1000n, 100n, 1n);
    const leaf2 = HaiChainClient.computeCompositeCapabilityLeaf(subAgent, attackerMerchant, 1000n, 100n, 1n);

    expect(leaf1.equals(leaf2)).to.be.false;
  });

  it("3. [DOMAIN SEPARATION]: Micro-voucher payload contains Domain Separator and cluster ID", () => {
    const programId = Keypair.generate().publicKey;
    const vaultPda = Keypair.generate().publicKey;
    const providerPubkey = Keypair.generate().publicKey;

    const payloadDevnet = HaiChainClient.buildVoucherSigningPayload(
      "devnet",
      programId,
      vaultPda,
      providerPubkey,
      "session_abc",
      1n,
      500n
    );

    const payloadMainnet = HaiChainClient.buildVoucherSigningPayload(
      "mainnet-beta",
      programId,
      vaultPda,
      providerPubkey,
      "session_abc",
      1n,
      500n
    );

    // Cross-cluster signature replay is mathematically impossible
    expect(payloadDevnet.equals(payloadMainnet)).to.be.false;
    expect(payloadDevnet.length).to.equal(32);
  });

  it("4. [OFF-CHAIN PROOF VERIFICATION PARITY]: verifyCompositeProof accurately validates Merkle proof matching on-chain Anchor logic", () => {
    // Construct a 2-leaf Merkle tree with sorted pair hashing
    const subAgent = Keypair.generate().publicKey;
    const merchantAta = Keypair.generate().publicKey;
    const leafA = HaiChainClient.computeCompositeCapabilityLeaf(subAgent, merchantAta, 1000n, 200n, 1n);
    const leafB = HaiChainClient.computeCompositeCapabilityLeaf(subAgent, merchantAta, 2000n, 300n, 2n);

    // Compute root with sorted pair logic
    let root: Buffer;
    if (Buffer.compare(leafA, leafB) <= 0) {
      root = Buffer.from(keccak_256(Buffer.concat([leafA, leafB])));
    } else {
      root = Buffer.from(keccak_256(Buffer.concat([leafB, leafA])));
    }

    // Proof for leafA is [leafB]
    const proofForA = [leafB];
    const isValid = HaiChainClient.verifyCompositeProof(leafA, proofForA, root);
    expect(isValid).to.be.true;

    // Proof for leafB is [leafA]
    const proofForB = [leafA];
    const isValidB = HaiChainClient.verifyCompositeProof(leafB, proofForB, root);
    expect(isValidB).to.be.true;

    // Tampered leaf or proof fails
    const tamperedLeaf = Buffer.from(leafA);
    tamperedLeaf[0] ^= 0xff;
    const isTamperedValid = HaiChainClient.verifyCompositeProof(tamperedLeaf, proofForA, root);
    expect(isTamperedValid).to.be.false;
  });

  it("5. [ED25519 VOUCHER SIGNING & VERIFICATION]: Produces valid cryptographic signature and blocks tampering", () => {
    const agentKeypair = Keypair.generate();
    const programId = Keypair.generate().publicKey;
    const vaultPda = Keypair.generate().publicKey;
    const providerPubkey = Keypair.generate().publicKey;

    const voucherArgs = {
      clusterId: "mainnet-beta" as const,
      programId,
      vaultPda,
      providerPubkey,
      sessionId: "session_agent_99",
      nonce: 1n,
      cumulativeAmount: 50_000n,
    };

    const { payloadHash, signature, signatureBase64 } = HaiChainClient.signMicroVoucher(
      agentKeypair,
      voucherArgs
    );

    expect(signature.length).to.equal(64); // Standard Ed25519 64-byte signature
    expect(signatureBase64).to.be.a("string");

    // Verification succeeds with correct signer
    const isValid = HaiChainClient.verifyMicroVoucherSignature(
      agentKeypair.publicKey,
      payloadHash,
      signature
    );
    expect(isValid).to.be.true;

    // Verification fails if signer is substituted (imposter attack)
    const attackerKeypair = Keypair.generate();
    const isAttackerValid = HaiChainClient.verifyMicroVoucherSignature(
      attackerKeypair.publicKey,
      payloadHash,
      signature
    );
    expect(isAttackerValid).to.be.false;

    // Verification fails if amount is altered by malicious provider (inflation attack)
    const alteredPayloadHash = HaiChainClient.buildVoucherSigningPayload(
      "mainnet-beta",
      programId,
      vaultPda,
      providerPubkey,
      "session_agent_99",
      1n,
      100_000n // altered amount!
    );
    const isAlteredValid = HaiChainClient.verifyMicroVoucherSignature(
      agentKeypair.publicKey,
      alteredPayloadHash,
      signature
    );
    expect(isAlteredValid).to.be.false;
  });
  it("6. [ANCHOR DISCRIMINATOR & INSTRUCTION SERIALIZATION PARITY]: Verifies Anchor discriminators and writable account invariants", () => {
    const client = new HaiChainClient(null as any);
    const masterOwner = Keypair.generate().publicKey;
    const dedicatedAta = Keypair.generate().publicKey;
    const safeDestination = Keypair.generate().publicKey;

    // 1. Verify Panic instruction discriminator matches sha256("global:trigger_emergency_panic")[0..8]
    const panicIx = client.buildTriggerPanicInstruction(masterOwner, dedicatedAta, safeDestination);
    expect(panicIx.data.length).to.equal(8);
    const expectedPanicDisc = Buffer.from([232, 177, 104, 97, 82, 33, 17, 191]);
    expect(panicIx.data.equals(expectedPanicDisc)).to.be.true;

    // 2. Verify Reclaim Nullifier instruction discriminator, u64 LE nonce, and isWritable=true on vault
    const testNonce = 123456789n;
    const reclaimIx = client.buildReclaimNullifierInstruction(masterOwner, testNonce);
    expect(reclaimIx.data.length).to.equal(16); // 8 bytes disc + 8 bytes u64 LE nonce
    const expectedReclaimDisc = Buffer.from([16, 165, 146, 96, 207, 57, 80, 93]);
    expect(reclaimIx.data.subarray(0, 8).equals(expectedReclaimDisc)).to.be.true;
    expect(reclaimIx.data.readBigUInt64LE(8)).to.equal(testNonce);

    // Invariant: agentVaultPda MUST be writable because vault.min_valid_nonce is modified
    const vaultAccountMeta = reclaimIx.keys[1];
    expect(vaultAccountMeta.isWritable).to.be.true;

    // 3. Verify Advance Nonce instruction discriminator and serialization
    const advanceIx = client.buildAdvanceMinValidNonceInstruction(masterOwner, 9999n);
    expect(advanceIx.data.length).to.equal(16);
    const expectedAdvanceDisc = Buffer.from([81, 92, 116, 233, 79, 68, 222, 129]);
    expect(advanceIx.data.subarray(0, 8).equals(expectedAdvanceDisc)).to.be.true;
    expect(advanceIx.data.readBigUInt64LE(8)).to.equal(9999n);

    // 4. Verify Update Composite Root instruction discriminator and 32-byte payload
    const newRoot = Buffer.alloc(32, 0xaa);
    const updateRootIx = client.buildUpdateCompositeRootInstruction(masterOwner, newRoot);
    expect(updateRootIx.data.length).to.equal(40); // 8 bytes disc + 32 bytes root
    const expectedRootDisc = Buffer.from([230, 8, 5, 238, 82, 121, 117, 97]);
    expect(updateRootIx.data.subarray(0, 8).equals(expectedRootDisc)).to.be.true;
    expect(updateRootIx.data.subarray(8).equals(newRoot)).to.be.true;
  });
  it("7. [PROTOCOL LIFECYCLE INSTRUCTIONS & INVARIANT CONSTANTS]: Verifies initialize, deposit, execute payment, and constants", () => {
    // 1. Verify on-chain invariant constants parity
    expect(PROTOCOL_CONSTANTS.FLASH_LOAN_QUARANTINE_SLOTS).to.equal(2n);
    expect(PROTOCOL_CONSTANTS.MIN_QUARANTINE_TRIGGER_DEPOSIT).to.equal(1_000_000n);
    expect(PROTOCOL_CONSTANTS.ROOT_ROTATION_GRACE_SLOTS).to.equal(150n);
    expect(PROTOCOL_CONSTANTS.MAX_SAFE_MICRO_TICK_PAYMENT).to.equal(50_000_000n);
    expect(PROTOCOL_CONSTANTS.MIN_PROVIDER_BOND_AMOUNT).to.equal(20_000_000n);

    const client = new HaiChainClient(null as any);
    const masterOwner = Keypair.generate().publicKey;
    const root = Buffer.alloc(32, 0xbb);

    // 2. buildInitializeVaultInstruction
    const initIx = client.buildInitializeVaultInstruction(masterOwner, SOLANA_USDT_MINT, root);
    expect(initIx.data.length).to.equal(40); // 8 bytes disc + 32 bytes root
    const expectedInitDisc = Buffer.from([230, 71, 53, 169, 238, 108, 169, 111]);
    expect(initIx.data.subarray(0, 8).equals(expectedInitDisc)).to.be.true;
    expect(initIx.keys.length).to.equal(5);

    // 3. buildDepositFundsInstruction
    const depositor = Keypair.generate().publicKey;
    const userSourceAta = Keypair.generate().publicKey;
    const depositIx = client.buildDepositFundsInstruction(masterOwner, depositor, userSourceAta, 5_000_000n);
    expect(depositIx.data.length).to.equal(16); // 8 bytes disc + 8 bytes u64 LE
    const expectedDepositDisc = Buffer.from([202, 39, 52, 211, 53, 20, 250, 88]);
    expect(depositIx.data.subarray(0, 8).equals(expectedDepositDisc)).to.be.true;
    expect(depositIx.data.readBigUInt64LE(8)).to.equal(5_000_000n);

    // 4. buildExecuteMasterPaymentInstruction
    const subAgent = Keypair.generate().publicKey;
    const payer = Keypair.generate().publicKey;
    const providerAta = Keypair.generate().publicKey;
    const proofElem1 = Buffer.alloc(32, 0x11);
    const proofElem2 = Buffer.alloc(32, 0x22);
    const proof = [proofElem1, proofElem2];

    const paymentIx = client.buildExecuteMasterPaymentInstruction(
      masterOwner,
      subAgent,
      payer,
      providerAta,
      2000n,
      10000n,
      50000n,
      1n,
      proof
    );
    // Data: 8 (disc) + 8*4 (spend, max, expiry, nonce) + 4 (proof len) + 32*2 (proof elems) = 8 + 32 + 4 + 64 = 108 bytes
    expect(paymentIx.data.length).to.equal(108);
    const expectedPayDisc = Buffer.from([164, 225, 64, 108, 234, 236, 177, 124]);
    expect(paymentIx.data.subarray(0, 8).equals(expectedPayDisc)).to.be.true;
    expect(paymentIx.data.readBigUInt64LE(8)).to.equal(2000n); // spend
    expect(paymentIx.data.readBigUInt64LE(16)).to.equal(10000n); // max
    expect(paymentIx.data.readBigUInt64LE(24)).to.equal(50000n); // expiry
    expect(paymentIx.data.readBigUInt64LE(32)).to.equal(1n); // nonce
    expect(paymentIx.data.readUInt32LE(40)).to.equal(2); // proof count
    expect(paymentIx.data.subarray(44, 76).equals(proofElem1)).to.be.true;
    expect(paymentIx.data.subarray(76, 108).equals(proofElem2)).to.be.true;
    expect(paymentIx.keys.length).to.equal(8);
  });
});
