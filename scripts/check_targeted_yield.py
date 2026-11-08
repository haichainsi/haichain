import os, re

files_to_check = ['index.html', 'dashboard.html', 'i18n.js']
for fname in files_to_check:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        matches = re.findall(r'(?:40%|real yield)', c, re.I)
        print(f'{fname}: {len(matches)} matches')
        for m in re.finditer(r'(?:40%|real yield)', c, re.I):
            start = max(0, m.start() - 30)
            end = min(len(c), m.end() + 30)
            print("  ", c[start:end].replace('\n', ' '))
