with open('packages/agent-pay/src/index.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(295, 360):
    if i < len(lines):
        print(f"L{i+1}: {lines[i]}", end='')
