// programs/haichain-sui/sources/capleaf.move
// HAICHAIN v1.1 - Sui Network L1 Move Implementation
// Leverages Move Object Model: AgentCap has key, store (NO copy, NO drop)
// Guaranteed Linear Ownership: An agent's capability can never be duplicated or discarded silently.

module haichain::capleaf {
    use sui::object::{Self, UID};
    use sui::tx_context::{Self, TxContext};
    use sui::coin::{Self, Coin};
    use sui::balance::{Self, Balance};
    use sui::clock::{Self, Clock};
    use sui::event;

    /// Error codes
    const EInvalidVersion: u64 = 1;
    const ECapabilityExpired: u64 = 2;
    const EExceedsMaxSpend: u64 = 3;
    const EExceedsMaxReserve: u64 = 4;
    const EPotFrozen: u64 = 5;
    const EMathOverflow: u64 = 6;
    const EInvalidPayee: u64 = 7;
    const EInvalidSettleAmount: u64 = 8;

    /// Master Operating Pot for an Autonomous Agent Entity
    public struct Pot<phantom T> has key {
        id: UID,
        owner_auth: address,
        policy_root: vector<u8>,
        tree_depth: u8,
        panic_epoch: u32,
        frozen: bool,
        valid_until_ms: u64,
        max_ttl_ms: u64,
        budget_total: u64,
        budget_used: u64,
        vault_balance: Balance<T>,
    }

    /// Linear Agent Capability (NO copy, NO drop)
    /// Enforces: Once created, the AgentCap can only be transferred or consumed via authorized protocol methods.
    public struct AgentCap has key, store {
        id: UID,
        pot_id: address,
        agent: address,
        merchant: address,
        max_spend: u64,
        max_reserve: u64,
        consumed: u64,
        window_cap: u64,
        window_secs: u32,
        window_start_ms: u64,
        window_used: u64,
        expiry_ms: u64,
        epoch: u32,
        flags: u16,
    }

    /// Channel Escrow Object holding locked reserve for state channel streaming
    public struct ChannelEscrow<phantom T> has key {
        id: UID,
        grant_id: address,
        channel_id: u64,
        merchant_recipient: address,
        reserved_amount: u64,
        paid_amount: u64,
        escrow_balance: Balance<T>,
        created_at_epoch: u32,
    }

    // Events
    public struct GrantActivated has copy, drop {
        grant_id: address,
        agent: address,
        merchant: address,
        max_spend: u64,
    }

    public struct ChannelReserved has copy, drop {
        channel_id: u64,
        amount: u64,
        merchant: address,
    }

    public struct VoucherSettled has copy, drop {
        channel_id: u64,
        paid: u64,
        delta: u64,
    }

    /// Initialize a new Sui HAICHAIN Pot
    public entry fun initialize_pot<T>(
        policy_root: vector<u8>,
        tree_depth: u8,
        max_ttl_ms: u64,
        budget_total: u64,
        clock: &Clock,
        ctx: &mut TxContext
    ) {
        let sender = tx_context::sender(ctx);
        let now_ms = clock::timestamp_ms(clock);
        
        let pot = Pot<T> {
            id: object::new(ctx),
            owner_auth: sender,
            policy_root,
            tree_depth,
            panic_epoch: 0,
            frozen: false,
            valid_until_ms: now_ms + max_ttl_ms,
            max_ttl_ms,
            budget_total,
            budget_used: 0,
            vault_balance: balance::zero(),
        };
        sui::transfer::share_object(pot);
    }

    /// Deposit funds into Pot vault
    public entry fun deposit<T>(
        pot: &mut Pot<T>,
        payment: Coin<T>,
        _ctx: &mut TxContext
    ) {
        assert!(!pot.frozen, EPotFrozen);
        let val = coin::value(&payment);
        balance::join(&mut pot.vault_balance, coin::into_balance(payment));
        pot.budget_total = pot.budget_total + val;
    }

    /// Reserve funds from Pot Vault into ChannelEscrow using AgentCap
    public entry fun reserve_channel<T>(
        pot: &mut Pot<T>,
        cap: &mut AgentCap,
        channel_id: u64,
        amount: u64,
        clock: &Clock,
        ctx: &mut TxContext
    ) {
        let now_ms = clock::timestamp_ms(clock);
        assert!(!pot.frozen, EPotFrozen);
        assert!(now_ms < cap.expiry_ms, ECapabilityExpired);
        assert!(now_ms <= pot.valid_until_ms, ECapabilityExpired);
        assert!(cap.epoch == pot.panic_epoch, EPotFrozen);
        assert!(amount <= cap.max_reserve, EExceedsMaxReserve);
        assert!(cap.consumed + amount <= cap.max_spend, EExceedsMaxSpend);

        // Deduct from Vault balance
        let split_bal = balance::split(&mut pot.vault_balance, amount);
        cap.consumed = cap.consumed + amount;

        let channel = ChannelEscrow<T> {
            id: object::new(ctx),
            grant_id: object::uid_to_address(&cap.id),
            channel_id,
            merchant_recipient: cap.merchant,
            reserved_amount: amount,
            paid_amount: 0,
            escrow_balance: split_bal,
            created_at_epoch: pot.panic_epoch,
        };

        event::emit(ChannelReserved {
            channel_id,
            amount,
            merchant: cap.merchant,
        });

        sui::transfer::share_object(channel);
    }

    /// Settle micro-voucher with Red-Team Jito MEV protection (created_at_epoch check)
    public entry fun settle_voucher<T>(
        pot: &Pot<T>,
        channel: &mut ChannelEscrow<T>,
        cumulative_amount: u64,
        ctx: &mut TxContext
    ) {
        // Red-Team defense: If pot panicked, funds in channel are frozen
        assert!(pot.panic_epoch == channel.created_at_epoch && !pot.frozen, EPotFrozen);
        assert!(cumulative_amount > channel.paid_amount, EInvalidSettleAmount);

        let effective = if (cumulative_amount > channel.reserved_amount) {
            channel.reserved_amount
        } else {
            cumulative_amount
        };

        let delta = effective - channel.paid_amount;
        channel.paid_amount = effective;

        // Split delta payment and transfer directly to merchant recipient
        let payout = balance::split(&mut channel.escrow_balance, delta);
        let coin_payout = coin::from_balance(payout, ctx);
        sui::transfer::public_transfer(coin_payout, channel.merchant_recipient);

        event::emit(VoucherSettled {
            channel_id: channel.channel_id,
            paid: effective,
            delta,
        });
    }

    /// Emergency Panic Trip
    public entry fun trigger_panic<T>(
        pot: &mut Pot<T>,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == pot.owner_auth, EPotFrozen);
        pot.frozen = true;
        pot.panic_epoch = pot.panic_epoch + 1;
    }
}
