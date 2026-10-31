// scripts/deploy-devnet.ts
// HAICHAIN v6.9.3: Solana Devnet Genesis Deployment & Orchestration Engine

import { Connection, Keypair, PublicKey, LAMPORTS_PER_SOL } from "@solana/web3.js";
import * as fs from "fs";
import * as path from "path";

const DEVNET_RPC = process.env.SOLANA_RPC_URL || "https://api.devnet.solana.com";

interface DeploymentConfig {
  network: "devnet";
  rpcUrl: string;
  deployerPublicKey: string;
  programId: string;
  masterVaultPda: string;
  vaultBump: number;
  sampleNullifierPda: string;
  timestamp: string;
  explorerLinks: {
    deployer: string;
    program: string;
    vault: string;
  };
}

function loadOrCreateKeypair(filename: string, label: string): Keypair {
  const filePath = path.join(__dirname, "..", filename);
  if (fs.existsSync(filePath)) {
    try {
      const secretKey = Uint8Array.from(JSON.parse(fs.readFileSync(filePath, "utf-8")));
      const kp = Keypair.fromSecretKey(secretKey);
      console.log(`[+] Loaded existing ${label} keypair: ${kp.publicKey.toBase58()}`);
      return kp;
    } catch (err) {
      console.warn(`[!] Failed to parse existing ${filename}, regenerating...`);
    }
  }

  const kp = Keypair.generate();
  fs.writeFileSync(filePath, JSON.stringify(Array.from(kp.secretKey)));
  console.log(`[+] Generated fresh ${label} keypair: ${kp.publicKey.toBase58()}`);
  return kp;
}

