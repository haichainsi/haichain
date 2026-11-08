// sdk/typescript/src/policy-engine.ts
// HAICHAIN v1.1 - Out-of-Process Policy Engine & Key Isolation Sandbox
// Implements Zero-Knowledge Session Key Security: LLM never sees private keys.
// Enforces Per-Domain Rate Limiting & Anti-Prompt-Injection Micro-Loop Protection.

import { Keypair, PublicKey } from "@solana/web3.js";
import * as crypto from "crypto";
import nacl from "tweetnacl";
import { CapLeafV1, CapLeafV1Engine, CapLeafFlags } from "./capleaf";

export interface PaymentIntent {
  resource: string;
  maxAmount: bigint;
  merchant: PublicKey;
  mint: PublicKey;
  scopeClass: number;
  cosignerSignature?: Uint8Array;
  cosignerPublicKey?: PublicKey;
}

export interface ScopePolicy {
  origin: string;
  pathPrefix: string;
  allowedMethods: string[];
  maxPerCall: bigint;
  maxDailySpend: bigint;
}

export interface DomainThrottleRecord {
  callTimestamps: number[];
  totalSpent: bigint;
  lastCallTime: number;
  isProbation: boolean;
}

export class PolicyEngine {
  private agentKeypair: Keypair;
  private activeGrants: Map<string, CapLeafV1> = new Map();
  private domainThrottles: Map<string, DomainThrottleRecord> = new Map();
  private cumulativeSpendPerChannel: Map<string, bigint> = new Map();

  // Red-Team Safety Thresholds
  public static readonly PROBATION_MAX_CALLS_PER_WINDOW = 3;
  public static readonly PROBATION_WINDOW_SECONDS = 600; // 10 minutes

  constructor(agentKeypair: Keypair) {
    this.agentKeypair = agentKeypair;
  }

  public getAgentPublicKey(): PublicKey {
    return this.agentKeypair.publicKey;
  }

  public registerActiveGrant(leaf: CapLeafV1): void {
    const leafBytes = CapLeafV1Engine.serialize(leaf);
    const leafHashHex = crypto.createHash("sha256").update(leafBytes).digest("hex");
    this.activeGrants.set(leafHashHex, leaf);
  }

  /**
   * Evaluates an LLM's proposed PaymentIntent against ActiveGrants, hard limits, and domain throttles.
   * Throws an error if any invariant is violated (Fail-Closed principle).
   */
  public evaluateAndAuthorize(
    intent: PaymentIntent,
    leafHashHex: string,
    channelId: bigint,
    now: number = Math.floor(Date.now() / 1000)
  ): {
    authorizedAmount: bigint;
    cumulativeVoucherAmount: bigint;
    signature: Uint8Array;
    potPubkey: PublicKey;
    grantNonce: bigint;
  } {
    const grant = this.activeGrants.get(leafHashHex);
    if (!grant) {
      throw new Error("SECURITY FAULT: No active grant found matching requested leaf hash");
    }

    // 1. Recipient & Mint strict match (Hard Layer)
    if (!grant.merchant.equals(intent.merchant)) {
      throw new Error(`SECURITY ALERT: Merchant mismatch! Expected ${grant.merchant.toBase58()}, received ${intent.merchant.toBase58()}`);
    }
    if (!grant.mint.equals(intent.mint)) {
      throw new Error(`SECURITY ALERT: Token Mint mismatch! Expected ${grant.mint.toBase58()}, received ${intent.mint.toBase58()}`);
    }

    // 2. Scope class bitmask check (Soft Layer)
    if ((intent.scopeClass & grant.scopeClass) === 0) {
      throw new Error(`SECURITY ALERT: Unauthorized ScopeClass! Requested ${intent.scopeClass}, allowed bitmask ${grant.scopeClass}`);
    }

    // 3. Time bounds check
    if (BigInt(now) >= grant.expiry) {
      throw new Error("SECURITY ALERT: Grant capability ticket has expired");
    }
    if (BigInt(now) < grant.notBefore) {
      throw new Error("SECURITY ALERT: Grant capability ticket is not yet active");
    }

    // 4. Red-Team Vector 5: Domain Frequency Throttling against Indirect Prompt Injection Micro-Loop
    const domain = this.extractDomainFromResource(intent.resource);
    this.enforceDomainRateLimit(domain, (grant.flags & CapLeafFlags.PROBATION) !== 0, now);

    // 4b. TEE Co-Signer Invariant Enforcement (bit REQUIRE_COSIGN)
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
    const currentCumulative = this.cumulativeSpendPerChannel.get(channelId.toString()) || 0n;
    const requestedSpend = intent.maxAmount;

    if (requestedSpend <= 0n) {
      throw new Error("SECURITY ALERT: Spend amount must be strictly greater than 0");
    }
    if (requestedSpend > grant.maxReserve) {
      throw new Error(`SECURITY ALERT: Spend amount ${requestedSpend} exceeds maxReserve ${grant.maxReserve}`);
    }

    const newCumulative = currentCumulative + requestedSpend;
    if (newCumulative > grant.maxSpend) {
      throw new Error(`SECURITY ALERT: Cumulative spend ${newCumulative} exceeds lifetime maxSpend ${grant.maxSpend}`);
    }

    // Sign micro-voucher with isolated agent private key (LLM never sees this key!)
    const voucherPayload = PolicyEngine.buildVoucherPayload(grant.pot, grant.merchant, channelId, newCumulative, grant.nonce);
    const signature = nacl.sign.detached(voucherPayload, this.agentKeypair.secretKey);

    // Update internal accounting
    this.cumulativeSpendPerChannel.set(channelId.toString(), newCumulative);

    return {
      authorizedAmount: requestedSpend,
      cumulativeVoucherAmount: newCumulative,
      signature,
      potPubkey: grant.pot,
      grantNonce: grant.nonce,
    };
  }

