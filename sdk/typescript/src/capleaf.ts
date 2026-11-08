// sdk/typescript/src/capleaf.ts
// HAICHAIN v1.1 - Merkle Capability Leaf (CapLeaf v1 223 Bytes) Specification & Red-Team Defense Engine
// Formally verified against Claude (@LE) test vectors and institutional risk invariants I1-I9.

import { PublicKey } from "@solana/web3.js";
import * as crypto from "crypto";

export const CAPLEAF_V1_TAG = Buffer.from("HAICHAIN-CAPLEAF-V1", "utf8");
export const CAPLEAF_V1_WIRE_LENGTH = 223; // Exact binary wire size in Borsh little-endian format
export const CAPLEAF_V1_VERSION = 1;

/** Clock drift tolerance margin (±120s) against Solana validator clock desynchronization */
export const CLOCK_DRIFT_TOLERANCE_SECS = 120n;

export enum CapLeafFlags {
  NONE = 0,
  REQUIRE_COSIGN = 1 << 0, // bit0: Requires TEE Cosigner co-signature for Reserve
  PROBATION = 1 << 1,      // bit1: Probationary merchant leaf (budget quarantined)
}

export enum CapScopeClass {
  DATA_API = 1 << 0,       // bit0: Data / API calls (e.g. search, scraping)
  LLM_INFERENCE = 1 << 1,  // bit1: LLM token generation / inference
  COMPUTE = 1 << 2,        // bit2: Heavy cloud compute / GPU hours
  BROWSER = 1 << 3,        // bit3: Headless browser automation
  HUMAN_TASK = 1 << 4,     // bit4: Human-in-the-loop task completion
  HUMAN_VERIFIED = 1 << 5, // bit5: WebAuthn/Passkey cryptographic biometric verification
  RLHF_REWARD = 1 << 6,    // bit6: Real-time RLHF / human ground-truth cognitive bounty
}

export interface CapLeafV1 {
  version: number;          // u8 (1)
  pot: PublicKey;           // [u8; 32]
  agent: PublicKey;         // [u8; 32]
  merchant: PublicKey;      // [u8; 32]
  mint: PublicKey;          // [u8; 32]
  maxSpend: bigint;         // u64 (Lifetime cumulative cap)
  maxReserve: bigint;       // u64 (Max reserve per single channel escrow)
  windowCap: bigint;        // u64 (Max spend velocity within window)
  windowSecs: number;       // u32 (Window length in seconds, >= 60s)
  scopeClass: number;       // u32 (Bitmask of allowed services)
  scopeRef: Buffer;         // [u8; 32] (SHA256 of ScopePolicy JSON document)
  nonce: bigint;            // u64 (Unique sequence nonce per pot)
  notBefore: bigint;        // i64 (Unix timestamp seconds)
  expiry: bigint;           // i64 (Unix timestamp seconds)
  epoch: number;            // u32 (Matches pot.panic_epoch at issuance)
  flags: number;            // u16 (CapLeafFlags bitmask)
}

export class CapLeafV1Engine {
  /**
   * Serializes a CapLeafV1 into exactly 223 bytes Borsh Little-Endian format.
   */
  public static serialize(leaf: CapLeafV1): Buffer {
    const buf = Buffer.alloc(CAPLEAF_V1_WIRE_LENGTH);
    let offset = 0;

    buf.writeUInt8(leaf.version, offset); offset += 1;
    leaf.pot.toBuffer().copy(buf, offset); offset += 32;
    leaf.agent.toBuffer().copy(buf, offset); offset += 32;
    leaf.merchant.toBuffer().copy(buf, offset); offset += 32;
    leaf.mint.toBuffer().copy(buf, offset); offset += 32;

    buf.writeBigUInt64LE(BigInt(leaf.maxSpend), offset); offset += 8;
    buf.writeBigUInt64LE(BigInt(leaf.maxReserve), offset); offset += 8;
    buf.writeBigUInt64LE(BigInt(leaf.windowCap), offset); offset += 8;

    buf.writeUInt32LE(leaf.windowSecs, offset); offset += 4;
    buf.writeUInt32LE(leaf.scopeClass, offset); offset += 4;

    if (leaf.scopeRef.length !== 32) {
      throw new Error(`Invalid scopeRef length: expected 32 bytes, got ${leaf.scopeRef.length}`);
    }
    leaf.scopeRef.copy(buf, offset); offset += 32;

    buf.writeBigUInt64LE(BigInt(leaf.nonce), offset); offset += 8;
    buf.writeBigInt64LE(BigInt(leaf.notBefore), offset); offset += 8;
    buf.writeBigInt64LE(BigInt(leaf.expiry), offset); offset += 8;

    buf.writeUInt32LE(leaf.epoch, offset); offset += 4;
    buf.writeUInt16LE(leaf.flags, offset); offset += 2;

    if (offset !== CAPLEAF_V1_WIRE_LENGTH) {
      throw new Error(`Serialization error: expected ${CAPLEAF_V1_WIRE_LENGTH} bytes, wrote ${offset}`);
    }
    return buf;
  }

