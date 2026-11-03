import { PublicKey } from "@solana/web3.js";
export declare const CAPLEAF_V1_TAG: Buffer<ArrayBuffer>;
export declare const CAPLEAF_V1_WIRE_LENGTH = 223;
export declare const CAPLEAF_V1_VERSION = 1;
export declare enum CapLeafFlags {
    NONE = 0,
    REQUIRE_COSIGN = 1,// bit0: Requires TEE Cosigner co-signature for Reserve
    PROBATION = 2
}
export declare enum CapScopeClass {
    DATA_API = 1,// bit0: Data / API calls (e.g. search, scraping)
    LLM_INFERENCE = 2,// bit1: LLM token generation / inference
    COMPUTE = 4,// bit2: Heavy cloud compute / GPU hours
    BROWSER = 8,// bit3: Headless browser automation
    HUMAN_TASK = 16
}
export interface CapLeafV1 {
    version: number;
    pot: PublicKey;
    agent: PublicKey;
    merchant: PublicKey;
    mint: PublicKey;
    maxSpend: bigint;
    maxReserve: bigint;
    windowCap: bigint;
    windowSecs: number;
    scopeClass: number;
    scopeRef: Buffer;
    nonce: bigint;
    notBefore: bigint;
    expiry: bigint;
    epoch: number;
    flags: number;
}
export declare class CapLeafV1Engine {
    /**
     * Serializes a CapLeafV1 into exactly 223 bytes Borsh Little-Endian format.
     */
    static serialize(leaf: CapLeafV1): Buffer;
    /**
     * Deserializes 223 bytes Borsh Little-Endian buffer into a CapLeafV1 struct.
     */
    static deserialize(bytes: Buffer): CapLeafV1;
    /**
     * Computes the 3-layer Domain-Separated leaf hash:
     * leaf_hash = SHA256( 0x00 || TAG || program_id || leaf_bytes )
     */
    static computeLeafHash(programId: PublicKey, leafBytes: Buffer): Buffer;
    /**
     * Computes an internal Merkle node hash:
     * node(l, r) = SHA256( 0x01 || left || right )
     */
    static computeMerkleNode(left: Uint8Array, right: Uint8Array): Buffer;
    /**
     * Computes the canonical empty padding leaf hash:
     * EMPTY = SHA256( 0x02 || TAG )
     */
    static computeEmptyLeaf(): Buffer;
    /**
     * Verifies a Merkle proof with positional routing (index-based) against expected root.
     * Tree depth d must match proof.length (e.g. d = 12 for 4,096 leaves).
     */
    static verifyProof(leafHash: Buffer, proof: Buffer[], leafIndex: number, expectedRoot: Buffer): boolean;
    /**
     * PDA Derivations for HAICHAIN v1.1 Architecture
     */
    static getPotPda(programId: PublicKey, owner: PublicKey): [PublicKey, number];
    static getActiveGrantPda(programId: PublicKey, potPda: PublicKey, leafHash: Buffer): [PublicKey, number];
    static getChannelPda(programId: PublicKey, activeGrantPda: PublicKey, channelId: bigint | number): [PublicKey, number];
    /**
     * Red-Team Defense Patch 2: Sliding/Leaky-Bucket Window Rate-Limiter
     * Calculates maximum permitted reserve at timestamp `now` preventing the Window Straddle "Double-Dip".
     */
    static calculateSlidingWindowAvailable(windowCap: bigint, windowSecs: number, lastWindowStart: bigint, windowUsed: bigint, now: bigint): bigint;
}
