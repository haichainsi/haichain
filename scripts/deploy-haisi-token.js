/**
 * Haichain SI ($HAISI) - Official Token-2022 Deployment Script
 * Architecture: Solana SPL Token-2022
 * Extensions:
 *   1. TransferHook (bound to HAICHAIN L1 Kernel Program: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk)
 *   2. MetadataPointer (Self-referential on-chain token metadata: Name: "Haichain SI", Symbol: "HAISI")
 */

const {
  Connection,
  Keypair,
  PublicKey,
  SystemProgram,
  Transaction,
  sendAndConfirmTransaction
} = require('@solana/web3.js');

const {
  TOKEN_2022_PROGRAM_ID,
  ExtensionType,
  getMintLen,
  createInitializeTransferHookInstruction,
  createInitializeMetadataPointerInstruction,
  createInitializeMintInstruction,
  tokenMetadataInitializeWithRentTransfer,
  getOrCreateAssociatedTokenAccount,
  mintTo
} = require('@solana/spl-token');

const fs = require('fs');
const path = require('path');

async function main() {
  console.log('========================================================');
  console.log('🚀 DEPLOYING OFFICIAL $HAISI TOKEN ON SOLANA DEVNET');
  console.log('Token Name: Haichain SI');
  console.log('Token Symbol: HAISI (Super Intelligence)');
  console.log('========================================================');

  const connection = new Connection('https://api.devnet.solana.com', 'confirmed');
  
  // 1. Load Deployer Keypair
  const deployerKeyPath = path.join(__dirname, '..', 'devnet-deployer.json');
  const secret = JSON.parse(fs.readFileSync(deployerKeyPath, 'utf8'));
  const payer = Keypair.fromSecretKey(Uint8Array.from(secret));
  console.log(`[1] Deployer Public Key: ${payer.publicKey.toBase58()}`);

  const balance = await connection.getBalance(payer.publicKey);
  console.log(`    Devnet SOL Balance: ${balance / 1e9} SOL`);
  if (balance < 0.1 * 1e9) {
    throw new Error('Insufficient SOL balance on Devnet Deployer.');
  }

  // 2. Generate Mint Keypair
  const mintKeypair = Keypair.generate();
  const mint = mintKeypair.publicKey;
  console.log(`[2] New $HAISI Mint Address: ${mint.toBase58()}`);

  // 3. Define Extensions
  const transferHookProgramId = new PublicKey('DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk');
  const extensions = [ExtensionType.TransferHook, ExtensionType.MetadataPointer];
  const mintLen = getMintLen(extensions);
  const lamports = await connection.getMinimumBalanceForRentExemption(mintLen);

  console.log(`[3] Calculated Space & Rent: ${mintLen} bytes, ${lamports / 1e9} SOL`);

  // 4. Build Mint Initialization Transaction
  const initMintTx = new Transaction().add(
    SystemProgram.createAccount({
      fromPubkey: payer.publicKey,
      newAccountPubkey: mint,
      space: mintLen,
      lamports,
      programId: TOKEN_2022_PROGRAM_ID
    }),
    createInitializeTransferHookInstruction(
      mint,
      payer.publicKey,
      transferHookProgramId,
      TOKEN_2022_PROGRAM_ID
    ),
    createInitializeMetadataPointerInstruction(
      mint,
      payer.publicKey,
      mint,
      TOKEN_2022_PROGRAM_ID
    ),
    createInitializeMintInstruction(
      mint,
      9, // 9 decimals
      payer.publicKey,
      payer.publicKey,
      TOKEN_2022_PROGRAM_ID
    )
  );

  console.log('[4] Sending Mint Initialization Transaction...');
  const initSig = await sendAndConfirmTransaction(
    connection,
    initMintTx,
    [payer, mintKeypair],
    { commitment: 'confirmed' }
  );
  console.log(`    ✓ Mint Initialized! Tx: ${initSig}`);

  // 5. Initialize On-Chain Metadata (Token-2022 native metadata)
  console.log('[5] Initializing On-Chain Metadata for "Haichain SI" ($HAISI)...');
  const metadataSig = await tokenMetadataInitializeWithRentTransfer(
    connection,
    payer,
    mint,
    payer.publicKey,
    payer.publicKey,
    'Haichain SI',
    'HAISI',
    'https://haichain.si/assets/haisi-metadata.json',
    [],
    { commitment: 'confirmed' },
    TOKEN_2022_PROGRAM_ID
  );
  console.log(`    ✓ Metadata Bound! Tx: ${metadataSig}`);

  // 6. Create Associated Token Account for Treasury & Mint Genesis Supply
  console.log('[6] Creating Treasury Token Account (ATA) and minting initial supply...');
  const treasuryAta = await getOrCreateAssociatedTokenAccount(
    connection,
    payer,
    mint,
    payer.publicKey,
    false,
    'confirmed',
    { commitment: 'confirmed' },
    TOKEN_2022_PROGRAM_ID
  );
  console.log(`    Treasury ATA: ${treasuryAta.address.toBase58()}`);

  // Mint 1,000,000,000 HAISI (1 Billion HAISI tokens @ 9 decimals)
  const genesisSupply = BigInt(1_000_000_000) * BigInt(10 ** 9);
  const mintToSig = await mintTo(
    connection,
    payer,
    mint,
    treasuryAta.address,
    payer.publicKey,
    genesisSupply,
    [],
    { commitment: 'confirmed' },
    TOKEN_2022_PROGRAM_ID
  );
  console.log(`    ✓ Minted 1,000,000,000 HAISI to Treasury! Tx: ${mintToSig}`);

  // 7. Save deployment artifact
  const tokenConfig = {
    tokenName: 'Haichain SI',
    symbol: 'HAISI',
    meaning: 'HAI Super Intelligence',
    mintAddress: mint.toBase58(),
    decimals: 9,
    genesisSupply: '1,000,000,000',
    programId: TOKEN_2022_PROGRAM_ID.toBase58(),
    transferHookProgram: transferHookProgramId.toBase58(),
    treasuryAta: treasuryAta.address.toBase58(),
    deployer: payer.publicKey.toBase58(),
    deployedAt: new Date().toISOString(),
    explorerLinks: {
      mint: `https://explorer.solana.com/address/${mint.toBase58()}?cluster=devnet`,
      treasuryAta: `https://explorer.solana.com/address/${treasuryAta.address.toBase58()}?cluster=devnet`,
      initTx: `https://explorer.solana.com/tx/${initSig}?cluster=devnet`,
      metadataTx: `https://explorer.solana.com/tx/${metadataSig}?cluster=devnet`,
      mintToTx: `https://explorer.solana.com/tx/${mintToSig}?cluster=devnet`
    }
  };

  fs.writeFileSync(
    path.join(__dirname, '..', 'haisi-token-config.json'),
    JSON.stringify(tokenConfig, null, 2)
  );

  console.log('========================================================');
  console.log('🎉 $HAISI TOKEN OFFICIALLY CREATED ON SOLANA DEVNET!');
  console.log(`Official Mint: ${mint.toBase58()}`);
  console.log(`Solana Explorer: ${tokenConfig.explorerLinks.mint}`);
  console.log('Saved to: haisi-token-config.json');
  console.log('========================================================');
}

main().catch(err => {
  console.error('❌ Deployment Failed:', err);
  process.exit(1);
});
