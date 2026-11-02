import { Connection, PublicKey, Keypair, TransactionInstruction } from "@solana/web3.js";
import { AnchorProvider } from "@coral-xyz/anchor";
export declare const SOLANA_USDT_MINT: PublicKey;
export declare const SOLANA_USDC_MINT: PublicKey;
export type SupportedFiatCurrency = "USD" | "EUR" | "GBP" | "JPY" | "CAD" | "AUD" | "BRL" | "INR" | "SGD";
export type SupportedCrossChainNetwork = "solana_spl" | "tron_trc20" | "ethereum_erc20" | "arbitrum" | "base_erc20" | "binance_smart_chain";
export type SupportedPaymentRail = "apple_pay" | "google_pay" | "stripe_link" | "card_international" | "sepa_instant" | "fednow_ach" | "crypto_usdt_deposit";
/**
 * Standard HTTP x402 (Payment Required) Header Interface for MCP
 */
export interface X402PaymentRequestHeaders {
    "X-402-PayTo": string;
    "X-402-Amount": string;
    "X-402-Nonce": string;
    "X-402-Action-Tag"?: string;
}
export interface X402PaymentAuthorizationHeaders {
    "X-402-Authorization": string;
    "X-402-Payer-Vault": string;
    "X-402-Timestamp": string;
}
export interface UsdtDepositSessionRequest {
    userUid: string;
    amountUsdt: number;
    sourceNetwork?: SupportedCrossChainNetwork;
    preferredRail?: SupportedPaymentRail;
}
export interface UsdtDepositSessionResponse {
    sessionId: string;
    depositAddressSolanaSpl: string;
    crossChainDepositAddressTron?: string;
    checkoutUrlFiat: string;
    amountUsdtExpected: number;
    decimals: number;
    expiresAtIso: string;
}
export declare class HaiChainClient {
    connection: Connection;
    programId: PublicKey;
    usdtMint: PublicKey;
    constructor(connection: Connection, programId?: PublicKey, usdtMint?: PublicKey);
    createUsdtDepositSession(request: UsdtDepositSessionRequest): Promise<UsdtDepositSessionResponse>;
    /**
     * Handles HTTP x402 Payment Challenge with strict destination whitelist verification
     * and dynamically derived Payer Vault PDA.
     */
    handleX402Challenge(headers: X402PaymentRequestHeaders, agentPrivateKey: Uint8Array, whitelistedProviders: PublicKey[], vaultOwner?: PublicKey): Promise<X402PaymentAuthorizationHeaders>;
    /**
     * Computes the 5-Tuple Cryptographic Composite Capability Leaf.
     * Cryptographically binds the authorized Sub-Agent to a specific Whitelisted Merchant Token Account (ATA).
     * Enforced on-chain by haichain-core Anchor smart contract to eliminate prompt injection / memory poisoning theft.
     */
    static computeCompositeCapabilityLeaf(subAgentSigner: PublicKey, whitelistedMerchantAta: PublicKey, maxAuthorizedAmount: bigint | number, expirySlot: bigint | number, nonce: bigint | number): Buffer;
    /**
     * Generates cryptographic payload for State Channel Micro-Voucher signing with full Domain Separation.
     * Prevents cross-cluster, cross-contract, cross-provider, and cross-session replay attacks.
     */
    static buildVoucherSigningPayload(clusterId: "mainnet-beta" | "devnet" | "testnet", programId: PublicKey, vaultPda: PublicKey, providerPubkey: PublicKey, sessionId: string, nonce: number | bigint, cumulativeAmount: number | bigint): Buffer;
    /**
     * Verifies a Merkle proof against a composite root with sorted pair hashing.
     * Exactly replicates the on-chain Anchor verification in haichain-core (lib.rs lines 164-171).
     * Enables zero-cost off-chain pre-flight simulation before submitting transactions to Solana.
     */
    static verifyCompositeProof(leaf: Uint8Array | Buffer, proof: (Uint8Array | Buffer)[], expectedRoot: Uint8Array | Buffer): boolean;
    /**
     * Cryptographically signs a micro-voucher with an Ed25519 keypair.
     * Combines domain-separated payload hashing with detached Ed25519 signing.
     */
    static signMicroVoucher(agentKeypair: Keypair, voucherArgs: {
        clusterId: "mainnet-beta" | "devnet" | "testnet";
        programId: PublicKey;
        vaultPda: PublicKey;
        providerPubkey: PublicKey;
        sessionId: string;
        nonce: number | bigint;
        cumulativeAmount: number | bigint;
    }): {
        payloadHash: Buffer;
        signature: Uint8Array;
        signatureBase64: string;
    };
    /**
     * Verifies an Ed25519 micro-voucher signature off-chain.
     * Can be executed by providers and gateway proxies in sub-millisecond latency (<0.1ms).
     */
    static verifyMicroVoucherSignature(signerPubkey: PublicKey, payloadHash: Uint8Array | Buffer, signature: Uint8Array | Buffer): boolean;
    getAgentVaultPda(owner: PublicKey): [PublicKey, number];
    getNullifierPda(vaultPda: PublicKey, nonce: number | bigint): [PublicKey, number];
    getProviderBondPda(providerAuthority: PublicKey): [PublicKey, number];
    /**
     * Builds the instruction for triggering the emergency panic kill-switch.
     * Anchor Discriminator: sha256("global:trigger_emergency_panic")[0..8] = [232, 177, 104, 97, 82, 33, 17, 191]
     */
    buildTriggerPanicInstruction(masterOwner: PublicKey, agentDedicatedAta: PublicKey, userSafeDestinationAta: PublicKey): TransactionInstruction;
    triggerPanicKillSwitch(provider: AnchorProvider, agentDedicatedAta: PublicKey, userSafeDestinationAta: PublicKey): Promise<string>;
    /**
     * Builds the instruction for reclaiming expired nullifier SOL rent.
     * Anchor Discriminator: sha256("global:reclaim_expired_nullifier")[0..8] = [16, 165, 146, 96, 207, 57, 80, 93]
     * Invariant: agentVaultPda MUST be writable because vault.min_valid_nonce is monotonically updated on-chain.
     */
    buildReclaimNullifierInstruction(vaultOwner: PublicKey, nonce: number | bigint, rentReceiver?: PublicKey): TransactionInstruction;
    reclaimExpiredNullifierRent(provider: AnchorProvider, vaultOwner: PublicKey, nonce: number | bigint, rentReceiver?: PublicKey): Promise<string>;
    /**
     * Builds the instruction for O(1) mass-invalidation of capability tickets.
     * Anchor Discriminator: sha256("global:advance_min_valid_nonce")[0..8] = [81, 92, 116, 233, 79, 68, 222, 129]
     */
    buildAdvanceMinValidNonceInstruction(masterOwner: PublicKey, newMinNonce: number | bigint): TransactionInstruction;
    /**
     * Builds the instruction for rotating composite Merkle roots with sliding window grace period.
     * Anchor Discriminator: sha256("global:update_composite_root")[0..8] = [230, 8, 5, 238, 82, 121, 117, 97]
     */
    buildUpdateCompositeRootInstruction(masterOwner: PublicKey, newCompositeRoot: Uint8Array | Buffer): TransactionInstruction;
}
export interface SlaExecutionReceipt {
    providerAuthority: string;
    taskPromptHash: string;
    responsePayloadHash: string;
    executionTimestamp: number;
    claimedQualityScore: number;
}
export declare class ProbabilisticSlaAuditor {
    private faultRecords;
    static hashPayload(payload: string): string;
    static generateReceipt(providerAuthority: PublicKey, taskPrompt: string, responsePayload: string, claimedQualityScore?: number): SlaExecutionReceipt;
    shouldPerformSpotCheck(spotCheckProbability?: number): boolean;
    recordExecution(providerAuthority: string, isFault: boolean): {
        faultRate: number;
        shouldSlash: boolean;
    };
}
export interface ProviderEndpoint {
    id: string;
    type: "web2_reseller" | "depin_node";
    name: string;
    ataAddress: string;
    costMicroUsdt: number;
    isHealthy: boolean;
}
export declare class DePinProviderRouter {
    private providers;
    registerEndpoint(category: string, endpoint: ProviderEndpoint): void;
    routeRequest(category: string, forceDePinOnly?: boolean): ProviderEndpoint;
    markFailure(category: string, endpointId: string): void;
}
export interface CrossChainPaymentIntent {
    sourceChain: SupportedCrossChainNetwork;
    senderAddress: string;
    recipientHaiChainAta: string;
    amountUsdt: number;
    nonce: number;
    intentSignature: string;
    expiryTimestamp: number;
}
export declare class CrossChainIntentSolver {
    private executedIntents;
    verifyAndFrontLiquidity(intent: CrossChainPaymentIntent): {
        authorized: boolean;
        solverTxHash: string;
        frontedAmountUsdt: number;
    };
}
export interface DynamicSpotTicket {
    providerAuthority: string;
    basePriceMicroUsdt: number;
    spotPriceMicroUsdt: number;
    surgeFactorBps: number;
    loadRatio: number;
    expirySlot: number;
    nonce: number;
    signature?: string;
}
export declare class DynamicSpotTicketEngine {
    static calculateDynamicPrice(basePriceMicroUsdt: number, currentLoad: number, maxCapacity: number, surgeBpsMax?: number): {
        spotPrice: number;
        loadRatio: number;
        surgeBps: number;
    };
    static createQuotationTicket(providerAuthority: PublicKey, basePriceMicroUsdt: number, currentLoad: number, maxCapacity: number, currentSlot: number, validitySlots?: number, nonce?: number): DynamicSpotTicket;
    static verifyQuotationTicket(ticket: DynamicSpotTicket, maxBudgetCapMicroUsdt: number, currentSlot: number): {
        valid: boolean;
        reason?: string;
    };
}
export declare class ActionCreditsConverter {
    static readonly MICRO_USDT_PER_CREDIT = 1000;
    static readonly DEFAULT_VND_PER_CREDIT = 25;
    static usdtToCredits(usdtAmount: number): number;
    static microUsdtToCredits(microUnits: number | bigint): number;
    static creditsToUsdt(credits: number): number;
    static creditsToVnd(credits: number, rate?: number): number;
    static formatCredits(credits: number): string;
    static formatVnd(credits: number, rate?: number): string;
}
export declare class IdempotencyEngine {
    private cache;
    private ttlMs;
    constructor(ttlMs?: number);
    generateIdempotencyKey(sessionId: string, taskStepIndex: number, nonce: number | bigint): string;
    executeIdempotent<T>(key: string, executeFn: () => Promise<T>): Promise<{
        result: T;
        cached: boolean;
    }>;
}
export interface MicroTransactionRecord {
    transactionId: string;
    timestamp: string;
    providerAuthority: string;
    serviceCategory: "ai_inference" | "web_scraping" | "data_indexing" | "gpu_compute";
    costUsdt: number;
    nonce: number;
}
export interface EnterpriseConsolidatedInvoice {
    invoiceNumber: string;
    organizationName: string;
    billingPeriod: string;
    totalTransactionsCount: number;
    subtotalUsdt: number;
    vatTaxPct: number;
    taxAmountUsdt: number;
    totalDueUsdt: number;
    totalDueCredits: number;
    totalDueVndEstimated: number;
    merkleAuditRoot: string;
    categoryBreakdown: Record<string, {
        count: number;
        totalCostUsdt: number;
    }>;
    generatedAtIso: string;
}
export declare class EnterpriseRollupInvoiceGenerator {
    static generateMonthlyInvoice(transactions: MicroTransactionRecord[], organizationName: string, billingPeriod: string, vatTaxPct?: number): EnterpriseConsolidatedInvoice;
}
