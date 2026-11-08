with open('tests/haichain-phase2-ai-gateway.test.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "  CapLeafV1,\n  CapLeafFlags,",
    "  CapLeafV1,\n  CapLeafV1Engine,\n  CapLeafFlags,"
)

with open('tests/haichain-phase2-ai-gateway.test.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added CapLeafV1Engine import to tests/haichain-phase2-ai-gateway.test.ts")
