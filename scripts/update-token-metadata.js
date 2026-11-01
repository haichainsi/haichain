/**
 * Haichain SI ($HAISI) - Update On-Chain Token-2022 Metadata
 * Updates:
 *   1. Name -> "Haichain SI"
 *   2. URI  -> "https://haichain.si/assets/haisi-metadata.json"
 */

const {
  Connection,
  Keypair,
  PublicKey,
  sendAndConfirmTransaction,
  Transaction,
  SystemProgram
} = require('@solana/web3.js');

const {
  TOKEN_2022_PROGRAM_ID,
  getTokenMetadata,
  tokenMetadataUpdateFieldWithRentTransfer
} = require('@solana/spl-token');

const { Field } = require('@solana/spl-token-metadata');

const fs = require('fs');
const path = require('path');

async function main() {
  console.log('========================================================');
  console.log('🔄 UPDATING ON-CHAIN TOKEN-2022 METADATA FOR $HAISI');
  console.log('========================================================');

  const connection = new Connection('https://api.devnet.solana.com', 'confirmed');
  
  // 1. Load Deployer Keypair
  const deployerKeyPath = path.join(__dirname, '..', 'devnet-deployer.json');
  const secret = JSON.parse(fs.readFileSync(deployerKeyPath, 'utf8'));
  const payer = Keypair.fromSecretKey(Uint8Array.from(secret));
  console.log(`[1] Update Authority / Deployer: ${payer.publicKey.toBase58()}`);

  const mint = new PublicKey('3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu');
  console.log(`[2] Mint Address: ${mint.toBase58()}`);

  // Fetch current on-chain metadata
  const beforeMeta = await getTokenMetadata(connection, mint, 'confirmed', TOKEN_2022_PROGRAM_ID);
  console.log('[3] Current On-Chain Metadata:', JSON.stringify(beforeMeta, null, 2));

  // 4. Update Name -> "Haichain SI"
  console.log('\n[4] Updating Name to "Haichain SI"...');
  const nameTxSig = await tokenMetadataUpdateFieldWithRentTransfer(
    connection,
    payer,
    mint,
    payer,
    'Name',
    'Haichain SI',
    [],
    { commitment: 'confirmed' },
    TOKEN_2022_PROGRAM_ID
  );
  console.log(`    ✓ Name Updated! Tx: ${nameTxSig}`);

  // 5. Update URI -> "https://haichain.si/assets/haisi-metadata-v2.json"
  console.log('\n[5] Updating URI to "https://haichain.si/assets/haisi-metadata-v2.json"...');
  const uriTxSig = await tokenMetadataUpdateFieldWithRentTransfer(
    connection,
    payer,
    mint,
    payer,
    'Uri',
    'https://haichain.si/assets/haisi-metadata-v2.json',
    [],
    { commitment: 'confirmed' },
    TOKEN_2022_PROGRAM_ID
  );
  console.log(`    ✓ URI Updated! Tx: ${uriTxSig}`);

  // 6. Verify updated on-chain metadata
  const afterMeta = await getTokenMetadata(connection, mint, 'confirmed', TOKEN_2022_PROGRAM_ID);
  console.log('\n[6] Verified New On-Chain Metadata:', JSON.stringify(afterMeta, null, 2));

  console.log('========================================================');
  console.log('🎉 METADATA SUCCESSFULLY SYNCHRONIZED ON-CHAIN!');
  console.log(`Solana Explorer: https://explorer.solana.com/address/${mint.toBase58()}?cluster=devnet`);
  console.log('========================================================');
}

main().catch(err => {
  console.error('❌ Update Failed:', err);
  process.exit(1);
});
