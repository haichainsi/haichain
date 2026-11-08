// sdk/typescript/src/x402-client.ts
// HAICHAIN v1.1 - HTTP x402 Micro-Payment Client & Guardrail Protocol Engine
// Standardized RFC-compliant implementation of autonomous machine payment handshakes.
// Fully interoperable with Coinbase x402 Specification and HAICHAIN Policy Vault.

import { PublicKey } from "@solana/web3.js";
import { PolicyEngine, PaymentIntent } from "./policy-engine";
import { CapLeafV1 } from "./capleaf";

export interface X402Challenge {
  payee: string;           // Merchant recipient Pubkey / address
  mint: string;            // SPL token mint / token contract address
  amountMicroUnits: string;// Micro-units demanded (e.g. "3000" = 0.003 USDT)
  amountUsd: number;       // Amount in USD/USDT (e.g. 0.003)
  scheme: "haichain-v1-voucher" | "x402-rfc" | string;
  resource: string;        // Canonical URI endpoint
  network: string;         // e.g. "solana-devnet", "solana-mainnet-beta"
  expires: number;         // Unix timestamp seconds
  nonce: string;           // Cryptographic nonce against replay
  paymentId?: string;      // Unique challenge identifier
  rawPayload?: any;        // Original server challenge
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

export class X402Client {
  private policyEngine: PolicyEngine;

  constructor(policyEngine: PolicyEngine) {
    this.policyEngine = policyEngine;
  }

  /**
   * Universal parser for HTTP 402 challenge payloads.
   * Gracefully parses both Coinbase x402 JSON format and HAICHAIN native voucher challenges.
   */
  public static parseChallenge(input: string | any): X402Challenge {
    try {
      let parsed: any;
      if (typeof input === "string") {
        const trimmed = input.trim();
        // Check if input is JSON
        if (trimmed.startsWith("{") && trimmed.endsWith("}")) {
          parsed = JSON.parse(trimmed);
        } else if (trimmed.startsWith("X402 ") || trimmed.includes("realm=")) {
          // Parse WWW-Authenticate parameter style
          parsed = {};
          const matches = trimmed.matchAll(/(\w+)="([^"]+)"/g);
          for (const match of matches) {
            parsed[match[1]] = match[2];
          }
        } else {
          parsed = JSON.parse(trimmed);
        }
      } else {
        parsed = input;
      }

      // Universal field normalizer:
      const payee = parsed.payTo || parsed.paymentAddress || parsed.payee || parsed.recipient || "";
      if (!payee) {
        throw new Error("Missing recipient payee address in x402 challenge");
      }

      const mint = parsed.assetAddress || parsed.asset || parsed.mint || "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB";
      const resource = parsed.resource || parsed.path || "/";
      const network = parsed.network || "solana-devnet";
      const expires = Number(parsed.expiresAt || parsed.expires || (Math.floor(Date.now() / 1000) + 300));
      const nonce = String(parsed.nonce || "");
      const paymentId = parsed.paymentId ? String(parsed.paymentId) : undefined;

      let amountMicroUnits = "10000"; // default 0.01
      let amountUsd = 0.01;

      if (parsed.amountMicroUnits) {
        amountMicroUnits = String(parsed.amountMicroUnits);
        amountUsd = Number(amountMicroUnits) / 1_000_000;
      } else if (parsed.maxAmountRequired || parsed.priceUsdt || parsed.amount) {
        const rawAmt = parsed.maxAmountRequired || parsed.priceUsdt || parsed.amount;
        amountUsd = parseFloat(String(rawAmt));
        amountMicroUnits = Math.round(amountUsd * 1_000_000).toString();
      }

      const scheme = parsed.scheme || (parsed.haichainGuardrail ? "haichain-v1-voucher" : "x402-rfc");

      return {
        payee,
        mint,
        amountMicroUnits,
        amountUsd,
        scheme,
        resource,
        network,
        expires,
        nonce,
        paymentId,
        rawPayload: parsed,
      };
    } catch (e: any) {
      throw new Error(`Invalid x402 challenge format: ${e.message}`);
    }
  }

  /**
   * Evaluates an HTTP 402 challenge against the isolated PolicyEngine and generates
   * dual-compatible headers:
   * 1. "X-PAYMENT" (Base64 JSON): Standard x402 Header for Coinbase specification.
   * 2. "Authorization": "X402 <base64>" RFC compliant HTTP Authorization.
   * 3. HAICHAIN telemetry headers.
   */
  public generatePaymentResponse(
    challenge: X402Challenge,
    leafHashHex: string,
    channelId: bigint,
    scopeClass: number
  ): {
    headers: Record<string, string>;
    authorizedAmount: bigint;
    authPayload: X402AuthorizationHeader;
  } {
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
      potPubkey: auth.potPubkey.toBase58(),
      merchantPubkey: intent.merchant.toBase58(),
      nonce: auth.grantNonce.toString(),
      timestamp: Math.floor(Date.now() / 1000),
      authorizedAmount: auth.authorizedAmount.toString(),
      resource: challenge.resource,
    };

    const b64Payload = Buffer.from(JSON.stringify(authPayload)).toString("base64");

    return {
      headers: {
        "X-PAYMENT": b64Payload,
        "Authorization": `X402 ${b64Payload}`,
        "X-Haichain-Voucher-Amount": auth.authorizedAmount.toString(),
        "X-Haichain-Cumulative": auth.cumulativeVoucherAmount.toString(),
        "X-Haichain-Agent-Pubkey": this.policyEngine.getAgentPublicKey().toBase58(),
        "X-Haichain-Scheme": "haichain-v1-voucher",
      },
      authorizedAmount: auth.authorizedAmount,
      authPayload,
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
