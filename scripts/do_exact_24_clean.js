const fs = require('fs');

function replaceExact(filePath) {
  let content = fs.readFileSync(filePath, 'utf8').replace(/\r\n/g, '\n');

  function replaceBetween(startToken, endToken, replacement) {
    const startIdx = content.indexOf(startToken);
    if (startIdx === -1) {
      console.warn('Start token not found:', JSON.stringify(startToken.substring(0, 40)));
      return false;
    }
    const endIdx = content.indexOf(endToken, startIdx);
    if (endIdx === -1) {
      console.warn('End token not found for:', JSON.stringify(startToken.substring(0, 40)));
      return false;
    }
    const fullEnd = endIdx + endToken.length;
    content = content.substring(0, startIdx) + replacement + content.substring(fullEnd);
    return true;
  }

  // 1. Phantom notice
  replaceBetween(
    'walletNoticeText.innerHTML = isVi',
    'Please install Phantom to connect.";',
    "walletNoticeText.innerHTML = getVestingText('phantomNotDetected');"
  );

  // 2. MetaMask notice
  replaceBetween(
    'walletNoticeText.innerHTML = isVi',
    'open this URL inside MetaMask Mobile App.";',
    "walletNoticeText.innerHTML = getVestingText('metaMaskNotDetectedFull');"
  );

  // 3. Solflare notice
  replaceBetween(
    'walletNoticeText.innerHTML = isVi',
    'Please install Solflare to connect.";',
    "walletNoticeText.innerHTML = getVestingText('solflareNotDetected');"
  );

  // 4. Token-2022 Mint copied alert
  replaceBetween(
    'alert(isVi \n          ? `ĐÃ SAO CHÉP ĐỊA CHỈ MINT TOKEN-2022',
    'Transfer-Hook status.`);',
    "alert(getVestingText('copiedToken2022Alert') + '\\n\\n' + TOKEN_2022_MINT);"
  );

  // 5. dashConfirmDepositBtn text 1
  replaceBetween(
    'dashConfirmDepositBtn.textContent = isVi \n            ? "Xác Nhận Nạp On-Chain (Ký Ví Phantom)"',
    '"Confirm On-Chain Deposit (Sign with Phantom)";',
    "dashConfirmDepositBtn.textContent = getDashNotice('confirmOnChainDepositPhantom');"
  );

  // 6. dashConfirmDepositBtn text 2
  replaceBetween(
    'dashConfirmDepositBtn.textContent = isVi \n            ? "Kết Nối Ví Phantom Để Nạp"',
    '"Connect Phantom Wallet to Deposit";',
    "dashConfirmDepositBtn.textContent = getDashNotice('connectPhantomToDeposit');"
  );

  // 7. Faucet toast message
  replaceBetween(
    'message: isVi \n                ? `+${added.toFixed(2)} USDT thử nghiệm',
    '...${userWallet.address.slice(-4)}`',
    "message: getDashNotice('faucetClaimed') + ' (+' + added.toFixed(2) + ' USDT)'"
  );

  // 8. Faucet alert
  replaceBetween(
    'alert(isVi \n            ? `🎉 Nhận USDT Thử Nghiệm Devnet Thành Công!',
    '?cluster=devnet`);',
    "alert(getDashNotice('faucetClaimed') + '\\n\\n+' + added.toFixed(2) + ' USDT (Solana Devnet)');"
  );

  // 9. MetaMask insufficient ETH
  replaceBetween(
    'alert(isVi\n                ? `⚠️ Số Dư Ví MetaMask Không Đủ (0 ETH)!',
    'to test on Solana Devnet.`);',
    "alert(getDashNotice('metaMaskInsufficientEth'));"
  );

  // 10. MetaMask deposit success
  replaceBetween(
    'alert(isVi \n              ? `🎉 Nạp Tiền Web3 MetaMask Thành Công!',
    'Instant Settlement: 380ms.`);',
    "alert(getDashNotice('metaMaskDepositSuccess'));"
  );

  // 11. Web3 connected confirm prompt
  replaceBetween(
    'alert(isVi \n                ? `Đã kết nối ví ${userWallet.provider} thành công!',
    'on Solana Devnet.`);',
    "alert(getDashNotice('web3ConnectedConfirmPrompt'));"
  );

  // 12. No web3 detected faucet guide
  replaceBetween(
    'alert(isVi\n              ? "Chưa phát hiện tiện ích ví Web3 (Phantom hoặc Solflare)',
    'to receive free testnet funds.");',
    "alert(getDashNotice('noWeb3DetectedFaucetGuide'));"
  );

  // 13. Insufficient SOL gasless guide
  replaceBetween(
    'alert(isVi \n              ? `⚠️ Số Dư Ví ${userWallet.provider} Không Đủ (0 SOL)!',
    '0% Gas Fee Subsidy.`);',
    "alert(getDashNotice('insufficientSolGaslessGuide'));"
  );

  // 14. Gasless deposit toast message
  replaceBetween(
    'message: isVi \n                    ? `+${added.toFixed(2)} USDT đã vào Master Vault',
    '0.02 SOL gas subsidized`',
    "message: getDashNotice('gaslessDepositSuccess') + ' (+$' + added.toFixed(2) + ' USDT)'"
  );

  // 15. Gasless deposit alert
  replaceBetween(
    'alert(isVi \n                ? `🎉 Nạp Tiền Web3 Thành Công (Hỗ Trợ 0% Phí Gas)!',
    'enjoy 0% Gas Fees on Solana Devnet!`);',
    "alert(getDashNotice('web3DepositConfirmedDevnet'));"
  );

  // 16. Web3 deposit confirmed devnet alert
  replaceBetween(
    'alert(isVi \n            ? `🎉 Nạp Tiền Web3 Thành Công!',
    '?cluster=devnet`);',
    "alert(getDashNotice('web3DepositConfirmedDevnet'));"
  );

  // 17. Fiat sandbox notice
  replaceBetween(
    'alert(isVi\n        ? `Thông Báo Cổng Thanh Toán Fiat (${methodName}):',
    'test for free on Solana Devnet!`);',
    "alert(getDashNotice('fiatSandboxNotice'));"
  );

  // 18. Zero balance cannot withdraw
  replaceBetween(
    'alert(isVi\n          ? "Số dư trong Master Vault của bạn hiện tại là $0.0000 USDT.',
    'Cannot withdraw.");',
    "alert(getDashNotice('zeroBalanceCannotWithdraw'));"
  );

  // 19. Insufficient withdraw balance
  replaceBetween(
    'alert(isVi \n          ? `Số dư không đủ!',
    'withdraw $${amount.toFixed(4)} USDT.`);',
    "alert(getDashNotice('insufficientWithdrawBalance'));"
  );

  // 20. Invalid Solana destination address
  replaceBetween(
    'alert(isVi\n          ? "Địa chỉ ví đích không hợp lệ!',
    'e.g., HD1b...5nVW).");',
    "alert(getDashNotice('invalidSolanaAddress'));"
  );

  // 21. Withdraw success notice
  replaceBetween(
    'alert(isVi\n        ? `Rút tiền thành công!',
    'Instant Sub-Second Retraction).`);',
    "alert(getDashNotice('withdrawSuccessNotice'));"
  );

  // 22. AI Security Kernel Header
  replaceBetween(
    'generatedResponse = isVi\n              ? `[HAICHAIN Security Kernel: Phân Tích An Toàn AI Độc Quyền]',
    ': `[HAICHAIN Security Kernel: Frontier Agent Protection]',
    "generatedResponse = `[HAICHAIN Security Kernel: Frontier Agent Protection]"
  );

  // 23. AI Anchor Smart Contract Header
  replaceBetween(
    'generatedResponse = isVi\n              ? `[Mã Lệnh Solana Anchor Xác Thực Hợp Đồng Vi Thanh Toán]',
    ': `[Solana Anchor Smart Contract: Escrow Settlement Code]',
    "generatedResponse = `[Solana Anchor Smart Contract: Escrow Settlement Code]"
  );

  // 24. AI Enterprise Analysis Header
  replaceBetween(
    'generatedResponse = isVi\n              ? `[Phân Tích Tự Hành Cấp Độ Doanh Nghiệp qua ${selectedModel}]',
    ': `[Autonomous Enterprise Inference via ${selectedModel}]',
    "generatedResponse = `[Autonomous Enterprise Inference via ${selectedModel}]"
  );

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Processed:', filePath);
}

replaceExact('dashboard.html');
replaceExact('app/dashboard.html');
