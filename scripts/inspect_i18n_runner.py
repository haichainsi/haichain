# -*- coding: utf-8 -*-
with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines[:100]):
    if 'function' in l or 'apply' in l or 'update' in l:
        print(f'{i+1}: {l.strip()[:100]}')
for i, l in enumerate(lines[-150:]):
    line_num = len(lines) - 150 + i + 1
    if 'function' in l or 'data-i18n' in l or 'addEventListener' in l or 'switch' in l:
        print(f'{line_num}: {l.strip()[:100]}')
