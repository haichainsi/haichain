with open('sale-controller.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'currentLang' in l or 'getLanguage' in l or 'languageChanged' in l or 'lang =' in l:
        print(f"L{idx}: {l.strip()}")
