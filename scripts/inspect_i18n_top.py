with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines[:100], 1):
    if 'TRANSLATIONS' in l or 'const ' in l or 'var ' in l:
        print(f"L{idx}: {l.strip()}")
