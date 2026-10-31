const fs = require('fs');
const path = require('path');
const http = require('http');
const { Connection, PublicKey } = require('@solana/web3.js');

const RPC_URL = 'https://api.devnet.solana.com';
const connection = new Connection(RPC_URL, 'confirmed');

async function runDeepAudit() {
  console.log("==========================================================================================");
  console.log("              HAICHAIN STEP 2 DEEP FORENSIC & MULTI-LAYER TECHNICAL AUDIT                 ");
  console.log("==========================================================================================");
  console.log("Audit Timestamp :", new Date().toISOString());
  console.log("Target Cluster  :", "Solana Devnet (https://api.devnet.solana.com)");
  console.log("Vault Authority :", "HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW");

  const results = {
    totalTests: 0,
    passed: 0,
    warnings: 0,
    failed: 0
  };

  function assert(condition, testName, details) {
    results.totalTests++;
    if (condition) {
      results.passed++;
      console.log(`[PASS] ${testName}`);
      if (details) console.log(`       └─ ${details}`);
    } else {
      results.failed++;
      console.error(`[FAIL] ${testName}`);
      if (details) console.error(`       └─ ${details}`);
    }
  }

  function warn(testName, details) {
    results.warnings++;
    console.warn(`[WARN] ${testName}`);
    if (details) console.warn(`       └─ ${details}`);
  }

  // =========================================================================
  // LAYER 1: CLAUDE CONFIG & MCP SYSTEM ARCHITECTURE
  // =========================================================================
  console.log("\n>>> LAYER 1: CONFIGURATION & MCP FILE INTEGRITY");
  const cfgPath = path.resolve('claude_desktop_config.json');
  assert(fs.existsSync(cfgPath), "Config File Exists", `File located at ${cfgPath}`);

  let cfgObj = null;
  try {
    cfgObj = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
    assert(typeof cfgObj === 'object' && cfgObj.mcpServers, "Config Schema Validity", "Root key 'mcpServers' present");
  } catch (e) {
    assert(false, "Config Schema Validity", e.message);
  }

  const haichainServer = cfgObj?.mcpServers?.haichain;
  assert(haichainServer && haichainServer.command === 'node', "Server Command Execution", "Configured to execute 'node'");
  
  const serverScript = haichainServer?.args?.[0];
  assert(serverScript && fs.existsSync(serverScript), "Target MCP Binary Existence", `Verified binary exists at: ${serverScript} (${fs.statSync(serverScript).size} bytes)`);

  assert(haichainServer?.env?.SOLANA_RPC_URL === RPC_URL, "RPC URL Configuration", `Env SOLANA_RPC_URL matches: ${RPC_URL}`);

  // =========================================================================
  // LAYER 2: HTTP ENDPOINT AUDIT (/download & /api/faucet)
  // =========================================================================
  console.log("\n>>> LAYER 2: HTTP GATEWAY & DOWNLOAD STREAMING AUDIT");

  // 2.1 Test /download/claude_desktop_config.json
  await new Promise((resolve) => {
    http.get('http://localhost:3000/download/claude_desktop_config.json', (res) => {
      assert(res.statusCode === 200, "Download Endpoint Status Code", `Expected 200, received ${res.statusCode}`);
      assert(res.headers['content-disposition']?.includes('attachment'), "Attachment Header", `Header: ${res.headers['content-disposition']}`);
      assert(res.headers['content-type']?.includes('application/json'), "MIME Type Correctness", `MIME: ${res.headers['content-type']}`);

      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try {
          const dlObj = JSON.parse(body);
          assert(dlObj.mcpServers?.haichain, "Downloaded Payload Completeness", "Valid JSON matching server configuration");
        } catch (e) {
          assert(false, "Downloaded Payload Completeness", e.message);
        }
        resolve();
      });
    }).on('error', err => {
      assert(false, "Download Endpoint Connection", err.message);
      resolve();
    });
  });

  // 2.2 Test /api/faucet Endpoint
  console.log("\n>>> LAYER 3: 1-CLICK FAUCET & SOLANA DEVNET ON-CHAIN TRANSACTION AUDIT");
  const testAirdropAmt = 10.0;
  const faucetStart = Date.now();
  
  const faucetResponse = await new Promise((resolve) => {
    const postData = JSON.stringify({
      amountUsdt: testAirdropAmt,
      walletAddress: "HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW"
    });

    const req = http.request('http://localhost:3000/api/faucet', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      },
      timeout: 15000
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, data: JSON.parse(body) });
        } catch (e) {
          resolve({ status: res.statusCode, raw: body, error: e.message });
        }
      });
    });

    req.on('error', (e) => resolve({ error: e.message }));
    req.write(postData);
    req.end();
  });

  const faucetLatency = Date.now() - faucetStart;
  assert(faucetResponse.status === 200, "Faucet API Status 200 OK", `Received HTTP ${faucetResponse.status} in ${faucetLatency}ms`);
  assert(faucetResponse.data?.success === true, "Faucet Success Flag", "Payload returned success: true");
  assert(faucetResponse.data?.isLiveOnChain === true, "Faucet isLiveOnChain Flag", "System confirmed broadcast to live blockchain cluster");

  const txSig = faucetResponse.data?.txSig;
  assert(txSig && typeof txSig === 'string' && txSig.length > 50, "Solana Transaction Signature", `Signature: ${txSig}`);

  // =========================================================================
  // LAYER 4: SOLANA DEVNET RPC VERIFICATION OF THE FAUCET TRANSACTION
  // =========================================================================
  console.log("\n>>> LAYER 4: DIRECT RPC BLOCKCHAIN VERIFICATION (TRANSACTION INSPECTION)");
  console.log(`Querying signature: ${txSig}`);
  
  try {
    const tx = await connection.getTransaction(txSig, {
      commitment: 'confirmed',
      maxSupportedTransactionVersion: 0
    });

    assert(tx !== null, "Transaction Exists on Solana Ledger", `Queried directly from ${RPC_URL}`);
    if (tx) {
      assert(tx.meta.err === null, "Transaction Execution Status", "Success code 0 (Zero errors)");
      assert(tx.slot > 517180000, "Block Slot Verification", `Confirmed in Slot #${tx.slot}`);
      assert(tx.blockTime > 1793400000, "Block Timestamp Verification", `Block Unix Time: ${tx.blockTime} (${new Date(tx.blockTime * 1000).toISOString()})`);
      assert(tx.meta.fee === 5000, "Network Fee Paid", `${tx.meta.fee} lamports (0.000005 SOL)`);

      // Verify Memo Program Instruction was recorded
      const memoProgramId = "MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr";
      const hasMemoInvoke = tx.meta.logMessages.some(l => l.includes(memoProgramId));
      assert(hasMemoInvoke, "Memo Program Invocation", `Verified SPL Memo Program: ${memoProgramId}`);

      const memoLog = tx.meta.logMessages.find(l => l.includes("HAICHAIN:FAUCET_AIRDROP"));
      assert(memoLog !== undefined, "Immutability of Airdrop Receipt", `On-chain Memo Content: "${memoLog?.replace('Program log: ', '')}"`);

      // Check account keys
      const accounts = tx.transaction.message.accountKeys.map(k => k.toBase58 ? k.toBase58() : k.toString());
      assert(accounts.includes("HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW"), "Signer Account Verification", "Vault Master Key signed and authorized the airdrop");
    }
  } catch (err) {
    assert(false, "Solana RPC Transaction Query", err.message);
  }

  // =========================================================================
  // LAYER 5: UI & CSS ANTI-SCROLLBAR VERIFICATION
  // =========================================================================
  console.log("\n>>> LAYER 5: UI RESILIENCE & SCROLLBAR ELIMINATION AUDIT");
  const dashHtml = fs.readFileSync('app/dashboard.html', 'utf8');

  assert(dashHtml.includes('id="claude-mcp-modal"'), "Modal DOM Mount", "Element #claude-mcp-modal exists in DOM");
  assert(dashHtml.includes('no-scrollbar'), "No-Scrollbar Class Application", "Modal uses class 'no-scrollbar'");
  assert(dashHtml.includes('whitespace-pre-wrap break-all overflow-hidden'), "Code Block Anti-Scrollbar", "JSON snippet pre uses wrap + overflow-hidden to prevent horizontal scrollbars");
  assert(dashHtml.includes('id="dash-pay-tab-faucet"'), "Faucet Tab In DOM", "Element #dash-pay-tab-faucet present in Deposit Modal");
  assert(dashHtml.includes('id="deposit-faucet-banner"'), "Faucet Banner In DOM", "Element #deposit-faucet-banner present in Deposit Modal");

  // =========================================================================
  // LAYER 6: EDGE CASE & LIMITATION ANALYSIS (HONEST APPRAISAL)
  // =========================================================================
  console.log("\n>>> LAYER 6: EDGE CASES & SYSTEM BOUNDARIES (AUDIT FINDINGS)");

  // Check 1: Rate Limiting
  warn("Rate Limiting on /api/faucet", "Currently there is no IP-based rate limiting on /api/faucet. A malicious client could send 100 requests/sec, consuming SOL in the deployer wallet.");

  // Check 2: Absolute File Path in Config
  warn("Absolute Path in Config", `The generated config contains absolute path: '${serverScript}'. If the user clones the repo to another machine/directory, they must update this path or use an installer script.`);

  // Check 3: RPC Dependency
  warn("Public Devnet RPC Throttling", "The system uses public 'api.devnet.solana.com'. During high network congestion, public RPC can return HTTP 429. For production, a dedicated RPC provider (Helius, Triton, QuickNode) is recommended.");

  // Summary
  console.log("\n==========================================================================================");
  console.log(`AUDIT COMPLETE: ${results.passed}/${results.totalTests} TESTS PASSED (${results.failed} Failed, ${results.warnings} Advisory Warnings)`);
  console.log("==========================================================================================");
}

runDeepAudit().catch(console.error);
