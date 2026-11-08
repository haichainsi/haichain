const fs = require('fs');

function replaceInFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // 1. Vesting overview banner line
  content = content.replace(/\$\{isVi\s*\?\s*`Ví <strong class="text-black dark:text-white">\$\{shortAddr\}<\/strong> đang sở hữu[\s\S]*?:[\s\S]*?Transfer-Hook locked until TGE\.`\}/s,
    `\${shortAddr}: \${haiTotal.toLocaleString()} \\$HAISI (Token-2022 Transfer-Hook Locked)`);

  // 2. dashConfirmDepositBtn.textContent
  content = content.replace(/dashConfirmDepositBtn\.textContent = isVi\s*\?\s*"Kết Nối Ví Phantom Để Nạp"\s*:\s*"Connect Phantom Wallet to Deposit"/s,
    `dashConfirmDepositBtn.textContent = getDashNotice('connectPhantomToDeposit')`);

  // 3. Faucet toast message
  content = content.replace(/message: isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT thử nghiệm đã nạp vào ví[\s\S]*?:[\s\S]*?testnet funds credited to[\s\S]*?`,/s,
    `message: \`+\${added.toFixed(2)} USDT \${getDashNotice('faucetCredited')}\`,`);

  // 4. Faucet alert
  content = content.replace(/alert\(isVi\s*\?\s*`🎉 Nhận USDT Thử Nghiệm Devnet Thành Công![\s\S]*?:[\s\S]*?Devnet Testnet USDT Claimed![\s\S]*?`\);/s,
    `alert(getDashNotice('faucetCredited'));`);

  // 5. MetaMask 0 ETH alert
  content = content.replace(/alert\(isVi\s*\?\s*`⚠️ Số Dư Ví MetaMask Không Đủ \(0 ETH\)![\s\S]*?:[\s\S]*?MetaMask Balance Insufficient \(0 ETH\)![\s\S]*?`\);/s,
    `alert(getDashNotice('metaMaskInsufficientEth'));`);

  // 6. MetaMask success alert
  content = content.replace(/alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 MetaMask Thành Công![\s\S]*?:[\s\S]*?Web3 MetaMask Deposit Confirmed![\s\S]*?`\);/s,
    `alert(getDashNotice('metaMaskDepositSuccess'));`);

  // 7. Web3 connected prompt
  content = content.replace(/alert\(isVi\s*\?\s*`Đã kết nối ví \$\{userWallet\.provider\} thành công![\s\S]*?:[\s\S]*?Connected \$\{userWallet\.provider\} wallet successfully![\s\S]*?`\);/s,
    `alert(getDashNotice('web3ConnectedConfirmPrompt'));`);

  // 8. No Web3 wallet detected
  content = content.replace(/alert\(isVi\s*\?\s*"Chưa phát hiện tiện ích ví Web3 \(Phantom hoặc Solflare\)[\s\S]*?:[\s\S]*?Web3 wallet \(Phantom or Solflare\) not detected[\s\S]*?"\);/s,
    `alert(getDashNotice('noWeb3DetectedFaucetGuide'));`);

  // 9. 0 SOL alert
  content = content.replace(/alert\(isVi\s*\?\s*`⚠️ Số Dư Ví \$\{userWallet\.provider\} Không Đủ \(0 SOL\)![\s\S]*?:[\s\S]*?Insufficient SOL in \$\{userWallet\.provider\} \(0 SOL\)![\s\S]*?`\);/s,
    `alert(getDashNotice('insufficientSolGaslessGuide'));`);

  // 10. Gasless subsidized message
  content = content.replace(/message: isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT đã vào Master Vault & Trợ cấp 0\.02 SOL vào ví`\s*:\s*`\+\$\{added\.toFixed\(2\)\} USDT credited & 0\.02 SOL gas subsidized`,/s,
    `message: \`+\${added.toFixed(2)} USDT (\${getDashNotice('gaslessDepositSuccess')})\`,`);

  // 11. Normal web3 deposit alert
  content = content.replace(/alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 Thành Công!\s*\\n\\nGiao dịch đã được xác nhận bất biến trên mạng Solana Devnet\.[\s\S]*?:[\s\S]*?Web3 Deposit Confirmed![\s\S]*?`\);/s,
    `alert(getDashNotice('web3DepositConfirmedDevnet'));`);

  // 12. Fiat sandbox notice
  content = content.replace(/alert\(isVi\s*\?\s*`Thông Báo Cổng Thanh Toán Fiat \(\$\{methodName\}\):[\s\S]*?:[\s\S]*?Fiat Gateway Notice \(\$\{methodName\}\):[\s\S]*?`\);/s,
    `alert(getDashNotice('fiatSandboxNotice'));`);

  // 13. Zero balance cannot withdraw
  content = content.replace(/alert\(isVi\s*\?\s*"Số dư trong Master Vault của bạn hiện tại là \$0\.0000 USDT[\s\S]*?:[\s\S]*?Your Master Vault balance is \$0\.0000 USDT[\s\S]*?"\);/s,
    `alert(getDashNotice('zeroBalanceCannotWithdraw'));`);

  // 14. Insufficient withdrawal balance
  content = content.replace(/alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault hiện tại của bạn là \$[\s\S]*?:[\s\S]*?Insufficient balance![\s\S]*?`\);/s,
    `alert(getDashNotice('insufficientWithdrawBalance'));`);

  // 15. Invalid Solana address
  content = content.replace(/alert\(isVi\s*\?\s*"Địa chỉ ví đích không hợp lệ![\s\S]*?:[\s\S]*?Invalid destination address![\s\S]*?"\);/s,
    `alert(getDashNotice('invalidSolanaAddress'));`);

  // 16. Task balance insufficient toast
  content = content.replace(/message: isVi\s*\?\s*`Số dư Master Vault \(\$[\s\S]*?:[\s\S]*?Please claim devnet faucet\.`,/s,
    `message: getDashNotice('vaultBalanceInsufficientForTask'),`);

  // 17. Task balance insufficient alert
  content = content.replace(/alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault của bạn hiện tại là \$[\s\S]*?:[\s\S]*?to continue\.`\);/s,
    `alert(getDashNotice('vaultBalanceInsufficientForTask'));`);

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Replaced with /s flag in:', filePath);
}

replaceInFile('dashboard.html');
replaceInFile('app/dashboard.html');
