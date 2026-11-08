"use strict";
// sdk/typescript/src/policy-engine.ts
// HAICHAIN v1.1 - Out-of-Process Policy Engine & Key Isolation Sandbox
// Implements Zero-Knowledge Session Key Security: LLM never sees private keys.
// Enforces Per-Domain Rate Limiting & Anti-Prompt-Injection Micro-Loop Protection.
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
exports.PolicyEngine = void 0;
const crypto = __importStar(require("crypto"));
const tweetnacl_1 = __importDefault(require("tweetnacl"));
const capleaf_1 = require("./capleaf");
class PolicyEngine {
    agentKeypair;
    activeGrants = new Map();
    domainThrottles = new Map();
    cumulativeSpendPerChannel = new Map();
    // Red-Team Safety Thresholds
    static PROBATION_MAX_CALLS_PER_WINDOW = 3;
    static PROBATION_WINDOW_SECONDS = 600; // 10 minutes
    constructor(agentKeypair) {
        this.agentKeypair = agentKeypair;
    }
    getAgentPublicKey() {
        return this.agentKeypair.publicKey;
    }
    registerActiveGrant(leaf) {
        const leafBytes = capleaf_1.CapLeafV1Engine.serialize(leaf);
        const leafHashHex = crypto.createHash("sha256").update(leafBytes).digest("hex");
        this.activeGrants.set(leafHashHex, leaf);
    }
    /**
     * Evaluates an LLM's proposed PaymentIntent against ActiveGrants, hard limits, and domain throttles.
     * Throws an error if any invariant is violated (Fail-Closed principle).
     */
    evaluateAndAuthorize(intent, leafHashHex, channelId, now = Math.floor(Date.now() / 1000)) {
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
        this.enforceDomainRateLimit(domain, (grant.flags & capleaf_1.CapLeafFlags.PROBATION) !== 0, now);
        // 4b. TEE Co-Signer Invariant Enforcement (bit REQUIRE_COSIGN)
        if ((grant.flags & capleaf_1.CapLeafFlags.REQUIRE_COSIGN) !== 0) {
            if (!intent.cosignerSignature || !intent.cosignerPublicKey) {
                throw new Error("SECURITY ALERT: CapLeaf requires TEE Co-Signer attestation, but no co-signature was provided");
            }
            const cosignPayload = PolicyEngine.buildCosignPayload(grant.pot, grant.merchant, channelId, intent.maxAmount, grant.nonce);
            const isCosignValid = tweetnacl_1.default.sign.detached.verify(cosignPayload, intent.cosignerSignature, intent.cosignerPublicKey.toBytes());
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
        const signature = tweetnacl_1.default.sign.detached(voucherPayload, this.agentKeypair.secretKey);
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
    verifyServicePayload(payload) {
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
    enforceDomainRateLimit(domain, isProbation, now) {
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
            throw new Error(`RATE LIMIT BREACH: Domain ${domain} under PROBATION exceeded ${PolicyEngine.PROBATION_MAX_CALLS_PER_WINDOW} calls per 10m window. Blocked against Prompt Injection loop!`);
        }
        record.callTimestamps.push(now);
        record.lastCallTime = now;
    }
    extractDomainFromResource(resource) {
        try {
            const url = new URL(resource);
            return url.hostname;
        }
        catch {
            return resource.split("/")[0] || "unknown";
        }
    }
    static buildCosignPayload(potPubkey, merchantPubkey, channelId, amount, nonce) {
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
    static buildVoucherPayload(pot, merchant, channelId, cumulativeAmount, nonce) {
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
    static verifyVoucherSignature(agentPubkey, pot, merchant, channelId, cumulativeAmount, nonce, signature) {
        const payload = PolicyEngine.buildVoucherPayload(pot, merchant, channelId, cumulativeAmount, nonce);
        return tweetnacl_1.default.sign.detached.verify(payload, signature, agentPubkey.toBytes());
    }
}
exports.PolicyEngine = PolicyEngine;
