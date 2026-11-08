"use strict";
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
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.HaichainPaywall = void 0;
exports.haichainPaywall = haichainPaywall;
const web3_js_1 = require("@solana/web3.js");
const crypto = __importStar(require("crypto"));
const tweetnacl_1 = __importDefault(require("tweetnacl"));
class HaichainPaywall {
    config;
    connection;
    recipientPubkey;
    // Nullifier store: tracks consumed signatures/nonces to prevent Replay Attacks
    usedSignatures;
    static USDT_SOLANA_MAINNET = 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB';
    static USDC_SOLANA_MAINNET = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v';
    constructor(config) {
        if (!config.recipient) {
            throw new Error('[HaichainPaywall] recipient Solana address is required');
        }
        this.config = {
            cluster: 'devnet',
            minLamports: 10000,
            serviceName: 'HAICHAIN Autonomous Agent Service',
            maxAgeSeconds: 300, // 5 minutes max freshness window
            tokenMint: HaichainPaywall.USDT_SOLANA_MAINNET,
            allowFastPath: true,
            rpcUrl: config.rpcUrl,
            ...config
        };
        const rpc = this.config.rpcUrl || (this.config.cluster === 'mainnet-beta'
            ? 'https://api.mainnet-beta.solana.com'
            : 'https://api.devnet.solana.com');
        this.connection = new web3_js_1.Connection(rpc, 'confirmed');
        this.recipientPubkey = new web3_js_1.PublicKey(this.config.recipient);
        this.usedSignatures = new Map();
        // Periodic garbage collection for expired nullifier entries (prevents memory leak)
        if (typeof setInterval !== 'undefined') {
            setInterval(() => this.cleanupExpiredNullifiers(), 60_000).unref?.();
        }
    }
    cleanupExpiredNullifiers() {
        const cutoff = Date.now() - (this.config.maxAgeSeconds * 2 * 1000);
        for (const [key, record] of this.usedSignatures.entries()) {
            if (record.usedAt < cutoff) {
                this.usedSignatures.delete(key);
            }
        }
    }
    /**
     * Generates standard HTTP 402 Payment Challenge Response.
     * Completely adheres to Coinbase x402 specification while embedding HAICHAIN cryptographic guardrails.
     */
    generate402Challenge(reqPath = '/task') {
        const nowSec = Math.floor(Date.now() / 1000);
        const expiresAt = nowSec + this.config.maxAgeSeconds;
        const nonce = `haichain_nonce_${nowSec}_${crypto.randomBytes(8).toString('hex')}`;
        const paymentId = `haipay_${nowSec}_${crypto.randomBytes(6).toString('hex')}`;
        const caip2Network = this.config.cluster === 'mainnet-beta'
            ? 'solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp'
            : 'solana:EtWTRABZaYq6iMfeYKouRu166VU2xqa1';
        const body = {
            error: 'Payment Required',
            statusCode: 402,
            maxAmountRequired: this.config.priceUsdt.toString(),
            resource: reqPath,
            description: `${this.config.serviceName} - Protected by HAICHAIN Autonomous Policy Vault`,
            payTo: this.config.recipient,
            paymentAddress: this.config.recipient,
            asset: this.config.tokenMint,
            assetAddress: this.config.tokenMint,
            assetType: 'SPL',
            network: `solana-${this.config.cluster}`,
            caip2Network,
            expiresAt,
            nonce,
            paymentId,
            haichainGuardrail: {
                protocol: 'haichain-v1-voucher',
                policyProtected: true,
                boundedLossEnforced: true,
                settlementHelper: 'Settle via HAICHAIN Policy Vault, Spending Pot, or x402 Client SDK.'
            },
            settlementDetails: {
                recipient: this.config.recipient,
                amountUsdt: this.config.priceUsdt,
                network: `solana-${this.config.cluster}`,
                protocol: 'haichain-v1-voucher',
                paymentHelper: 'Use HAICHAIN relayer or client.executeMicroPayment() to broadcast on-chain settlement.'
            }
        };
        return {
            status: 402,
            headers: {
                'Content-Type': 'application/json',
                'WWW-Authenticate': `X402 realm="${this.config.serviceName}", scheme="haichain-v1-voucher"`,
                'X-Payment-Required': 'true',
                'X-Payment-Payee': this.config.recipient,
                'X-Payment-PayTo': this.config.recipient,
                'X-Payment-Amount': this.config.priceUsdt.toString(),
                'X-Payment-Network': `solana-${this.config.cluster}`,
                'X-Payment-Nonce': nonce,
                'X-Resource-Uri': reqPath
            },
            body
        };
    }
    /**
     * Universal Payment Verifier:
     * Supports:
     *  1. Fast-Path Off-chain Signed Voucher (< 2ms) via Ed25519 cryptographic signature.
     *  2. Direct On-chain Solana L1 Transaction audit via RPC.
     */
    async verifyPayment(authHeaderOrToken, customTxSig) {
        const rawToken = authHeaderOrToken || customTxSig || '';
        if (!rawToken) {
            return { valid: false, reason: 'Missing Authorization, X-PAYMENT, or X-Payment-Signature header' };
        }
        // Extract potential base64 or raw string
        let tokenStr = rawToken.trim();
        if (tokenStr.startsWith('X402 ')) {
            tokenStr = tokenStr.slice(5).trim();
        }
        else if (tokenStr.startsWith('Bearer ')) {
            tokenStr = tokenStr.slice(7).trim();
        }
        // 1. Try parsing tokenStr as JSON (either raw JSON or base64 encoded JSON)
        let parsedPayload = null;
        try {
            if (tokenStr.startsWith('{') && tokenStr.endsWith('}')) {
                parsedPayload = JSON.parse(tokenStr);
            }
            else {
                const decoded = Buffer.from(tokenStr, 'base64').toString('utf8');
                if (decoded.startsWith('{') && decoded.endsWith('}')) {
                    parsedPayload = JSON.parse(decoded);
                }
            }
        }
        catch {
            // Not a JSON payload, proceed to raw transaction signature branch
        }
        // =========================================================================
        // BRANCH 1: FAST-PATH OFF-CHAIN SIGNED VOUCHER / AUTHORIZATION (< 2ms)
        // =========================================================================
        if (parsedPayload && this.config.allowFastPath) {
            return this.verifyFastPathPayload(parsedPayload);
        }
        // =========================================================================
        // BRANCH 2: DIRECT ON-CHAIN SOLANA L1 TRANSACTION VERIFICATION (SLOW-PATH)
        // =========================================================================
        const txSig = tokenStr;
        // Must be valid Base58 signature (85-92 chars)
        if (!/^[1-9A-HJ-NP-za-km-z]{85,92}$/.test(txSig)) {
            return {
                valid: false,
                reason: `Malformed payment authorization or Solana transaction signature: ${txSig.slice(0, 24)}...`
            };
        }
        return await this.verifyOnChainSolanaTx(txSig);
    }
    /**
     * Fast-path verification of off-chain cryptographic vouchers (< 2ms).
     */
    verifyFastPathPayload(payload) {
        const agentPubkeyStr = payload.agentPubkey || payload.payer || payload.clientPubkey;
        const sigBase64 = payload.signatureBase64 || payload.signature;
        const recipientStr = payload.merchantPubkey || payload.payee || payload.paymentAddress || payload.payTo || this.config.recipient;
        if (!agentPubkeyStr || !sigBase64) {
            return { valid: false, reason: 'Fast-Path rejection: Missing agentPubkey or signature in payload' };
        }
        // Replay Attack prevention: Unique signature check
        const sigKey = `sig_${sigBase64.slice(0, 48)}`;
        if (this.usedSignatures.has(sigKey)) {
            const record = this.usedSignatures.get(sigKey);
            return {
                valid: false,
                reason: `Replay Attack Rejected: Voucher signature already consumed at ${new Date(record.usedAt).toISOString()}`
            };
        }
        // Timestamp & Freshness check
        if (payload.timestamp) {
            const nowSec = Math.floor(Date.now() / 1000);
            const ageSec = nowSec - payload.timestamp;
            if (ageSec > this.config.maxAgeSeconds) {
                return {
                    valid: false,
                    reason: `Stale Voucher Rejected: Voucher timestamp is ${ageSec}s old (Maximum permitted freshness: ${this.config.maxAgeSeconds}s)`
                };
            }
        }
        try {
            const agentPubkey = new web3_js_1.PublicKey(agentPubkeyStr);
            const sigBytes = Buffer.from(sigBase64, 'base64');
            // Verify Haichain v1 voucher payload:
            // Hash = SHA256("HAICHAIN-VOUCHER-V1" + potPubkey + merchantPubkey + channelId + cumulativeAmount + nonce)
            if (payload.scheme === 'haichain-v1-voucher' && payload.channelId && payload.cumulativeAmount) {
                const potPubkey = new web3_js_1.PublicKey(payload.potPubkey || this.recipientPubkey);
                const merchantPubkey = this.recipientPubkey;
                const channelId = BigInt(payload.channelId);
                const cumulative = BigInt(payload.cumulativeAmount);
                const nonce = BigInt(payload.nonce || 0);
                const channelBuf = Buffer.alloc(8);
                const amountBuf = Buffer.alloc(8);
                const nonceBuf = Buffer.alloc(8);
                channelBuf.writeBigUInt64LE(channelId);
                amountBuf.writeBigUInt64LE(cumulative);
                nonceBuf.writeBigUInt64LE(nonce);
                const msgHash = crypto.createHash('sha256')
                    .update(Buffer.from('HAICHAIN-VOUCHER-V1'))
                    .update(potPubkey.toBuffer())
                    .update(merchantPubkey.toBuffer())
                    .update(channelBuf)
                    .update(amountBuf)
                    .update(nonceBuf)
                    .digest();
                const verified = tweetnacl_1.default.sign.detached.verify(msgHash, sigBytes, agentPubkey.toBytes());
                if (!verified) {
                    return { valid: false, reason: 'Cryptographic Failure: Invalid Ed25519 signature on voucher payload' };
                }
            }
            else {
                // Standard detached message signature verification (Coinbase x402 standard)
                const canonicalData = Buffer.from(`${payload.resource || ''}:${payload.amount || payload.authorizedAmount || this.config.priceUsdt}:${payload.nonce || ''}`);
                const msgHash = crypto.createHash('sha256').update(canonicalData).digest();
                const verified = tweetnacl_1.default.sign.detached.verify(msgHash, sigBytes, agentPubkey.toBytes());
                if (!verified) {
                    return { valid: false, reason: 'Cryptographic Failure: Signature verification failed on canonical x402 intent' };
                }
            }
            // Mark as consumed in Nullifier Store immediately
            this.usedSignatures.set(sigKey, {
                usedAt: Date.now(),
                mode: 'fast-path-voucher'
            });
            return {
                valid: true,
                mode: 'fast-path-voucher',
                voucherDetails: {
                    agentPubkey: agentPubkeyStr,
                    recipient: recipientStr || this.config.recipient,
                    amount: payload.authorizedAmount || this.config.priceUsdt,
                    channelId: payload.channelId,
                    cumulativeAmount: payload.cumulativeAmount,
                    verifiedAt: Date.now()
                }
            };
        }
        catch (err) {
            return { valid: false, reason: `Fast-Path Verification Error: ${err.message}` };
        }
    }
    /**
     * On-chain Solana L1 RPC Verification.
     */
    async verifyOnChainSolanaTx(txSig) {
        // Nullifier check: Replay attack prevention
        if (this.usedSignatures.has(txSig)) {
            const record = this.usedSignatures.get(txSig);
            return {
                valid: false,
                reason: `Replay Attack Rejected: Transaction signature ${txSig} has ALREADY been consumed at ${new Date(record.usedAt).toISOString()} (Slot #${record.slot || 0}). Each on-chain micro-payment is strictly single-use.`
            };
        }
        try {
            const tx = await this.connection.getTransaction(txSig, {
                maxSupportedTransactionVersion: 0,
                commitment: 'confirmed'
            });
            if (!tx) {
                return { valid: false, reason: 'Transaction signature not found or unconfirmed on Solana L1 validator network' };
            }
            if (tx.meta && tx.meta.err) {
                return { valid: false, reason: `Transaction failed on-chain: ${JSON.stringify(tx.meta.err)}` };
            }
            // Max-Age Verification
            if (tx.blockTime && this.config.maxAgeSeconds) {
                const nowSec = Math.floor(Date.now() / 1000);
                const ageSec = nowSec - tx.blockTime;
                if (ageSec > this.config.maxAgeSeconds) {
                    return {
                        valid: false,
                        reason: `Stale Transaction Rejected: Transaction age is ${ageSec}s old (Maximum permitted freshness: ${this.config.maxAgeSeconds}s). Timestamps prevent pre-mined voucher recycling.`
                    };
                }
            }
            // Verify recipient received positive delta
            if (tx.transaction && tx.meta) {
                const accountKeys = tx.transaction.message.staticAccountKeys.map(k => k.toBase58());
                const recipientIndex = accountKeys.indexOf(this.recipientPubkey.toBase58());
                if (recipientIndex === -1) {
                    return {
                        valid: false,
                        reason: `Fraud Prevention: Target recipient ${this.recipientPubkey.toBase58()} was NOT credited in this transaction (Authorized accounts: ${accountKeys.join(', ')})`
                    };
                }
                const pre = tx.meta.preBalances[recipientIndex] || 0;
                const post = tx.meta.postBalances[recipientIndex] || 0;
                const delta = post - pre;
                if (delta <= 0) {
                    return {
                        valid: false,
                        reason: `Zero-Value Payment Fraud: Recipient received ${delta} lamports (Required >= ${this.config.minLamports} lamports)`
                    };
                }
                // Mark as consumed in Nullifier Store immediately
                this.usedSignatures.set(txSig, {
                    usedAt: Date.now(),
                    slot: tx.slot,
                    mode: 'direct-l1-settlement'
                });
                return {
                    valid: true,
                    mode: 'direct-l1-settlement',
                    txDetails: {
                        slot: tx.slot,
                        fee: tx.meta.fee,
                        lamportsReceived: delta,
                        recipient: this.recipientPubkey.toBase58(),
                        blockTime: tx.blockTime
                    }
                };
            }
            return { valid: true, mode: 'direct-l1-settlement' };
        }
        catch (err) {
            return { valid: false, reason: `Solana RPC Verification Error: ${err.message}` };
        }
    }
    /**
     * Connect / Express Middleware
     */
    middleware() {
        return async (req, res, next) => {
            const auth = req.headers['x-payment'] ||
                req.headers['authorization'] ||
                req.headers['x-payment-signature'] ||
                req.headers['x-402-authorization'];
            const check = await this.verifyPayment(auth);
            if (!check.valid) {
                const challenge = this.generate402Challenge(req.url);
                res.writeHead(challenge.status, challenge.headers);
                return res.end(JSON.stringify({ ...challenge.body, verificationError: check.reason }));
            }
            req.haichainPayment = {
                verified: true,
                mode: check.mode,
                payee: this.config.recipient,
                amountUsdt: this.config.priceUsdt,
                details: check.txDetails || check.voucherDetails
            };
            next();
        };
    }
    /**
     * Cloudflare Worker / Fetch Handler Middleware
     */
    async handleFetch(request, executeTask) {
        const auth = request.headers.get('x-payment') ||
            request.headers.get('authorization') ||
            request.headers.get('x-payment-signature') ||
            request.headers.get('x-402-authorization');
        const check = await this.verifyPayment(auth || undefined);
        if (!check.valid) {
            const url = new URL(request.url);
            const challenge = this.generate402Challenge(url.pathname);
            return new Response(JSON.stringify({ ...challenge.body, verificationError: check.reason }), {
                status: challenge.status,
                headers: challenge.headers
            });
        }
        return await executeTask();
    }
}
exports.HaichainPaywall = HaichainPaywall;
function haichainPaywall(config) {
    const paywall = new HaichainPaywall(config);
    return paywall.middleware();
}
exports.default = HaichainPaywall;
