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
});
