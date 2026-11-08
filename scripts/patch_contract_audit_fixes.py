with open('programs/haichain-core/src/lib.rs', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CloseNotRequested to HaiChainMasterError
old_err = 'enum HaiChainMasterError {\n    #[msg("Authorization: Signer is not authorized for this operation.")]\n    Unauthorized,'
new_err = '''enum HaiChainMasterError {
    #[msg("Authorization: Signer is not authorized for this operation.")]
    Unauthorized,
    #[msg("Channel: Close has not been requested yet. Must call request_close_channel and wait for dispute window.")]
    CloseNotRequested,'''
assert old_err in content, "Could not find HaiChainMasterError definition"
content = content.replace(old_err, new_err)

# 2. Update close_channel to enforce CloseNotRequested
old_close = '''        // Refund any residual reserved funds
        let unspent = channel.reserved.saturating_sub(channel.paid);
        if unspent > 0 {
            let now = Clock::get()?.unix_timestamp;
            // Enforce dispute window for unspent funds if close was requested
            if channel.close_requested_at > 0 {
                require!(
                    now >= channel.close_requested_at + channel.dispute_secs as i64,
                    HaiChainMasterError::DisputeWindowActive
                );
            }'''

new_close = '''        // Refund any residual reserved funds
        let unspent = channel.reserved.saturating_sub(channel.paid);
        if unspent > 0 {
            let now = Clock::get()?.unix_timestamp;
            // Formal dispute window invariant: close MUST have been requested and window elapsed
            require!(
                channel.close_requested_at > 0,
                HaiChainMasterError::CloseNotRequested
            );
            require!(
                now >= channel.close_requested_at + channel.dispute_secs as i64,
                HaiChainMasterError::DisputeWindowActive
            );'''

assert old_close in content, "Could not find close_channel logic"
content = content.replace(old_close, new_close)

# 3. Update RequestCloseChannelContext to add pot constraint on active_grant
old_req_ctx = '''pub struct RequestCloseChannelContext<'info> {
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

    pub active_grant: Account<'info, ActiveGrantAccount>,'''

new_req_ctx = '''pub struct RequestCloseChannelContext<'info> {
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

    #[account(
        constraint = active_grant.pot == pot.key() @ HaiChainMasterError::PotMismatch
    )]
    pub active_grant: Account<'info, ActiveGrantAccount>,'''

assert old_req_ctx in content, "Could not find RequestCloseChannelContext"
content = content.replace(old_req_ctx, new_req_ctx)

# 4. Add unfreeze_pot instruction inside #[program]
old_fn = '''    /// 22. REQUEST CLOSE CHANNEL (INITIATES DISPUTE WINDOW COUNTDOWN)
    pub fn request_close_channel(ctx: Context<RequestCloseChannelContext>) -> Result<()> {'''

new_fn = '''    /// 23. UNFREEZE POT (MASTER OWNER RESTORES POT AFTER EMERGENCY INVESTIGATION)
    pub fn unfreeze_pot(ctx: Context<UnfreezePotContext>) -> Result<()> {
        let pot = &mut ctx.accounts.pot;
        require!(pot.frozen, HaiChainMasterError::InvalidSpendAmount);
        pot.frozen = false;
        msg!("HAICHAIN: Pot unfrozen by master owner. Normal state channel operations resumed.");
        Ok(())
    }

    /// 22. REQUEST CLOSE CHANNEL (INITIATES DISPUTE WINDOW COUNTDOWN)
    pub fn request_close_channel(ctx: Context<RequestCloseChannelContext>) -> Result<()> {'''

assert old_fn in content, "Could not find request_close_channel"
content = content.replace(old_fn, new_fn)

# 5. Add UnfreezePotContext definition
old_ctx_anchor = '''#[derive(Accounts)]
pub struct PanicPotContext<'info> {'''

new_ctx_anchor = '''#[derive(Accounts)]
pub struct UnfreezePotContext<'info> {
    #[account(
        mut,
        has_one = owner_auth @ HaiChainMasterError::Unauthorized,
        seeds = [b"pot", owner_auth.key().as_ref()],
        bump = pot.bump
    )]
    pub pot: Account<'info, PotAccount>,
    pub owner_auth: Signer<'info>,
}

#[derive(Accounts)]
pub struct PanicPotContext<'info> {'''

assert old_ctx_anchor in content, "Could not find PanicPotContext anchor"
content = content.replace(old_ctx_anchor, new_ctx_anchor)

# 6. Replace comments referring to "Claude Audit"
content = content.replace("CLAUDE AUDIT HARDENING:", "FORMAL INVARIANT HARDENING:")
content = content.replace("CLAUDE AUDIT:", "FORMAL INVARIANT:")
content = content.replace("Claude Audit", "Formal Invariant Audit")
content = content.replace("Claude audit", "Formal invariant audit")

with open('programs/haichain-core/src/lib.rs', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied smart contract invariant fixes to programs/haichain-core/src/lib.rs")
