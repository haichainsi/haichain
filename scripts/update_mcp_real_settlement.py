import re

with open('mcp-server/src/index.ts', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''    const finalCost = Math.max(bidAmount, targetAgent.pricingUsdt || 0.002);
    const jobId = "JOB-" + Date.now().toString(36).toUpperCase() + "-" + Math.floor(Math.random() * 9000 + 1000);
    const mockTxSignature = "4AgntH1re" + Array.from({ length: 80 }, () => Math.floor(Math.random() * 36).toString(36)).join("").slice(0, 80);

    let executionSummary = "";'''

new_block = '''    const finalCost = Math.max(bidAmount, targetAgent.pricingUsdt || 0.002);
    const jobId = "JOB-" + Date.now().toString(36).toUpperCase() + "-" + Math.floor(Math.random() * 9000 + 1000);

    // REAL ON-CHAIN SOLANA SETTLEMENT: Broadcast micro-escrow to Solana Devnet L1
    let realTxSignature = "";
    const lamportsTransferred = 15000;
    try {
      const recipientPubkey = new PublicKey(targetAgent.recipientAddress || "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3");
      const tx = new Transaction().add(
        SystemProgram.transfer({
          fromPubkey: vaultKeypair.publicKey,
          toPubkey: recipientPubkey,
          lamports: lamportsTransferred,
        })
      );
      realTxSignature = await sendAndConfirmTransaction(connection, tx, [vaultKeypair], {
        commitment: "confirmed",
        preflightCommitment: "confirmed",
      });
    } catch (err: any) {
      console.error(`[MCP hire_global_agent] Solana on-chain settlement error: ${err.message}`);
      throw new Error(`Failed to settle on-chain micro-escrow on Solana ${CLUSTER}: ${err.message}`);
    }

    let executionSummary = "";'''

# Normalize newlines
content = content.replace('\r\n', '\n')
old_block = old_block.replace('\r\n', '\n')
new_block = new_block.replace('\r\n', '\n')

if old_block in content:
    content = content.replace(old_block, new_block)
    # Also replace mockTxSignature references in this function
    content = content.replace('transactionSignature: mockTxSignature,', 'transactionSignature: realTxSignature,')
    content = content.replace('explorerUrl: `https://explorer.solana.com/tx/${mockTxSignature}?cluster=${CLUSTER}`,', 'explorerUrl: `https://explorer.solana.com/tx/${realTxSignature}?cluster=${CLUSTER}`,')
    with open('mcp-server/src/index.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated mcp-server/src/index.ts with real on-chain settlement!")
else:
    print("ERROR: old_block not found in content!")
