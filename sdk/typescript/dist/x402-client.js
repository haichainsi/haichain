"use strict";
// sdk/typescript/src/x402-client.ts
// HAICHAIN v1.1 - HTTP x402 Micro-Payment Client Protocol Engine
// Standardized RFC-compliant implementation of autonomous machine payment handshakes.
Object.defineProperty(exports, "__esModule", { value: true });
exports.X402Client = void 0;
const web3_js_1 = require("@solana/web3.js");
class X402Client {
    policyEngine;
    constructor(policyEngine) {
        this.policyEngine = policyEngine;
    }
    /**
     * Parses the HTTP 402 challenge header from merchant response.
     */
    static parseChallenge(headerValue) {
        try {
            const parsed = JSON.parse(headerValue);
            if (parsed.scheme !== "haichain-v1-voucher") {
                throw new Error(`Unsupported payment scheme: ${parsed.scheme}`);
            }
            return parsed;
        }
        catch (e) {
            throw new Error(`Invalid x402 challenge format: ${e.message}`);
        }
    }
    /**
     * Processes an HTTP 402 challenge against the isolated PolicyEngine and generates
     * the authorization header with a monotonically signed voucher.
     */
    generatePaymentResponse(challenge, leafHashHex, channelId, scopeClass) {
        const intent = {
            resource: challenge.resource,
            maxAmount: BigInt(challenge.amountMicroUnits),
            merchant: new web3_js_1.PublicKey(challenge.payee),
            mint: new web3_js_1.PublicKey(challenge.mint),
            scopeClass,
        };
        const auth = this.policyEngine.evaluateAndAuthorize(intent, leafHashHex, channelId);
        const authPayload = {
            scheme: "haichain-v1-voucher",
            channelId: channelId.toString(),
            cumulativeAmount: auth.cumulativeVoucherAmount.toString(),
            signatureBase64: Buffer.from(auth.signature).toString("base64"),
            agentPubkey: this.policyEngine.getAgentPublicKey().toBase58(),
            potPubkey: intent.merchant.toBase58(), // Referenced merchant binding
        };
        return {
            headers: {
                "Authorization": `X402 ${JSON.stringify(authPayload)}`,
                "X-Haichain-Voucher-Amount": auth.authorizedAmount.toString(),
                "X-Haichain-Cumulative": auth.cumulativeVoucherAmount.toString(),
            },
            authorizedAmount: auth.authorizedAmount,
        };
    }
    /**
     * Verifies the receipt delivered by the merchant after fulfilling the resource stream.
     */
    verifyDeliveryReceipt(receipt, expectedResource) {
        if (receipt.resource !== expectedResource) {
            throw new Error("RECEIPT MISMATCH: Provider delivered receipt for wrong resource URI");
        }
        if (receipt.bytesDelivered <= 0) {
            throw new Error("RECEIPT ANOMALY: Zero bytes delivered for paid request");
        }
        return true;
    }
}
exports.X402Client = X402Client;
