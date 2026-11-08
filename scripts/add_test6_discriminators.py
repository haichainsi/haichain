import os

test_path = os.path.join("tests", "haichain-sdk-verification.test.ts")
with open(test_path, "r", encoding="utf-8") as f:
    content = f.read()

test6_code = '''
  it("6. [ANCHOR DISCRIMINATOR & INSTRUCTION SERIALIZATION PARITY]: Verifies Anchor discriminators and writable account invariants", () => {
    const client = new HaiChainClient(null as any);
    const masterOwner = Keypair.generate().publicKey;
    const dedicatedAta = Keypair.generate().publicKey;
    const safeDestination = Keypair.generate().publicKey;

    // 1. Verify Panic instruction discriminator matches sha256("global:trigger_emergency_panic")[0..8]
    const panicIx = client.buildTriggerPanicInstruction(masterOwner, dedicatedAta, safeDestination);
    expect(panicIx.data.length).to.equal(8);
    const expectedPanicDisc = Buffer.from([232, 177, 104, 97, 82, 33, 17, 191]);
    expect(panicIx.data.equals(expectedPanicDisc)).to.be.true;

    // 2. Verify Reclaim Nullifier instruction discriminator, u64 LE nonce, and isWritable=true on vault
    const testNonce = 123456789n;
    const reclaimIx = client.buildReclaimNullifierInstruction(masterOwner, testNonce);
    expect(reclaimIx.data.length).to.equal(16); // 8 bytes disc + 8 bytes u64 LE nonce
    const expectedReclaimDisc = Buffer.from([16, 165, 146, 96, 207, 57, 80, 93]);
    expect(reclaimIx.data.subarray(0, 8).equals(expectedReclaimDisc)).to.be.true;
    expect(reclaimIx.data.readBigUInt64LE(8)).to.equal(testNonce);

    // Invariant: agentVaultPda MUST be writable because vault.min_valid_nonce is modified
    const vaultAccountMeta = reclaimIx.keys[1];
    expect(vaultAccountMeta.isWritable).to.be.true;

    // 3. Verify Advance Nonce instruction discriminator and serialization
    const advanceIx = client.buildAdvanceMinValidNonceInstruction(masterOwner, 9999n);
    expect(advanceIx.data.length).to.equal(16);
    const expectedAdvanceDisc = Buffer.from([81, 92, 116, 233, 79, 68, 222, 129]);
    expect(advanceIx.data.subarray(0, 8).equals(expectedAdvanceDisc)).to.be.true;
    expect(advanceIx.data.readBigUInt64LE(8)).to.equal(9999n);

    // 4. Verify Update Composite Root instruction discriminator and 32-byte payload
    const newRoot = Buffer.alloc(32, 0xaa);
    const updateRootIx = client.buildUpdateCompositeRootInstruction(masterOwner, newRoot);
    expect(updateRootIx.data.length).to.equal(40); // 8 bytes disc + 32 bytes root
    const expectedRootDisc = Buffer.from([230, 8, 5, 238, 82, 121, 117, 97]);
    expect(updateRootIx.data.subarray(0, 8).equals(expectedRootDisc)).to.be.true;
    expect(updateRootIx.data.subarray(8).equals(newRoot)).to.be.true;
  });
});'''

if "expect(isAlteredValid).to.be.false;\n  });\n});" in content:
    content = content.replace("expect(isAlteredValid).to.be.false;\n  });\n});", "expect(isAlteredValid).to.be.false;\n  });" + test6_code)
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: test 6 added.")
elif "expect(isAlteredValid).to.be.false;\r\n  });\r\n});" in content:
    content = content.replace("expect(isAlteredValid).to.be.false;\r\n  });\r\n});", "expect(isAlteredValid).to.be.false;\r\n  });" + test6_code.replace('\n', '\r\n'))
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS (CRLF): test 6 added.")
else:
    print("Target not found.")
