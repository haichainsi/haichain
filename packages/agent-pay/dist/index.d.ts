/**
 * ==============================================================================
 * @haichainsi/agent-pay
 * Universal HTTP 402 Micro-Payment Paywall & Solana Escrow Middleware
 * For Autonomous AI Agents on Smithery, Fetch.ai, and MCP Servers.
 * ==============================================================================
 * REAL ON-CHAIN PRODUCTION-GRADE ENFORCEMENT:
 * - Zero bypass backdoor.
 * - Confirms on-chain Solana L1 transactions via RPC.
 * - Verifies recipient address inclusion and positive lamport delta.
 */
export interface PaywallConfig {
    recipient: string;
    priceUsdt: number;
    cluster?: 'devnet' | 'mainnet-beta';
    rpcUrl?: string;
    serviceName?: string;
    minLamports?: number;
}
export declare class HaichainPaywall {
    private config;
    private connection;
    private recipientPubkey;
    constructor(config: PaywallConfig);
    /**
     * Generates standard HTTP 402 Payment Challenge Response
     */
    generate402Challenge(reqPath?: string): {
        status: number;
        headers: {
            'Content-Type': string;
            'WWW-Authenticate': string;
            'X-Payment-Required': string;
            'X-Payment-Payee': string;
            'X-Payment-Amount': string;
            'X-Payment-Network': string;
            'X-Resource-Uri': string;
        };
        body: {
            error: string;
            statusCode: number;
            service: string | undefined;
            message: string;
            settlementDetails: {
                recipient: string;
                amountUsdt: number;
                network: string;
                protocol: string;
                paymentHelper: string;
            };
        };
    };
    /**
     * REAL ON-CHAIN SOLANA AUDIT:
     * 1. Inspects raw Solana Transaction on L1 via RPC.
     * 2. Confirms zero execution errors on-chain.
     * 3. Confirms recipient balance received the micro-payment.
     */
    verifyPayment(authHeader?: string, customTxSig?: string): Promise<{
        valid: boolean;
        reason?: string;
        txDetails?: any;
    }>;
    /**
     * Connect / Express Middleware
     */
    middleware(): (req: any, res: any, next: any) => Promise<any>;
    /**
     * Cloudflare Worker / Fetch Handler Middleware
     */
    handleFetch(request: Request, executeTask: () => Promise<Response>): Promise<Response>;
}
export declare function haichainPaywall(config: PaywallConfig): (req: any, res: any, next: any) => Promise<any>;
export default HaichainPaywall;
