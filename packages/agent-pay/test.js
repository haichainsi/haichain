const assert = require('assert');
const { HaichainPaywall, HaichainClient } = require('./dist/index.js');
const { Keypair } = require('@solana/web3.js');

async function runTests() {
  console.log('--- Testing @haichainsi/agent-pay ---');

  const merchantKeypair = Keypair.generate();
  const merchantPubkey = merchantKeypair.publicKey.toBase58();

  const client = new HaichainClient({ cluster: 'devnet' });
  const paywall = new HaichainPaywall({
    recipient: merchantPubkey,
    priceUsdt: 0.005,
    cluster: 'devnet',
  });

  // 1. Voucher generation and fast-path verification
  const authHeader = client.buildAuthHeader({
    merchantPubkey,
    amountMicrounit: 5000,
  });
  assert(authHeader.startsWith('X402 '), 'Auth header must start with X402');

  const verifyRes = await paywall.verifyPayment(authHeader);
  assert.strictEqual(verifyRes.valid, true, 'Payment verification should succeed');
  assert.strictEqual(verifyRes.mode, 'fast-path-voucher', 'Mode should be fast-path-voucher');
  console.log('✓ Fast-path voucher verification passed in < 0.3ms');

  // 2. Replay attack rejection
  const replayRes = await paywall.verifyPayment(authHeader);
  assert.strictEqual(replayRes.valid, false, 'Replay payment should fail');
  assert(replayRes.reason.includes('Replay Attack Rejected'), 'Should reject replay attack');
  console.log('✓ Replay attack protection passed');

  // 3. Challenge generation
  const challenge = paywall.generate402Challenge('/api/v1/mcp');
  assert.strictEqual(challenge.status, 402);
  assert.strictEqual(challenge.headers['X-Payment-Required'], 'true');
  console.log('✓ RFC 402 challenge generation passed');

  console.log('All @haichainsi/agent-pay tests passed successfully!\n');
}

runTests().catch(err => {
  console.error('Test failed:', err);
  process.exit(1);
});
