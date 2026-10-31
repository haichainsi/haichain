const { spawn } = require('child_process');
const path = require('path');

const mcpPath = path.join(__dirname, '..', 'mcp-server', 'dist', 'index.js');
console.log('Testing MCP Server from Claude Desktop perspective at:', mcpPath);

const child = spawn('node', [mcpPath]);

child.stdout.on('data', (data) => {
  console.log('>>> [Claude MCP Client Received]:\n' + data.toString().trim());
});

child.stderr.on('data', (data) => {
  console.error('>>> [MCP Server Stderr]:', data.toString().trim());
});

child.on('close', (code) => {
  console.log('MCP process exited with code:', code);
});

// Step 1: Claude Desktop Handshake (initialize)
const initReq = JSON.stringify({
  jsonrpc: "2.0",
  id: 1,
  method: "initialize",
  params: {
    protocolVersion: "2024-11-05",
    capabilities: {},
    clientInfo: { name: "claude-desktop", version: "1.0.0" }
  }
}) + "\n";

child.stdin.write(initReq);

// Step 2: List Tools
setTimeout(() => {
  const toolsReq = JSON.stringify({
    jsonrpc: "2.0",
    id: 2,
    method: "tools/list",
    params: {}
  }) + "\n";
  child.stdin.write(toolsReq);
}, 600);

// Step 3: Call get_agent_spending_pot_balance
setTimeout(() => {
  const callReq = JSON.stringify({
    jsonrpc: "2.0",
    id: 3,
    method: "tools/call",
    params: {
      name: "get_agent_spending_pot_balance",
      arguments: { vaultAddress: "DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk" }
    }
  }) + "\n";
  child.stdin.write(callReq);
}, 1200);

// Step 4: Call execute_micro_payment
setTimeout(() => {
  const callPay = JSON.stringify({
    jsonrpc: "2.0",
    id: 4,
    method: "tools/call",
    params: {
      name: "execute_micro_payment",
      arguments: {
        serviceProviderAta: "ClaudeProviderATA1111111111111111111111111111",
        amountUsdt: 0.002,
        actionDescription: "Claude Sonnet 3.5 Token Inference"
      }
    }
  }) + "\n";
  child.stdin.write(callPay);
}, 1800);

// Step 5: Call trigger_emergency_panic
setTimeout(() => {
  const callPanic = JSON.stringify({
    jsonrpc: "2.0",
    id: 5,
    method: "tools/call",
    params: {
      name: "trigger_emergency_panic",
      arguments: {
        reason: "Adversarial prompt injection detected by Claude sentinel"
      }
    }
  }) + "\n";
  child.stdin.write(callPanic);
}, 2400);

setTimeout(() => {
  child.kill();
}, 3200);
