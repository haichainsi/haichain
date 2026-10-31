import { Connection, PublicKey } from "@solana/web3.js";
import { AnchorProvider } from "@coral-xyz/anchor";
export declare const SOLANA_USDT_MINT: PublicKey;
export type SupportedFiatCurrency = "USD" | "EUR" | "GBP" | "JPY" | "CAD" | "AUD" | "BRL" | "INR" | "SGD";
export type SupportedCrossChainNetwork = "solana_spl" | "tron_trc20" | "ethereum_erc20" | "arbitrum" | "binance_smart_chain";
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
    /**
     * Generates a multi-channel USDT deposit session (Apple Pay, SEPA, Cards, or Native USDT)
     */
    createUsdtDepositSession(request: UsdtDepositSessionRequest): Promise<UsdtDepositSessionResponse>;
    /**
     * Processes an incoming HTTP x402 (Payment Required) challenge from an MCP Server
     * Automatically verifies destination whitelist, signs off-chain micro-tick, and returns auth headers.
     */
    handleX402Challenge(headers: X402PaymentRequestHeaders, agentPrivateKey: Uint8Array, whitelistedProviders: PublicKey[]): Promise<X402PaymentAuthorizationHeaders>;
    /**
     * Derives deterministic PDA for Agent Spending Pot
     * Seeds: [b"agent-vault", owner]
     */
    getAgentVaultPda(owner: PublicKey): [PublicKey, number];
    /**
     * Derives deterministic Nullifier PDA for Double-Spend Replay Defense
     * Seeds: [b"nullifier", vaultPda, nonce (u64 le)]
     */
    getNullifierPda(vaultPda: PublicKey, nonce: number | bigint): [PublicKey, number];
    /**
     * One-Click Global Panic Kill-Switch (v6.9 Direct PDA Authority)
     */
    triggerPanicKillSwitch(provider: AnchorProvider, agentDedicatedAta: PublicKey, userSafeDestinationAta: PublicKey): Promise<string>;
    /**
     * Reclaims 100% of Rent-Exempt SOL lamports from an expired Nullifier PDA
     * Invariant v6.9.2: Rent is strictly refunded to the vaultOwner (Anti-Rent-Theft Invariant)
     */
    reclaimExpiredNullifierRent(provider: AnchorProvider, vaultOwner: PublicKey, nonce: number | bigint, rentReceiver?: PublicKey): Promise<string>;
}
