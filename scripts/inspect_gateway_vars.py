with open('tests/haichain-phase2-ai-gateway.test.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Top 35 lines:")
for i in range(min(35, len(lines))):
    print(f"L{i+1}: {lines[i]}", end='')

print("\nLines 110-140:")
for i in range(110, 140):
    if i < len(lines):
        print(f"L{i+1}: {lines[i]}", end='')
