import os

def patch_lib_rs():
    path = "programs/haichain-core/src/lib.rs"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Update HaiChainMasterError enum
    target_err = '    #[msg("Wormhole Exploit Defense: Invalid sysvar::instructions ID.")]\n    InvalidSysvarAddress,'
    repl_err = '''    #[msg("Authorization: Signer is not authorized for this operation.")]
    Unauthorized,
    #[msg("Channel: Close already requested. Dispute window is currently running.")]
    CloseAlreadyRequested,
    #[msg("Wormhole Exploit Defense: Invalid sysvar::instructions ID.")]
    InvalidSysvarAddress,'''
    assert target_err in code, "Target error not found"
    code = code.replace(target_err, repl_err)

    # 2. Add sysvar instructions check helper
    target_empty_leaf = '''pub fn compute_empty_leaf() -> [u8; 32] {
    anchor_lang::solana_program::hash::hashv(&[
        &[0x02],
        CAPLEAF_V1_TAG,
    ]).to_bytes()
}'''
    repl_empty_leaf = '''pub fn compute_empty_leaf() -> [u8; 32] {
    anchor_lang::solana_program::hash::hashv(&[
        &[0x02],
        CAPLEAF_V1_TAG,
    ]).to_bytes()
}

/// INVARIANT: WORMHOLE INSTRUCTIONS SYSVAR VERIFICATION ($320M EXPLOIT DEFENSE)
/// Ensures instructions sysvar matches the canonical Solana Sysvar Instructions address.
pub fn verify_instructions_sysvar_account(instructions_sysvar: &AccountInfo) -> Result<()> {
    require!(
        instructions_sysvar.key == &solana_program::sysvar::instructions::ID,
        HaiChainMasterError::InvalidSysvarAddress
    );
    Ok(())
}'''
    assert target_empty_leaf in code, "Target empty leaf not found"
    code = code.replace(target_empty_leaf, repl_empty_leaf)

    # 3. Update reserve_channel constraint in body
    target_res = '''        require!(!pot.frozen, HaiChainMasterError::PotFrozen);
        require!(!grant.revoked, HaiChainMasterError::CapLeafExpired);
        require!(grant.epoch == pot.panic_epoch, HaiChainMasterError::EpochMismatch);'''
    repl_res = '''        require!(!pot.frozen, HaiChainMasterError::PotFrozen);
        require!(!grant.revoked, HaiChainMasterError::CapLeafExpired);
        require!(grant.epoch == pot.panic_epoch, HaiChainMasterError::EpochMismatch);
        require!(ctx.accounts.agent.key() == grant.agent, HaiChainMasterError::Unauthorized);'''
    assert target_res in code, "Target reserve body not found"
    code = code.replace(target_res, repl_res)

    # 4. Update activate_child constraint in body
    target_act = '''        require!(!pot.frozen, HaiChainMasterError::PotFrozen);
        require!(!template_grant.revoked, HaiChainMasterError::CapLeafExpired);'''
    repl_act = '''        require!(!pot.frozen, HaiChainMasterError::PotFrozen);
        require!(!template_grant.revoked, HaiChainMasterError::CapLeafExpired);
        require!(ctx.accounts.agent.key() == template_grant.agent, HaiChainMasterError::Unauthorized);'''
    assert target_act in code, "Target activate_child body not found"
    code = code.replace(target_act, repl_act)

    # 5. Update settle_voucher
    target_settle = '''    /// 15. SETTLE VOUCHER (SETTLEMENT WITH ANTI-JITO-PANIC MEV IMMUNITY)
    pub fn settle_voucher(
        ctx: Context<SettleVoucherContext>,
        cumulative_amount: u64,
    ) -> Result<()> {
        let pot = &ctx.accounts.pot;
        let channel = &mut ctx.accounts.channel;

        // RED-TEAM PATCH 1: Reject settlement if pot was panicked!
        require!(pot.panic_epoch == channel.created_at_epoch && !pot.frozen, HaiChainMasterError::PotPanickedFundsFrozen);'''

    repl_settle = '''    /// 15. SETTLE VOUCHER (SETTLEMENT WITH ANTI-JITO-PANIC MEV IMMUNITY & EXPLICIT REVOCATION CHECK)
    pub fn settle_voucher(
        ctx: Context<SettleVoucherContext>,
        cumulative_amount: u64,
    ) -> Result<()> {
        let pot = &ctx.accounts.pot;
        let grant = &ctx.accounts.active_grant;
        let channel = &mut ctx.accounts.channel;

        // CLAUDE AUDIT HARDENING: Check frozen pot, revoked grant, and panic epoch mismatch
        require!(!pot.frozen, HaiChainMasterError::PotPanickedFundsFrozen);
        require!(!grant.revoked, HaiChainMasterError::CapLeafExpired);
        require!(pot.panic_epoch == channel.created_at_epoch, HaiChainMasterError::EpochMismatch);'''
    assert target_settle in code, "Target settle_voucher not found"
    code = code.replace(target_settle, repl_settle)

    # 6. Update close_channel
    target_close = '''    /// 17. CLOSE CHANNEL (REFUNDS RESIDUAL RESERVED & RED-TEAM PATCH 4 RENT PRESERVATION)
    pub fn close_channel(
        ctx: Context<CloseChannelContext>,
    ) -> Result<()> {
        let channel = &ctx.accounts.channel;
        let grant = &mut ctx.accounts.active_grant;

        // Refund any residual reserved funds
        let unspent = channel.reserved.saturating_sub(channel.paid);
        if unspent > 0 {
            grant.consumed = grant.consumed.saturating_sub(unspent);'''

    repl_close = '''    /// 17. CLOSE CHANNEL (REFUNDS RESIDUAL RESERVED, DISPUTE WINDOW & SIGNER ENFORCED)
    pub fn close_channel(
        ctx: Context<CloseChannelContext>,
    ) -> Result<()> {
        let channel = &ctx.accounts.channel;
        let grant = &mut ctx.accounts.active_grant;
        let pot = &ctx.accounts.pot;
        let authority = &ctx.accounts.authority;

        // CLAUDE AUDIT HARDENING: Enforce authorized signer (agent or pot owner)
        require!(
            authority.key() == channel.agent_key || authority.key() == pot.owner_auth,
            HaiChainMasterError::Unauthorized
        );

        // Refund any residual reserved funds
        let unspent = channel.reserved.saturating_sub(channel.paid);
        if unspent > 0 {
            let now = Clock::get()?.unix_timestamp;
            // Enforce dispute window for unspent funds if close was requested
            if channel.close_requested_at > 0 {
                require!(
                    now >= channel.close_requested_at + channel.dispute_secs as i64,
                    HaiChainMasterError::DisputeWindowActive
                );
            }
            grant.consumed = grant.consumed.saturating_sub(unspent);'''
    assert target_close in code, "Target close_channel not found"
    code = code.replace(target_close, repl_close)

    # 7. Add new instructions before the end of pub mod haichain_core
    target_end_mod = '''        msg!("HAICHAIN v1.1: Activated probation child grant for merchant {}", new_merchant);
        Ok(())
    }


}'''

    new_instructions = '''        msg!("HAICHAIN v1.1: Activated probation child grant for merchant {}", new_merchant);
        Ok(())
    }

    /// 19. PANIC POT (EMERGENCY FREEZE & INITIATE NEW PANIC EPOCH)
    pub fn panic_pot(ctx: Context<PanicPotContext>) -> Result<()> {
        let pot = &mut ctx.accounts.pot;
        pot.frozen = true;
        pot.panic_epoch = pot.panic_epoch.checked_add(1).ok_or(HaiChainMasterError::MathOverflow)?;
        msg!("HAICHAIN: Pot panicked! Frozen = true, new panic_epoch = {}", pot.panic_epoch);
        Ok(())
    }

    /// 20. REVOKE GRANT (MASTER OWNER REVOKES CAPABILITY GRANT)
    pub fn revoke_grant(ctx: Context<RevokeGrantContext>) -> Result<()> {
        let grant = &mut ctx.accounts.active_grant;
        grant.revoked = true;
        msg!("HAICHAIN: Capability grant {:?} explicitly revoked by master owner.", grant.key());
        Ok(())
    }

    /// 21. WITHDRAW POT (MASTER OWNER WITHDRAWS FUNDS FROM VAULT ATA)
    pub fn withdraw_pot(ctx: Context<WithdrawPotContext>, amount: u64) -> Result<()> {
        let pot = &ctx.accounts.pot;
        require!(amount > 0, HaiChainMasterError::InvalidSpendAmount);

        let owner_auth_key = pot.owner_auth;
        let pot_bump = pot.bump;
        let seeds: &[&[&[u8]]] = &[&[
            b"pot",
            owner_auth_key.as_ref(),
            &[pot_bump],
        ]];

        let cpi_accounts = Transfer {
            from: ctx.accounts.vault_ata.to_account_info(),
            to: ctx.accounts.recipient_ata.to_account_info(),
            authority: pot.to_account_info(),
        };
        token::transfer(
            CpiContext::new_with_signer(ctx.accounts.token_program.to_account_info(), cpi_accounts, seeds),
            amount,
        )?;

        msg!("HAICHAIN: Master owner withdrew {} tokens from pot.", amount);
        Ok(())
    }

    /// 22. REQUEST CLOSE CHANNEL (INITIATES DISPUTE WINDOW COUNTDOWN)
    pub fn request_close_channel(ctx: Context<RequestCloseChannelContext>) -> Result<()> {
        let channel = &mut ctx.accounts.channel;
        let pot = &ctx.accounts.pot;
        let authority = &ctx.accounts.authority;

        require!(
            authority.key() == channel.agent_key || authority.key() == pot.owner_auth,
            HaiChainMasterError::Unauthorized
        );
        require!(channel.close_requested_at == 0, HaiChainMasterError::CloseAlreadyRequested);

        channel.close_requested_at = Clock::get()?.unix_timestamp;
        msg!("HAICHAIN: Close requested for channel {}. Dispute timer active ({}s).", channel.channel_id, channel.dispute_secs);
        Ok(())
    }

}'''
    assert target_end_mod in code, "Target end mod not found"
    code = code.replace(target_end_mod, new_instructions)

    # 8. Update ReserveChannelContext struct
    target_res_ctx = '''    pub agent: Signer<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,'''
    repl_res_ctx = '''    #[account(
        constraint = agent.key() == active_grant.agent @ HaiChainMasterError::Unauthorized
    )]
    pub agent: Signer<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,'''
    assert target_res_ctx in code, "Target ReserveChannelContext agent not found"
    code = code.replace(target_res_ctx, repl_res_ctx)

    # 9. Update SettleVoucherContext struct
    target_settle_ctx = '''#[derive(Accounts)]
pub struct SettleVoucherContext<'info> {
    #[account(
        seeds = [b"pot", pot.owner_auth.as_ref()],
        bump = pot.bump
    )]
    pub pot: Account<'info, PotAccount>,

    #[account(
        mut,
        seeds = [b"chan", channel.grant.as_ref(), &channel.channel_id.to_le_bytes()],
        bump = channel.bump
    )]
    pub channel: Account<'info, ChannelAccount>,

    #[account(
        mut,
        constraint = channel_escrow_ata.owner == channel.key() @ HaiChainMasterError::InvalidDedicatedAtaOwner,
        constraint = channel_escrow_ata.mint == pot.token_mint @ HaiChainMasterError::InvalidTokenMint
    )]
    pub channel_escrow_ata: Account<'info, TokenAccount>,

    #[account(
        mut,
        constraint = payee_ata.key() == channel.payee_ata @ HaiChainMasterError::InvalidPayeeAta
    )]
    pub payee_ata: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
}'''

    repl_settle_ctx = '''#[derive(Accounts)]
pub struct SettleVoucherContext<'info> {
    #[account(
        seeds = [b"pot", pot.owner_auth.as_ref()],
        bump = pot.bump
    )]
    pub pot: Account<'info, PotAccount>,

    #[account(
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
        constraint = channel_escrow_ata.owner == channel.key() @ HaiChainMasterError::InvalidDedicatedAtaOwner,
        constraint = channel_escrow_ata.mint == pot.token_mint @ HaiChainMasterError::InvalidTokenMint
    )]
    pub channel_escrow_ata: Account<'info, TokenAccount>,

    #[account(
        mut,
        constraint = payee_ata.key() == channel.payee_ata @ HaiChainMasterError::InvalidPayeeAta,
        constraint = payee_ata.owner == payee.key() @ HaiChainMasterError::Unauthorized
    )]
    pub payee_ata: Account<'info, TokenAccount>,

    pub payee: Signer<'info>,

    pub token_program: Program<'info, Token>,
}'''
    assert target_settle_ctx in code, "Target SettleVoucherContext not found"
    code = code.replace(target_settle_ctx, repl_settle_ctx)

    # 10. Update CloseChannelContext struct
    target_close_ctx = '''    /// CHECK: RED-TEAM PATCH 4: 100% of rent lamports strictly refunded to original rent_recipient
    #[account(
        mut,
        address = channel.rent_recipient @ HaiChainMasterError::UnauthorizedRentRecipient
    )]
    pub rent_recipient: AccountInfo<'info>,

    pub token_program: Program<'info, Token>,
}'''
    repl_close_ctx = '''    /// CHECK: RED-TEAM PATCH 4: 100% of rent lamports strictly refunded to original rent_recipient
    #[account(
        mut,
        address = channel.rent_recipient @ HaiChainMasterError::UnauthorizedRentRecipient
    )]
    pub rent_recipient: AccountInfo<'info>,

    /// Authorized closer: agent or pot master owner
    pub authority: Signer<'info>,

    pub token_program: Program<'info, Token>,
}'''
    assert target_close_ctx in code, "Target CloseChannelContext not found"
    code = code.replace(target_close_ctx, repl_close_ctx)

    # 11. Update ActivateChildContext struct
    target_child_ctx = '''    pub agent: Signer<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,

    pub system_program: Program<'info, System>,
}'''
    repl_child_ctx = '''    #[account(
        constraint = agent.key() == template_grant.agent @ HaiChainMasterError::Unauthorized
    )]
    pub agent: Signer<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,

    pub system_program: Program<'info, System>,
}'''
    assert target_child_ctx in code, "Target ActivateChildContext not found"
    code = code.replace(target_child_ctx, repl_child_ctx)

    # 12. Add new Accounts structs after ActivateChildContext
    new_structs = '''

#[derive(Accounts)]
pub struct PanicPotContext<'info> {
    #[account(
        mut,
        seeds = [b"pot", pot.owner_auth.as_ref()],
        bump = pot.bump,
        constraint = signer.key() == pot.owner_auth || signer.key() == pot.cosigner @ HaiChainMasterError::Unauthorized
    )]
    pub pot: Account<'info, PotAccount>,
    pub signer: Signer<'info>,
}

#[derive(Accounts)]
pub struct RevokeGrantContext<'info> {
    #[account(
        seeds = [b"pot", pot.owner_auth.as_ref()],
        bump = pot.bump,
        has_one = owner_auth @ HaiChainMasterError::UnauthorizedOwner
    )]
    pub pot: Account<'info, PotAccount>,

    #[account(
        mut,
        has_one = pot @ HaiChainMasterError::PotMismatch,
        seeds = [b"grant", pot.key().as_ref(), active_grant.leaf_hash.as_ref()],
        bump = active_grant.bump
    )]
    pub active_grant: Account<'info, ActiveGrantAccount>,

    pub owner_auth: Signer<'info>,
}

#[derive(Accounts)]
pub struct WithdrawPotContext<'info> {
    #[account(
        seeds = [b"pot", pot.owner_auth.as_ref()],
        bump = pot.bump,
        has_one = owner_auth @ HaiChainMasterError::UnauthorizedOwner
    )]
    pub pot: Account<'info, PotAccount>,

    pub owner_auth: Signer<'info>,

    #[account(
        mut,
        constraint = vault_ata.owner == pot.key() @ HaiChainMasterError::InvalidDedicatedAtaOwner,
        constraint = vault_ata.mint == pot.token_mint @ HaiChainMasterError::InvalidTokenMint
    )]
    pub vault_ata: Account<'info, TokenAccount>,

    #[account(
        mut,
        constraint = recipient_ata.owner == pot.owner_auth @ HaiChainMasterError::UnauthorizedOwner,
        constraint = recipient_ata.mint == pot.token_mint @ HaiChainMasterError::InvalidTokenMint
    )]
    pub recipient_ata: Account<'info, TokenAccount>,

    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct RequestCloseChannelContext<'info> {
    #[account(
        seeds = [b"pot", pot.owner_auth.as_ref()],
        bump = pot.bump
    )]
    pub pot: Account<'info, PotAccount>,

    #[account(
        mut,
        constraint = channel.grant == active_grant.key() @ HaiChainMasterError::PotMismatch,
        seeds = [b"chan", active_grant.key().as_ref(), &channel.channel_id.to_le_bytes()],
        bump = channel.bump
    )]
    pub channel: Account<'info, ChannelAccount>,

    pub active_grant: Account<'info, ActiveGrantAccount>,

    pub authority: Signer<'info>,
}'''

    target_after_child = repl_child_ctx
    code = code.replace(target_after_child, target_after_child + new_structs, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print("[OK] Successfully patched programs/haichain-core/src/lib.rs")

if __name__ == "__main__":
    patch_lib_rs()
