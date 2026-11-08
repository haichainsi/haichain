/**
 * ==============================================================================
 * HAICHAIN END-TO-END DEVELOPER INTEGRATION & LIFECYCLE SIMULATION
 * ==============================================================================
 * Simulates the entire lifecycle from zero to full payment and on-chain defense:
 * 1. Watchtower Sentinel Daemon starts on port 8089
 * 2. Seller Agent API starts on port 8090 with HaichainPaywall & Watchtower auto-forwarding
 * 3. Buyer AI Agent connects with PolicyEngine & HaichainClient
 * 4. Step A: Unauthenticated call -> 402 Challenge received
 * 5. Step B: Autonomous 402 negotiation -> Ed25519 voucher signed (< 0.2ms)
 * 6. Step C: Seller verifies signature & executes AI task -> 200 OK
 * 7. Step D: Watchtower Sentinel receives & persists voucher in background
 * 8. Step E: Adversarial Replay Attack is blocked by Nullifier Store
 * 9. Step F: Watchtower executes Channel Settlement Defense
 */

const http = require('http');
const path = require('path');
const assert = require('assert');
const { Keypair, PublicKey } = require('@solana/web3.js');
const { HaichainPaywall, HaichainClient } = require(path.join(__dirname, '../packages/agent-pay/dist/index.js'));
const { ProductionAgentRelayer } = require(path.join(__dirname, '../server/production-agent-relayer.js'));

const WATCHTOWER_PORT = 8089;
const SELLER_AGENT_PORT = 8090;

