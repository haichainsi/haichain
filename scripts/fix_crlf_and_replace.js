const fs = require('fs');

function cleanFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  const wasCRLF = content.includes('\r\n');
  let text = content.replace(/\r\n/g, '\n');

  // 1. Quick Demos label
  text = text.replace(/<span>Quick Demos<\/span>/g, `<span data-i18n="playground.quickDemos">Quick Demos</span>`);
  text = text.replace(/<span class="truncate">Anti-Drain<\/span>/g, `<span class="truncate" data-i18n="playground.demoAntiDrain">Anti-Drain</span>`);
  text = text.replace(/<span class="truncate">Micro-Escrow<\/span>/g, `<span class="truncate" data-i18n="playground.demoMicroEscrow">Micro-Escrow</span>`);
  text = text.replace(/<span class="truncate">Optimus AI<\/span>/g, `<span class="truncate" data-i18n="playground.demoOptimus">Optimus AI</span>`);
  text = text.replace(/<span class="truncate">Anchor CPI<\/span>/g, `<span class="truncate" data-i18n="playground.demoAnchor">Anchor CPI</span>`);

  // 2. Replace any remaining isVi ternary:
  // e.g. alert(isVi ? ... : ...);
  // We can write a parser that finds `isVi \s* \?` and replaces the block appropriately!
  
  // Notice 1: copy token 2022 mint
  text = text.replace(/alert\(isVi\s*\?\s*`ĐÃ SAO CHÉP ĐỊA CHỈ MINT TOKEN-2022[\s\S]*?`\s*:\s*`TOKEN-2022 MINT COPIED[\s\S]*?`\);/g,
    `alert(\`\${getDashNotice('copyMintPrompt') || 'TOKEN-2022 MINT:'}\\n\\n\${TOKEN_2022_MINT}\\n\\n\${getDashNotice('copyMintGuide') || ''}\`);`);

  // Notice 2: Vesting overview banner summary
  text = text.replace(/\$\{isVi\s*\?\s*`Ví <strong class="text-black dark:text-white">\$\{shortAddr\}<\/strong> đang sở hữu[\s\S]*?`\s*:\s*`Investor <strong class="text-black dark:text-white">\$\{shortAddr\}<\/strong> holds[\s\S]*?`\}/g,
    `\${shortAddr}: \${haiTotal.toLocaleString()} \\$HAISI (Token-2022 Locked)`);

  // Notice 3: deposit button text
  text = text.replace(/dashConfirmDepositBtn\.textContent = isVi\s*\?\s*"Xác Nhận Nạp On-Chain \(Ký Ví Phantom\)"\s*:\s*"Confirm On-Chain Deposit \(Sign Phantom\)";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('confirmOnChainDepositPhantom');`);

  text = text.replace(/dashConfirmDepositBtn\.textContent = isVi\s*\?\s*"Kết Nối Ví Phantom Để Nạp"\s*:\s*"Connect Phantom to Deposit";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('connectPhantomToDeposit');`);

  // Notice 4: Faucet added msg
  text = text.replace(/message: isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT thử nghiệm đã nạp vào ví[\s\S]*?`\s*:\s*`\+\$\{added\.toFixed\(2\)\} USDT testnet funds credited[\s\S]*?`,/g,
    `message: \`+\${added.toFixed(2)} USDT \${getDashNotice('faucetCredited')}\`,`);

  text = text.replace(/alert\(isVi\s*\?\s*`🎉 Nhận USDT Thử Nghiệm Devnet Thành Công![\s\S]*?`\s*:\s*`🎉 Devnet Testnet USDT Claimed![\s\S]*?`\);/g,
    `alert(getDashNotice('faucetCredited'));`);

  // Notice 5: MetaMask 0 ETH
  text = text.replace(/alert\(isVi\s*\?\s*`⚠️ Số Dư Ví MetaMask Không Đủ \(0 ETH\)![\s\S]*?`\s*:\s*`⚠️ MetaMask Balance Insufficient \(0 ETH\)![\s\S]*?`\);/g,
    `alert(getDashNotice('metaMaskInsufficientEth'));`);

  // Notice 6: MetaMask success
  text = text.replace(/alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 MetaMask Thành Công![\s\S]*?`\s*:\s*`🎉 Web3 MetaMask Deposit Confirmed![\s\S]*?`\);/g,
    `alert(getDashNotice('metaMaskDepositSuccess'));`);

  // Notice 7: Web3 connected confirm prompt
  text = text.replace(/alert\(isVi\s*\?\s*`Đã kết nối ví \$\{userWallet\.provider\} thành công![\s\S]*?`\s*:\s*`Connected \$\{userWallet\.provider\} wallet successfully![\s\S]*?`\);/g,
    `alert(getDashNotice('web3ConnectedConfirmPrompt'));`);

  // Notice 8: No web3 detected faucet guide
  text = text.replace(/alert\(isVi\s*\?\s*"Chưa phát hiện tiện ích ví Web3 \(Phantom hoặc Solflare\)[\s\S]*?"\s*:\s*"Web3 wallet \(Phantom or Solflare\) not detected[\s\S]*?"\);/g,
    `alert(getDashNotice('noWeb3DetectedFaucetGuide'));`);

  // Notice 9: 0 SOL insufficient
  text = text.replace(/alert\(isVi\s*\?\s*`⚠️ Số Dư Ví \$\{userWallet\.provider\} Không Đủ \(0 SOL\)![\s\S]*?`\s*:\s*`⚠️ Insufficient SOL in \$\{userWallet\.provider\} \(0 SOL\)![\s\S]*?`\);/g,
    `alert(getDashNotice('insufficientSolGaslessGuide'));`);

  // Notice 10: Relayer gasless toast
  text = text.replace(/message: isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT đã vào Master Vault & Trợ cấp 0\.02 SOL vào ví`\s*:\s*`\+\$\{added\.toFixed\(2\)\} USDT credited & 0\.02 SOL gas subsidized`,/g,
    `message: \`+\${added.toFixed(2)} USDT (\${getDashNotice('gaslessDepositSuccess')})\`,`);

  // Notice 11: Relayer gasless alert
  text = text.replace(/alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 Thành Công \(Hỗ Trợ 0% Phí Gas\)![\s\S]*?`\s*:\s*`🎉 Web3 Gasless Deposit Confirmed![\s\S]*?`\);/g,
    `alert(getDashNotice('gaslessDepositSuccess'));`);

  // Notice 12: Normal web3 deposit alert
  text = text.replace(/alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 Thành Công!\s*\\n\\nGiao dịch đã được xác nhận bất biến trên mạng Solana Devnet\.[\s\S]*?`\s*:\s*`🎉 Web3 Deposit Confirmed![\s\S]*?`\);/g,
    `alert(getDashNotice('web3DepositConfirmedDevnet'));`);

  // Notice 13: Fiat sandbox notice
  text = text.replace(/alert\(isVi\s*\?\s*`Thông Báo Cổng Thanh Toán Fiat[\s\S]*?`\s*:\s*`Fiat Gateway Notice[\s\S]*?`\);/g,
    `alert(getDashNotice('fiatSandboxNotice'));`);

  // Notice 14: Zero balance cannot withdraw
  text = text.replace(/alert\(isVi\s*\?\s*"Số dư trong Master Vault của bạn hiện tại là \$0\.0000 USDT[\s\S]*?"\s*:\s*"Your Master Vault balance is \$0\.0000 USDT[\s\S]*?"\);/g,
    `alert(getDashNotice('zeroBalanceCannotWithdraw'));`);

  // Notice 15: Insufficient balance to withdraw
  text = text.replace(/alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault hiện tại của bạn là \$[\s\S]*?`\s*:\s*`Insufficient balance![\s\S]*?`\);/g,
    `alert(getDashNotice('insufficientWithdrawBalance'));`);

  // Notice 16: Invalid Solana address
  text = text.replace(/alert\(isVi\s*\?\s*"Địa chỉ ví đích không hợp lệ![\s\S]*?"\s*:\s*"Invalid destination address![\s\S]*?"\);/g,
    `alert(getDashNotice('invalidSolanaAddress'));`);

  // Notice 17: AI task insufficient balance msg
  text = text.replace(/message: isVi\s*\?\s*`Số dư Master Vault \(\$[\s\S]*?\) không đủ cho tác vụ \$[\s\S]*?\. Vui lòng nạp thêm qua Faucet Devnet\.`\s*:\s*`Master Vault balance \(\$[\s\S]*?\) insufficient for \$[\s\S]*? task\. Please claim devnet faucet\.`,/g,
    `message: getDashNotice('vaultBalanceInsufficientForTask'),`);

  // Notice 18: AI task insufficient balance alert
  text = text.replace(/alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault của bạn hiện tại là \$[\s\S]*?để tiếp tục\.`\s*:\s*`Insufficient balance![\s\S]*?to continue\.`\);/g,
    `alert(getDashNotice('vaultBalanceInsufficientForTask'));`);

  if (wasCRLF) {
    text = text.replace(/\n/g, '\r\n');
  }

  fs.writeFileSync(filePath, text, 'utf8');
  console.log('Cleaned and standardized:', filePath);
}

cleanFile('dashboard.html');
cleanFile('app/dashboard.html');
