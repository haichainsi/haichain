with open("programs/haichain-core/src/lib.rs", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add new instructions
idx = content.find("msg!(\"HAICHAIN: Master owner updated composite root. Active grace window set for previous root.\");")
assert idx != -1, "update root not found"
end_fn_idx = content.find("    }\n}", idx)
if end_fn_idx == -1:
    end_fn_idx = content.find("    }\r\n}", idx)
assert end_fn_idx != -1, "end_fn_idx not found"

new_instructions = """    }

    /// 8. REGISTER PROVIDER SLA BOND (STAKED REPUTATION & ANTI-GARBAGE GUARANTEE)
    pub fn register_provider_bond(
        ctx: Context<RegisterProviderBondContext>,
        stake_amount: u64,
        min_sla_quality_score: u8,
    ) -> Result<()> {
        require!(stake_amount >= MIN_PROVIDER_BOND_AMOUNT, HaiChainMasterError::InsufficientBondStake);

        let bond = &mut ctx.accounts.provider_bond;
        bond.provider_authority = ctx.accounts.provider_authority.key();
        bond.dedicated_ata = ctx.accounts.provider_dedicated_ata.key();
        bond.token_mint = ctx.accounts.token_mint.key();
        bond.staked_amount = stake_amount;
        bond.slashed_amount = 0;
        bond.total_executions = 0;
        bond.fault_reports = 0;
        bond.min_sla_quality_score = min_sla_quality_score;
        bond.is_active = true;
        bond.bump = ctx.bumps.provider_bond;

        let cpi_accounts = Transfer {
            from: ctx.accounts.provider_source_ata.to_account_info(),
            to: ctx.accounts.provider_dedicated_ata.to_account_info(),
            authority: ctx.accounts.provider_authority.to_account_info(),
        };
        token::transfer(
            CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts),
            stake_amount,
        )?;

        msg!("HAICHAIN v7.0: Provider SLA bond registered for authority: {} with stake {} USDT micro-units",
             bond.provider_authority, stake_amount);
        Ok(())
    }

    /// 9. REPORT FAULT AND SLASH PROVIDER BOND (AUTOMATED ON-CHAIN SLA ENFORCEMENT)
    pub fn report_and_slash_faulty_provider(
        ctx: Context<ReportAndSlashProviderContext>,
        fault_proof_hash: [u8; 32],
        slash_amount: u64,
    ) -> Result<()> {
        let bond = &mut ctx.accounts.provider_bond;
        require!(bond.is_active, HaiChainMasterError::ProviderBondInactive);
        require!(slash_amount > 0 && slash_amount <= MAX_SLASH_PER_INCIDENT, HaiChainMasterError::ExceedsMaxMicroTick);
        require!(bond.staked_amount >= slash_amount, HaiChainMasterError::ExceedsAvailableBond);

        bond.staked_amount = bond.staked_amount.checked_sub(slash_amount)
            .ok_or(HaiChainMasterError::MathUnderflow)?;
        bond.slashed_amount = bond.slashed_amount.checked_add(slash_amount)
            .ok_or(HaiChainMasterError::MathOverflow)?;
        bond.fault_reports = bond.fault_reports.checked_add(1)
            .ok_or(HaiChainMasterError::MathOverflow)?;

        if bond.staked_amount < MIN_PROVIDER_BOND_AMOUNT {
            bond.is_active = false;
            msg!("HAICHAIN v7.0: Provider bond depleted below threshold. Provider deactivated.");
        }

        let provider_authority_bytes = bond.provider_authority.to_bytes();
        let seeds: &[&[&[u8]]] = &[&[
            b"provider-bond",
            provider_authority_bytes.as_ref(),
            &[bond.bump],
        ]];

        let cpi_accounts = Transfer {
            from: ctx.accounts.provider_dedicated_ata.to_account_info(),
            to: ctx.accounts.compensation_destination_ata.to_account_info(),
            authority: bond.to_account_info(),
        };
        token::transfer(
            CpiContext::new_with_signer(ctx.accounts.token_program.to_account_info(), cpi_accounts, seeds),
            slash_amount,
        )?;

        msg!("HAICHAIN v7.0: Provider slashed {} USDT micro-units for fault hash: {:?}. Remaining stake: {}",
             slash_amount, fault_proof_hash, bond.staked_amount);
        Ok(())
    }

    /// 10. VERIFY DYNAMIC SPOT TICKET (M2M AUTONOMOUS PRICING DISCOVERY)
    pub fn verify_dynamic_spot_ticket(
        _ctx: Context<VerifyDynamicSpotContext>,
        base_price: u64,
        load_factor_bps: u64,
        max_budget_cap: u64,
        expiry_slot: u64,
    ) -> Result<()> {
        let current_slot = Clock::get()?.slot;
        require!(current_slot <= expiry_slot, HaiChainMasterError::SpotTicketExpired);

        let dynamic_surge = (base_price as u128)
            .checked_mul(load_factor_bps as u128)
            .ok_or(HaiChainMasterError::MathOverflow)?
            .checked_div(10_000)
            .ok_or(HaiChainMasterError::MathOverflow)? as u64;

        let spot_price = base_price.checked_add(dynamic_surge)
            .ok_or(HaiChainMasterError::MathOverflow)?;

        require!(spot_price <= max_budget_cap, HaiChainMasterError::SpotPriceExceedsCap);

        msg!("HAICHAIN v7.0: Dynamic spot price verified: {} USDT micro-units (surge: {} bps)", 
             spot_price, load_factor_bps);
        Ok(())
    }
}"""

content = content[:end_fn_idx] + new_instructions + content[end_fn_idx + (7 if "\r\n" in content[end_fn_idx:end_fn_idx+10] else 6):]

# 2. Add contexts before DATA STORAGE ACCOUNTS
data_storage_idx = content.find("// DATA STORAGE ACCOUNTS")
assert data_storage_idx != -1, "DATA STORAGE ACCOUNTS not found"
# find the line before data storage
target_pos = content.rfind("// ===", 0, data_storage_idx)

new_contexts = """#[derive(Accounts)]
pub struct RegisterProviderBondContext<'info> {
    #[account(
        init,
        payer = provider_authority,
        space = 8 + 32 + 32 + 32 + 8 + 8 + 8 + 8 + 1 + 1 + 1,
        seeds = [b"provider-bond", provider_authority.key().as_ref()],
        bump
    )]
    pub provider_bond: Account<'info, ProviderBondAccount>,

    #[account(
        constraint = provider_dedicated_ata.owner == provider_bond.key() 
            @ HaiChainMasterError::InvalidDedicatedAtaOwner,
        constraint = provider_dedicated_ata.mint == token_mint.key() 
            @ HaiChainMasterError::InvalidTokenMint
    )]
    pub provider_dedicated_ata: Account<'info, TokenAccount>,

    #[account(mut)]
    pub provider_source_ata: Account<'info, TokenAccount>,

    /// CHECK: USDT Token Mint
    pub token_mint: AccountInfo<'info>,

    #[account(mut)]
    pub provider_authority: Signer<'info>,

    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ReportAndSlashProviderContext<'info> {
    #[account(
        mut,
        seeds = [b"provider-bond", provider_bond.provider_authority.as_ref()],
        bump = provider_bond.bump,
        constraint = provider_bond.dedicated_ata == provider_dedicated_ata.key() 
            @ HaiChainMasterError::MismatchedDedicatedAta
    )]
    pub provider_bond: Account<'info, ProviderBondAccount>,

    #[account(mut)]
    pub provider_dedicated_ata: Account<'info, TokenAccount>,

    #[account(
        mut,
        constraint = compensation_destination_ata.mint == provider_bond.token_mint 
            @ HaiChainMasterError::InvalidTokenMint
    )]
    pub compensation_destination_ata: Account<'info, TokenAccount>,

    pub reporter: Signer<'info>,

    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct VerifyDynamicSpotContext<'info> {
    pub clock: Sysvar<'info, Clock>,
}

"""
content = content[:target_pos] + new_contexts + content[target_pos:]

# 3. Add ProviderBondAccount after NullifierRecord
nullifier_idx = content.find("pub struct NullifierRecord {")
assert nullifier_idx != -1, "NullifierRecord not found"
nullifier_end = content.find("}", nullifier_idx)
assert nullifier_end != -1, "nullifier end not found"

new_account = """}

#[account]
pub struct ProviderBondAccount {
    pub provider_authority: Pubkey,
    pub dedicated_ata: Pubkey,
    pub token_mint: Pubkey,
    pub staked_amount: u64,
    pub slashed_amount: u64,
    pub total_executions: u64,
    pub fault_reports: u64,
    pub min_sla_quality_score: u8,
    pub is_active: bool,
    pub bump: u8,
"""
content = content[:nullifier_end] + new_account + content[nullifier_end + 1:]

# 4. Add Errors
nonce_seq_idx = content.find("InvalidNonceSequence,")
assert nonce_seq_idx != -1, "InvalidNonceSequence not found"
error_end = content.find("}", nonce_seq_idx)

new_errors = """,
    #[msg("SLA: Provider bond deposit below minimum required amount (20 USDT).")]
    InsufficientBondStake,
    #[msg("SLA: Provider is currently inactive or slashed below required reserve.")]
    ProviderBondInactive,
    #[msg("SLA: Slashed amount exceeds available staked provider bond balance.")]
    ExceedsAvailableBond,
    #[msg("Pricing: Dynamic spot price exceeds maximum acceptable user budget cap.")]
    SpotPriceExceedsCap,
    #[msg("Pricing: Dynamic spot quotation ticket has expired on Solana clock.")]
    SpotTicketExpired,
}"""
content = content[:error_end] + new_errors + content[error_end + 1:]

with open("programs/haichain-core/src/lib.rs", "w", encoding="utf-8") as f:
    f.write(content)
print("Successfully upgraded programs/haichain-core/src/lib.rs to v7.0")
