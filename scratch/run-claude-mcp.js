const { Client } = require("@modelcontextprotocol/sdk/client/index.js");
const { StdioClientTransport } = require("@modelcontextprotocol/sdk/client/stdio.js");
const path = require("path");

async function run() {
  const mcpDistPath = path.resolve(__dirname, "..", "mcp-server", "dist", "index.js");
  console.log("Connecting Claude MCP Client to:", mcpDistPath);

  const transport = new StdioClientTransport({
    command: "node",
    args: [mcpDistPath]
  });

  const client = new Client(
    { name: "claude-desktop-test-runner", version: "1.0.0" },
    { capabilities: {} }
  );

  await client.connect(transport);
  console.log("✅ Claude Desktop connected successfully to HAICHAIN MCP Server via Stdio!\n");

  // 1. List tools
  console.log("--- 1. Testing List Tools ---");
  const tools = await client.listTools();
  console.log(`Discovered ${tools.tools.length} Tools:`);
  tools.tools.forEach(t => console.log(`  - [${t.name}]: ${t.description}`));

  // 2. Call get_agent_spending_pot_balance
  console.log("\n--- 2. Testing get_agent_spending_pot_balance ---");
  const balanceRes = await client.callTool({
    name: "get_agent_spending_pot_balance",
    arguments: { vaultAddress: "DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk" }
  });
  console.log("Balance Response:", JSON.stringify(balanceRes, null, 2));

  // 3. Call execute_micro_payment
  console.log("\n--- 3. Testing execute_micro_payment ---");
  const payRes = await client.callTool({
    name: "execute_micro_payment",
    arguments: {
      serviceProviderAta: "ClaudeProviderATA1111111111111111111111111111",
      amountUsdt: 0.0025,
      actionDescription: "Claude 3.5 Sonnet Tool Call Execution"
    }
  });
  console.log("Payment Response:", JSON.stringify(payRes, null, 2));

  // 4. Call trigger_emergency_panic
  console.log("\n--- 4. Testing trigger_emergency_panic ---");
  const panicRes = await client.callTool({
    name: "trigger_emergency_panic",
    arguments: {
      reason: "Suspicious recursive looping detected by Claude watchdog"
    }
  });
  console.log("Panic Response:", JSON.stringify(panicRes, null, 2));

  await client.close();
  console.log("\n✅ End-to-end Claude MCP test completed successfully!");
}

run().catch(console.error);
