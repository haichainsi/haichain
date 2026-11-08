import os

sdk_path = os.path.join("sdk", "typescript", "src", "index.ts")
with open(sdk_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add nacl import if not present
if 'import nacl from "tweetnacl";' not in content:
    content = content.replace(
        'import { keccak_256 } from "@noble/hashes/sha3";',
        'import { keccak_256 } from "@noble/hashes/sha3";\nimport nacl from "tweetnacl";'
    )

target = '    return crypto.createHash("sha256").update(payloadStr).digest();\n  }'

replacement = '''    return crypto.createHash("sha256").update(payloadStr).digest();
  }

  /**
   * Verifies a Merkle proof against a composite root with sorted pair hashing.
   * Exactly replicates the on-chain Anchor verification in haichain-core (lib.rs lines 164-171).
   * Enables zero-cost off-chain pre-flight simulation before submitting transactions to Solana.
   */
  public static verifyCompositeProof(
    leaf: Uint8Array | Buffer,
    proof: (Uint8Array | Buffer)[],
    expectedRoot: Uint8Array | Buffer
  ): boolean {
    let computedHash = Buffer.from(leaf);
    for (const elem of proof) {
      const proofElement = Buffer.from(elem);
      if (Buffer.compare(computedHash, proofElement) <= 0) {
        computedHash = Buffer.from(keccak_256(Buffer.concat([computedHash, proofElement])));
      } else {
        computedHash = Buffer.from(keccak_256(Buffer.concat([proofElement, computedHash])));
      }
    }
    return computedHash.equals(Buffer.from(expectedRoot));
  }

  /**
   * Cryptographically signs a micro-voucher with an Ed25519 keypair.
   * Combines domain-separated payload hashing with detached Ed25519 signing.
   */
  public static signMicroVoucher(
    agentKeypair: Keypair,
    voucherArgs: {
      clusterId: "mainnet-beta" | "devnet" | "testnet";
      programId: PublicKey;
      vaultPda: PublicKey;
      providerPubkey: PublicKey;
      sessionId: string;
      nonce: number | bigint;
      cumulativeAmount: number | bigint;
    }
  ): { payloadHash: Buffer; signature: Uint8Array; signatureBase64: string } {
    const payloadHash = this.buildVoucherSigningPayload(
      voucherArgs.clusterId,
      voucherArgs.programId,
      voucherArgs.vaultPda,
      voucherArgs.providerPubkey,
      voucherArgs.sessionId,
      voucherArgs.nonce,
      voucherArgs.cumulativeAmount
    );
    const signature = nacl.sign.detached(payloadHash, agentKeypair.secretKey);
    return {
      payloadHash,
      signature,
      signatureBase64: Buffer.from(signature).toString("base64"),
    };
  }

  /**
   * Verifies an Ed25519 micro-voucher signature off-chain.
   * Can be executed by providers and gateway proxies in sub-millisecond latency (<0.1ms).
   */
  public static verifyMicroVoucherSignature(
    signerPubkey: PublicKey,
    payloadHash: Uint8Array | Buffer,
    signature: Uint8Array | Buffer
  ): boolean {
    return nacl.sign.detached.verify(
      Uint8Array.from(payloadHash),
      Uint8Array.from(signature),
      signerPubkey.toBytes()
    );
  }'''

if target in content:
    content = content.replace(target, replacement, 1)
    with open(sdk_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: sdk/typescript/src/index.ts updated with verifyCompositeProof & signMicroVoucher.")
else:
    # check CRLF
    target_crlf = target.replace('\n', '\r\n')
    if target_crlf in content:
        replacement_crlf = replacement.replace('\n', '\r\n')
        content = content.replace(target_crlf, replacement_crlf, 1)
        with open(sdk_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("SUCCESS (CRLF): sdk/typescript/src/index.ts updated.")
    else:
        print("Target not found.")
