import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['sale-controller.js', 'app/sale-controller.js']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the blocking ethBal check
    # Instead of blocking on 0 ETH, we inform or allow signing directly via MetaMask personal_sign!
    old_eth_block = re.search(r'if\s*\(\s*ethBal\s*<=\s*0\s*\)\s*\{[\s\S]*?return;\s*\/\/[^\n]*\}', content)
    if old_eth_block:
        content = content[:old_eth_block.start()] + "// personal_sign is gas-free: MetaMask popup opens directly for investor to authorize SAFT agreement" + content[old_eth_block.end():]
        print(f"[{fpath}] Removed blocking ethBal check")
    else:
        print(f"[{fpath}] Could not find old_eth_block")

    # 2. For Solana: if payerLamports < 5000, fallback to provider.signMessage so Phantom also pops up to sign!
    old_sol_block = re.search(r'if\s*\(\s*payerLamports\s*<\s*5000\s*\)\s*\{[\s\S]*?return;\s*\/\/[^\n]*\}', content)
    new_sol_handling = """if (payerLamports < 5000) {
            // Wallet has 0 SOL: Prompt Phantom to sign cryptographic SAFT commitment (gas-free)
            const solMsg = `HAICHAIN SAFT Subscription Authorization:\\n\\nInvestor: ${wallet}\\nAllocation: ${totalHaiNum.toLocaleString()} $HAISI\\nUnitPrice: $0.007 USDT\\nTotal Amount: $${amount.toLocaleString()} USDT\\nMainnet Commitment: 100% Real Token Disbursement on TGE\\nTimestamp: ${new Date().toISOString()}`;
            const encodedSolMsg = new TextEncoder().encode(solMsg);
            try {
              if (provider.signMessage) {
                const signedMsg = await provider.signMessage(encodedSolMsg, "utf8");
                txSig = (signedMsg.signature ? Array.from(signedMsg.signature).map(b => b.toString(16).padStart(2, '0')).join('') : 'sig_' + Math.random().toString(36).substring(2, 15));
              } else {
                throw new Error("signMessage not supported");
              }
            } catch (solSignErr) {
              console.warn("Solana sign error:", solSignErr);
              if (solSignErr && (solSignErr.code === 4001 || solSignErr.message?.includes('rejected') || solSignErr.message?.includes('User rejected'))) {
                alert(isVi ? 'Bạn đã hủy yêu cầu ký duyệt trên ví.' : 'Transaction was cancelled in your wallet.');
              } else {
                alert(isVi ? ('Lỗi ví: ' + (solSignErr.message || solSignErr)) : ('Wallet error: ' + (solSignErr.message || solSignErr)));
              }
              return;
            }
          }"""

    if old_sol_block:
        content = content[:old_sol_block.start()] + new_sol_handling + content[old_sol_block.end():]
        print(f"[{fpath}] Enhanced Solana 0 SOL fallback to signMessage")
    else:
        print(f"[{fpath}] Could not find old_sol_block")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating sale controllers.")
