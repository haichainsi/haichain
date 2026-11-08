import { Keypair, PublicKey } from "@solana/web3.js";
import { CapLeafV1 } from "./capleaf";
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
export declare class PolicyEngine {
    private agentKeypair;
    private activeGrants;
    private domainThrottles;
    private cumulativeSpendPerChannel;
    static readonly PROBATION_MAX_CALLS_PER_WINDOW = 3;
    static readonly PROBATION_WINDOW_SECONDS = 600;
    constructor(agentKeypair: Keypair);
    getAgentPublicKey(): PublicKey;
    registerActiveGrant(leaf: CapLeafV1): void;
    /**
     * Evaluates an LLM's proposed PaymentIntent against ActiveGrants, hard limits, and domain throttles.
     * Throws an error if any invariant is violated (Fail-Closed principle).
     */
    evaluateAndAuthorize(intent: PaymentIntent, leafHashHex: string, channelId: bigint, now?: number): {
        authorizedAmount: bigint;
        cumulativeVoucherAmount: bigint;
        signature: Uint8Array;
        potPubkey: PublicKey;
        grantNonce: bigint;
    };
    /**
     * Validates server response payload to detect empty data traps or infinite replay loops.
     */
    verifyServicePayload(payload: Buffer | string): boolean;
    private enforceDomainRateLimit;
    private extractDomainFromResource;
    static buildCosignPayload(potPubkey: PublicKey, merchantPubkey: PublicKey, channelId: bigint, amount: bigint, nonce: bigint): Buffer;
    static buildVoucherPayload(pot: PublicKey, merchant: PublicKey, channelId: bigint, cumulativeAmount: bigint, nonce: bigint): Buffer;
    static verifyVoucherSignature(agentPubkey: PublicKey, pot: PublicKey, merchant: PublicKey, channelId: bigint, cumulativeAmount: bigint, nonce: bigint, signature: Uint8Array): boolean;
}
