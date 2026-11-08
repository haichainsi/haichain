const fs = require('fs');

const handlerCode = fs.readFileSync('server/cloud-mcp-functions/_mcp_handler.js', 'utf8');

// Strip export from handleMcpRequest so it's a local function inside worker
const cleanHandlerCode = handlerCode.replace('export async function handleMcpRequest', 'async function handleMcpRequest');

const workerCode = `/**
 * ==============================================================================
 * HAICHAIN Cloud MCP Gateway Worker v6.9.3
 * Target: Cloudflare Worker (Deploy on https://mcp.haichain.si)
 * Protocols: Streamable HTTP (JSON-RPC 2.0) & SSE Handshake
 * Tools: 4 Solana On-Chain Tools (Query, Micro-Payment, Panic Kill-Switch, Merkle Proof)
 * ==============================================================================
 */

${cleanHandlerCode}

export default {
  async fetch(request, env, ctx) {
    return await handleMcpRequest(request);
  }
};
`;

fs.writeFileSync('server/haichain-mcp-worker.js', workerCode, 'utf8');
console.log('Successfully created server/haichain-mcp-worker.js (Size: ' + workerCode.length + ' bytes)');
