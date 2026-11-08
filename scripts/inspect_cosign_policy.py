with open('sdk/typescript/src/policy-engine.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'flags' in l or 'REQUIRE_COSIGN' in l or 'cosign' in l:
        print(f"L{i+1}: {l.strip()}")