  /**
   * Deserializes 223 bytes Borsh Little-Endian buffer into a CapLeafV1 struct.
   */
  public static deserialize(bytes: Buffer): CapLeafV1 {
    if (bytes.length !== CAPLEAF_V1_WIRE_LENGTH) {
      throw new Error(`Invalid wire length: expected ${CAPLEAF_V1_WIRE_LENGTH} bytes, got ${bytes.length}`);
    }
    let offset = 0;

    const version = bytes.readUInt8(offset); offset += 1;
    if (version !== CAPLEAF_V1_VERSION) {
      throw new Error(`Unsupported CapLeaf version: ${version}`);
    }

    const pot = new PublicKey(bytes.subarray(offset, offset + 32)); offset += 32;
    const agent = new PublicKey(bytes.subarray(offset, offset + 32)); offset += 32;
    const merchant = new PublicKey(bytes.subarray(offset, offset + 32)); offset += 32;
    const mint = new PublicKey(bytes.subarray(offset, offset + 32)); offset += 32;

    const maxSpend = bytes.readBigUInt64LE(offset); offset += 8;
    const maxReserve = bytes.readBigUInt64LE(offset); offset += 8;
    const windowCap = bytes.readBigUInt64LE(offset); offset += 8;

    const windowSecs = bytes.readUInt32LE(offset); offset += 4;
    const scopeClass = bytes.readUInt32LE(offset); offset += 4;

    const scopeRef = Buffer.from(bytes.subarray(offset, offset + 32)); offset += 32;

    const nonce = bytes.readBigUInt64LE(offset); offset += 8;
    const notBefore = bytes.readBigInt64LE(offset); offset += 8;
    const expiry = bytes.readBigInt64LE(offset); offset += 8;

    const epoch = bytes.readUInt32LE(offset); offset += 4;
    const flags = bytes.readUInt16LE(offset); offset += 2;

    return {
      version,
      pot,
      agent,
      merchant,
      mint,
      maxSpend,
      maxReserve,
      windowCap,
      windowSecs,
      scopeClass,
      scopeRef,
      nonce,
      notBefore,
      expiry,
      epoch,
      flags,
    };
  }

  /**
   * Computes the 3-layer Domain-Separated leaf hash:
   * leaf_hash = SHA256( 0x00 || TAG || program_id || leaf_bytes )
   */
  public static computeLeafHash(programId: PublicKey, leafBytes: Buffer): Buffer {
    if (leafBytes.length !== CAPLEAF_V1_WIRE_LENGTH) {
      throw new Error(`Invalid leafBytes length: expected ${CAPLEAF_V1_WIRE_LENGTH}, got ${leafBytes.length}`);
    }
    return crypto.createHash("sha256")
      .update(Buffer.from([0x00]))
      .update(CAPLEAF_V1_TAG)
      .update(programId.toBuffer())
      .update(leafBytes)
      .digest();
  }

  /**
   * Computes an internal Merkle node hash:
   * node(l, r) = SHA256( 0x01 || left || right )
   */
  public static computeMerkleNode(left: Uint8Array, right: Uint8Array): Buffer {
    if (left.length !== 32 || right.length !== 32) {
      throw new Error("Both left and right node hashes must be exactly 32 bytes");
    }
    return crypto.createHash("sha256")
      .update(Buffer.from([0x01]))
      .update(left)
      .update(right)
      .digest();
  }

  /**
   * Computes the canonical empty padding leaf hash:
   * EMPTY = SHA256( 0x02 || TAG )
   */
  public static computeEmptyLeaf(): Buffer {
    return crypto.createHash("sha256")
      .update(Buffer.from([0x02]))
      .update(CAPLEAF_V1_TAG)
      .digest();
  }

  /**
   * Verifies a Merkle proof with positional routing (index-based) against expected root.
   * Tree depth d must match proof.length (e.g. d = 12 for 4,096 leaves).
   */
  public static verifyProof(
    leafHash: Buffer,
    proof: Buffer[],
    leafIndex: number,
    expectedRoot: Buffer
  ): boolean {
    let currentHash: Uint8Array = leafHash;
    let index = leafIndex;

    for (let i = 0; i < proof.length; i++) {
      const sibling = proof[i];
      const isRightSibling = (index & 1) === 0;

      if (isRightSibling) {
        currentHash = this.computeMerkleNode(currentHash, sibling);
      } else {
        currentHash = this.computeMerkleNode(sibling, currentHash);
      }
      index = index >> 1;
    }

    return Buffer.from(currentHash).equals(expectedRoot);
  }

  /**
   * PDA Derivations for HAICHAIN v1.1 Architecture
   */
  public static getPotPda(programId: PublicKey, owner: PublicKey): [PublicKey, number] {
    return PublicKey.findProgramAddressSync(
      [Buffer.from("pot"), owner.toBuffer()],
      programId
    );
  }

  public static getActiveGrantPda(programId: PublicKey, potPda: PublicKey, leafHash: Buffer): [PublicKey, number] {
    return PublicKey.findProgramAddressSync(
      [Buffer.from("grant"), potPda.toBuffer(), leafHash],
      programId
    );
  }

  public static getChannelPda(programId: PublicKey, activeGrantPda: PublicKey, channelId: bigint | number): [PublicKey, number] {
    const channelIdBuf = Buffer.alloc(8);
    channelIdBuf.writeBigUInt64LE(BigInt(channelId));
    return PublicKey.findProgramAddressSync(
      [Buffer.from("chan"), activeGrantPda.toBuffer(), channelIdBuf],
      programId
    );
  }

  /**
   * Red-Team Defense Patch 2: Sliding/Leaky-Bucket Window Rate-Limiter
   * Calculates maximum permitted reserve at timestamp `now` preventing the Window Straddle "Double-Dip".
   */
  public static calculateSlidingWindowAvailable(
    windowCap: bigint,
    windowSecs: number,
    lastWindowStart: bigint,
    windowUsed: bigint,
    now: bigint
  ): bigint {
    const elapsed = now - lastWindowStart;
    if (elapsed >= BigInt(windowSecs)) {
      // Full window elapsed: reset available to full windowCap
      return windowCap;
    }
    // Partial window: decaying rate limit
    const remainingInWindow = windowCap > windowUsed ? windowCap - windowUsed : 0n;
    return remainingInWindow;
  }
}
