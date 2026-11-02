// tests/haichain-sdk-verification.test.ts
import { expect } from "chai";
import { Keypair, PublicKey } from "@solana/web3.js";
import { HaiChainClient } from "../sdk/typescript/src/index";
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
});
