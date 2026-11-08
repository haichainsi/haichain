with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'function t(' in l or 'const t =' in l or 'let t =' in l:
        print(f"L{idx}: {l.strip()}")
        for j in range(idx, min(idx + 30, len(lines))):
            print(f"  L{j+1}: {lines[j].rstrip()}")
        break
