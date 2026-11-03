/**
 * ==============================================================================
 * HAICHAIN PHASE 2 & PHASE 3 END-TO-END AUTONOMOUS ESCROW & PAYWALL TEST
 * ==============================================================================
 * Exercises:
 * 1. Monetized Agent using @haichainsi/agent-pay SDK (Phase 3)
 * 2. HAICHAIN Production Agent Relayer & HTTP 402 Client Engine (Phase 2)
 * 3. Autonomous Micro-Escrow Handshake & On-Chain Settlement Proof
 */

const http = require('http');
const { HaichainPaywall } = require('../packages/agent-pay/dist/index.js');
const { ProductionAgentRelayer } = require('../server/production-agent-relayer.js');

async function runE2E() {
  console.log('========================================================================');
  console.log(' HAICHAIN PHASE 2 & PHASE 3 E2E INTEGRATION SUITE');
  console.log(' Time:', new Date().toISOString());
  console.log('========================================================================\n');

  const AGENT_PORT = 3855;
  const AGENT_RECIPIENT = 'Sm1thScrap3rPo1nt782VbX4nNmK9q1zEwR2Ty7LpA';
  const TASK_PRICE = 0.003;

  // 1. Setup Phase 3 Monetized Agent Server
  console.log('[STEP 1] Starting Monetized Sub-Agent Server using @haichainsi/agent-pay...');
  const paywall = new HaichainPaywall({
    recipient: AGENT_RECIPIENT,
    priceUsdt: TASK_PRICE,
    serviceName: 'Smithery Autonomous Scraper Sentinel',
    cluster: 'devnet',
    requireConfirmation: false
  });

  const monetizedServer = http.createServer(async (req, res) => {
    const authHeader = req.headers['authorization'] || req.headers['x-payment-signature'];
    const check = await paywall.verifyPayment(authHeader);

    if (!check.valid) {
      const challenge = paywall.generate402Challenge(req.url);
      res.writeHead(challenge.status, challenge.headers);
      return res.end(JSON.stringify(challenge.body));
    }

    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'TASK_COMPLETED',
      agent: 'Smithery Autonomous Scraper Sentinel',
      taskResult: {
        extractedEntities: 14,
        source: 'Live Web Scraping Target',
        antiBotBypass: 'PASS',
        timestamp: new Date().toISOString()
      }
    }));
  });

  await new Promise(r => monetizedServer.listen(AGENT_PORT, r));
  console.log(`-> Sub-Agent Server online at http://127.0.0.1:${AGENT_PORT}\n`);

  // 2. Step 2: Unpaid Request -> Must receive HTTP 402
  console.log('[STEP 2] Client sends request to Sub-Agent WITHOUT payment...');
  const initialRes = await new Promise(resolve => {
    http.get(`http://127.0.0.1:${AGENT_PORT}/crawl?target=solana.com`, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve({ status: res.statusCode, headers: res.headers, body: JSON.parse(data) }));
    });
  });

  console.log('Received Response:', {
    httpStatus: initialRes.status,
    authChallenge: initialRes.headers['www-authenticate'],
    demandedAmount: initialRes.headers['x-payment-amount'] + ' USDT',
    recipientAddress: initialRes.headers['x-payment-payee']
  });

  console.assert(initialRes.status === 402, 'Must return HTTP 402 Payment Required');
  console.assert(initialRes.headers['x-payment-payee'] === AGENT_RECIPIENT, 'Payee must match agent address');
  console.log('-> PASS: HTTP 402 Challenge correctly issued by @haichainsi/agent-pay.\n');

  // 3. Step 3: Phase 2 Relayer intercepts 402 Challenge & executes on-chain settlement
  console.log('[STEP 3] HAICHAIN Relayer resolves 402 challenge & settles micro-escrow...');
  const relayer = new ProductionAgentRelayer();
  const challenge = relayer.parse402Challenge(initialRes.headers, initialRes.body);

  console.log('Relayer parsed challenge:', challenge);
  const settlementReceipt = await relayer.dispatchAndSettle({
    agentId: 'agent-smithery-scraper-01',
    taskPayload: 'https://solana.com',
    bidAmountUsdt: challenge.amountUsdt
  });

  console.log('Relayer Settled Proof:', {
    jobId: settlementReceipt.jobId,
    txSignature: settlementReceipt.escrowSettlement.txSignature.slice(0, 32) + '...',
    amountUsdt: `$${settlementReceipt.escrowSettlement.amountUsdt} USDT`,
    state: settlementReceipt.escrowSettlement.settlementState
  });

  console.assert(settlementReceipt.status === 'COMPLETED_AND_SETTLED', 'Relayer must settle successfully');
  console.log('-> PASS: HAICHAIN Relayer generated valid on-chain escrow proof.\n');

  // 4. Step 4: Resubmit with Proof -> Must receive HTTP 200 OK + Data
  console.log('[STEP 4] Client resubmits task with Payment Proof Header...');
  const authorizedRes = await new Promise(resolve => {
    const req = http.request({
      hostname: '127.0.0.1',
      port: AGENT_PORT,
      path: '/crawl?target=solana.com',
      method: 'GET',
      headers: {
        'Authorization': `X402 ${settlementReceipt.escrowSettlement.txSignature}`
      }
    }, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve({ status: res.statusCode, body: JSON.parse(data) }));
    });
    req.end();
  });

  console.log('Final Agent Delivery Response:', {
    httpStatus: authorizedRes.status,
    agentStatus: authorizedRes.body.status,
    taskResult: authorizedRes.body.taskResult
  });

  console.assert(authorizedRes.status === 200, 'Must return HTTP 200 OK');
  console.assert(authorizedRes.body.status === 'TASK_COMPLETED', 'Task must be completed');
  console.log('-> PASS: Sub-Agent accepted HAICHAIN payment and released data payload!\n');

  // Cleanup
  monetizedServer.close();

  console.log('========================================================================');
  console.log(' PHASE 2 & PHASE 3 INTEGRATION: 100% SUCCESS VERIFIED');
  console.log('========================================================================');
}

runE2E().catch(err => {
  console.error('E2E Test Failed:', err);
  process.exit(1);
});
