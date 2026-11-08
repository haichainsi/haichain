with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'apply(' in l or 'applyTranslations' in l or 'data-i18n' in l:
        print(f"L{idx}: {l.strip()}")
        for j in range(idx, min(idx + 30, len(lines))):
            print(f"  L{j+1}: {lines[j].rstrip()}")
        break
