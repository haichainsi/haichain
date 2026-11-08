const fs = require('fs');

function patchDashboard(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // 1. Add data-i18n to playground quick demos & demo items
  content = content.replace(
    '<span>Quick Demos:</span>',
    '<span data-i18n="playground.quickDemos">Quick Demos:</span>'
  );
  content = content.replace(
    '<span class="truncate">Anti-Drain</span>',
    '<span class="truncate" data-i18n="playground.demoAntiDrain">Anti-Drain</span>'
  );
  content = content.replace(
    '<span class="truncate">Micro-Escrow</span>',
    '<span class="truncate" data-i18n="playground.demoMicroEscrow">Micro-Escrow</span>'
  );
  content = content.replace(
    '<span class="truncate">Optimus AI</span>',
    '<span class="truncate" data-i18n="playground.demoOptimus">Optimus AI</span>'
  );
  content = content.replace(
    '<span class="truncate">Anchor CPI</span>',
    '<span class="truncate" data-i18n="playground.demoAnchor">Anchor CPI</span>'
  );

  // 2. Replace wallet notice texts (Matches 1, 2, 3)
  content = content.replace(
    /walletNoticeText\.innerHTML\s*=\s*isVi[\s\S]*?Phantom extension not detected<\/strong>[^"]*";/,
    `walletNoticeText.innerHTML = getVestingText('phantomNotDetected');`
  );
  content = content.replace(
    /walletNoticeText\.innerHTML\s*=\s*isVi[\s\S]*?MetaMask extension not detected<\/strong>[^"]*";/,
    `walletNoticeText.innerHTML = getVestingText('metaMaskNotDetectedFull');`
  );
  content = content.replace(
    /walletNoticeText\.innerHTML\s*=\s*isVi[\s\S]*?Solflare extension not detected<\/strong>[^"]*";/,
    `walletNoticeText.innerHTML = getVestingText('solflareNotDetected');`
  );

  // 3. Match 4: Token 2022 mint copy alert
  content = content.replace(
    /alert\(isVi[\s\S]*?ĐÃ SAO CHÉP ĐỊA CHỈ MINT TOKEN-2022[\s\S]*?3\. Done! Enjoy your \$HAISI allocation.`\);/,
    `alert(getVestingText('copiedToken2022Alert') + '\\n\\n' + TOKEN_2022_MINT);`
  );

  // 4. Match 5 & 6: dashConfirmDepositBtn.textContent
  content = content.replace(
    /dashConfirmDepositBtn\.textContent\s*=\s*isVi[\s\S]*?Confirm On-Chain Deposit \(Sign with Phantom\)";/,
    `dashConfirmDepositBtn.textContent = getDashNotice('confirmOnChainDepositPhantom');`
  );
  content = content.replace(
    /dashConfirmDepositBtn\.textContent\s*=\s*isVi[\s\S]*?Connect Phantom Wallet to Deposit";/,
    `dashConfirmDepositBtn.textContent = getDashNotice('connectPhantomToDeposit');`
  );

  // 5. Match 7: Faucet toast message
  content = content.replace(
    /message:\s*isVi[\s\S]*?\+\$\{added\.toFixed\(2\)\} Devnet test USDT added to \$\{userWallet\.address\.slice\(0, 4\)\}\.\.\.\$\{userWallet\.address\.slice\(-4\)\}`/,
    `message: getDashNotice('faucetClaimed') + ' (+' + added.toFixed(2) + ' USDT)'`
  );

  // 6. Match 8: Faucet alert
  content = content.replace(
    /alert\(isVi[\s\S]*?🎉 Nhận USDT Thử Nghiệm Devnet Thành Công![\s\S]*?devnet`\);/,
    `alert(getDashNotice('faucetClaimed') + '\\n\\n+' + added.toFixed(2) + ' USDT (Solana Devnet)');`
  );

  // 7. Match 9: MetaMask insufficient ETH
  content = content.replace(
    /alert\(isVi[\s\S]*?⚠️ Số Dư Ví MetaMask Không Đủ \(0 ETH\)![\s\S]*?to test on Solana Devnet.`\);/,
    `alert(getDashNotice('metaMaskInsufficientEth'));`
  );

  // 8. Match 10: MetaMask deposit success
  content = content.replace(
    /alert\(isVi[\s\S]*?🎉 Nạp Tiền Web3 MetaMask Thành Công![\s\S]*?Instant Settlement: 380ms`\);/,
    `alert(getDashNotice('metaMaskDepositSuccess'));`
  );

  // 9. Match 11: Web3 connected confirm prompt
  content = content.replace(
    /alert\(isVi[\s\S]*?Đã kết nối ví \$\{userWallet\.provider\} thành công![\s\S]*?on Solana Devnet.`\);/,
    `alert(getDashNotice('web3ConnectedConfirmPrompt'));`
  );

  // 10. Match 12: No web3 detected faucet guide
  content = content.replace(
    /alert\(isVi[\s\S]*?Chưa phát hiện tiện ích ví Web3 \(Phantom hoặc Solflare\)[\s\S]*?Faucet \(+\$10\)' tab to receive free testnet funds.`\);/,
    `alert(getDashNotice('noWeb3DetectedFaucetGuide'));`
  );

  // 11. Match 13: Insufficient SOL gasless guide
  content = content.replace(
    /alert\(isVi[\s\S]*?⚠️ Số Dư Ví \$\{userWallet\.provider\} Không Đủ \(0 SOL\)![\s\S]*?0% Gas Fee Subsidy.`\);/,
    `alert(getDashNotice('insufficientSolGaslessGuide'));`
  );

  // 12. Match 14: Gasless deposit toast message
  content = content.replace(
    /message:\s*isVi[\s\S]*?\+\$\{added\.toFixed\(2\)\} USDT đã vào Master Vault[\s\S]*?\+\$\$\{added\.toFixed\(2\)\} USDT credited & 0\.02 SOL gas subsidized`/,
    `message: getDashNotice('gaslessDepositSuccess') + ' (+$' + added.toFixed(2) + ' USDT)'`
  );

  // 13. Match 15: Gasless deposit alert
  content = content.replace(
    /alert\(isVi[\s\S]*?🎉 Nạp Tiền Web3 Thành Công \(Hỗ Trợ 0% Phí Gas\)![\s\S]*?enjoy 0% Gas Fees on Solana Devnet!`\);/,
    `alert(getDashNotice('web3DepositConfirmedDevnet'));`
  );

  // 14. Match 16: Web3 deposit confirmed devnet alert
  content = content.replace(
    /alert\(isVi[\s\S]*?🎉 Nạp Tiền Web3 Thành Công![\s\S]*?finalized irreversibly on Solana Devnet.`\);/,
    `alert(getDashNotice('web3DepositConfirmedDevnet'));`
  );

  // 15. Match 17: Fiat sandbox notice
  content = content.replace(
    /alert\(isVi[\s\S]*?Thông Báo Cổng Thanh Toán Fiat[\s\S]*?test for free on Solana Devnet!`\);/,
    `alert(getDashNotice('fiatSandboxNotice'));`
  );

  // 16. Match 18: Zero balance cannot withdraw
  content = content.replace(
    /alert\(isVi[\s\S]*?Số dư trong Master Vault của bạn hiện tại là \$0\.0000 USDT[\s\S]*?cannot request a withdrawal.`\);/,
    `alert(getDashNotice('zeroBalanceCannotWithdraw'));`
  );

  // 17. Match 19: Insufficient withdraw balance
  content = content.replace(
    /alert\(isVi[\s\S]*?Số dư không đủ!\\n\\nSố dư Master Vault hiện tại của bạn là[\s\S]*?withdraw \$\$\{amount\.toFixed\(4\)\} USDT.`\);/,
    `alert(getDashNotice('insufficientWithdrawBalance'));`
  );

  // 18. Match 20: Invalid Solana destination address
  content = content.replace(
    /alert\(isVi[\s\S]*?Địa chỉ ví đích không hợp lệ![\s\S]*?e\.g\., HD1b\.\.\.5nVW\).`\);/,
    `alert(getDashNotice('invalidSolanaAddress'));`
  );

  // 19. Match 21: Withdraw success notice
  content = content.replace(
    /alert\(isVi[\s\S]*?Rút tiền thành công!\\n\\nĐã giải ngân[\s\S]*?Instant Sub-Second Retraction\).`\);/,
    `alert(getDashNotice('withdrawSuccessNotice'));`
  );

  // 20. Match 22, 23, 24: Generated AI responses
  content = content.replace(
    /generatedResponse\s*=\s*isVi[\s\S]*?\[HAICHAIN Security Kernel: Phân Tích An Toàn AI Độc Quyền\][\s\S]*?`\s*:\s*`\[HAICHAIN Security Kernel/g,
    `generatedResponse = \`\${getDashNotice('aiSecurityKernelHeader')}\\n\\n\` + \`[HAICHAIN Security Kernel`
  );

  content = content.replace(
    /generatedResponse\s*=\s*isVi[\s\S]*?\[Mã Lệnh Solana Anchor Xác Thực Hợp Đồng Vi Thanh Toán\][\s\S]*?`\s*:\s*`\[Solana Anchor Smart Contract/g,
    `generatedResponse = \`\${getDashNotice('aiAnchorCodeHeader')}\\n\\n\` + \`[Solana Anchor Smart Contract`
  );

  content = content.replace(
    /generatedResponse\s*=\s*isVi[\s\S]*?\[Phân Tích Tự Hành Cấp Độ Doanh Nghiệp qua \$\{selectedModel\}\][\s\S]*?`\s*:\s*`\[Autonomous Enterprise Inference/g,
    `generatedResponse = \`\${getDashNotice('aiEnterpriseAnalysisHeader')}\\n\\n\` + \`[Autonomous Enterprise Inference`
  );

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Successfully patched:', filePath);
}

patchDashboard('dashboard.html');
patchDashboard('app/dashboard.html');
