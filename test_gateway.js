const http = require('http');

function post(path, body, headers = {}) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify(body);
    const req = http.request({
      hostname: 'localhost',
      port: 3000,
      path: path,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData),
        ...headers
      },
      timeout: 25000
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, headers: res.headers, body: JSON.parse(data) });
        } catch(e) {
          resolve({ status: res.statusCode, headers: res.headers, raw: data });
        }
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function get(path, headers = {}) {
  return new Promise((resolve, reject) => {
    const req = http.request({
      hostname: 'localhost',
      port: 3000,
      path: path,
      method: 'GET',
      headers: headers,
      timeout: 10000
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, headers: res.headers, body: JSON.parse(data) });
        } catch(e) {
          resolve({ status: res.statusCode, headers: res.headers, raw: data });
        }
      });
    });
    req.on('error', reject);
    req.end();
  });
}

async function runTests() {
  console.log('=== TEST 1: GET /v1/models ===');
  const models = await get('/v1/models');
  console.log('Status:', models.status);
  console.log('Available Models:', models.body.data.map(m => m.id));

  console.log('\n=== TEST 2: POST /v1/chat/completions (OpenAI Format) ===');
  const chatResp = await post('/v1/chat/completions', {
    model: 'gpt-4o',
    messages: [{ role: 'user', content: 'Write a quick rust snippet to verify smart contract capability ticket' }]
  }, {
    'Authorization': 'Bearer agent_cursor_ide_02'
  });
  console.log('Status:', chatResp.status);
  console.log('OpenAI ID:', chatResp.body.id);
  console.log('Cost Settled USDT:', chatResp.headers['x-haichain-fee-settled-usdt']);
  console.log('Treasury 20% Margin USDT:', chatResp.headers['x-haichain-treasury-margin-usdt']);
  console.log('Live Solana TxSig:', chatResp.headers['x-haichain-tx-sig']);
  console.log('Explorer URL:', chatResp.body.haichain_settlement?.explorer_url);

  console.log('\n=== TEST 3: POST /v1/messages (Anthropic Claude Code Format) ===');
  const claudeResp = await post('/v1/messages', {
    model: 'claude-3-5-sonnet-20241022',
    messages: [{ role: 'user', content: 'Explain HAICHAIN circuit breaker security' }]
  }, {
    'x-api-key': 'agent_claude_desktop_01'
  });
  console.log('Status:', claudeResp.status);
  console.log('Anthropic ID:', claudeResp.body.id);
  console.log('Fee Settled USDT:', claudeResp.headers['x-haichain-fee-settled-usdt']);
  console.log('Treasury 20% Margin USDT:', claudeResp.headers['x-haichain-treasury-margin-usdt']);
  console.log('Live Solana TxSig:', claudeResp.headers['x-haichain-tx-sig']);
  console.log('Explorer URL:', claudeResp.body.haichain_settlement?.explorer_url);

  console.log('\n=== TEST 4: GET /api/gateway/stats ===');
  const stats = await get('/api/gateway/stats');
  console.log('Treasury Margin Earned ($USDT):', stats.body.treasury.totalMarginEarnedUsdt);
  console.log('Total Transactions Settled:', stats.body.treasury.totalTransactionsSettled);
  console.log('Total Tokens Processed:', stats.body.treasury.totalTokensProcessed);

  console.log('\n=== TEST 5: CIRCUIT BREAKER TRIGGER (Kill-switch) ===');
  const panicResp = await post('/api/gateway/panic', {
    potId: 'agent_cursor_ide_02',
    isPanic: true
  });
  console.log('Panic Status:', panicResp.body.message, 'TxSig:', panicResp.body.txSig);

  console.log('\n=== TEST 6: VERIFY BLOCKED CALL AFTER CIRCUIT BREAKER ===');
  const blockedResp = await post('/v1/chat/completions', {
    model: 'gpt-4o',
    messages: [{ role: 'user', content: 'Drain funds' }]
  }, {
    'Authorization': 'Bearer agent_cursor_ide_02'
  });
  console.log('Blocked Call Status (Expected 403):', blockedResp.status);
  console.log('Blocked Error Message:', blockedResp.body.error?.message);

  // Reset circuit breaker for normal operations
  await post('/api/gateway/panic', { potId: 'agent_cursor_ide_02', isPanic: false });
  console.log('\n=== TEST COMPLETED SUCCESSFULLY ===');
}

runTests().catch(console.error);