async function main() {
  console.log("================================================================================");
  console.log("            HAICHAIN v6.9.3: SOLANA DEVNET DEPLOYMENT ORCHESTRATOR               ");
  console.log("================================================================================\n");

  const connection = new Connection(DEVNET_RPC, "confirmed");
  console.log(`[*] Connecting to Solana Devnet: ${DEVNET_RPC}`);

  try {
    const version = await connection.getVersion();
    console.log(`[+] Connected successfully. Solana Node Version: ${version["solana-core"]}\n`);
  } catch (err: any) {
    console.error(`[-] Failed to connect to Solana Devnet RPC: ${err.message}`);
    process.exit(1);
  }

  // 1. Load or Create Deployer Wallet
  console.log("[1/5] Initializing Deployer Wallet...");
  const deployer = loadOrCreateKeypair("devnet-deployer.json", "Deployer Wallet");
  
  // 2. Check SOL Balance & Request Airdrop
  console.log("\n[2/5] Inspecting SOL Balance for deployment rent & gas...");
  let balance = 0;
  try {
    balance = await connection.getBalance(deployer.publicKey);
    console.log(`[*] Current Balance: ${(balance / LAMPORTS_PER_SOL).toFixed(4)} SOL`);
  } catch (e: any) {
    console.warn(`[!] Unable to fetch balance: ${e.message}`);
  }

  if (balance < 1 * LAMPORTS_PER_SOL) {
    console.log("[*] Balance is low (< 1 SOL). Attempting automatic Devnet faucet airdrop (1.0 SOL)...");
    try {
      const airdropSig = await connection.requestAirdrop(deployer.publicKey, 1 * LAMPORTS_PER_SOL);
      console.log(`[*] Airdrop requested. Signature: ${airdropSig}`);
      const latestBlockhash = await connection.getLatestBlockhash();
      await connection.confirmTransaction({
        signature: airdropSig,
        blockhash: latestBlockhash.blockhash,
        lastValidBlockHeight: latestBlockhash.lastValidBlockHeight
      });
      balance = await connection.getBalance(deployer.publicKey);
      console.log(`[+] Airdrop confirmed! New Balance: ${(balance / LAMPORTS_PER_SOL).toFixed(4)} SOL`);
    } catch (airdropErr: any) {
      console.warn(`[!] Automatic airdrop failed or rate-limited: ${airdropErr.message}`);
      console.log(`\n--------------------------------------------------------------------------------`);
      console.log(`>>> ACTION REQUIRED: Please fund this deployer wallet on Devnet:`);
      console.log(`>>> Wallet Address: ${deployer.publicKey.toBase58()}`);
      console.log(`>>> Faucets: https://faucet.solana.com or https://solfaucet.com`);
      console.log(`--------------------------------------------------------------------------------\n`);
    }
  }

  // 3. Load or Create Program Keypair
  console.log("[3/5] Configuring Program ID...");
  const programKeypair = loadOrCreateKeypair("devnet-program-keypair.json", "HAICHAIN Program");
  const programId = programKeypair.publicKey;
  console.log(`[*] Program ID: ${programId.toBase58()}`);

  // 4. Derive Protocol PDAs
  console.log("\n[4/5] Deriving Cryptographic PDAs & Verification Checks...");
  const [vaultPda, vaultBump] = PublicKey.findProgramAddressSync(
    [Buffer.from("vault"), deployer.publicKey.toBuffer()],
    programId
  );
  console.log(`[*] Master Vault PDA: ${vaultPda.toBase58()} (Bump: ${vaultBump})`);

  // Sample Nullifier PDA for Nonce 1
  const nonceBuffer = Buffer.alloc(8);
  nonceBuffer.writeBigUInt64LE(BigInt(1));
  const [sampleNullifierPda, nullifierBump] = PublicKey.findProgramAddressSync(
    [Buffer.from("nullifier"), vaultPda.toBuffer(), nonceBuffer],
    programId
  );
  console.log(`[*] Sample Nullifier PDA (Nonce 1): ${sampleNullifierPda.toBase58()} (Bump: ${nullifierBump})`);

  // 5. Generate Environment & Deployment Manifest
  console.log("\n[5/5] Generating Deployment Metadata & Environment Profiles...");
  
  const deploymentConfig: DeploymentConfig = {
    network: "devnet",
    rpcUrl: DEVNET_RPC,
    deployerPublicKey: deployer.publicKey.toBase58(),
    programId: programId.toBase58(),
    masterVaultPda: vaultPda.toBase58(),
    vaultBump,
    sampleNullifierPda: sampleNullifierPda.toBase58(),
    timestamp: new Date().toISOString(),
    explorerLinks: {
      deployer: `https://explorer.solana.com/address/${deployer.publicKey.toBase58()}?cluster=devnet`,
      program: `https://explorer.solana.com/address/${programId.toBase58()}?cluster=devnet`,
      vault: `https://explorer.solana.com/address/${vaultPda.toBase58()}?cluster=devnet`
    }
  };

  const manifestPath = path.join(__dirname, "..", "devnet-deployment.json");
  fs.writeFileSync(manifestPath, JSON.stringify(deploymentConfig, null, 2));
  console.log(`[+] Saved deployment manifest: ${manifestPath}`);

  const envDevnetContent = `# HAICHAIN Solana Devnet Environment
SOLANA_NETWORK=devnet
SOLANA_RPC_URL=${DEVNET_RPC}
HAICHAIN_PROGRAM_ID=${programId.toBase58()}
DEPLOYER_WALLET=${deployer.publicKey.toBase58()}
MASTER_VAULT_PDA=${vaultPda.toBase58()}
USDT_MINT=Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB
`;

  const envPath = path.join(__dirname, "..", ".env.devnet");
  fs.writeFileSync(envPath, envDevnetContent);
  console.log(`[+] Created environment profile: ${envPath}`);

  console.log("\n================================================================================");
  console.log("                      DEVNET PRE-DEPLOYMENT SUMMARY                              ");
  console.log("================================================================================");
  console.log(`• Program ID:         ${programId.toBase58()}`);
  console.log(`• Deployer Wallet:    ${deployer.publicKey.toBase58()}`);
  console.log(`• Master Vault PDA:   ${vaultPda.toBase58()}`);
  console.log(`• Solana Explorer:    ${deploymentConfig.explorerLinks.deployer}`);
  console.log("================================================================================\n");
  console.log("Next Command to Build & Broadcast sBPF Bytecode:");
  console.log(`  cargo build-sbf`);
  console.log(`  solana program deploy --program-id devnet-program-keypair.json target/deploy/haichain_core.so -u devnet -k devnet-deployer.json\n`);
}

main().catch((err) => {
  console.error("[-] Unexpected deployment orchestrator failure:", err);
  process.exit(1);
});
