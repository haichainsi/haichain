const fs = require('fs');

function replaceFinal12(filePath) {
  let content = fs.readFileSync(filePath, 'utf8').replace(/\r\n/g, '\n');

  // Match 1: Faucet Devnet Alert
  const p1 = content.indexOf('alert(isVi \n            ? `🎉 Nhận USDT Thử Nghiệm Devnet Thành Công!');
  if (p1 !== -1) {
    const end1 = content.indexOf(');', p1) + 2;
    content = content.substring(0, p1) + "alert(getDashNotice('faucetClaimed') + '\\n\\n+' + added.toFixed(2) + ' USDT (Solana Devnet)');" + content.substring(end1);
  }

  // Match 2: MetaMask insufficient ETH
  const p2 = content.indexOf('alert(isVi\n                ? `⚠️ Số Dư Ví MetaMask Không Đủ (0 ETH)!');
  if (p2 !== -1) {
    const end2 = content.indexOf(');', p2) + 2;
    content = content.substring(0, p2) + "alert(getDashNotice('metaMaskInsufficientEth'));" + content.substring(end2);
  }

  // Match 3: MetaMask deposit success
  const p3 = content.indexOf('alert(isVi \n              ? `🎉 Nạp Tiền Web3 MetaMask Thành Công!');
  if (p3 !== -1) {
    const end3 = content.indexOf(');', p3) + 2;
    content = content.substring(0, p3) + "alert(getDashNotice('metaMaskDepositSuccess'));" + content.substring(end3);
  }

  // Match 4: No web3 detected faucet guide
  const p4 = content.indexOf('alert(isVi\n              ? "Chưa phát hiện tiện ích ví Web3 (Phantom hoặc Solflare)');
  if (p4 !== -1) {
    const end4 = content.indexOf(');', p4) + 2;
    content = content.substring(0, p4) + "alert(getDashNotice('noWeb3DetectedFaucetGuide'));" + content.substring(end4);
  }

  // Match 5: Insufficient SOL gasless guide
  const p5 = content.indexOf('alert(isVi \n              ? `⚠️ Số Dư Ví ${userWallet.provider} Không Đủ (0 SOL)!');
  if (p5 !== -1) {
    const end5 = content.indexOf(');', p5) + 2;
    content = content.substring(0, p5) + "alert(getDashNotice('insufficientSolGaslessGuide'));" + content.substring(end5);
  }

  // Match 6: Gasless deposit success
  const p6 = content.indexOf('alert(isVi \n                ? `🎉 Nạp Tiền Web3 Thành Công (Hỗ Trợ 0% Phí Gas)!');
  if (p6 !== -1) {
    const end6 = content.indexOf(');', p6) + 2;
    content = content.substring(0, p6) + "alert(getDashNotice('web3DepositConfirmedDevnet'));" + content.substring(end6);
  }

  // Match 7: Web3 deposit confirmed devnet
  const p7 = content.indexOf('alert(isVi \n            ? `🎉 Nạp Tiền Web3 Thành Công!');
  if (p7 !== -1) {
    const end7 = content.indexOf(');', p7) + 2;
    content = content.substring(0, p7) + "alert(getDashNotice('web3DepositConfirmedDevnet'));" + content.substring(end7);
  }

  // Match 8: Fiat sandbox notice
  const p8 = content.indexOf('alert(isVi\n        ? `Thông Báo Cổng Thanh Toán Fiat (${methodName}):');
  if (p8 !== -1) {
    const end8 = content.indexOf(');', p8) + 2;
    content = content.substring(0, p8) + "alert(getDashNotice('fiatSandboxNotice'));" + content.substring(end8);
  }

  // Match 9: Invalid destination address
  const p9 = content.indexOf('alert(isVi\n          ? "Địa chỉ ví đích không hợp lệ!');
  if (p9 !== -1) {
    const end9 = content.indexOf(');', p9) + 2;
    content = content.substring(0, p9) + "alert(getDashNotice('invalidSolanaAddress'));" + content.substring(end9);
  }

  // Match 10: Withdraw success
  const p10 = content.indexOf('alert(isVi\n        ? `Rút tiền thành công!');
  if (p10 !== -1) {
    const end10 = content.indexOf(');', p10) + 2;
    content = content.substring(0, p10) + "alert(getDashNotice('withdrawSuccessNotice'));" + content.substring(end10);
  }

  // Match 11: Solana Anchor Mock Code
  const p11 = content.indexOf('generatedResponse = isVi\n              ? `[Mã Lệnh Solana Anchor Xác Thực Hợp Đồng Vi Thanh Toán]');
  if (p11 !== -1) {
    const colon11 = content.indexOf(':\n              `[Solana Anchor', p11);
    const end11 = content.indexOf('; // End of response', p11) !== -1 ? content.indexOf('; // End of response', p11) : content.indexOf('Ok(())\\n`', colon11) + 9;
    const replacement11 = `generatedResponse = \`[Solana Anchor Smart Contract: Escrow Settlement Code]\\n\\n\` +
                \`#[derive(Accounts)]\\n\` +
                \`pub struct SettleEscrow<'info> {\\n\` +
                \`    #[account(mut, seeds = [b"vault", authority.key().as_ref()], bump)]\\n\` +
                \`    pub master_vault: Account<'info, MasterVault>,\\n\` +
                \`    #[account(mut)]\\n\` +
                \`    pub agent_ticket: Account<'info, CapabilityTicket>,\\n\` +
                \`    pub token_program: Program<'info, Token>,\\n\` +
                \`    pub system_program: Program<'info, System>,\\n\` +
                \`}\\n\\n\` +
                \`// Zero-griefing single instruction escrow release\\n\` +
                \`pub fn settle_micro_escrow(ctx: Context<SettleEscrow>, amount_micro_usdt: u64) -> Result<()> {\\n\` +
                \`    // 1. Verify ephemeral signature against Merkle root\\n\` +
                \`    // 2. Transfer-Hook settlement via Token-2022\\n\` +
                \`    // 3. Burn ticket nullifier\\n\` +
                \`    Ok(())\\n\` +
                \`};\`;`;
    // Find until semicolon of the ternary assignment
    const semi11 = content.indexOf(';\n          }', colon11);
    content = content.substring(0, p11) + replacement11 + content.substring(semi11 + 1);
  }

  // Match 12: Enterprise analysis
  const p12 = content.indexOf('generatedResponse = isVi\n              ? `[Phân Tích Tự Hành Cấp Độ Doanh Nghiệp qua ${selectedModel}]');
  if (p12 !== -1) {
    const colon12 = content.indexOf(':\n              `[Autonomous Enterprise', p12);
    const replacement12 = `generatedResponse = \`[Autonomous Enterprise Inference via \${selectedModel}]\\n\\n\` +
                \`Prompt Query: "\${cleanPrompt.length > 80 ? cleanPrompt.slice(0, 80) + '...' : cleanPrompt}"\\n\\n\` +
                \`1. Context Analysis: Verification passed zero-knowledge constraints & capability ticket quota.\\n\` +
                \`2. Execution Result: Successfully calculated and executed on Solana Devnet (Program: DK4Q...w4xk). Micro-escrow settled for \${selectedCost.toFixed(4)} USDT.\\n\` +
                \`3. Security Invariant: Master Vault private keys remained unexposed; ephemeral ticket consumed and nullified.\`;`;
    const semi12 = content.indexOf(';\n          }', colon12);
    content = content.substring(0, p12) + replacement12 + content.substring(semi12 + 1);
  }

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Processed:', filePath);
}

replaceFinal12('dashboard.html');
replaceFinal12('app/dashboard.html');
