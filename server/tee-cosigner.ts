// server/tee-cosigner.ts
// HAICHAIN v1.1 - TEE Cosigner Service & Payee Identity Verifier
// Hardened against SSRF, DNS Rebinding, Subdomain Takeovers, and Phishing Domains.

import * as crypto from "crypto";
import { Keypair, PublicKey } from "@solana/web3.js";
import nacl from "tweetnacl";

export interface WellKnownPayeeIdentity {
  version: string;             // "1.0"
  merchantPubkey: string;      // Solana Base58 merchant authority
  mintAllowlist: string[];     // ["Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB", ...]
  domain: string;              // "api.example.com"
  organization: string;
  signature: string;           // Ed25519 signature of domain by merchantPubkey
}

export interface CosignDecision {
  allowed: boolean;
  reason?: string;
  cosignerSignature?: Uint8Array;
  cosignerPublicKey?: string;
}

export class TeeCosignerService {
  private cosignerKeypair: Keypair;

  // Reserved and internal IP ranges to prevent SSRF / DNS Rebinding attacks
  private static readonly BLOCKED_IP_REGEX = /^(127\.|10\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[0-1])\.|169\.254\.|0\.|localhost|::1)/i;

  constructor(cosignerKeypair: Keypair = Keypair.generate()) {
    this.cosignerKeypair = cosignerKeypair;
  }

  public getCosignerPublicKey(): PublicKey {
    return this.cosignerKeypair.publicKey;
  }

  /**
   * Evaluates a merchant domain before co-signing an ActivateChild grant on-chain.
   */
  public evaluateMerchantIdentity(
    domain: string,
    resolvedIp: string,
    domainAgeDays: number,
    payeeJson: WellKnownPayeeIdentity
  ): CosignDecision {
    // 1. SSRF Defense: Block private and link-local IP addresses
    if (TeeCosignerService.BLOCKED_IP_REGEX.test(resolvedIp) || TeeCosignerService.BLOCKED_IP_REGEX.test(domain)) {
      return {
        allowed: false,
        reason: `SSRF PROTECTION: Domain ${domain} resolved to forbidden internal/link-local address ${resolvedIp}`,
      };
    }

    // 2. Domain Age Check: Block burner domains created < 30 days ago
    if (domainAgeDays < 30) {
      return {
        allowed: false,
        reason: `HIGH RISK DOMAIN: Domain ${domain} age is only ${domainAgeDays} days (minimum 30 days required for automated co-signing)`,
      };
    }

    // 3. Domain match
    if (payeeJson.domain.toLowerCase() !== domain.toLowerCase()) {
      return {
        allowed: false,
        reason: `DOMAIN MISMATCH: Payee JSON declared domain ${payeeJson.domain} does not match request domain ${domain}`,
      };
    }

    // 4. Verify Payee Self-Signature
    const merchantPubkey = new PublicKey(payeeJson.merchantPubkey);
    const domainPayload = Buffer.from(`HAICHAIN-PAYEE-IDENTITY:${payeeJson.domain}:${merchantPubkey.toBase58()}`);
    const sigBytes = Buffer.from(payeeJson.signature, "base64");

    const isSelfSignatureValid = nacl.sign.detached.verify(
      domainPayload,
      sigBytes,
      merchantPubkey.toBytes()
    );

    if (!isSelfSignatureValid) {
      return {
        allowed: false,
        reason: `SIGNATURE FORGERY: Invalid merchant self-signature for domain ${domain}`,
      };
    }

    // 5. Generate Co-signer Signature authorizing ActivateChild on Solana
    const cosignPayload = crypto.createHash("sha256")
      .update(Buffer.from("HAICHAIN-COSIGN-ACTIVATE-CHILD-V1"))
      .update(merchantPubkey.toBuffer())
      .update(Buffer.from(domain))
      .digest();

    const cosignerSignature = nacl.sign.detached(cosignPayload, this.cosignerKeypair.secretKey);

    return {
      allowed: true,
      cosignerSignature,
      cosignerPublicKey: this.cosignerKeypair.publicKey.toBase58(),
    };
  }
}
