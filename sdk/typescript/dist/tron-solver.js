"use strict";
// sdk/typescript/src/tron-solver.ts
// HAICHAIN v1.1 - Tron Enterprise USDT Rails & Cross-Chain Intent Settlement Engine
// Provides high-volume, sub-cent USDT transaction routing with zero bridge lockup delay.
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
exports.TronEnterpriseSolver = void 0;
const crypto = __importStar(require("crypto"));
class TronEnterpriseSolver {
    static TRON_USDT_CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"; // Official TRC20 USDT
    /**
     * Hashes a cross-chain payment intent for Tron enterprise clearing.
     */
    static computeIntentHash(intent) {
        const payload = `TRON-HAICHAIN-INTENT-V1:${intent.sourceVaultSolana}:${intent.destinationTronAddress}:${intent.amountUsdt.toFixed(6)}:${intent.maxFeeUsdt.toFixed(6)}:${intent.nonce.toString()}:${intent.expiryTimestamp}`;
        return crypto.createHash("sha256").update(payload).digest("hex");
    }
    /**
     * Validates intent expiration and economic solvency before dispatching to Tron network.
     */
    static validateIntent(intent, currentTimestamp = Math.floor(Date.now() / 1000)) {
        if (currentTimestamp >= intent.expiryTimestamp) {
            return false; // Expired
        }
        if (intent.amountUsdt <= 0 || intent.maxFeeUsdt < 0) {
            return false;
        }
        if (!intent.destinationTronAddress.startsWith("T") || intent.destinationTronAddress.length !== 34) {
            return false; // Invalid Tron Base58 address format
        }
        return true;
    }
    /**
     * Generates a verifiable Merkle audit leaf for enterprise audit and Big 4 reporting.
     */
    static createSettlementReceipt(intent, tronTxHash, blockNumber) {
        const merkleLeaf = crypto.createHash("sha256")
            .update(`${intent.intentId}:${tronTxHash}:${blockNumber}`)
            .digest("hex");
        return {
            intentId: intent.intentId,
            tronTxHash,
            settledAmountUsdt: intent.amountUsdt,
            tronBlockNumber: blockNumber,
            timestampIso: new Date().toISOString(),
            merkleAuditLeaf: merkleLeaf,
        };
    }
}
exports.TronEnterpriseSolver = TronEnterpriseSolver;
