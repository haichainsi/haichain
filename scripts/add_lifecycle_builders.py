import os

sdk_path = os.path.join("sdk", "typescript", "src", "index.ts")
with open(sdk_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Export Protocol Constants at top
constants_code = '''export const SOLANA_USDT_MINT = new PublicKey("Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB");
// Official Solana Mainnet Circle USD (USDC) SPL Token Mint (EU MiCA & Global Regulatory Compliant)
export const SOLANA_USDC_MINT = new PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v");

// Official On-Chain Protocol Invariant Constants (programs/haichain-core/src/lib.rs)
export const PROTOCOL_CONSTANTS = {
  FLASH_LOAN_QUARANTINE_SLOTS: 2n,
  MIN_QUARANTINE_TRIGGER_DEPOSIT: 1_000_000n, // 1.00 USDT minimum deposit to reset quarantine barrier
  ROOT_ROTATION_GRACE_SLOTS: 150n,           // ~60 seconds sliding window for in-flight capability tickets
  MAX_SAFE_MICRO_TICK_PAYMENT: 50_000_000n,  // 50.00 USDT max per single micro-tick (6 decimals)
  MIN_PROVIDER_BOND_AMOUNT: 20_000_000n,     // 20.00 USDT minimum bond stake
  MAX_SLASH_PER_INCIDENT: 10_000_000n,       // 10.00 USDT max slash penalty per incident
};'''

content = content.replace(
    '''export const SOLANA_USDT_MINT = new PublicKey("Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB");
// Official Solana Mainnet Circle USD (USDC) SPL Token Mint (EU MiCA & Global Regulatory Compliant)
export const SOLANA_USDC_MINT = new PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v");''',
    constants_code
)

# 2. Add buildInitializeVaultInstruction, buildDepositFundsInstruction, buildExecuteMasterPaymentInstruction
target_insertion = '''  public getAgentVaultPda(owner: PublicKey): [PublicKey, number] {'''

new_instructions = '''  /**
   * Builds the instruction for initializing an Agent Vault on Solana.
   * Anchor Discriminator: sha256("global:initialize_agent_vault")[0..8] = [230, 71, 53, 169, 238, 108, 169, 111]
   */
  public buildInitializeVaultInstruction(
    masterOwner: PublicKey,
    tokenMint: PublicKey,
    compositeRoot: Uint8Array | Buffer
  ): TransactionInstruction {
    if (compositeRoot.length !== 32) {
      throw new Error("Invalid composite root: expected 32 bytes");
    }
    const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
    const agentDedicatedAta = getAssociatedTokenAddress(tokenMint, agentVaultPda, true);

    return new TransactionInstruction({
      keys: [
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: tokenMint, isSigner: false, isWritable: false },
        { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
        { pubkey: masterOwner, isSigner: true, isWritable: true },
        { pubkey: SystemProgram.programId, isSigner: false, isWritable: false },
      ],
      programId: this.programId,
      data: Buffer.concat([
        Buffer.from([230, 71, 53, 169, 238, 108, 169, 111]),
        Buffer.from(compositeRoot),
      ]),
    });
  }

  /**
   * Builds the instruction for depositing funds into the vault.
   * Supports decoupled depositors (e.g. background fiat relayers, Stripe/Apple Pay, or master owner).
   * Anchor Discriminator: sha256("global:deposit_funds")[0..8] = [202, 39, 52, 211, 53, 20, 250, 88]
   */
  public buildDepositFundsInstruction(
    masterOwner: PublicKey,
    depositor: PublicKey,
    userSourceAta: PublicKey,
    amountMicroUnits: number | bigint,
    tokenMint: PublicKey = this.usdtMint
  ): TransactionInstruction {
    const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
    const agentDedicatedAta = getAssociatedTokenAddress(tokenMint, agentVaultPda, true);

    const amountBuf = Buffer.alloc(8);
    amountBuf.writeBigUInt64LE(BigInt(amountMicroUnits));

    return new TransactionInstruction({
      keys: [
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
        { pubkey: userSourceAta, isSigner: false, isWritable: true },
        { pubkey: depositor, isSigner: true, isWritable: false },
        { pubkey: TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
      ],
      programId: this.programId,
      data: Buffer.concat([
        Buffer.from([202, 39, 52, 211, 53, 20, 250, 88]),
        amountBuf,
      ]),
    });
  }

  /**
   * Builds the instruction for executing a micro-payment on Solana L1 with Merkle proof verification.
   * Anchor Discriminator: sha256("global:execute_master_payment")[0..8] = [164, 225, 64, 108, 234, 236, 177, 124]
   */
  public buildExecuteMasterPaymentInstruction(
    masterOwner: PublicKey,
    subAgentSigner: PublicKey,
    payer: PublicKey,
    serviceProviderAta: PublicKey,
    spendAmount: number | bigint,
    maxAuthorizedAmount: number | bigint,
    expirySlot: number | bigint,
    nonce: number | bigint,
    compositeProof: (Uint8Array | Buffer)[],
    tokenMint: PublicKey = this.usdtMint
  ): TransactionInstruction {
    const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
    const agentDedicatedAta = getAssociatedTokenAddress(tokenMint, agentVaultPda, true);
    const [nullifierPda] = this.getNullifierPda(agentVaultPda, nonce);

    // Borsh serialization for Vec<[u8; 32]>
    const proofLengthBuf = Buffer.alloc(4);
    proofLengthBuf.writeUInt32LE(compositeProof.length);
    const proofBuffers = compositeProof.map(p => {
      const b = Buffer.from(p);
      if (b.length !== 32) throw new Error("Each Merkle proof element must be exactly 32 bytes");
      return b;
    });

    const spendBuf = Buffer.alloc(8);
    const maxBuf = Buffer.alloc(8);
    const expiryBuf = Buffer.alloc(8);
    const nonceBuf = Buffer.alloc(8);
    spendBuf.writeBigUInt64LE(BigInt(spendAmount));
    maxBuf.writeBigUInt64LE(BigInt(maxAuthorizedAmount));
    expiryBuf.writeBigUInt64LE(BigInt(expirySlot));
    nonceBuf.writeBigUInt64LE(BigInt(nonce));

    const instructionData = Buffer.concat([
      Buffer.from([164, 225, 64, 108, 234, 236, 177, 124]),
      spendBuf,
      maxBuf,
      expiryBuf,
      nonceBuf,
      proofLengthBuf,
      ...proofBuffers,
    ]);

    return new TransactionInstruction({
      keys: [
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
        { pubkey: serviceProviderAta, isSigner: false, isWritable: true },
        { pubkey: subAgentSigner, isSigner: true, isWritable: false },
        { pubkey: payer, isSigner: true, isWritable: true },
        { pubkey: nullifierPda, isSigner: false, isWritable: true },
        { pubkey: TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
        { pubkey: SystemProgram.programId, isSigner: false, isWritable: false },
      ],
      programId: this.programId,
      data: instructionData,
    });
  }

  public getAgentVaultPda(owner: PublicKey): [PublicKey, number] {'''

if target_insertion in content:
    content = content.replace(target_insertion, new_instructions, 1)
    with open(sdk_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Added full lifecycle instruction builders to sdk/typescript/src/index.ts")
else:
    target_crlf = target_insertion.replace('\n', '\r\n')
    if target_crlf in content:
        content = content.replace(target_crlf, new_instructions.replace('\n', '\r\n'), 1)
        with open(sdk_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("SUCCESS (CRLF): Added full lifecycle instruction builders to sdk/typescript/src/index.ts")
    else:
        print("ERROR: Target insertion point not found.")
