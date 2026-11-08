// tests/haichain-watchtower-daemon.test.ts
// COMPREHENSIVE TEST SUITE FOR HAICHAIN WATCHTOWER DISPUTE SENTINEL DAEMON

import { expect } from "chai";
import { Keypair, PublicKey } from "@solana/web3.js";
import * as crypto from "crypto";
import nacl from "tweetnacl";
import { createRequire } from "module";

const require = createRequire(import.meta.url);
const { ProductionAgentRelayer } = require("../server/production-agent-relayer");

describe("HAICHAIN v0.1.0-prototype: Watchtower Dispute Sentinel Daemon", () => {
  let relayer: any;
  const merchant = Keypair.generate();
  const pot = Keypair.generate();
  const agent = Keypair.generate();
  const channelId = 42;

  beforeEach(() => {
    relayer = new ProductionAgentRelayer({ port: 8999 });
  });

  function signVoucher(
    agentKp: Keypair,
    potPk: PublicKey,
    merchantPk: PublicKey,
    chanId: number,
    cumulative: bigint,
    nonce: bigint
  ): string {
    const chanBuf = Buffer.alloc(8);
    const amountBuf = Buffer.alloc(8);
    const nonceBuf = Buffer.alloc(8);
    chanBuf.writeBigUInt64LE(BigInt(chanId));
    amountBuf.writeBigUInt64LE(cumulative);
    nonceBuf.writeBigUInt64LE(nonce);

    const hash = crypto
      .createHash("sha256")
      .update(Buffer.from("HAICHAIN-VOUCHER-V1"))
      .update(potPk.toBuffer())
      .update(merchantPk.toBuffer())
      .update(chanBuf)
      .update(amountBuf)
      .update(nonceBuf)
      .digest();

    const sig = nacl.sign.detached(hash, agentKp.secretKey);
    return Buffer.from(sig).toString("base64");
  }

  it("1. [WATCHTOWER INITIAL STATUS]: Daemon initializes with active sentinel and 0 channels", () => {
    const status = relayer.getWatchtowerStatus();
    expect(status.watchtowerActive).to.be.true;
    expect(status.totalMonitoredChannels).to.equal(0);
    expect(status.protectionMechanism).to.include("Dispute Window");
  });

  it("2. [VOUCHER REGISTRATION SUCCESS]: Valid signed voucher is accepted and monitored", () => {
    const sig = signVoucher(agent, pot.publicKey, merchant.publicKey, channelId, 50000n, 1n);

    const result = relayer.registerWatchtowerVoucher({
      channelId,
      potPubkey: pot.publicKey.toBase58(),
      merchantPubkey: merchant.publicKey.toBase58(),
      agentPubkey: agent.publicKey.toBase58(),
      cumulativeAmount: "50000",
      nonce: "1",
      signatureBase64: sig,
    });

    expect(result.status).to.equal("REGISTERED_SUCCESS");
    expect(result.cumulativeAmount).to.equal("50000");

    const status = relayer.getWatchtowerStatus();
    expect(status.totalMonitoredChannels).to.equal(1);
    expect(status.channels[0].channelId).to.equal(channelId.toString());
  });

  it("3. [TAMPERED SIGNATURE REJECTION]: Forged voucher signature is rejected by Watchtower", () => {
    const forgedSig = Buffer.alloc(64, 0xef).toString("base64");

    expect(() => {
      relayer.registerWatchtowerVoucher({
        channelId,
        potPubkey: pot.publicKey.toBase58(),
        merchantPubkey: merchant.publicKey.toBase58(),
        agentPubkey: agent.publicKey.toBase58(),
        cumulativeAmount: "50000",
        nonce: "1",
        signatureBase64: forgedSig,
      });
    }).to.throw("Watchtower Cryptographic Rejection: Invalid Ed25519 signature");
  });

  it("4. [MONOTONIC UPDATE]: Higher cumulative voucher supersedes previous voucher", () => {
    const sig1 = signVoucher(agent, pot.publicKey, merchant.publicKey, channelId, 50000n, 1n);
    relayer.registerWatchtowerVoucher({
      channelId,
      potPubkey: pot.publicKey.toBase58(),
      merchantPubkey: merchant.publicKey.toBase58(),
      agentPubkey: agent.publicKey.toBase58(),
      cumulativeAmount: "50000",
      nonce: "1",
      signatureBase64: sig1,
    });

    const sig2 = signVoucher(agent, pot.publicKey, merchant.publicKey, channelId, 80000n, 2n);
    const updateResult = relayer.registerWatchtowerVoucher({
      channelId,
      potPubkey: pot.publicKey.toBase58(),
      merchantPubkey: merchant.publicKey.toBase58(),
      agentPubkey: agent.publicKey.toBase58(),
      cumulativeAmount: "80000",
      nonce: "2",
      signatureBase64: sig2,
    });

    expect(updateResult.status).to.equal("REGISTERED_SUCCESS");
    expect(updateResult.cumulativeAmount).to.equal("80000");

    // Lesser or equal voucher should be ignored
    const staleResult = relayer.registerWatchtowerVoucher({
      channelId,
      potPubkey: pot.publicKey.toBase58(),
      merchantPubkey: merchant.publicKey.toBase58(),
      agentPubkey: agent.publicKey.toBase58(),
      cumulativeAmount: "70000",
      nonce: "3",
      signatureBase64: sig2, // doesn't matter, ignored before check or after
    });
    expect(staleResult.status).to.equal("IGNORED_LESSER_OR_EQUAL");
  });

  it("5. [DEFEND CHANNEL]: Watchtower triggers settlement defense for registered channel", async () => {
    const sig = signVoucher(agent, pot.publicKey, merchant.publicKey, channelId, 100000n, 10n);
    relayer.registerWatchtowerVoucher({
      channelId,
      potPubkey: pot.publicKey.toBase58(),
      merchantPubkey: merchant.publicKey.toBase58(),
      agentPubkey: agent.publicKey.toBase58(),
      cumulativeAmount: "100000",
      nonce: "10",
      signatureBase64: sig,
    });

    const defense = await relayer.defendChannel(channelId);
    expect(defense.defended).to.be.true;
    expect(defense.action).to.equal("SETTLEMENT_DEFENSE_EXECUTED");
    expect(defense.securedAmount).to.equal("100000");
    expect(defense.merchantPubkey).to.equal(merchant.publicKey.toBase58());
  });
});
