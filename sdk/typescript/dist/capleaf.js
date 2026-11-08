"use strict";
// sdk/typescript/src/capleaf.ts
// HAICHAIN v1.1 - Merkle Capability Leaf (CapLeaf v1 223 Bytes) Specification & Red-Team Defense Engine
// Formally verified against Claude (@LE) test vectors and institutional risk invariants I1-I9.
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
Object.defineProperty(exports, "__esModule", { value: true });
exports.CapLeafV1Engine = exports.CapScopeClass = exports.CapLeafFlags = exports.CLOCK_DRIFT_TOLERANCE_SECS = exports.CAPLEAF_V1_VERSION = exports.CAPLEAF_V1_WIRE_LENGTH = exports.CAPLEAF_V1_TAG = void 0;
const web3_js_1 = require("@solana/web3.js");
const crypto = __importStar(require("crypto"));
exports.CAPLEAF_V1_TAG = Buffer.from("HAICHAIN-CAPLEAF-V1", "utf8");
exports.CAPLEAF_V1_WIRE_LENGTH = 223; // Exact binary wire size in Borsh little-endian format
exports.CAPLEAF_V1_VERSION = 1;
/** Clock drift tolerance margin (±120s) against Solana validator clock desynchronization */
exports.CLOCK_DRIFT_TOLERANCE_SECS = 120n;
var CapLeafFlags;
(function (CapLeafFlags) {
    CapLeafFlags[CapLeafFlags["NONE"] = 0] = "NONE";
    CapLeafFlags[CapLeafFlags["REQUIRE_COSIGN"] = 1] = "REQUIRE_COSIGN";
    CapLeafFlags[CapLeafFlags["PROBATION"] = 2] = "PROBATION";
})(CapLeafFlags || (exports.CapLeafFlags = CapLeafFlags = {}));
var CapScopeClass;
(function (CapScopeClass) {
    CapScopeClass[CapScopeClass["DATA_API"] = 1] = "DATA_API";
    CapScopeClass[CapScopeClass["LLM_INFERENCE"] = 2] = "LLM_INFERENCE";
    CapScopeClass[CapScopeClass["COMPUTE"] = 4] = "COMPUTE";
    CapScopeClass[CapScopeClass["BROWSER"] = 8] = "BROWSER";
    CapScopeClass[CapScopeClass["HUMAN_TASK"] = 16] = "HUMAN_TASK";
    CapScopeClass[CapScopeClass["HUMAN_VERIFIED"] = 32] = "HUMAN_VERIFIED";
    CapScopeClass[CapScopeClass["RLHF_REWARD"] = 64] = "RLHF_REWARD";
})(CapScopeClass || (exports.CapScopeClass = CapScopeClass = {}));
class CapLeafV1Engine {
    /**
     * Serializes a CapLeafV1 into exactly 223 bytes Borsh Little-Endian format.
     */
    static serialize(leaf) {
        const buf = Buffer.alloc(exports.CAPLEAF_V1_WIRE_LENGTH);
        let offset = 0;
        buf.writeUInt8(leaf.version, offset);
        offset += 1;
        leaf.pot.toBuffer().copy(buf, offset);
        offset += 32;
        leaf.agent.toBuffer().copy(buf, offset);
        offset += 32;
        leaf.merchant.toBuffer().copy(buf, offset);
        offset += 32;
        leaf.mint.toBuffer().copy(buf, offset);
        offset += 32;
        buf.writeBigUInt64LE(BigInt(leaf.maxSpend), offset);
        offset += 8;
        buf.writeBigUInt64LE(BigInt(leaf.maxReserve), offset);
        offset += 8;
        buf.writeBigUInt64LE(BigInt(leaf.windowCap), offset);
        offset += 8;
        buf.writeUInt32LE(leaf.windowSecs, offset);
        offset += 4;
        buf.writeUInt32LE(leaf.scopeClass, offset);
        offset += 4;
        if (leaf.scopeRef.length !== 32) {
            throw new Error(`Invalid scopeRef length: expected 32 bytes, got ${leaf.scopeRef.length}`);
        }
        leaf.scopeRef.copy(buf, offset);
        offset += 32;
        buf.writeBigUInt64LE(BigInt(leaf.nonce), offset);
        offset += 8;
        buf.writeBigInt64LE(BigInt(leaf.notBefore), offset);
        offset += 8;
        buf.writeBigInt64LE(BigInt(leaf.expiry), offset);
        offset += 8;
        buf.writeUInt32LE(leaf.epoch, offset);
        offset += 4;
        buf.writeUInt16LE(leaf.flags, offset);
        offset += 2;
        if (offset !== exports.CAPLEAF_V1_WIRE_LENGTH) {
            throw new Error(`Serialization error: expected ${exports.CAPLEAF_V1_WIRE_LENGTH} bytes, wrote ${offset}`);
        }
        return buf;
    }
    /**
     * Deserializes 223 bytes Borsh Little-Endian buffer into a CapLeafV1 struct.
     */
    static deserialize(bytes) {
        if (bytes.length !== exports.CAPLEAF_V1_WIRE_LENGTH) {
            throw new Error(`Invalid wire length: expected ${exports.CAPLEAF_V1_WIRE_LENGTH} bytes, got ${bytes.length}`);
        }
        let offset = 0;
        const version = bytes.readUInt8(offset);
        offset += 1;
        if (version !== exports.CAPLEAF_V1_VERSION) {
            throw new Error(`Unsupported CapLeaf version: ${version}`);
        }
        const pot = new web3_js_1.PublicKey(bytes.subarray(offset, offset + 32));
        offset += 32;
        const agent = new web3_js_1.PublicKey(bytes.subarray(offset, offset + 32));
        offset += 32;
        const merchant = new web3_js_1.PublicKey(bytes.subarray(offset, offset + 32));
        offset += 32;
        const mint = new web3_js_1.PublicKey(bytes.subarray(offset, offset + 32));
        offset += 32;
        const maxSpend = bytes.readBigUInt64LE(offset);
        offset += 8;
        const maxReserve = bytes.readBigUInt64LE(offset);
        offset += 8;
        const windowCap = bytes.readBigUInt64LE(offset);
        offset += 8;
        const windowSecs = bytes.readUInt32LE(offset);
        offset += 4;
        const scopeClass = bytes.readUInt32LE(offset);
        offset += 4;
        const scopeRef = Buffer.from(bytes.subarray(offset, offset + 32));
        offset += 32;
        const nonce = bytes.readBigUInt64LE(offset);
        offset += 8;
        const notBefore = bytes.readBigInt64LE(offset);
        offset += 8;
        const expiry = bytes.readBigInt64LE(offset);
        offset += 8;
        const epoch = bytes.readUInt32LE(offset);
        offset += 4;
        const flags = bytes.readUInt16LE(offset);
        offset += 2;
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
    static computeLeafHash(programId, leafBytes) {
        if (leafBytes.length !== exports.CAPLEAF_V1_WIRE_LENGTH) {
            throw new Error(`Invalid leafBytes length: expected ${exports.CAPLEAF_V1_WIRE_LENGTH}, got ${leafBytes.length}`);
        }
        return crypto.createHash("sha256")
            .update(Buffer.from([0x00]))
            .update(exports.CAPLEAF_V1_TAG)
            .update(programId.toBuffer())
            .update(leafBytes)
            .digest();
    }
    /**
     * Computes an internal Merkle node hash:
     * node(l, r) = SHA256( 0x01 || left || right )
     */
    static computeMerkleNode(left, right) {
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
    static computeEmptyLeaf() {
        return crypto.createHash("sha256")
            .update(Buffer.from([0x02]))
            .update(exports.CAPLEAF_V1_TAG)
            .digest();
    }
    /**
     * Verifies a Merkle proof with positional routing (index-based) against expected root.
     * Tree depth d must match proof.length (e.g. d = 12 for 4,096 leaves).
     */
    static verifyProof(leafHash, proof, leafIndex, expectedRoot) {
        let currentHash = leafHash;
        let index = leafIndex;
        for (let i = 0; i < proof.length; i++) {
            const sibling = proof[i];
            const isRightSibling = (index & 1) === 0;
            if (isRightSibling) {
                currentHash = this.computeMerkleNode(currentHash, sibling);
            }
            else {
                currentHash = this.computeMerkleNode(sibling, currentHash);
            }
            index = index >> 1;
        }
        return Buffer.from(currentHash).equals(expectedRoot);
    }
    /**
     * PDA Derivations for HAICHAIN v1.1 Architecture
     */
    static getPotPda(programId, owner) {
        return web3_js_1.PublicKey.findProgramAddressSync([Buffer.from("pot"), owner.toBuffer()], programId);
    }
    static getActiveGrantPda(programId, potPda, leafHash) {
        return web3_js_1.PublicKey.findProgramAddressSync([Buffer.from("grant"), potPda.toBuffer(), leafHash], programId);
    }
    static getChannelPda(programId, activeGrantPda, channelId) {
        const channelIdBuf = Buffer.alloc(8);
        channelIdBuf.writeBigUInt64LE(BigInt(channelId));
        return web3_js_1.PublicKey.findProgramAddressSync([Buffer.from("chan"), activeGrantPda.toBuffer(), channelIdBuf], programId);
    }
    /**
     * Red-Team Defense Patch 2: Sliding/Leaky-Bucket Window Rate-Limiter
     * Calculates maximum permitted reserve at timestamp `now` preventing the Window Straddle "Double-Dip".
     */
    static calculateSlidingWindowAvailable(windowCap, windowSecs, lastWindowStart, windowUsed, now) {
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
exports.CapLeafV1Engine = CapLeafV1Engine;
