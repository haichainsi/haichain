import os

test_path = os.path.join("tests", "haichain-sdk-verification.test.ts")
with open(test_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add PROTOCOL_CONSTANTS import
if "PROTOCOL_CONSTANTS" not in content:
    content = content.replace(
        'import { HaiChainClient } from "../sdk/typescript/src/index";',
        'import { HaiChainClient, PROTOCOL_CONSTANTS, SOLANA_USDT_MINT, SOLANA_USDC_MINT } from "../sdk/typescript/src/index";'
    )

test7_code = '''
  it("7. [PROTOCOL LIFECYCLE INSTRUCTIONS & INVARIANT CONSTANTS]: Verifies initialize, deposit, execute payment, and constants", () => {
    // 1. Verify on-chain invariant constants parity
    expect(PROTOCOL_CONSTANTS.FLASH_LOAN_QUARANTINE_SLOTS).to.equal(2n);
    expect(PROTOCOL_CONSTANTS.MIN_QUARANTINE_TRIGGER_DEPOSIT).to.equal(1_000_000n);
    expect(PROTOCOL_CONSTANTS.ROOT_ROTATION_GRACE_SLOTS).to.equal(150n);
    expect(PROTOCOL_CONSTANTS.MAX_SAFE_MICRO_TICK_PAYMENT).to.equal(50_000_000n);
    expect(PROTOCOL_CONSTANTS.MIN_PROVIDER_BOND_AMOUNT).to.equal(20_000_000n);

    const client = new HaiChainClient(null as any);
    const masterOwner = Keypair.generate().publicKey;
    const root = Buffer.alloc(32, 0xbb);

    // 2. buildInitializeVaultInstruction
    const initIx = client.buildInitializeVaultInstruction(masterOwner, SOLANA_USDT_MINT, root);
    expect(initIx.data.length).to.equal(40); // 8 bytes disc + 32 bytes root
    const expectedInitDisc = Buffer.from([230, 71, 53, 169, 238, 108, 169, 111]);
    expect(initIx.data.subarray(0, 8).equals(expectedInitDisc)).to.be.true;
    expect(initIx.keys.length).to.equal(5);

    // 3. buildDepositFundsInstruction
    const depositor = Keypair.generate().publicKey;
    const userSourceAta = Keypair.generate().publicKey;
    const depositIx = client.buildDepositFundsInstruction(masterOwner, depositor, userSourceAta, 5_000_000n);
    expect(depositIx.data.length).to.equal(16); // 8 bytes disc + 8 bytes u64 LE
    const expectedDepositDisc = Buffer.from([202, 39, 52, 211, 53, 20, 250, 88]);
    expect(depositIx.data.subarray(0, 8).equals(expectedDepositDisc)).to.be.true;
    expect(depositIx.data.readBigUInt64LE(8)).to.equal(5_000_000n);

    // 4. buildExecuteMasterPaymentInstruction
    const subAgent = Keypair.generate().publicKey;
    const payer = Keypair.generate().publicKey;
    const providerAta = Keypair.generate().publicKey;
    const proofElem1 = Buffer.alloc(32, 0x11);
    const proofElem2 = Buffer.alloc(32, 0x22);
    const proof = [proofElem1, proofElem2];

    const paymentIx = client.buildExecuteMasterPaymentInstruction(
      masterOwner,
      subAgent,
      payer,
      providerAta,
      2000n,
      10000n,
      50000n,
      1n,
      proof
    );
    // Data: 8 (disc) + 8*4 (spend, max, expiry, nonce) + 4 (proof len) + 32*2 (proof elems) = 8 + 32 + 4 + 64 = 108 bytes
    expect(paymentIx.data.length).to.equal(108);
    const expectedPayDisc = Buffer.from([164, 225, 64, 108, 234, 236, 177, 124]);
    expect(paymentIx.data.subarray(0, 8).equals(expectedPayDisc)).to.be.true;
    expect(paymentIx.data.readBigUInt64LE(8)).to.equal(2000n); // spend
    expect(paymentIx.data.readBigUInt64LE(16)).to.equal(10000n); // max
    expect(paymentIx.data.readBigUInt64LE(24)).to.equal(50000n); // expiry
    expect(paymentIx.data.readBigUInt64LE(32)).to.equal(1n); // nonce
    expect(paymentIx.data.readUInt32LE(40)).to.equal(2); // proof count
    expect(paymentIx.data.subarray(44, 76).equals(proofElem1)).to.be.true;
    expect(paymentIx.data.subarray(76, 108).equals(proofElem2)).to.be.true;
    expect(paymentIx.keys.length).to.equal(8);
  });
});'''

target = "expect(updateRootIx.data.subarray(8).equals(newRoot)).to.be.true;\n  });\n});"
if target in content:
    content = content.replace(target, "expect(updateRootIx.data.subarray(8).equals(newRoot)).to.be.true;\n  });" + test7_code)
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Test 7 added.")
else:
    target_crlf = target.replace('\n', '\r\n')
    if target_crlf in content:
        content = content.replace(target_crlf, ("expect(updateRootIx.data.subarray(8).equals(newRoot)).to.be.true;\n  });" + test7_code).replace('\n', '\r\n'))
        with open(test_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("SUCCESS (CRLF): Test 7 added.")
    else:
        print("ERROR: Target not found.")
