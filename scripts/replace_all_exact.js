const fs = require('fs');

function cleanFile(filePath) {
  let code = fs.readFileSync(filePath, 'utf8');

  // We find all `alert(isVi` and replace with `alert(getDashNotice(...))`
  // Let's do replacements by targeting the unique text inside each of the 16 spots:

  // 1. Vesting overview banner
  code = code.replace(/\$\{isVi\s*\?[\s\S]*?Transfer-Hook locked until TGE\.[^`]*`\}/,
    `\${shortAddr}: \${haiTotal.toLocaleString()} \\$HAISI (Token-2022 Transfer-Hook Locked)`);

  // 2. Faucet toast message
  code = code.replace(/message:\s*isVi\s*\?[\s\S]*?Devnet test USDT credited to[\s\S]*?`,/,
    `message: \`+\${added.toFixed(2)} USDT (\${getDashNotice('faucetCredited')})\`,`);

  // 3. Faucet alert
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Devnet Testnet Faucet Confirmed![\s\S]*?\);/,
    `alert(getDashNotice('faucetCredited'));`);

  // 4. MetaMask 0 ETH alert
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?MetaMask Balance Insufficient \(0 ETH\)![\s\S]*?\);/,
    `alert(getDashNotice('metaMaskInsufficientEth'));`);

  // 5. MetaMask success alert
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Web3 MetaMask Deposit Confirmed![\s\S]*?\);/,
    `alert(getDashNotice('metaMaskDepositSuccess'));`);

  // 6. Web3 connected prompt
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Connected \$\{userWallet\.provider\} wallet successfully![\s\S]*?\);/,
    `alert(getDashNotice('web3ConnectedConfirmPrompt'));`);

  // 7. No Web3 wallet detected
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Web3 wallet \(Phantom or Solflare\) not detected[\s\S]*?\);/,
    `alert(getDashNotice('noWeb3DetectedFaucetGuide'));`);

  // 8. 0 SOL alert
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Insufficient SOL in \$\{userWallet\.provider\} \(0 SOL\)![\s\S]*?\);/,
    `alert(getDashNotice('insufficientSolGaslessGuide'));`);

  // 9. Gasless subsidized message
  code = code.replace(/message:\s*isVi\s*\?[\s\S]*?0\.02 SOL gas subsidized`,/,
    `message: \`+\${added.toFixed(2)} USDT (\${getDashNotice('gaslessDepositSuccess')})\`,`);

  // 10. Normal web3 deposit alert
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Web3 Deposit Confirmed![\s\S]*?\);/,
    `alert(getDashNotice('web3DepositConfirmedDevnet'));`);

  // 11. Fiat sandbox notice
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Fiat Gateway Notice \(\$\{methodName\}\):[\s\S]*?\);/,
    `alert(getDashNotice('fiatSandboxNotice'));`);

  // 12. Zero balance cannot withdraw
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Your Master Vault balance is currently \$0\.0000 USDT[\s\S]*?\);/,
    `alert(getDashNotice('zeroBalanceCannotWithdraw'));`);

  // 13. Insufficient withdrawal balance
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Insufficient Balance![\s\S]*?\);/,
    `alert(getDashNotice('insufficientWithdrawBalance'));`);

  // 14. Invalid Solana address
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Invalid Destination Address![\s\S]*?\);/,
    `alert(getDashNotice('invalidSolanaAddress'));`);

  // 15. Task balance insufficient toast
  code = code.replace(/message:\s*isVi\s*\?[\s\S]*?Please claim devnet faucet\.`,/,
    `message: getDashNotice('vaultBalanceInsufficientForTask'),`);

  // 16. Task balance insufficient alert
  code = code.replace(/alert\(\s*isVi\s*\?[\s\S]*?Insufficient Balance![\s\S]*?Please claim devnet faucet to proceed\.`\);/,
    `alert(getDashNotice('vaultBalanceInsufficientForTask'));`);

  fs.writeFileSync(filePath, code, 'utf8');
  console.log('Cleaned file:', filePath);
}

cleanFile('dashboard.html');
cleanFile('app/dashboard.html');
