import os

def patch():
    path = "programs/haichain-core/src/lib.rs"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Add instruction extend_channel_reserve after reserve_channel
    target_reserve_end = '''        msg!("HAICHAIN v1.1: Reserved {} tokens into channel {}", amount, channel_id);
        Ok(())
    }'''

    extend_fn = '''        msg!("HAICHAIN v1.1: Reserved {} tokens into channel {}", amount, channel_id);
        Ok(())
    }

    /// 14b. EXTEND CHANNEL RESERVE (CHANNEL RECYCLING & RENT PRESERVATION)
    pub fn extend_channel_reserve(
        ctx: Context<ExtendChannelReserveContext>,
        additional_amount: u64,
    ) -> Result<()> {
        let pot = &mut ctx.accounts.pot;
        let grant = &mut ctx.accounts.active_grant;
        let channel = &mut ctx.accounts.channel;

        require!(!pot.frozen, HaiChainMasterError::PotFrozen);
        require!(!grant.revoked, HaiChainMasterError::CapLeafExpired);
        require!(grant.epoch == pot.panic_epoch, HaiChainMasterError::EpochMismatch);
        require!(channel.created_at_epoch == pot.panic_epoch, HaiChainMasterError::EpochMismatch);
        require!(ctx.accounts.agent.key() == grant.agent, HaiChainMasterError::Unauthorized);

        let now = Clock::get()?.unix_timestamp;
        require!(now < grant.expiry, HaiChainMasterError::CapLeafExpired);
        require!(now <= pot.valid_until, HaiChainMasterError::CapabilityExpired);

        require!(additional_amount > 0, HaiChainMasterError::InvalidSpendAmount);
        let new_reserved = channel.reserved.checked_add(additional_amount).ok_or(HaiChainMasterError::MathOverflow)?;
        require!(new_reserved <= grant.max_reserve, HaiChainMasterError::ExceedsMaxReserve);
        require!(grant.consumed.checked_add(additional_amount).ok_or(HaiChainMasterError::MathOverflow)? <= grant.max_spend, HaiChainMasterError::ExceedsMaxSpend);

        if now >= grant.window_start + grant.window_secs as i64 {
            grant.window_start = now;
            grant.window_used = 0;
        }
        require!(grant.window_used.checked_add(additional_amount).ok_or(HaiChainMasterError::MathOverflow)? <= grant.window_cap, HaiChainMasterError::WindowCapExceeded);

        grant.consumed = grant.consumed.checked_add(additional_amount).ok_or(HaiChainMasterError::MathOverflow)?;
        grant.window_used = grant.window_used.checked_add(additional_amount).ok_or(HaiChainMasterError::MathOverflow)?;
        channel.reserved = new_reserved;

        // Reset dispute timer if it was pending
        channel.close_requested_at = 0;

        // Transfer tokens from vault ATA to channel escrow ATA
        let owner_auth_key = pot.owner_auth;
        let pot_bump = pot.bump;
        let seeds: &[&[&[u8]]] = &[&[
            b"pot",
            owner_auth_key.as_ref(),
            &[pot_bump],
        ]];

        let cpi_accounts = Transfer {
            from: ctx.accounts.vault_ata.to_account_info(),
            to: ctx.accounts.channel_escrow_ata.to_account_info(),
            authority: pot.to_account_info(),
        };
        token::transfer(
            CpiContext::new_with_signer(ctx.accounts.token_program.to_account_info(), cpi_accounts, seeds),
            additional_amount,
        )?;

        msg!("HAICHAIN v1.1: Extended channel {} by {} tokens. Total reserved: {}", channel.channel_id, additional_amount, channel.reserved);
        Ok(())
    }'''

    assert target_reserve_end in code, "reserve_channel end target not found"
    code = code.replace(target_reserve_end, extend_fn)

    # 2. Add ExtendChannelReserveContext after ReserveChannelContext
    target_reserve_ctx_end = '''    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct SettleVoucherContext<'info> {'''

    extend_ctx = '''    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ExtendChannelReserveContext<'info> {
    #[account(
        mut,
        seeds = [b"pot", pot.owner_auth.as_ref()],
        bump = pot.bump
    )]
    pub pot: Account<'info, PotAccount>,

    #[account(
        mut,
        has_one = pot @ HaiChainMasterError::PotMismatch,
        seeds = [b"grant", pot.key().as_ref(), active_grant.leaf_hash.as_ref()],
        bump = active_grant.bump
    )]
    pub active_grant: Account<'info, ActiveGrantAccount>,

    #[account(
        mut,
        constraint = channel.grant == active_grant.key() @ HaiChainMasterError::PotMismatch,
        seeds = [b"chan", active_grant.key().as_ref(), &channel.channel_id.to_le_bytes()],
        bump = channel.bump
    )]
    pub channel: Account<'info, ChannelAccount>,

    #[account(
        mut,
        constraint = vault_ata.owner == pot.key() @ HaiChainMasterError::InvalidDedicatedAtaOwner,
        constraint = vault_ata.mint == pot.token_mint @ HaiChainMasterError::InvalidTokenMint
    )]
    pub vault_ata: Account<'info, TokenAccount>,

    #[account(
        mut,
        constraint = channel_escrow_ata.owner == channel.key() @ HaiChainMasterError::InvalidDedicatedAtaOwner,
        constraint = channel_escrow_ata.mint == pot.token_mint @ HaiChainMasterError::InvalidTokenMint
    )]
    pub channel_escrow_ata: Account<'info, TokenAccount>,

    #[account(
        constraint = agent.key() == active_grant.agent @ HaiChainMasterError::Unauthorized
    )]
    pub agent: Signer<'info>,

    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct SettleVoucherContext<'info> {'''

    assert target_reserve_ctx_end in code, "ReserveChannelContext end target not found"
    code = code.replace(target_reserve_ctx_end, extend_ctx)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print("[OK] Successfully added extend_channel_reserve to programs/haichain-core/src/lib.rs")

if __name__ == "__main__":
    patch()
