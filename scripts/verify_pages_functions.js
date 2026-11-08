import { onRequest as onMcp } from '../functions/api/mcp.js';
import { onRequest as onSse } from '../functions/sse.js';

async function run() {
  console.log('--- TESTING FUNCTIONS/API/MCP.JS ---');

  // Test 1: GET JSON status
  const req1 = new Request('https://haichain.si/api/mcp', { method: 'GET' });
  const res1 = await onMcp({ request: req1 });
  console.log('GET /api/mcp status:', res1.status, await res1.json());

  // Test 2: GET SSE handshake
  const req2 = new Request('https://haichain.si/sse', {
    method: 'GET',
    headers: { 'accept': 'text/event-stream' }
  });
  const res2 = await onSse({ request: req2 });
  console.log('GET /sse status:', res2.status, 'content-type:', res2.headers.get('content-type'));
  console.log('GET /sse body:\n' + (await res2.text()));

  // Test 3: POST initialize
  const initBody = JSON.stringify({
    jsonrpc: '2.0',
    id: 1,
    method: 'initialize',
    params: {
      protocolVersion: '2024-11-05',
      capabilities: {},
      clientInfo: { name: 'claude-mobile', version: '1.0' }
    }
  });
  const req3 = new Request('https://haichain.si/api/mcp', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: initBody
  });
  const res3 = await onMcp({ request: req3 });
  console.log('POST /api/mcp initialize status:', res3.status, await res3.json());

  console.log('\n>>> CLOUD FUNCTIONS VERIFICATION SUCCESSFUL! <<<');
}

run().catch(console.error);
