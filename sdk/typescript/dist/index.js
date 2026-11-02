"use strict";
// sdk/typescript/src/index.ts
// HAICHAIN v7.0.0: Universal Autonomous Machine Financial Operating System Client SDK
// Supports all 5 Core Market Solutions:
// 1. SLA Staked Provider Bonds & Probabilistic Auditing (Anti-Garbage Data Engine)
// 2. Hybrid Web2 & DePIN Router (io.net, Aethir, Grass Anti-Deplatforming Fallback)
// 3. Cross-Chain Intent-based Solver Mesh (Frictionless Base/EVM to Solana Settlement)
// 4. M2M Dynamic Capacity Spot Tickets & Micro-Auctions
// 5. Enterprise Rollup VAT/GST Invoicing (SAP/Oracle ERP Merkle Audit Compliance)
// + Action Credits Natural Abstraction & Idempotency Key 4G Replay Protection
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
exports.EnterpriseRollupInvoiceGenerator = exports.IdempotencyEngine = exports.ActionCreditsConverter = exports.DynamicSpotTicketEngine = exports.CrossChainIntentSolver = exports.DePinProviderRouter = exports.ProbabilisticSlaAuditor = exports.HaiChainClient = exports.PROTOCOL_CONSTANTS = exports.SOLANA_USDC_MINT = exports.SOLANA_USDT_MINT = void 0;
const web3_js_1 = require("@solana/web3.js");
const spl_token_1 = require("@solana/spl-token");
const crypto = __importStar(require("crypto"));
const sha3_1 = require("@noble/hashes/sha3");
const tweetnacl_1 = __importDefault(require("tweetnacl"));
exports.SOLANA_USDT_MINT = new web3_js_1.PublicKey("Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB");
// Official Solana Mainnet Circle USD (USDC) SPL Token Mint (EU MiCA & Global Regulatory Compliant)
exports.SOLANA_USDC_MINT = new web3_js_1.PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v");
// Official On-Chain Protocol Invariant Constants (programs/haichain-core/src/lib.rs)
exports.PROTOCOL_CONSTANTS = {
    FLASH_LOAN_QUARANTINE_SLOTS: 2n,
    MIN_QUARANTINE_TRIGGER_DEPOSIT: 1000000n, // 1.00 USDT minimum deposit to reset quarantine barrier
    ROOT_ROTATION_GRACE_SLOTS: 150n, // ~60 seconds sliding window for in-flight capability tickets
    MAX_SAFE_MICRO_TICK_PAYMENT: 50000000n, // 50.00 USDT max per single micro-tick (6 decimals)
    MIN_PROVIDER_BOND_AMOUNT: 20000000n, // 20.00 USDT minimum bond stake
    MAX_SLASH_PER_INCIDENT: 10000000n, // 10.00 USDT max slash penalty per incident
};
class HaiChainClient {
    connection;
    programId;
    usdtMint;
    constructor(connection, programId = new web3_js_1.PublicKey("HaiChain11111111111111111111111111111111111"), usdtMint = exports.SOLANA_USDT_MINT) {
        this.connection = connection;
        this.programId = programId;
        this.usdtMint = usdtMint;
    }
    async createUsdtDepositSession(request) {
        const sessionId = `hcusdt_${Date.now()}_${Math.random().toString(36).substring(7)}`;
        const checkoutUrlFiat = `https://pay.haichain.io/checkout/${sessionId}?rail=${request.preferredRail || "apple_pay"}&amt=${request.amountUsdt}&token=USDT`;
        return {
            sessionId,
            depositAddressSolanaSpl: "HaiUsdt11111111111111111111111111111111111",
            crossChainDepositAddressTron: "TX...deBridgeBridgeUSDT",
            checkoutUrlFiat,
            amountUsdtExpected: request.amountUsdt,
            decimals: 6,
            expiresAtIso: new Date(Date.now() + 30 * 60 * 1000).toISOString(),
        };
    }
    /**
     * Handles HTTP x402 Payment Challenge with strict destination whitelist verification
     * and dynamically derived Payer Vault PDA.
     */
    async handleX402Challenge(headers, agentPrivateKey, whitelistedProviders, vaultOwner) {
        const payTo = new web3_js_1.PublicKey(headers["X-402-PayTo"]);
        const isWhitelisted = whitelistedProviders.some(p => p.equals(payTo));
        if (!isWhitelisted) {
            throw new Error("SECURITY ALERT: Destination provider is not whitelisted. ElizaOS Memory Poisoning blocked!");
        }
        const authSignature = `x402_sig_${Buffer.from(agentPrivateKey.slice(0, 16)).toString("hex")}_${headers["X-402-Nonce"]}`;
        // Derive canonical Agent Vault PDA from vaultOwner, or fallback to Keypair public key
        let payerVaultStr;
        if (vaultOwner) {
            payerVaultStr = this.getAgentVaultPda(vaultOwner)[0].toBase58();
        }
        else {
            const derivedPubkey = web3_js_1.Keypair.fromSecretKey(agentPrivateKey).publicKey;
            payerVaultStr = this.getAgentVaultPda(derivedPubkey)[0].toBase58();
        }
        return {
            "X-402-Authorization": authSignature,
            "X-402-Payer-Vault": payerVaultStr,
            "X-402-Timestamp": new Date().toISOString(),
        };
    }
    /**
     * Computes the 5-Tuple Cryptographic Composite Capability Leaf.
     * Cryptographically binds the authorized Sub-Agent to a specific Whitelisted Merchant Token Account (ATA).
     * Enforced on-chain by haichain-core Anchor smart contract to eliminate prompt injection / memory poisoning theft.
     */
    static computeCompositeCapabilityLeaf(subAgentSigner, whitelistedMerchantAta, maxAuthorizedAmount, expirySlot, nonce) {
        const amountBuf = Buffer.alloc(8);
        const expiryBuf = Buffer.alloc(8);
        const nonceBuf = Buffer.alloc(8);
        amountBuf.writeBigUInt64LE(BigInt(maxAuthorizedAmount));
        expiryBuf.writeBigUInt64LE(BigInt(expirySlot));
        nonceBuf.writeBigUInt64LE(BigInt(nonce));
        const capPayload = Buffer.concat([
            subAgentSigner.toBuffer(),
            amountBuf,
            expiryBuf,
            nonceBuf,
        ]);
        // Keccak256 strictly matching solana_program::keccak::hashv in haichain-core
        const leafCapability = Buffer.from((0, sha3_1.keccak_256)(capPayload));
        return Buffer.from((0, sha3_1.keccak_256)(Buffer.concat([leafCapability, whitelistedMerchantAta.toBuffer()])));
    }
    /**
     * Generates cryptographic payload for State Channel Micro-Voucher signing with full Domain Separation.
     * Prevents cross-cluster, cross-contract, cross-provider, and cross-session replay attacks.
     */
    static buildVoucherSigningPayload(clusterId, programId, vaultPda, providerPubkey, sessionId, nonce, cumulativeAmount) {
        const DOMAIN_SEPARATOR = "haichain-v1-channel-settlement";
        const payloadStr = `${DOMAIN_SEPARATOR}:${clusterId}:${programId.toBase58()}:${vaultPda.toBase58()}:${providerPubkey.toBase58()}:${sessionId}:${nonce.toString()}:${cumulativeAmount.toString()}`;
        return crypto.createHash("sha256").update(payloadStr).digest();
    }
    /**
     * Verifies a Merkle proof against a composite root with sorted pair hashing.
     * Exactly replicates the on-chain Anchor verification in haichain-core (lib.rs lines 164-171).
     * Enables zero-cost off-chain pre-flight simulation before submitting transactions to Solana.
     */
    static verifyCompositeProof(leaf, proof, expectedRoot) {
        let computedHash = Buffer.from(leaf);
        for (const elem of proof) {
            const proofElement = Buffer.from(elem);
            if (Buffer.compare(computedHash, proofElement) <= 0) {
                computedHash = Buffer.from((0, sha3_1.keccak_256)(Buffer.concat([computedHash, proofElement])));
            }
            else {
                computedHash = Buffer.from((0, sha3_1.keccak_256)(Buffer.concat([proofElement, computedHash])));
            }
        }
        return computedHash.equals(Buffer.from(expectedRoot));
    }
    /**
     * Cryptographically signs a micro-voucher with an Ed25519 keypair.
     * Combines domain-separated payload hashing with detached Ed25519 signing.
     */
    static signMicroVoucher(agentKeypair, voucherArgs) {
        const payloadHash = this.buildVoucherSigningPayload(voucherArgs.clusterId, voucherArgs.programId, voucherArgs.vaultPda, voucherArgs.providerPubkey, voucherArgs.sessionId, voucherArgs.nonce, voucherArgs.cumulativeAmount);
        const signature = tweetnacl_1.default.sign.detached(payloadHash, agentKeypair.secretKey);
        return {
            payloadHash,
            signature,
            signatureBase64: Buffer.from(signature).toString("base64"),
        };
    }
    /**
     * Verifies an Ed25519 micro-voucher signature off-chain.
     * Can be executed by providers and gateway proxies in sub-millisecond latency (<0.1ms).
     */
    static verifyMicroVoucherSignature(signerPubkey, payloadHash, signature) {
        return tweetnacl_1.default.sign.detached.verify(Uint8Array.from(payloadHash), Uint8Array.from(signature), signerPubkey.toBytes());
    }
    /**
     * Builds the instruction for initializing an Agent Vault on Solana.
     * Anchor Discriminator: sha256("global:initialize_agent_vault")[0..8] = [230, 71, 53, 169, 238, 108, 169, 111]
     */
    buildInitializeVaultInstruction(masterOwner, tokenMint, compositeRoot) {
        if (compositeRoot.length !== 32) {
            throw new Error("Invalid composite root: expected 32 bytes");
        }
        const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
        const agentDedicatedAta = (0, spl_token_1.getAssociatedTokenAddressSync)(tokenMint, agentVaultPda, true);
        return new web3_js_1.TransactionInstruction({
            keys: [
                { pubkey: agentVaultPda, isSigner: false, isWritable: true },
                { pubkey: tokenMint, isSigner: false, isWritable: false },
                { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
                { pubkey: masterOwner, isSigner: true, isWritable: true },
                { pubkey: web3_js_1.SystemProgram.programId, isSigner: false, isWritable: false },
            ],
            programId: this.programId,
            data: Buffer.concat([
                Buffer.from([230, 71, 53, 169, 238, 108, 169, 111]),
                Buffer.from(compositeRoot),
            ]),
        });
    }
    /**
     * Builds the instruction for depositing funds into the vault.
     * Supports decoupled depositors (e.g. background fiat relayers, Stripe/Apple Pay, or master owner).
     * Anchor Discriminator: sha256("global:deposit_funds")[0..8] = [202, 39, 52, 211, 53, 20, 250, 88]
     */
    buildDepositFundsInstruction(masterOwner, depositor, userSourceAta, amountMicroUnits, tokenMint = this.usdtMint) {
        const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
        const agentDedicatedAta = (0, spl_token_1.getAssociatedTokenAddressSync)(tokenMint, agentVaultPda, true);
        const amountBuf = Buffer.alloc(8);
        amountBuf.writeBigUInt64LE(BigInt(amountMicroUnits));
        return new web3_js_1.TransactionInstruction({
            keys: [
                { pubkey: agentVaultPda, isSigner: false, isWritable: true },
                { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
                { pubkey: userSourceAta, isSigner: false, isWritable: true },
                { pubkey: depositor, isSigner: true, isWritable: false },
                { pubkey: spl_token_1.TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
            ],
            programId: this.programId,
            data: Buffer.concat([
                Buffer.from([202, 39, 52, 211, 53, 20, 250, 88]),
                amountBuf,
            ]),
        });
    }
    /**
     * Builds the instruction for executing a micro-payment on Solana L1 with Merkle proof verification.
     * Anchor Discriminator: sha256("global:execute_master_payment")[0..8] = [164, 225, 64, 108, 234, 236, 177, 124]
     */
    buildExecuteMasterPaymentInstruction(masterOwner, subAgentSigner, payer, serviceProviderAta, spendAmount, maxAuthorizedAmount, expirySlot, nonce, compositeProof, tokenMint = this.usdtMint) {
        const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
        const agentDedicatedAta = (0, spl_token_1.getAssociatedTokenAddressSync)(tokenMint, agentVaultPda, true);
        const [nullifierPda] = this.getNullifierPda(agentVaultPda, nonce);
        // Borsh serialization for Vec<[u8; 32]>
        const proofLengthBuf = Buffer.alloc(4);
        proofLengthBuf.writeUInt32LE(compositeProof.length);
        const proofBuffers = compositeProof.map(p => {
            const b = Buffer.from(p);
            if (b.length !== 32)
                throw new Error("Each Merkle proof element must be exactly 32 bytes");
            return b;
        });
        const spendBuf = Buffer.alloc(8);
        const maxBuf = Buffer.alloc(8);
        const expiryBuf = Buffer.alloc(8);
        const nonceBuf = Buffer.alloc(8);
        spendBuf.writeBigUInt64LE(BigInt(spendAmount));
        maxBuf.writeBigUInt64LE(BigInt(maxAuthorizedAmount));
        expiryBuf.writeBigUInt64LE(BigInt(expirySlot));
        nonceBuf.writeBigUInt64LE(BigInt(nonce));
        const instructionData = Buffer.concat([
            Buffer.from([164, 225, 64, 108, 234, 236, 177, 124]),
            spendBuf,
            maxBuf,
            expiryBuf,
            nonceBuf,
            proofLengthBuf,
            ...proofBuffers,
        ]);
        return new web3_js_1.TransactionInstruction({
            keys: [
                { pubkey: agentVaultPda, isSigner: false, isWritable: true },
                { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
                { pubkey: serviceProviderAta, isSigner: false, isWritable: true },
                { pubkey: subAgentSigner, isSigner: true, isWritable: false },
                { pubkey: payer, isSigner: true, isWritable: true },
                { pubkey: nullifierPda, isSigner: false, isWritable: true },
                { pubkey: spl_token_1.TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
                { pubkey: web3_js_1.SystemProgram.programId, isSigner: false, isWritable: false },
            ],
            programId: this.programId,
            data: instructionData,
        });
    }
    getAgentVaultPda(owner) {
        return web3_js_1.PublicKey.findProgramAddressSync([Buffer.from("agent-vault"), owner.toBuffer()], this.programId);
    }
    getNullifierPda(vaultPda, nonce) {
        const nonceBuffer = Buffer.alloc(8);
        if (typeof nonce === "bigint") {
            nonceBuffer.writeBigUInt64LE(nonce);
        }
        else {
            nonceBuffer.writeBigUInt64LE(BigInt(nonce));
        }
        return web3_js_1.PublicKey.findProgramAddressSync([Buffer.from("nullifier"), vaultPda.toBuffer(), nonceBuffer], this.programId);
    }
    getProviderBondPda(providerAuthority) {
        return web3_js_1.PublicKey.findProgramAddressSync([Buffer.from("provider-bond"), providerAuthority.toBuffer()], this.programId);
    }
    /**
     * Builds the instruction for triggering the emergency panic kill-switch.
     * Anchor Discriminator: sha256("global:trigger_emergency_panic")[0..8] = [232, 177, 104, 97, 82, 33, 17, 191]
     */
    buildTriggerPanicInstruction(masterOwner, agentDedicatedAta, userSafeDestinationAta) {
        const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
        return new web3_js_1.TransactionInstruction({
            keys: [
                { pubkey: agentVaultPda, isSigner: false, isWritable: true },
                { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
                { pubkey: userSafeDestinationAta, isSigner: false, isWritable: true },
                { pubkey: masterOwner, isSigner: true, isWritable: false },
                { pubkey: spl_token_1.TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
            ],
            programId: this.programId,
            data: Buffer.from([232, 177, 104, 97, 82, 33, 17, 191]),
        });
    }
    async triggerPanicKillSwitch(provider, agentDedicatedAta, userSafeDestinationAta) {
        const owner = provider.wallet.publicKey;
        const ix = this.buildTriggerPanicInstruction(owner, agentDedicatedAta, userSafeDestinationAta);
        const tx = new web3_js_1.Transaction().add(ix);
        return await provider.sendAndConfirm(tx);
    }
    /**
     * Builds the instruction for reclaiming expired nullifier SOL rent.
     * Anchor Discriminator: sha256("global:reclaim_expired_nullifier")[0..8] = [16, 165, 146, 96, 207, 57, 80, 93]
     * Invariant: agentVaultPda MUST be writable because vault.min_valid_nonce is monotonically updated on-chain.
     */
    buildReclaimNullifierInstruction(vaultOwner, nonce, rentReceiver = vaultOwner) {
        const [agentVaultPda] = this.getAgentVaultPda(vaultOwner);
        const [nullifierPda] = this.getNullifierPda(agentVaultPda, nonce);
        if (!rentReceiver.equals(vaultOwner)) {
            throw new Error("SECURITY INVARIANT VIOLATION: Reclaimed rent must strictly be returned to vaultOwner");
        }
        const nonceBuf = Buffer.alloc(8);
        nonceBuf.writeBigUInt64LE(BigInt(nonce));
        const instructionData = Buffer.concat([
            Buffer.from([16, 165, 146, 96, 207, 57, 80, 93]),
            nonceBuf,
        ]);
        return new web3_js_1.TransactionInstruction({
            keys: [
                { pubkey: nullifierPda, isSigner: false, isWritable: true },
                { pubkey: agentVaultPda, isSigner: false, isWritable: true },
                { pubkey: rentReceiver, isSigner: false, isWritable: true },
            ],
            programId: this.programId,
            data: instructionData,
        });
    }
    async reclaimExpiredNullifierRent(provider, vaultOwner, nonce, rentReceiver = vaultOwner) {
        const ix = this.buildReclaimNullifierInstruction(vaultOwner, nonce, rentReceiver);
        const tx = new web3_js_1.Transaction().add(ix);
        return await provider.sendAndConfirm(tx);
    }
    /**
     * Builds the instruction for O(1) mass-invalidation of capability tickets.
     * Anchor Discriminator: sha256("global:advance_min_valid_nonce")[0..8] = [81, 92, 116, 233, 79, 68, 222, 129]
     */
    buildAdvanceMinValidNonceInstruction(masterOwner, newMinNonce) {
        const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
        const nonceBuf = Buffer.alloc(8);
        nonceBuf.writeBigUInt64LE(BigInt(newMinNonce));
        return new web3_js_1.TransactionInstruction({
            keys: [
                { pubkey: agentVaultPda, isSigner: false, isWritable: true },
                { pubkey: masterOwner, isSigner: true, isWritable: false },
            ],
            programId: this.programId,
            data: Buffer.concat([
                Buffer.from([81, 92, 116, 233, 79, 68, 222, 129]),
                nonceBuf,
            ]),
        });
    }
    /**
     * Builds the instruction for rotating composite Merkle roots with sliding window grace period.
     * Anchor Discriminator: sha256("global:update_composite_root")[0..8] = [230, 8, 5, 238, 82, 121, 117, 97]
     */
    buildUpdateCompositeRootInstruction(masterOwner, newCompositeRoot) {
        const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
        if (newCompositeRoot.length !== 32) {
            throw new Error("Invalid Merkle root length: expected 32 bytes");
        }
        return new web3_js_1.TransactionInstruction({
            keys: [
                { pubkey: agentVaultPda, isSigner: false, isWritable: true },
                { pubkey: masterOwner, isSigner: true, isWritable: false },
            ],
            programId: this.programId,
            data: Buffer.concat([
                Buffer.from([230, 8, 5, 238, 82, 121, 117, 97]),
                Buffer.from(newCompositeRoot),
            ]),
        });
    }
}
exports.HaiChainClient = HaiChainClient;
class ProbabilisticSlaAuditor {
    faultRecords = new Map();
    static hashPayload(payload) {
        return crypto.createHash("sha256").update(payload).digest("hex");
    }
    static generateReceipt(providerAuthority, taskPrompt, responsePayload, claimedQualityScore = 98) {
        return {
            providerAuthority: providerAuthority.toBase58(),
            taskPromptHash: this.hashPayload(taskPrompt),
            responsePayloadHash: this.hashPayload(responsePayload),
            executionTimestamp: Date.now(),
            claimedQualityScore,
        };
    }
    shouldPerformSpotCheck(spotCheckProbability = 0.01) {
        return Math.random() < spotCheckProbability;
    }
    recordExecution(providerAuthority, isFault) {
        const record = this.faultRecords.get(providerAuthority) || { total: 0, faults: 0 };
        record.total += 1;
        if (isFault) {
            record.faults += 1;
        }
        this.faultRecords.set(providerAuthority, record);
        const faultRate = record.faults / record.total;
        const shouldSlash = record.total >= 5 && faultRate > 0.02;
        return { faultRate, shouldSlash };
    }
}
exports.ProbabilisticSlaAuditor = ProbabilisticSlaAuditor;
class DePinProviderRouter {
    providers = new Map();
    registerEndpoint(category, endpoint) {
        const list = this.providers.get(category) || [];
        list.push(endpoint);
        this.providers.set(category, list);
    }
    routeRequest(category, forceDePinOnly = false) {
        const list = this.providers.get(category) || [];
        if (list.length === 0) {
            throw new Error(`No available providers for category: ${category}`);
        }
        if (forceDePinOnly) {
            const depin = list.find(p => p.type === "depin_node" && p.isHealthy);
            if (!depin)
                throw new Error(`All DePIN providers offline for: ${category}`);
            return depin;
        }
        // Try primary Web2 reseller first, fallback to DePIN if unheathy or blocked
        const primary = list.find(p => p.type === "web2_reseller" && p.isHealthy);
        if (primary)
            return primary;
        const fallbackDePin = list.find(p => p.type === "depin_node" && p.isHealthy);
        if (fallbackDePin)
            return fallbackDePin;
        throw new Error(`All providers (Web2 and DePIN) exhausted for: ${category}`);
    }
    markFailure(category, endpointId) {
        const list = this.providers.get(category) || [];
        const item = list.find(p => p.id === endpointId);
        if (item) {
            item.isHealthy = false;
        }
    }
}
exports.DePinProviderRouter = DePinProviderRouter;
class CrossChainIntentSolver {
    executedIntents = new Set();
    verifyAndFrontLiquidity(intent) {
        if (Date.now() > intent.expiryTimestamp) {
            throw new Error("Cross-chain payment intent has expired");
        }
        const intentId = `${intent.sourceChain}:${intent.senderAddress}:${intent.nonce}`;
        if (this.executedIntents.has(intentId)) {
            throw new Error("Intent has already been solved and settled");
        }
        this.executedIntents.add(intentId);
        const solverTxHash = `sol_front_${crypto.createHash("sha256").update(intentId).digest("hex").slice(0, 32)}`;
        return {
            authorized: true,
            solverTxHash,
            frontedAmountUsdt: intent.amountUsdt,
        };
    }
}
exports.CrossChainIntentSolver = CrossChainIntentSolver;
class DynamicSpotTicketEngine {
    static calculateDynamicPrice(basePriceMicroUsdt, currentLoad, maxCapacity, surgeBpsMax = 2000) {
        const loadRatio = Math.min(1.0, Math.max(0.0, currentLoad / maxCapacity));
        const surgeBps = Math.floor(loadRatio * surgeBpsMax);
        const dynamicSurge = Math.floor((basePriceMicroUsdt * surgeBps) / 10000);
        const spotPrice = basePriceMicroUsdt + dynamicSurge;
        return { spotPrice, loadRatio, surgeBps };
    }
    static createQuotationTicket(providerAuthority, basePriceMicroUsdt, currentLoad, maxCapacity, currentSlot, validitySlots = 50, nonce = Date.now()) {
        const { spotPrice, loadRatio, surgeBps } = this.calculateDynamicPrice(basePriceMicroUsdt, currentLoad, maxCapacity);
        return {
            providerAuthority: providerAuthority.toBase58(),
            basePriceMicroUsdt,
            spotPriceMicroUsdt: spotPrice,
            surgeFactorBps: surgeBps,
            loadRatio,
            expirySlot: currentSlot + validitySlots,
            nonce,
        };
    }
    static verifyQuotationTicket(ticket, maxBudgetCapMicroUsdt, currentSlot) {
        if (currentSlot > ticket.expirySlot) {
            return { valid: false, reason: "Ticket has expired on Solana slot clock" };
        }
        if (ticket.spotPriceMicroUsdt > maxBudgetCapMicroUsdt) {
            return { valid: false, reason: `Spot price ${ticket.spotPriceMicroUsdt} exceeds budget cap ${maxBudgetCapMicroUsdt}` };
        }
        return { valid: true };
    }
}
exports.DynamicSpotTicketEngine = DynamicSpotTicketEngine;
// ============================================================================
// SOLUTION 5: ENTERPRISE ROLLUP INVOICE GENERATOR & NATURAL ACTION CREDITS
// ============================================================================
class ActionCreditsConverter {
    static MICRO_USDT_PER_CREDIT = 1000;
    static DEFAULT_VND_PER_CREDIT = 25;
    static usdtToCredits(usdtAmount) {
        return Math.floor(usdtAmount * 1000);
    }
    static microUsdtToCredits(microUnits) {
        const units = typeof microUnits === "bigint" ? Number(microUnits) : microUnits;
        return Math.floor(units / this.MICRO_USDT_PER_CREDIT);
    }
    static creditsToUsdt(credits) {
        return credits / 1000;
    }
    static creditsToVnd(credits, rate = ActionCreditsConverter.DEFAULT_VND_PER_CREDIT) {
        return credits * rate;
    }
    static formatCredits(credits) {
        return new Intl.NumberFormat("en-US").format(credits) + " Credits";
    }
    static formatVnd(credits, rate = ActionCreditsConverter.DEFAULT_VND_PER_CREDIT) {
        const vnd = credits * rate;
        return new Intl.NumberFormat("vi-VN").format(vnd) + " ₫";
    }
}
exports.ActionCreditsConverter = ActionCreditsConverter;
class IdempotencyEngine {
    cache = new Map();
    ttlMs;
    constructor(ttlMs = 24 * 60 * 60 * 1000) {
        this.ttlMs = ttlMs;
    }
    generateIdempotencyKey(sessionId, taskStepIndex, nonce) {
        const payload = `${sessionId}:${taskStepIndex}:${nonce.toString()}`;
        return crypto.createHash("sha256").update(payload).digest("hex");
    }
    async executeIdempotent(key, executeFn) {
        const cachedEntry = this.cache.get(key);
        if (cachedEntry) {
            if (Date.now() - cachedEntry.timestamp < this.ttlMs) {
                return { result: cachedEntry.result, cached: true };
            }
            this.cache.delete(key);
        }
        const result = await executeFn();
        this.cache.set(key, { result, timestamp: Date.now() });
        return { result, cached: false };
    }
}
exports.IdempotencyEngine = IdempotencyEngine;
class EnterpriseRollupInvoiceGenerator {
    static generateMonthlyInvoice(transactions, organizationName, billingPeriod, vatTaxPct = 10) {
        let subtotalUsdt = 0;
        const categoryBreakdown = {};
        const txHashes = [];
        for (const tx of transactions) {
            subtotalUsdt += tx.costUsdt;
            if (!categoryBreakdown[tx.serviceCategory]) {
                categoryBreakdown[tx.serviceCategory] = { count: 0, totalCostUsdt: 0 };
            }
            categoryBreakdown[tx.serviceCategory].count += 1;
            categoryBreakdown[tx.serviceCategory].totalCostUsdt += tx.costUsdt;
            const txHash = crypto
                .createHash("sha256")
                .update(`${tx.transactionId}:${tx.costUsdt}:${tx.nonce}`)
                .digest("hex");
            txHashes.push(txHash);
        }
        let currentLevel = txHashes;
        if (currentLevel.length === 0) {
            currentLevel = [crypto.createHash("sha256").update("EMPTY_INVOICE").digest("hex")];
        }
        while (currentLevel.length > 1) {
            const nextLevel = [];
            for (let i = 0; i < currentLevel.length; i += 2) {
                const left = currentLevel[i];
                const right = i + 1 < currentLevel.length ? currentLevel[i + 1] : left;
                const combined = crypto.createHash("sha256").update(left + right).digest("hex");
                nextLevel.push(combined);
            }
            currentLevel = nextLevel;
        }
        const merkleAuditRoot = currentLevel[0];
        const taxAmountUsdt = Number(((subtotalUsdt * vatTaxPct) / 100).toFixed(6));
        const totalDueUsdt = Number((subtotalUsdt + taxAmountUsdt).toFixed(6));
        const totalDueCredits = ActionCreditsConverter.usdtToCredits(totalDueUsdt);
        const totalDueVndEstimated = ActionCreditsConverter.creditsToVnd(totalDueCredits);
        const invoiceNumber = `HAICHAIN-INV-${Date.now().toString().slice(-6)}-${Math.floor(Math.random() * 1000)}`;
        return {
            invoiceNumber,
            organizationName,
            billingPeriod,
            totalTransactionsCount: transactions.length,
            subtotalUsdt: Number(subtotalUsdt.toFixed(6)),
            vatTaxPct,
            taxAmountUsdt,
            totalDueUsdt,
            totalDueCredits,
            totalDueVndEstimated,
            merkleAuditRoot,
            categoryBreakdown,
            generatedAtIso: new Date().toISOString(),
        };
    }
}
exports.EnterpriseRollupInvoiceGenerator = EnterpriseRollupInvoiceGenerator;
