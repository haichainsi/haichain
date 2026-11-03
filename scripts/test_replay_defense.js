const { Connection, Keypair, PublicKey, SystemProgram, Transaction, sendAndConfirmTransaction } = require('@solana/web3.js');
const fs = require('fs');
const path = require('path');
const { HaichainPaywall } = require('../packages/agent-pay/dist/index.js');

const RPC_URL = 'https://api.devnet.solana.com';
const TREASURY_PUBKEY = '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';

async function main() {
  console.log('=== TEST STEP 1: AUDIT REPLAY ATTACK & FRESHNESS DEFENSE ===\n');

  // Load deployer keypair
  const keypairPath = path.resolve(__dirname, '../devnet-deployer.json');
  const secretKey = JSON.parse(fs.readFileSync(keypairPath, 'utf8'));
  const payer = Keypair.fromSecretKey(new Uint8Array(secretKey));
  const connection = new Connection(RPC_URL, 'confirmed');

  console.log(`[Payer Wallet]: ${payer.publicKey.toBase58()}`);
  console.log(`[Treasury]:     ${TREASURY_PUBKEY}`);

  // Broadcast a real 15,000 lamports micro-payment on Solana Devnet
  console.log('\n[1] Broadcasting 1 fresh on-chain micro-payment (15,000 lamports)...');
  const tx = new Transaction().add(
    SystemProgram.transfer({
      fromPubkey: payer.publicKey,
      toPubkey: new PublicKey(TREASURY_PUBKEY),
      lamports: 15000
    })
  );

  const sig = await sendAndConfirmTransaction(connection, tx, [payer], {
    commitment: 'confirmed'
  });
  console.log(`[SUCCESS] Confirmed Tx Signature: ${sig}`);
  console.log(`Explorer: https://explorer.solana.com/tx/${sig}?cluster=devnet`);

  // Initialize HaichainPaywall with Nullifier Store & 300s freshness
  const paywall = new HaichainPaywall({
    recipient: TREASURY_PUBKEY,
    priceUsdt: 0.003,
    cluster: 'devnet',
    maxAgeSeconds: 300
  });

  // Attempt 1: Valid initial consumption
  console.log('\n[2] Attempt 1: First consumption of Tx by Agent Sub-Service...');
  const firstCheck = await paywall.verifyPayment(undefined, sig);
  console.log('Result 1:', JSON.stringify(firstCheck, null, 2));

  if (!firstCheck.valid) {
    console.error('FAILED: First attempt should have passed!');
    process.exit(1);
  }
  console.log('[PASS] First attempt was accepted and recorded in Nullifier Store.');

  // Attempt 2: Replay attack with the exact same signature
  console.log('\n[3] Attempt 2: REPLAY ATTACK - Malicious agent attempts to reuse the same Tx...');
  const secondCheck = await paywall.verifyPayment(undefined, sig);
  console.log('Result 2:', JSON.stringify(secondCheck, null, 2));

  if (secondCheck.valid === false && secondCheck.reason.includes('Replay Attack Rejected')) {
    console.log('\n>>> [SECURITY AUDIT PASS]: REPLAY ATTACK WAS SUCCESSFULLY INTERCEPTED AND BLOCKED!');
  } else {
    console.error('\n>>> [CRITICAL FAILURE]: Paywall allowed duplicate voucher replay!');
    process.exit(1);
  }
}

main().catch(err => {
  console.error('[FATAL ERROR]:', err);
  process.exit(1);
});
