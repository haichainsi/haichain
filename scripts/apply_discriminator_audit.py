import os

sdk_path = os.path.join("sdk", "typescript", "src", "index.ts")
with open(sdk_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add TransactionInstruction to web3 import if not present
if "TransactionInstruction" not in content:
    content = content.replace(
        'Transaction, SystemProgram, SYSVAR_INSTRUCTIONS_PUBKEY',
        'Transaction, TransactionInstruction, SystemProgram, SYSVAR_INSTRUCTIONS_PUBKEY'
    )

old_panic = '''  public async triggerPanicKillSwitch(
    provider: AnchorProvider,
    agentDedicatedAta: PublicKey,
    userSafeDestinationAta: PublicKey
  ): Promise<string> {
    const owner = provider.wallet.publicKey;
    const [agentVaultPda] = this.getAgentVaultPda(owner);

    const tx = new Transaction().add({
      keys: [
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
        { pubkey: userSafeDestinationAta, isSigner: false, isWritable: true },
        { pubkey: owner, isSigner: true, isWritable: false },
        { pubkey: TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
      ],
      programId: this.programId,
      data: Buffer.from([139, 140, 195, 237, 245, 174, 237, 107]),
    });

    return await provider.sendAndConfirm(tx);
  }

  public async reclaimExpiredNullifierRent(
    provider: AnchorProvider,
    vaultOwner: PublicKey,
    nonce: number | bigint,
    rentReceiver: PublicKey = vaultOwner
  ): Promise<string> {
    const [agentVaultPda] = this.getAgentVaultPda(vaultOwner);
    const [nullifierPda] = this.getNullifierPda(agentVaultPda, nonce);

    if (!rentReceiver.equals(vaultOwner)) {
      throw new Error("SECURITY INVARIANT VIOLATION: Reclaimed rent must strictly be returned to vaultOwner");
    }

    const tx = new Transaction().add({
      keys: [
        { pubkey: nullifierPda, isSigner: false, isWritable: true },
        { pubkey: agentVaultPda, isSigner: false, isWritable: false },
        { pubkey: rentReceiver, isSigner: false, isWritable: true },
      ],
      programId: this.programId,
      data: Buffer.from([168, 203, 114, 182, 194, 111, 44, 219]),
    });

    return await provider.sendAndConfirm(tx);
  }'''

new_methods = '''  /**
   * Builds the instruction for triggering the emergency panic kill-switch.
   * Anchor Discriminator: sha256("global:trigger_emergency_panic")[0..8] = [232, 177, 104, 97, 82, 33, 17, 191]
   */
  public buildTriggerPanicInstruction(
    masterOwner: PublicKey,
    agentDedicatedAta: PublicKey,
    userSafeDestinationAta: PublicKey
  ): TransactionInstruction {
    const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
    return new TransactionInstruction({
      keys: [
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: agentDedicatedAta, isSigner: false, isWritable: true },
        { pubkey: userSafeDestinationAta, isSigner: false, isWritable: true },
        { pubkey: masterOwner, isSigner: true, isWritable: false },
        { pubkey: TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
      ],
      programId: this.programId,
      data: Buffer.from([232, 177, 104, 97, 82, 33, 17, 191]),
    });
  }

  public async triggerPanicKillSwitch(
    provider: AnchorProvider,
    agentDedicatedAta: PublicKey,
    userSafeDestinationAta: PublicKey
  ): Promise<string> {
    const owner = provider.wallet.publicKey;
    const ix = this.buildTriggerPanicInstruction(owner, agentDedicatedAta, userSafeDestinationAta);
    const tx = new Transaction().add(ix);
    return await provider.sendAndConfirm(tx);
  }

  /**
   * Builds the instruction for reclaiming expired nullifier SOL rent.
   * Anchor Discriminator: sha256("global:reclaim_expired_nullifier")[0..8] = [16, 165, 146, 96, 207, 57, 80, 93]
   * Invariant: agentVaultPda MUST be writable because vault.min_valid_nonce is monotonically updated on-chain.
   */
  public buildReclaimNullifierInstruction(
    vaultOwner: PublicKey,
    nonce: number | bigint,
    rentReceiver: PublicKey = vaultOwner
  ): TransactionInstruction {
    const [agentVaultPda] = this.getAgentVaultPda(vaultOwner);
    const [nullifierPda] = this.getNullifierPda(agentVaultPda, nonce);

    if (!rentReceiver.equals(vaultOwner)) {
      throw new Error("SECURITY INVARIANT VIOLATION: Reclaimed rent must strictly be returned to vaultOwner");
    }

    const nonceBuf = Buffer.alloc(8);
    nonceBuf.writeBigUInt64LE(BigInt(nonce));
    const instructionData = Buffer.concat([
      Buffer.from([16, 165, 146, 96, 207, 57, 80, 93]),
      nonceBuf,
    ]);

    return new TransactionInstruction({
      keys: [
        { pubkey: nullifierPda, isSigner: false, isWritable: true },
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: rentReceiver, isSigner: false, isWritable: true },
      ],
      programId: this.programId,
      data: instructionData,
    });
  }

  public async reclaimExpiredNullifierRent(
    provider: AnchorProvider,
    vaultOwner: PublicKey,
    nonce: number | bigint,
    rentReceiver: PublicKey = vaultOwner
  ): Promise<string> {
    const ix = this.buildReclaimNullifierInstruction(vaultOwner, nonce, rentReceiver);
    const tx = new Transaction().add(ix);
    return await provider.sendAndConfirm(tx);
  }

  /**
   * Builds the instruction for O(1) mass-invalidation of capability tickets.
   * Anchor Discriminator: sha256("global:advance_min_valid_nonce")[0..8] = [81, 92, 116, 233, 79, 68, 222, 129]
   */
  public buildAdvanceMinValidNonceInstruction(
    masterOwner: PublicKey,
    newMinNonce: number | bigint
  ): TransactionInstruction {
    const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
    const nonceBuf = Buffer.alloc(8);
    nonceBuf.writeBigUInt64LE(BigInt(newMinNonce));

    return new TransactionInstruction({
      keys: [
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: masterOwner, isSigner: true, isWritable: false },
      ],
      programId: this.programId,
      data: Buffer.concat([
        Buffer.from([81, 92, 116, 233, 79, 68, 222, 129]),
        nonceBuf,
      ]),
    });
  }

  /**
   * Builds the instruction for rotating composite Merkle roots with sliding window grace period.
   * Anchor Discriminator: sha256("global:update_composite_root")[0..8] = [230, 8, 5, 238, 82, 121, 117, 97]
   */
  public buildUpdateCompositeRootInstruction(
    masterOwner: PublicKey,
    newCompositeRoot: Uint8Array | Buffer
  ): TransactionInstruction {
    const [agentVaultPda] = this.getAgentVaultPda(masterOwner);
    if (newCompositeRoot.length !== 32) {
      throw new Error("Invalid Merkle root length: expected 32 bytes");
    }

    return new TransactionInstruction({
      keys: [
        { pubkey: agentVaultPda, isSigner: false, isWritable: true },
        { pubkey: masterOwner, isSigner: true, isWritable: false },
      ],
      programId: this.programId,
      data: Buffer.concat([
        Buffer.from([230, 8, 5, 238, 82, 121, 117, 97]),
        Buffer.from(newCompositeRoot),
      ]),
    });
  }'''

# Handle both LF and CRLF
target_found = False
if old_panic in content:
    content = content.replace(old_panic, new_methods, 1)
    target_found = True
else:
    old_panic_crlf = old_panic.replace('\n', '\r\n')
    if old_panic_crlf in content:
        new_methods_crlf = new_methods.replace('\n', '\r\n')
        content = content.replace(old_panic_crlf, new_methods_crlf, 1)
        target_found = True

if target_found:
    with open(sdk_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Updated sdk/typescript/src/index.ts with Anchor discriminators and instruction builders.")
else:
    print("ERROR: old_panic target not found in file.")
