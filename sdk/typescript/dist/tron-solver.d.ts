export interface TronUsdtIntent {
    intentId: string;
    sourceVaultSolana: string;
    destinationTronAddress: string;
    amountUsdt: number;
    maxFeeUsdt: number;
    nonce: number | bigint;
    expiryTimestamp: number;
    signature: string;
}
export interface TronSettlementReceipt {
    intentId: string;
    tronTxHash: string;
    settledAmountUsdt: number;
    tronBlockNumber: number;
    timestampIso: string;
    merkleAuditLeaf: string;
}
export declare class TronEnterpriseSolver {
    static readonly TRON_USDT_CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t";
    /**
     * Hashes a cross-chain payment intent for Tron enterprise clearing.
     */
    static computeIntentHash(intent: Omit<TronUsdtIntent, "intentId" | "signature">): string;
    /**
     * Validates intent expiration and economic solvency before dispatching to Tron network.
     */
    static validateIntent(intent: TronUsdtIntent, currentTimestamp?: number): boolean;
    /**
     * Generates a verifiable Merkle audit leaf for enterprise audit and Big 4 reporting.
     */
    static createSettlementReceipt(intent: TronUsdtIntent, tronTxHash: string, blockNumber: number): TronSettlementReceipt;
}
