import { PolicyEngine } from "./policy-engine";
export interface X402Challenge {
    payee: string;
    mint: string;
    amountMicroUnits: string;
    scheme: "haichain-v1-voucher";
    resource: string;
    expires: number;
}
export interface X402AuthorizationHeader {
    scheme: "haichain-v1-voucher";
    channelId: string;
    cumulativeAmount: string;
    signatureBase64: string;
    agentPubkey: string;
    potPubkey: string;
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
     * Parses the HTTP 402 challenge header from merchant response.
     */
    static parseChallenge(headerValue: string): X402Challenge;
    /**
     * Processes an HTTP 402 challenge against the isolated PolicyEngine and generates
     * the authorization header with a monotonically signed voucher.
     */
    generatePaymentResponse(challenge: X402Challenge, leafHashHex: string, channelId: bigint, scopeClass: number): {
        headers: Record<string, string>;
        authorizedAmount: bigint;
    };
    /**
     * Verifies the receipt delivered by the merchant after fulfilling the resource stream.
     */
    verifyDeliveryReceipt(receipt: X402DeliveryReceipt, expectedResource: string): boolean;
}
