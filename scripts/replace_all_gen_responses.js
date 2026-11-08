const fs = require('fs');

function replaceAllGeneratedResponse(filePath) {
  let content = fs.readFileSync(filePath, 'utf8').replace(/\r\n/g, '\n');

  // Loop Anchor code
  while (true) {
    const p11 = content.indexOf('generatedResponse = isVi\n              ? `[Mã Lệnh Solana Anchor Xác Thực Hợp Đồng Vi Thanh Toán]');
    if (p11 === -1) break;
    const colon11 = content.indexOf(':\n              `[Solana Anchor', p11);
    const semi11 = content.indexOf(';\n          }', colon11);
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
    content = content.substring(0, p11) + replacement11 + content.substring(semi11 + 1);
  }

  // Loop Enterprise analysis
  while (true) {
    const p12 = content.indexOf('generatedResponse = isVi\n              ? `[Phân Tích Tự Hành Cấp Độ Doanh Nghiệp qua ${selectedModel}]');
    if (p12 === -1) break;
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
  console.log('Finished replaceAllGeneratedResponse in', filePath);
}

replaceAllGeneratedResponse('dashboard.html');
replaceAllGeneratedResponse('app/dashboard.html');
