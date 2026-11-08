import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

alert_replacements = [
    "alert(getDashNotice('faucetClaimed') + '\\n\\n+' + added.toFixed(2) + ' USDT (Solana Devnet)');",
    "alert(getDashNotice('metaMaskInsufficientEth'));",
    "alert(getDashNotice('metaMaskDepositSuccess'));",
    "alert(getDashNotice('noWeb3DetectedFaucetGuide'));",
    "alert(getDashNotice('insufficientSolGaslessGuide'));",
    "alert(getDashNotice('web3DepositConfirmedDevnet'));",
    "alert(getDashNotice('web3DepositConfirmedDevnet'));",
    "alert(getDashNotice('fiatSandboxNotice'));",
    "alert(getDashNotice('invalidSolanaAddress'));",
    "alert(getDashNotice('withdrawSuccessNotice'));",
]

gen_replacement_1 = """generatedResponse = `[Solana Anchor Smart Contract: Escrow Settlement Code]\\n\\n` +
                `#[derive(Accounts)]\\n` +
                `pub struct SettleEscrow<'info> {\\n` +
                `    #[account(mut, seeds = [b"vault", authority.key().as_ref()], bump)]\\n` +
                `    pub master_vault: Account<'info, MasterVault>,\\n` +
                `    #[account(mut)]\\n` +
                `    pub agent_ticket: Account<'info, CapabilityTicket>,\\n` +
                `    pub token_program: Program<'info, Token>,\\n` +
                `    pub system_program: Program<'info, System>,\\n` +
                `}\\n\\n` +
                `// Zero-griefing single instruction escrow release\\n` +
                `pub fn settle_micro_escrow(ctx: Context<SettleEscrow>, amount_micro_usdt: u64) -> Result<()> {\\n` +
                `    // 1. Verify ephemeral signature against Merkle root\\n` +
                `    // 2. Transfer-Hook settlement via Token-2022\\n` +
                `    // 3. Burn ticket nullifier\\n` +
                `    Ok(())\\n` +
                `};`;"""

gen_replacement_2 = """generatedResponse = `[Autonomous Enterprise Inference via ${selectedModel}]\\n\\n` +
                `Prompt Query: "${cleanPrompt.length > 80 ? cleanPrompt.slice(0, 80) + '...' : cleanPrompt}"\\n\\n` +
                `1. Context Analysis: Verification passed zero-knowledge constraints & capability ticket quota.\\n` +
                `2. Execution Result: Successfully calculated and executed on Solana Devnet (Program: DK4Q...w4xk). Micro-escrow settled for ${selectedCost.toFixed(4)} USDT.\\n` +
                `3. Security Invariant: Master Vault private keys remained unexposed; ephemeral ticket consumed and nullified.`;"""

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace 10 alerts in reverse order of appearance
    alert_matches = list(re.finditer(r'alert\(isVi\s*\?[\s\S]*?\);', text))
    if len(alert_matches) == 10:
        for m, repl in zip(reversed(alert_matches), reversed(alert_replacements)):
            text = text[:m.start()] + repl + text[m.end():]
        print(f'{filepath}: Replaced all 10 alerts successfully!')
    else:
        print(f'{filepath}: Expected 10 alerts, found {len(alert_matches)}')

    # Replace 2 generatedResponse
    gen_matches = list(re.finditer(r'generatedResponse\s*=\s*isVi\s*\?[\s\S]*?;', text))
    if len(gen_matches) == 2:
        m2 = gen_matches[1]
        text = text[:m2.start()] + gen_replacement_2 + text[m2.end():]
        # Re-find first one
        m1 = list(re.finditer(r'generatedResponse\s*=\s*isVi\s*\?[\s\S]*?;', text))[0]
        text = text[:m1.start()] + gen_replacement_1 + text[m1.end():]
        print(f'{filepath}: Replaced both generatedResponse successfully!')
    else:
        print(f'{filepath}: Expected 2 gen matches, found {len(gen_matches)}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

patch_file('dashboard.html')
patch_file('app/dashboard.html')
