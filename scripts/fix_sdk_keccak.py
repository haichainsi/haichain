#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

sdk_file = "sdk/typescript/src/index.ts"
with open(sdk_file, "r", encoding="utf-8") as f:
    code = f.read()

# Add import if missing
if "from \"@noble/hashes/sha3\"" not in code:
    code = code.replace(
        "import * as crypto from \"crypto\";",
        "import * as crypto from \"crypto\";\nimport { keccak_256 } from \"@noble/hashes/sha3\";"
    )

# Fix computeCompositeCapabilityLeaf to use keccak_256
old_func = """    const capPayload = Buffer.concat([
      subAgentSigner.toBuffer(),
      amountBuf,
      expiryBuf,
      nonceBuf,
    ]);
    const leafCapability = crypto.createHash("sha256").update(capPayload).digest();

    return crypto.createHash("sha256").update(
      Buffer.concat([leafCapability, whitelistedMerchantAta.toBuffer()])
    ).digest();"""

new_func = """    const capPayload = Buffer.concat([
      subAgentSigner.toBuffer(),
      amountBuf,
      expiryBuf,
      nonceBuf,
    ]);
    // Keccak256 strictly matching solana_program::keccak::hashv in haichain-core
    const leafCapability = Buffer.from(keccak_256(capPayload));

    return Buffer.from(
      keccak_256(Buffer.concat([leafCapability, whitelistedMerchantAta.toBuffer()]))
    );"""

if old_func in code:
    code = code.replace(old_func, new_func)
    with open(sdk_file, "w", encoding="utf-8") as f:
        f.write(code)
    print("Successfully updated computeCompositeCapabilityLeaf to Keccak-256")
else:
    print("Could not find old_func in code")
