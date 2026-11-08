with open('sdk/typescript/src/capleaf.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines in capleaf.ts:", len(lines))
for i in range(min(80, len(lines))):
    print(f"L{i+1}: {lines[i]}", end='')
