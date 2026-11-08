/**
 * ==============================================================================
 * @haichainsi/agent-pay
 * HAICHAIN Universal HTTP 402 Micro-Payment Paywall & Cryptographic Guardrail Middleware
 * Fully compliant with RFC HTTP 402, Coinbase x402 Standard & HAICHAIN Policy Vault.
 * Designed for Autonomous AI Agents on Smithery, ElizaOS, Claude Desktop, MCP & DePIN.
 * ==============================================================================
 * DUAL-PATH ARCHITECTURE:
 * 1. FAST-PATH OFF-CHAIN VOUCHER (< 2ms):
 *    - Cryptographically verifies Ed25519 detached signatures against agent public key.
 *    - Zero RPC wait time; ideal for real-time AI token streaming & low-latency inference.
 *    - In-memory Nullifier Store protects against Replay Attacks.
 * 2. DIRECT ON-CHAIN L1 AUDIT:
 *    - Inspects Solana L1 transactions via RPC for confirmed status & positive lamport delta.
 *    - 300s freshness window against pre-mined voucher recycling.
 */
import { Keypair } from '@solana/web3.js';
export interface PaywallConfig {
    recipient: string;
    priceUsdt: number;
    cluster?: 'devnet' | 'mainnet-beta';
    rpcUrl?: string;
    serviceName?: string;
    minLamports?: number;
    maxAgeSeconds?: number;
    tokenMint?: string;
    watchtowerUrl?: string;
    allowFastPath?: boolean;
}
export interface X402StandardChallengeBody {
    error: string;
    statusCode: number;
    maxAmountRequired: string;
    resource: string;
    description: string;
    payTo: string;
    paymentAddress: string;
    asset: string;
    assetAddress: string;
    assetType: 'SPL' | 'ERC20';
    network: string;
    caip2Network: string;
    expiresAt: number;
    nonce: string;
    paymentId: string;
    haichainGuardrail: {
        protocol: 'haichain-v1-voucher';
        policyProtected: boolean;
        boundedLossEnforced: boolean;
        settlementHelper: string;
    };
    settlementDetails: {
        recipient: string;
        amountUsdt: number;
        network: string;
        protocol: string;
        paymentHelper: string;
    };
}
export interface PaymentVerificationResult {
    valid: boolean;
    mode?: 'fast-path-voucher' | 'direct-l1-settlement';
    reason?: string;
    txDetails?: any;
    voucherDetails?: {
        agentPubkey: string;
        recipient: string;
        amount: number | string;
        channelId?: string;
        cumulativeAmount?: string;
        verifiedAt: number;
    };
}
export declare class HaichainPaywall {
    /**
     * High-Performance OpenSSL Ed25519 Detached Verification (< 0.2ms)
     * Uses native C++ OpenSSL engine when available in Node.js runtime, with TweetNaCl fallback.
     */
    static verifyEd25519Detached(msg: Buffer | Uint8Array, sig: Buffer | Uint8Array, pubkey: Buffer | Uint8Array): boolean;
    private config;
    private connection;
    private recipientPubkey;
    private usedSignatures;
    static readonly USDT_SOLANA_MAINNET = "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB";
    static readonly USDC_SOLANA_MAINNET = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v";
    constructor(config: PaywallConfig);
    private cleanupExpiredNullifiers;
    /**
     * Generates standard HTTP 402 Payment Challenge Response.
     * Completely adheres to Coinbase x402 specification while embedding HAICHAIN cryptographic guardrails.
     */
    generate402Challenge(reqPath?: string): {
        status: number;
        headers: {
            'Content-Type': string;
            'WWW-Authenticate': string;
            'X-Payment-Required': string;
            'X-Payment-Payee': string;
            'X-Payment-PayTo': string;
            'X-Payment-Amount': string;
            'X-Payment-Network': string;
            'X-Payment-Nonce': string;
            'X-Resource-Uri': string;
            'Access-Control-Allow-Origin': string;
            'Access-Control-Allow-Headers': string;
            'Access-Control-Allow-Methods': string;
            'Access-Control-Expose-Headers': string;
        };
        body: X402StandardChallengeBody;
    };
    /**
     * Universal Payment Verifier:
     * Supports:
     *  1. Fast-Path Off-chain Signed Voucher (< 2ms) via Ed25519 cryptographic signature.
     *  2. Direct On-chain Solana L1 Transaction audit via RPC.
     */
    verifyPayment(authHeaderOrToken?: string, customTxSig?: string): Promise<PaymentVerificationResult>;
    /**
     * Fast-path verification of off-chain cryptographic vouchers (< 2ms).
     */
    private verifyFastPathPayload;
    /**
     * On-chain Solana L1 RPC Verification.
     */
    private verifyOnChainSolanaTx;
    /**
     * Connect / Express Middleware
     */
    middleware(): (req: any, res: any, next: any) => Promise<any>;
    /**
     * Asynchronously registers state channel vouchers with the Watchtower Sentinel
     */
    forwardVoucherToWatchtower(payload: any): void;
    /**
     * Cloudflare Worker / Fetch Handler Middleware
     */
    handleFetch(request: Request, executeTask: () => Promise<Response>): Promise<Response>;
}
export declare function haichainPaywall(config: PaywallConfig): (req: any, res: any, next: any) => Promise<any>;
export default HaichainPaywall;
export interface ClientConfig {
    keypair?: Keypair;
    potPubkey?: string;
    cluster?: 'devnet' | 'mainnet-beta';
}
export declare class HaichainClient {
    keypair: Keypair;
    agentPubkey: string;
    potPubkey: string;
    cluster: 'devnet' | 'mainnet-beta';
    private nonces;
    private cumulativeBalances;
    constructor(config?: ClientConfig);
    getNextNonce(merchantPubkey: string): number;
    createVoucher(params: {
        merchantPubkey: string;
        amountMicrounit: number;
        channelId?: number;
        scheme?: string;
        resource?: string;
    }): {
        scheme: string;
        version: string;
        cluster: "devnet" | "mainnet-beta";
        potPubkey: string;
        merchantPubkey: string;
        agentPubkey: string;
        channelId: number;
        cumulativeAmount: string;
        amountMicrounit: number;
        nonce: number;
        timestamp: number;
        resource: string;
        signature: string;
        signatureBase64: string;
        signer: string;
    };
    buildAuthHeader(params: {
        merchantPubkey: string;
        amountMicrounit: number;
        channelId?: number;
        scheme?: string;
        resource?: string;
    }): string;
    callPaidAgent(url: string, options?: {
        method?: string;
        body?: any;
        headers?: Record<string, string>;
        timeoutMs?: number;
    }): Promise<Response>;
}
