# -*- coding: utf-8 -*-
with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(4850, 5020):
    if i < len(lines):
        line = lines[i]
        if 'data-i18n' in line or 'applyLanguage' in line or 'changeLanguage' in line or 'translate' in line:
            print(f'{i+1}: {line.strip()[:100]}')
