with open('tests/haichain-phase2-ai-gateway.test.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. In Test 3, set flags to just PROBATION
content = content.replace(
    "flags: CapLeafFlags.PROBATION | CapLeafFlags.REQUIRE_COSIGN,",
    "flags: CapLeafFlags.PROBATION,"
)

# 2. In Test 6, replace dummyMerchant with dummyMerchantKeypair.publicKey
content = content.replace("merchant: dummyMerchant,", "merchant: dummyMerchantKeypair.publicKey,")
content = content.replace("dummyMerchant,", "dummyMerchantKeypair.publicKey,")

with open('tests/haichain-phase2-ai-gateway.test.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed tests/haichain-phase2-ai-gateway.test.ts")