async function runEndToEndSimulation() {
  console.log('======================================================================');
  console.log('       HAICHAIN COMPLETE DEVELOPER INTEGRATION LIFECYCLE AUDIT        ');
  console.log('======================================================================\n');

  // Generate real Solana keypairs for simulation
  const sellerKeypair = Keypair.generate();
  const sellerPubkey = sellerKeypair.publicKey.toBase58();
  const buyerKeypair = Keypair.generate();
  const buyerPubkey = buyerKeypair.publicKey.toBase58();

  console.log(`[SETUP] Seller Wallet Public Key: ${sellerPubkey}`);
  console.log(`[SETUP] Buyer Wallet Public Key:  ${buyerPubkey}\n`);

  // ---------------------------------------------------------------------------
  // STEP 1: Launch Watchtower Sentinel Daemon on Port 8089
  // ---------------------------------------------------------------------------
  console.log('--- STEP 1: Launching Watchtower Dispute Sentinel Daemon ---');
  const watchtowerRelayer = new ProductionAgentRelayer({
    port: WATCHTOWER_PORT,
    enableStorage: true,
    dbPath: path.join(__dirname, '../data/test-simulation-watchtower.db.json'),
  });

  await watchtowerRelayer.start();
  console.log(`✓ Watchtower Daemon active and listening on http://localhost:${WATCHTOWER_PORT}`);

  const initialStatus = watchtowerRelayer.getWatchtowerStatus();
  assert.strictEqual(initialStatus.watchtowerActive, true);
  console.log(`✓ Initial Watchtower Status: ACTIVE, Tracked Channels: ${initialStatus.totalMonitoredChannels}\n`);

  // ---------------------------------------------------------------------------
  // STEP 2: Launch Seller AI Agent API on Port 8090
  // ---------------------------------------------------------------------------
  console.log('--- STEP 2: Launching Monetized Seller AI Agent API ---');
  const paywall = new HaichainPaywall({
    recipient: sellerPubkey,
    priceUsdt: 0.005,
    cluster: 'devnet',
    serviceName: 'DeepSeek Market Intelligence Agent',
    watchtowerUrl: `http://localhost:${WATCHTOWER_PORT}`,
    maxAgeSeconds: 300,
  });

  const paywallMiddleware = paywall.middleware();
  const sellerServer = http.createServer((req, res) => {
    paywallMiddleware(req, res, () => {
      // Authenticated handler
      let body = '';
      req.on('data', chunk => { body += chunk; });
      req.on('end', () => {
        let parsed = {};
        try { parsed = JSON.parse(body); } catch (_) {}
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          status: 'SUCCESS',
          agent: 'DeepSeek-R1-Agent',
          taskResult: `Market sentiment analysis completed for "${parsed.symbol || 'SOL'}"`,
          costSettled: '0.005 USDT',
          haichainReceipt: req.haichainPayment,
        }));
      });
    });
  });

  await new Promise(resolve => sellerServer.listen(SELLER_AGENT_PORT, resolve));
  console.log(`✓ Seller AI Agent live on http://localhost:${SELLER_AGENT_PORT}/api/ai-research\n`);

  try {
    // -------------------------------------------------------------------------
    // STEP 3: Buyer Unauthenticated Request (Expect HTTP 402)
    // -------------------------------------------------------------------------
    console.log('--- STEP 3: Buyer AI Agent Dispatches Request Without Payment ---');
    const unauthResp = await fetch(`http://localhost:${SELLER_AGENT_PORT}/api/ai-research`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symbol: 'SOL/USDT' }),
    });

    assert.strictEqual(unauthResp.status, 402, 'Must return HTTP 402 Payment Required');
    assert.strictEqual(unauthResp.headers.get('x-payment-required'), 'true');
    const challengeBody = await unauthResp.json();
    console.log(`✓ Received RFC 402 Challenge: Status ${unauthResp.status} ${unauthResp.statusText}`);
    console.log(`✓ Challenge Payee: ${challengeBody.payTo}, Price: ${challengeBody.maxAmountRequired} USDT\n`);

    // -------------------------------------------------------------------------
    // STEP 4: Buyer Autonomous Payment & Voucher Generation (< 0.2ms)
    // -------------------------------------------------------------------------
    console.log('--- STEP 4: Autonomous Payment Negotiation via HaichainClient ---');
    const buyerClient = new HaichainClient({
      keypair: buyerKeypair,
      cluster: 'devnet',
    });

    const startTime = Date.now();
    const paidResp = await buyerClient.callPaidAgent(`http://localhost:${SELLER_AGENT_PORT}/api/ai-research`, {
      body: { symbol: 'SOL/USDT' },
    });
    const durationMs = Date.now() - startTime;

    assert.strictEqual(paidResp.status, 200, 'Autonomous retry must succeed with HTTP 200 OK');
    const resultJson = await paidResp.json();
    console.log(`✓ End-to-end payment & inference succeeded in ${durationMs}ms!`);
    console.log(`✓ Agent Output: ${resultJson.taskResult}`);
    console.log(`✓ Settlement Mode: ${resultJson.haichainReceipt.mode}`);
    console.log(`✓ Amount Settled: ${resultJson.haichainReceipt.amountUsdt} USDT\n`);

    // -------------------------------------------------------------------------
    // STEP 5: Watchtower Sentinel Auto-Registration Verification
    // -------------------------------------------------------------------------
    console.log('--- STEP 5: Verifying Watchtower Auto-Registration in Background ---');
    // Wait 250ms for asynchronous background fire-and-forget to deliver
    await new Promise(r => setTimeout(r, 250));

    const updatedStatus = watchtowerRelayer.getWatchtowerStatus();
    console.log(`✓ Watchtower Tracked Channels: ${updatedStatus.totalMonitoredChannels}`);
    assert(updatedStatus.totalMonitoredChannels >= 1, 'Watchtower must now be tracking the channel');

    const channelRecord = watchtowerRelayer.watchtowerStorage.get('1') || watchtowerRelayer.watchtowerVouchers.get('1');
    assert(channelRecord !== null && channelRecord !== undefined, 'Channel 1 voucher must be recorded in Watchtower');
    console.log(`✓ Watchtower Record: Channel ${channelRecord.channelId}, Cumulative Secured: ${channelRecord.cumulativeAmount} microunits`);
    console.log(`✓ Watchtower Dispute Sentinel Status: ${channelRecord.disputeStatus}\n`);

    // -------------------------------------------------------------------------
    // STEP 6: Adversarial Security Test - Replay Attack Rejection
    // -------------------------------------------------------------------------
    console.log('--- STEP 6: Adversarial Attack Simulation (Replay Attack) ---');
    // Forge raw call reusing the exact same voucher signature
    const voucher = buyerClient.createVoucher({
      merchantPubkey: sellerPubkey,
      amountMicrounit: 5000,
      channelId: 1,
    });
    const authHeader = `X402 ${Buffer.from(JSON.stringify(voucher)).toString('base64')}`;

    // Call once
    const firstCall = await fetch(`http://localhost:${SELLER_AGENT_PORT}/api/ai-research`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': authHeader },
      body: JSON.stringify({ symbol: 'SOL/USDT' }),
    });
    assert.strictEqual(firstCall.status, 200, 'Fresh voucher must be accepted');

    // Call second time with same voucher (REPLAY)
    const replayCall = await fetch(`http://localhost:${SELLER_AGENT_PORT}/api/ai-research`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': authHeader },
      body: JSON.stringify({ symbol: 'SOL/USDT' }),
    });

    assert.strictEqual(replayCall.status, 402, 'Replayed voucher must be rejected with 402');
    const replayErr = await replayCall.json();
    assert(replayErr.verificationError.includes('Replay Attack Rejected'), 'Must detect replay attack');
    console.log(`✓ Replay Attack Blocked: "${replayErr.verificationError}"\n`);

    // -------------------------------------------------------------------------
    // STEP 7: Watchtower Settlement Defense Execution
    // -------------------------------------------------------------------------
    console.log('--- STEP 7: Simulating Dispute & Triggering Watchtower Defense ---');
    const defenseResult = await watchtowerRelayer.defendChannel('1');
    console.log(`✓ Defense Execution Result:`);
    console.log(`  - Action: ${defenseResult.action}`);
    console.log(`  - Channel ID: ${defenseResult.channelId}`);
    console.log(`  - Secured Amount: ${defenseResult.securedAmount} microunits`);
    console.log(`  - On-Chain Status: ${defenseResult.onchainStatus}`);
    if (defenseResult.txHash) {
      console.log(`  - Solana Devnet Transaction: ${defenseResult.txHash}`);
    }
    assert.strictEqual(defenseResult.action, 'SETTLEMENT_DEFENSE_EXECUTED');
    console.log('\n======================================================================');
    console.log('>>> COMPLETE DEVELOPER INTEGRATION SIMULATION: 100% PASSED! <<<');
    console.log('======================================================================\n');
  } finally {
    sellerServer.close();
    if (watchtowerRelayer && typeof watchtowerRelayer.stop === 'function') {
      watchtowerRelayer.stop();
    }
    // Clean up temporary simulation db
    try {
      require('fs').unlinkSync(path.join(__dirname, '../data/test-simulation-watchtower.db.json'));
    } catch (_) {}
  }
}

runEndToEndSimulation().then(() => {
  process.exit(0);
}).catch(err => {
  console.error('\n❌ SIMULATION FAILED:', err);
  process.exit(1);
});
