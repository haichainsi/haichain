const http = require('http');

async function testDispatch() {
  console.log('=== TESTING REAL ON-CHAIN RELAYER DISPATCH VIA HTTP GATEWAY (PORT 8080) ===\n');

  const payload = JSON.stringify({
    agentId: 'smithery-web-scraper',
    taskPayload: 'https://example.com',
    bidAmountUsdt: 0.003,
    recipientAddress: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3'
  });

  const req = http.request({
    hostname: '127.0.0.1',
    port: 8080,
    path: '/api/relayer/dispatch',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(payload)
    }
  }, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      console.log(`HTTP Status: ${res.statusCode}`);
      try {
        const json = JSON.parse(data);
        console.log('Dispatch Response:', JSON.stringify(json, null, 2));

        if (json.status === 'COMPLETED_AND_SETTLED_ON_CHAIN' && json.escrowSettlement?.txSignature) {
          console.log('\n>>> [PASS]: REAL SOLANA ON-CHAIN TRANSACTION GENERATED VIA GATEWAY!');
          console.log(`Solana Explorer: ${json.escrowSettlement.solanaExplorerLink}`);
          console.log(`Downstream Web Extraction Title: "${json.executionResult?.title}"`);
        } else {
          console.error('\n>>> [FAIL]: Unexpected response structure');
          process.exit(1);
        }
      } catch (err) {
        console.error('Failed to parse JSON:', data);
        process.exit(1);
      }
    });
  });

  req.on('error', (err) => {
    console.error('Request error:', err);
    process.exit(1);
  });

  req.write(payload);
  req.end();
}

testDispatch();
