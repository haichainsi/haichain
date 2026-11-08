import { PolicyEngine } from "./policy-engine";
export interface X402Challenge {
    payee: string;
    mint: string;
    amountMicroUnits: string;
    amountUsd: number;
    scheme: "haichain-v1-voucher" | "x402-rfc" | string;
    resource: string;
    network: string;
    expires: number;
    nonce: string;
    paymentId?: string;
    rawPayload?: any;
}
export interface X402AuthorizationHeader {
    scheme: "haichain-v1-voucher" | "x402-rfc";
    channelId: string;
    cumulativeAmount: string;
    signatureBase64: string;
    agentPubkey: string;
    potPubkey: string;
    merchantPubkey?: string;
    nonce?: string;
    timestamp?: number;
    authorizedAmount?: string;
    resource?: string;
}
export interface X402DeliveryReceipt {
    resource: string;
    bytesDelivered: number;
    providerSignature: string;
    cumulativePaid: string;
}
export declare class X402Client {
    private policyEngine;
    constructor(policyEngine: PolicyEngine);
    /**
     * Universal parser for HTTP 402 challenge payloads.
     * Gracefully parses both Coinbase x402 JSON format and HAICHAIN native voucher challenges.
     */
    static parseChallenge(input: string | any): X402Challenge;
    /**
     * Evaluates an HTTP 402 challenge against the isolated PolicyEngine and generates
     * dual-compatible headers:
     * 1. "X-PAYMENT" (Base64 JSON): Standard x402 Header for Coinbase specification.
     * 2. "Authorization": "X402 <base64>" RFC compliant HTTP Authorization.
     * 3. HAICHAIN telemetry headers.
     */
    generatePaymentResponse(challenge: X402Challenge, leafHashHex: string, channelId: bigint, scopeClass: number): {
        headers: Record<string, string>;
        authorizedAmount: bigint;
        authPayload: X402AuthorizationHeader;
    };
    /**
     * Verifies the receipt delivered by the merchant after fulfilling the resource stream.
     */
    verifyDeliveryReceipt(receipt: X402DeliveryReceipt, expectedResource: string): boolean;
}
