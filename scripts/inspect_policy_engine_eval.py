with open('sdk/typescript/src/policy-engine.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(85, 140):
    if i < len(lines):
        print(f"L{i+1}: {lines[i]}", end='')
