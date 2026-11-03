// sdk/typescript/src/x402-client.ts
// HAICHAIN v1.1 - HTTP x402 Micro-Payment Client Protocol Engine
// Standardized RFC-compliant implementation of autonomous machine payment handshakes.

import { PublicKey } from "@solana/web3.js";
import { PolicyEngine, PaymentIntent } from "./policy-engine";
import { CapLeafV1 } from "./capleaf";

export interface X402Challenge {
  payee: string;           // Merchant recipient Pubkey
  mint: string;            // SPL token mint (USDT / USDC)
  amountMicroUnits: string;// Micro-units demanded (e.g. "2000" = 0.002 USDT)
  scheme: "haichain-v1-voucher";
  resource: string;        // Canonical URI endpoint
  expires: number;         // Unix timestamp seconds
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

export class X402Client {
  private policyEngine: PolicyEngine;

  constructor(policyEngine: PolicyEngine) {
    this.policyEngine = policyEngine;
  }

  /**
   * Parses the HTTP 402 challenge header from merchant response.
   */
  public static parseChallenge(headerValue: string): X402Challenge {
    try {
      const parsed = JSON.parse(headerValue);
      if (parsed.scheme !== "haichain-v1-voucher") {
        throw new Error(`Unsupported payment scheme: ${parsed.scheme}`);
      }
      return parsed;
    } catch (e: any) {
      throw new Error(`Invalid x402 challenge format: ${e.message}`);
    }
  }

  /**
   * Processes an HTTP 402 challenge against the isolated PolicyEngine and generates
   * the authorization header with a monotonically signed voucher.
   */
  public generatePaymentResponse(
    challenge: X402Challenge,
    leafHashHex: string,
    channelId: bigint,
    scopeClass: number
  ): { headers: Record<string, string>; authorizedAmount: bigint } {
    const intent: PaymentIntent = {
      resource: challenge.resource,
      maxAmount: BigInt(challenge.amountMicroUnits),
      merchant: new PublicKey(challenge.payee),
      mint: new PublicKey(challenge.mint),
      scopeClass,
    };

    const auth = this.policyEngine.evaluateAndAuthorize(intent, leafHashHex, channelId);

    const authPayload: X402AuthorizationHeader = {
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
  public verifyDeliveryReceipt(receipt: X402DeliveryReceipt, expectedResource: string): boolean {
    if (receipt.resource !== expectedResource) {
      throw new Error("RECEIPT MISMATCH: Provider delivered receipt for wrong resource URI");
    }
    if (receipt.bytesDelivered <= 0) {
      throw new Error("RECEIPT ANOMALY: Zero bytes delivered for paid request");
    }
    return true;
  }
}
