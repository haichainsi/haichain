with open('server/tee-cosigner.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(50, 110):
    if i < len(lines):
        print(f"L{i+1}: {lines[i]}", end='')
