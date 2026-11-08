/**
 * ==============================================================================
 * HAICHAIN STATE CHANNEL CLIENT & WEB3 WALLET ADAPTER (PHANTOM / SOLFLARE)
 * ==============================================================================
 * Allows Autonomous AI Agents & Humans using Phantom or Solflare wallets to:
 * 1. Sign and broadcast `extend_channel_reserve` transactions directly on-chain (0 SOL rent churn).
 * 2. Connect to the Watchtower Sentinel to auto-defend against malicious / stale channel closure.
 * 3. Query on-chain channel state and PDA addresses.
 */

(function(root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.HaichainChannelClient = factory();
  }
}(typeof self !== 'undefined' ? self : this, function() {
  'use strict';

  const DEFAULT_PROGRAM_ID = 'DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk';
  const DEFAULT_DEVNET_RPC = 'https://api.devnet.solana.com';
  const TOKEN_PROGRAM_ID = 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA';

  /**
   * Simple SHA256 helper for browser environments (using crypto.subtle or fallback)
   */
  async function sha256Bytes(str) {
    if (typeof crypto !== 'undefined' && crypto.subtle) {
      const buffer = new TextEncoder().encode(str);
      const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
      return new Uint8Array(hashBuffer);
    }
    // Node.js fallback
    try {
      const nodeCrypto = require('crypto');
      return nodeCrypto.createHash('sha256').update(str).digest();
    } catch (e) {
      throw new Error('No crypto provider available for sha256');
    }
  }

  /**
   * Helper to write 64-bit integer into Little-Endian Uint8Array
   */
  function writeBigUInt64LE(value) {
    const buf = new Uint8Array(8);
    let v = BigInt(value);
    for (let i = 0; i < 8; i++) {
      buf[i] = Number(v & 0xffn);
      v >>= 8n;
    }
    return buf;
  }

  class HaichainChannelClient {
    constructor(options = {}) {
      this.programId = options.programId || DEFAULT_PROGRAM_ID;
      this.rpcUrl = options.rpcUrl || DEFAULT_DEVNET_RPC;
      this.watchtowerUrl = options.watchtowerUrl || 'http://localhost:8080';
    }

    /**
     * Detect Phantom or Solflare wallet in browser
     */
    detectWallet() {
      if (typeof window === 'undefined') return null;
      if (window.phantom && window.phantom.solana && window.phantom.solana.isPhantom) {
        return { provider: window.phantom.solana, name: 'Phantom' };
      }
      if (window.solana && window.solana.isPhantom) {
        return { provider: window.solana, name: 'Phantom' };
      }
      if (window.solflare && window.solflare.isSolflare) {
        return { provider: window.solflare, name: 'Solflare' };
      }
      return null;
    }

    /**
     * Connect active Web3 Wallet
     */
    async connectWallet() {
      const detected = this.detectWallet();
      if (!detected) {
        throw new Error('No supported Solana Web3 wallet found. Please install Phantom or Solflare.');
      }
      const resp = await detected.provider.connect();
      return {
        providerName: detected.name,
        publicKey: resp.publicKey ? resp.publicKey.toString() : detected.provider.publicKey.toString()
      };
    }

    /**
     * Compute Anchor Instruction Discriminator: sha256("global:<name>")[..8]
     */
    async getAnchorDiscriminator(instructionName) {
      const hash = await sha256Bytes(`global:${instructionName}`);
      return hash.slice(0, 8);
    }

    /**
     * Construct `extend_channel_reserve` instruction payload for Phantom/Solflare
     */
    async buildExtendChannelReserveInstruction({
      potPubkey,
      activeGrantPubkey,
      channelPubkey,
      vaultAta,
      channelEscrowAta,
      agentPubkey,
      additionalAmount
    }) {
      const disc = await this.getAnchorDiscriminator('extend_channel_reserve');
      const amountBytes = writeBigUInt64LE(additionalAmount);
      const data = new Uint8Array(16);
      data.set(disc, 0);
      data.set(amountBytes, 8);

      return {
        programId: this.programId,
        keys: [
          { pubkey: potPubkey, isSigner: false, isWritable: true },
          { pubkey: activeGrantPubkey, isSigner: false, isWritable: true },
          { pubkey: channelPubkey, isSigner: false, isWritable: true },
          { pubkey: vaultAta, isSigner: false, isWritable: true },
          { pubkey: channelEscrowAta, isSigner: false, isWritable: true },
          { pubkey: agentPubkey, isSigner: true, isWritable: false },
          { pubkey: TOKEN_PROGRAM_ID, isSigner: false, isWritable: false }
        ],
        data
      };
    }

    /**
     * Request Phantom or Solflare to sign and broadcast `extend_channel_reserve` on Solana Devnet
     */
    async signAndBroadcastExtendReserve({
      solanaWeb3,
      potPubkey,
      activeGrantPubkey,
      channelPubkey,
      vaultAta,
      channelEscrowAta,
      additionalAmount
    }) {
      const detected = this.detectWallet();
      if (!detected) {
        throw new Error('Wallet not connected. Connect Phantom or Solflare first.');
      }

      const wallet = detected.provider;
      const agentPubkey = wallet.publicKey;

      const ixData = await this.buildExtendChannelReserveInstruction({
        potPubkey: potPubkey.toString ? potPubkey.toString() : potPubkey,
        activeGrantPubkey: activeGrantPubkey.toString ? activeGrantPubkey.toString() : activeGrantPubkey,
        channelPubkey: channelPubkey.toString ? channelPubkey.toString() : channelPubkey,
        vaultAta: vaultAta.toString ? vaultAta.toString() : vaultAta,
        channelEscrowAta: channelEscrowAta.toString ? channelEscrowAta.toString() : channelEscrowAta,
        agentPubkey: agentPubkey.toString(),
        additionalAmount
      });

      if (!solanaWeb3) {
        throw new Error('solanaWeb3 library reference required to build Transaction object');
      }

      const connection = new solanaWeb3.Connection(this.rpcUrl, 'confirmed');
      const tx = new solanaWeb3.Transaction();

      const instruction = new solanaWeb3.TransactionInstruction({
        programId: new solanaWeb3.PublicKey(ixData.programId),
        keys: ixData.keys.map(k => ({
          pubkey: new solanaWeb3.PublicKey(k.pubkey),
          isSigner: k.isSigner,
          isWritable: k.isWritable
        })),
        data: Buffer.from(ixData.data)
      });

      tx.add(instruction);
      tx.feePayer = agentPubkey;
      const { blockhash } = await connection.getLatestBlockhash();
      tx.recentBlockhash = blockhash;

      console.log(`[HAICHAIN Client] Requesting ${detected.name} wallet signature for extend_channel_reserve...`);
      const signedTx = await wallet.signTransaction(tx);
      const rawTx = signedTx.serialize();
      const txSig = await connection.sendRawTransaction(rawTx);
      await connection.confirmTransaction(txSig, 'confirmed');

      console.log(`[HAICHAIN Client] Confirmed on Solana Devnet: ${txSig}`);
      return {
        success: true,
        transactionSignature: txSig,
        explorerUrl: `https://explorer.solana.com/tx/${txSig}?cluster=devnet`,
        recycledRent: '0 SOL (Rent Churn Eliminated)',
        additionalReserve: additionalAmount
      };
    }

    /**
     * Trigger Watchtower On-Chain Settlement Defense
     */
    async defendChannelViaWatchtower(channelId) {
      const resp = await fetch(`${this.watchtowerUrl}/api/watchtower/defend`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ channelId })
      });
      if (!resp.ok) {
        const err = await resp.json().catch(() => ({}));
        throw new Error(err.error || `Watchtower defense failed with HTTP ${resp.status}`);
      }
      return await resp.json();
    }
  }

  return HaichainChannelClient;
}));
