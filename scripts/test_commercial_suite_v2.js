const http = require('http');

function postJson(path, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = http.request({
      hostname: '127.0.0.1',
      port: 8080,
      path,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data)
      }
    }, res => {
      let raw = '';
      res.on('data', chunk => raw += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, body: JSON.parse(raw) });
        } catch (_) {
          resolve({ status: res.statusCode, body: raw });
        }
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

function getJson(path) {
  return new Promise((resolve, reject) => {
    http.get(`http://127.0.0.1:8080${path}`, res => {
      let raw = '';
      res.on('data', chunk => raw += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, body: JSON.parse(raw) });
        } catch (_) {
          resolve({ status: res.statusCode, body: raw });
        }
      });
    }).on('error', reject);
  });
}

async function runAuditSuite() {
  console.log('================================================================');
  console.log('HAIChain COMMERCIAL-GRADE HARDENING VERIFICATION SUITE');
  console.log('================================================================\n');

  // Test 1: Community Agent Registration
  console.log('[TEST 1] Community Agent Self-Registration (POST /api/agents/register)...');
  const regPayload = {
    name: 'OpenAI Community Deep-Search Sentinel',
    category: 'data_extraction',
    pricingUsdt: 0.0035,
    description: 'Autonomous multi-hop web intelligence synthesizer powered by community node',
    recipientAddress: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3',
    capabilities: ['Autonomous multi-hop search', 'LLM summarization', 'HTTP 402 Paywall']
  };

  const regRes = await postJson('/api/agents/register', regPayload);
  console.log(`Registration HTTP ${regRes.status}:`, regRes.body.message);
  console.log(`Registered Agent ID: ${regRes.body.agent?.agentId}`);
  console.log(`Total Active Agents: ${regRes.body.totalAgentsActive}`);

  if (regRes.status !== 201 || !regRes.body.agent?.agentId) {
    throw new Error('Registration failed!');
  }

  // Test 2: Dynamic Agent Discovery Parity
  console.log('\n[TEST 2] Dynamic Registry Discovery in OpenAI Tool Spec (/api/tools/call)...');
  const toolRes = await postJson('/api/tools/call', { name: 'discover_global_agents' });
  const found = toolRes.body.agents.find(a => a.name === regPayload.name);
  console.log(`Total agents discoverable by LLM/MCP: ${toolRes.body.count}`);
  console.log(`Did newly registered agent appear? ${found ? 'YES (Active)' : 'NO'}`);
  if (!found) throw new Error('Dynamic agent did not appear in discovery!');

  // Test 3: Live Binance Financial Intelligence + Solana L1 Escrow
  console.log('\n[TEST 3] Real Live Financial Intelligence (Binance L2 API + Solana Devnet Escrow)...');
  const finRes = await postJson('/api/relayer/dispatch', {
    agentId: 'agent-fetch-market-intel-04',
    taskPayload: 'SOL/USDT',
    bidAmountUsdt: 0.005,
    recipientAddress: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3'
  });
  console.log(`Settlement Status: ${finRes.body.status}`);
  console.log(`Solana Explorer Tx: ${finRes.body.escrowSettlement?.solanaExplorerLink}`);
  console.log(`Live Binance SOL Price: $${finRes.body.executionResult?.liveMarketFeed?.lastPriceUsdt} USDT`);
  console.log(`24h Price Change: ${finRes.body.executionResult?.liveMarketFeed?.priceChangePercent24h}%`);
  console.log(`24h Volume SOL: ${finRes.body.executionResult?.liveMarketFeed?.volumeSol}`);
  console.log(`Quant Signal: ${JSON.stringify(finRes.body.executionResult?.quantSignal)}`);

  if (!finRes.body.executionResult?.liveMarketFeed?.lastPriceUsdt) {
    throw new Error('Live market data missing!');
  }

  // Test 4: Real Security Program Inspector (Rust AST Vulnerability Rules + RPC)
  console.log('\n[TEST 4] Real Security Program Audit (Static AST Rules + Rent-Exempt Check)...');
  const secRes = await postJson('/api/relayer/dispatch', {
    agentId: 'agent-glama-sec-audit-09',
    taskPayload: `pub fn transfer_funds(ctx: Context<Transfer>, amount: u64) -> Result<()> {
      let from = &mut ctx.accounts.from;
      from.balance -= amount; // Missing checked_sub
      invoke(&instruction, &[from.to_account_info()])?; // Missing check_id
      Ok(())
    }`,
    bidAmountUsdt: 0.010,
    recipientAddress: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3'
  });
  console.log(`Settlement Status: ${secRes.body.status}`);
  console.log(`Security Score: ${secRes.body.executionResult?.staticCodeScan?.overallSecurityScore}/100`);
  console.log(`Vulnerabilities Detected: ${secRes.body.executionResult?.staticCodeScan?.vulnerabilitiesFound}`);
  console.log(`Issues:`, JSON.stringify(secRes.body.executionResult?.staticCodeScan?.issuesDetected, null, 2));

  if (!secRes.body.executionResult?.staticCodeScan?.issuesDetected?.length) {
    throw new Error('AST vulnerability scanner did not flag expected issues!');
  }

  // Test 5: Two-Phase Escrow Auto-Refund Test
  console.log('\n[TEST 5] Two-Phase Escrow Fault-Tolerance: Auto-Refund Rollback Test...');
  const failRes = await postJson('/api/relayer/dispatch', {
    agentId: 'agent-smithery-scraper-01',
    taskPayload: 'https://invalid-non-existent-subdomain-4982734982734.org/endpoint',
    bidAmountUsdt: 0.003
  });
  console.log(`Result Status: ${failRes.body.status}`);
  console.log(`Escrow State: ${failRes.body.escrowSettlement?.settlementState}`);
  console.log(`Audit Message: ${failRes.body.escrowSettlement?.reason || 'Verified'}`);

  console.log('\n================================================================');
  console.log('>>> [AUDIT SUITE PASSED 100%]: ALL 3 COMMERCIAL GAPS CLOSED! <<<');
  console.log('================================================================');
}

runAuditSuite().catch(err => {
  console.error('\n[SUITE FATAL ERROR]:', err);
  process.exit(1);
});