  /**
   * Validates server response payload to detect empty data traps or infinite replay loops.
   */
  public verifyServicePayload(payload: Buffer | string): boolean {
    if (!payload || payload.length === 0) {
      throw new Error("PAYLOAD ANOMALY: Empty payload returned by provider. Potential drainage trap!");
    }
    // Check if payload contains error markers disguised as successful HTTP 200
    const str = typeof payload === "string" ? payload : payload.toString("utf8");
    if (str.includes('"error"') && (str.includes('500') || str.includes('"code": 500') || str.includes('"code":500'))) {
      throw new Error("PAYLOAD ANOMALY: Provider returned disguised internal error");
    }
    return true;
  }

  private enforceDomainRateLimit(domain: string, isProbation: boolean, now: number): void {
    let record = this.domainThrottles.get(domain);
    if (!record) {
      record = {
        callTimestamps: [],
        totalSpent: 0n,
        lastCallTime: now,
        isProbation,
      };
      this.domainThrottles.set(domain, record);
    }

    // Evict timestamps older than sliding window
    const windowStart = now - PolicyEngine.PROBATION_WINDOW_SECONDS;
    record.callTimestamps = record.callTimestamps.filter(t => t >= windowStart);

    if (record.isProbation && record.callTimestamps.length >= PolicyEngine.PROBATION_MAX_CALLS_PER_WINDOW) {
      throw new Error(
        `RATE LIMIT BREACH: Domain ${domain} under PROBATION exceeded ${PolicyEngine.PROBATION_MAX_CALLS_PER_WINDOW} calls per 10m window. Blocked against Prompt Injection loop!`
      );
    }

    record.callTimestamps.push(now);
    record.lastCallTime = now;
  }

  private extractDomainFromResource(resource: string): string {
    try {
      const url = new URL(resource);
      return url.hostname;
    } catch {
      return resource.split("/")[0] || "unknown";
    }
  }

  public static buildCosignPayload(
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

  public static buildVoucherPayload(
    pot: PublicKey,
    merchant: PublicKey,
    channelId: bigint,
    cumulativeAmount: bigint,
    nonce: bigint
  ): Buffer {
    const channelBuf = Buffer.alloc(8);
    const amountBuf = Buffer.alloc(8);
    const nonceBuf = Buffer.alloc(8);
    channelBuf.writeBigUInt64LE(channelId);
    amountBuf.writeBigUInt64LE(cumulativeAmount);
    nonceBuf.writeBigUInt64LE(nonce);

    return crypto.createHash("sha256")
      .update(Buffer.from("HAICHAIN-VOUCHER-V1"))
      .update(pot.toBuffer())
      .update(merchant.toBuffer())
      .update(channelBuf)
      .update(amountBuf)
      .update(nonceBuf)
      .digest();
  }

  public static verifyVoucherSignature(
    agentPubkey: PublicKey,
    pot: PublicKey,
    merchant: PublicKey,
    channelId: bigint,
    cumulativeAmount: bigint,
    nonce: bigint,
    signature: Uint8Array
  ): boolean {
    const payload = PolicyEngine.buildVoucherPayload(pot, merchant, channelId, cumulativeAmount, nonce);
    return nacl.sign.detached.verify(payload, signature, agentPubkey.toBytes());
  }
}
