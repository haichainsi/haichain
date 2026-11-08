with open('tests/haichain-phase2-ai-gateway.test.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines:", len(lines))
for i in range(max(0, len(lines)-60), len(lines)):
    print(f"L{i+1}: {lines[i]}", end='')
