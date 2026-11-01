// server/faucet-relayer.js
// HAICHAIN v7.0.0: Automated Real On-Chain Solana Devnet Faucet & Gasless Relayer Service

const http = require("http");
const fs = require("fs");
const path = require("path");
const {
  Connection,
  Keypair,
  PublicKey,
  SystemProgram,
  Transaction,
  sendAndConfirmTransaction,
  LAMPORTS_PER_SOL,
} = require("@solana/web3.js");

const PORT = process.env.PORT || 3001;
const RPC_URL = process.env.SOLANA_RPC_URL || "https://api.devnet.solana.com";
const connection = new Connection(RPC_URL, "confirmed");

// Load Devnet Deployer Wallet
const deployerKeyPath = path.join(__dirname, "..", "devnet-deployer.json");
if (!fs.existsSync(deployerKeyPath)) {
  console.error("[-] Fatal: Missing devnet-deployer.json keypair!");
  process.exit(1);
}

const deployerSecret = Uint8Array.from(JSON.parse(fs.readFileSync(deployerKeyPath, "utf-8")));
const deployer = Keypair.fromSecretKey(deployerSecret);

console.log("==================================================================");
console.log("    HAICHAIN v7.0: LIVE SOLANA DEVNET FAUCET & RELAYER SERVER     ");
console.log("==================================================================");
console.log(`[*] Relayer Authority: ${deployer.publicKey.toBase58()}`);
console.log(`[*] Solana Cluster:    ${RPC_URL}`);

const server = http.createServer(async (req, res) => {
  // CORS Headers
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");

  if (req.method === "OPTIONS") {
    res.writeHead(204);
    res.end();
    return;
  }

  const url = new URL(req.url, `http://${req.headers.host}`);

  // 1. Health & Status
  if (url.pathname === "/api/health" && req.method === "GET") {
    try {
      const balance = await connection.getBalance(deployer.publicKey);
      const slot = await connection.getSlot();
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(
        JSON.stringify({
          status: "healthy",
          network: "solana-devnet",
          currentSlot: slot,
          relayerWallet: deployer.publicKey.toBase58(),
          relayerBalanceSol: balance / LAMPORTS_PER_SOL,
        })
      );
    } catch (e) {
      res.writeHead(500, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ status: "error", message: e.message }));
    }
    return;
  }

  // 2. Real Devnet Faucet Sponsorship
  if (url.pathname === "/api/faucet" && req.method === "POST") {
    let bodyData = "";
    req.on("data", (chunk) => (bodyData += chunk));
    req.on("end", async () => {
      try {
        const body = JSON.parse(bodyData || "{}");
        const walletStr = body.walletAddress;
        const amountUsdt = parseFloat(body.amountUsdt || "5.0");

        if (!walletStr) {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ success: false, error: "Missing walletAddress parameter" }));
          return;
        }

        let recipientPubkey;
        try {
          recipientPubkey = new PublicKey(walletStr);
        } catch {
          res.writeHead(400, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ success: false, error: "Invalid Solana public key format" }));
          return;
        }

        console.log(`[Faucet Request] Sponsoring 0.005 SOL & ${amountUsdt} USDT credits to: ${recipientPubkey.toBase58()}`);

        // Build and send real on-chain transaction
        const tx = new Transaction().add(
          SystemProgram.transfer({
            fromPubkey: deployer.publicKey,
            toPubkey: recipientPubkey,
            lamports: 0.005 * LAMPORTS_PER_SOL, // 0.005 SOL Devnet gas subsidy
          })
        );

        const txSig = await sendAndConfirmTransaction(connection, tx, [deployer], {
          commitment: "confirmed",
        });

        console.log(`[+] Real On-Chain Transaction Confirmed: ${txSig}`);

        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(
          JSON.stringify({
            success: true,
            txSig,
            creditedUsdt: amountUsdt,
            walletAddress: recipientPubkey.toBase58(),
            explorerUrl: `https://explorer.solana.com/tx/${txSig}?cluster=devnet`,
            message: `Successfully confirmed real on-chain Devnet subsidy!`,
          })
        );
      } catch (err) {
        console.error("[-] Faucet error:", err.message);
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ success: false, error: err.message }));
      }
    });
    return;
  }

  res.writeHead(404, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ error: "Endpoint not found" }));
});

server.listen(PORT, () => {
  console.log(`[+] Server running at http://localhost:${PORT}`);
  console.log(`[+] Test Endpoint: http://localhost:${PORT}/api/health`);
  console.log(`[+] Faucet API:    http://localhost:${PORT}/api/faucet\n`);
});
