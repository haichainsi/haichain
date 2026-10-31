const fs = require('fs');
const path = require('path');
const http = require('http');
const { Connection, PublicKey } = require('@solana/web3.js');

const RPC_URL = 'https://api.devnet.solana.com';
const connection = new Connection(RPC_URL, 'confirmed');

async function auditStep2() {
  console.log("===============================================================================");
  console.log("             HAICHAIN STEP 2 INDEPENDENT TECHNICAL AUDIT REPORT");
  console.log("===============================================================================");
  console.log("Audit Timestamp:", new Date().toISOString());

  // 1. AUDIT CLAUDE CONFIG FILE
  console.log("\n--- [AUDIT 1/3]: CLAUDE DESKTOP & CURSOR CONFIG INTEGRITY ---");
  const configPath = path.resolve('claude_desktop_config.json');
  console.log("Checking config file at:", configPath);
  if (!fs.existsSync(configPath)) {
    console.error("❌ claude_desktop_config.json NOT FOUND!");
  } else {
    try {
      const raw = fs.readFileSync(configPath, 'utf8');
      const parsed = JSON.parse(raw);
      console.log("✅ JSON Validity: Syntax Valid 100%");
      const targetScript = parsed.mcpServers?.haichain?.args?.[0];
      console.log("Configured Target Script:", targetScript);
      if (fs.existsSync(targetScript)) {
        console.log("✅ Target Script Existence: File exists on disk (" + fs.statSync(targetScript).size + " bytes)");
      } else {
        console.error("❌ Target script does not exist at path!");
      }
    } catch (e) {
      console.error("❌ JSON Parse Error:", e.message);
    }
  }

  // 2. AUDIT DOWNLOAD ENDPOINT
  console.log("\n--- [AUDIT 2/3]: DOWNLOAD ENDPOINT (/download/claude_desktop_config.json) ---");
  await new Promise((resolve) => {
    http.get('http://localhost:3000/download/claude_desktop_config.json', (res) => {
      console.log("HTTP Response Status:", res.statusCode);
      console.log("Content-Disposition Header:", res.headers['content-disposition']);
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(d);
          console.log("✅ Endpoint Payload: Valid JSON with", Object.keys(parsed.mcpServers || {}).length, "server configured.");
        } catch (_) {
          console.error("❌ Failed to parse downloaded config as JSON");
        }
        resolve();
      });
    }).on('error', (err) => {
      console.error("❌ Download HTTP Error:", err.message);
      resolve();
    });
  });

  // 3. AUDIT FAUCET ON-CHAIN BROADCAST
  console.log("\n--- [AUDIT 3/3]: 1-CLICK FAUCET ON-CHAIN BROADCAST & RECORDING ---");
  const faucetPayload = JSON.stringify({ amountUsdt: 10.0 });
  const faucetResult = await new Promise((resolve) => {
    const req = http.request('http://localhost:3000/api/faucet', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(faucetPayload)
      }
    }, (res) => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try { resolve(JSON.parse(d)); } catch (e) { resolve({ error: e.message }); }
      });
    });
    req.on('error', (e) => resolve({ error: e.message }));
    req.write(faucetPayload);
    req.end();
  });

  console.log("Faucet API Result:", faucetResult);
  if (faucetResult.isLiveOnChain && faucetResult.txSig) {
    console.log("Querying transaction directly on Solana Devnet RPC for signature:", faucetResult.txSig);
    try {
      const tx = await connection.getTransaction(faucetResult.txSig, { commitment: 'confirmed', maxSupportedTransactionVersion: 0 });
      if (tx) {
        console.log("✅ ON-CHAIN CONFIRMATION VERIFIED!");
        console.log(`- Slot: #${tx.slot}`);
        console.log(`- Timestamp: ${new Date(tx.blockTime * 1000).toISOString()}`);
        console.log(`- Network Fee Paid: ${tx.meta.fee} lamports`);
        console.log("- Log Messages:");
        tx.meta.logMessages.forEach(m => console.log(`   > ${m}`));
        console.log(`- Solana Explorer URL: https://explorer.solana.com/tx/${faucetResult.txSig}?cluster=devnet`);
      } else {
        console.log("Transaction pending confirmation or not found.");
      }
    } catch (err) {
      console.error("Failed to query transaction on-chain:", err.message);
    }
  }

  console.log("\n===============================================================================");
  console.log("AUDIT STEP 2 VERIFICATION COMPLETE");
  console.log("===============================================================================");
}

auditStep2().catch(console.error);
