# -*- coding: utf-8 -*-
with open('i18n.js', 'r', encoding='utf-8') as f:
    for i, l in enumerate(f):
        if 'setLanguage' in l or 'applyLanguage' in l or 'data-i18n' in l:
            print(f'{i+1}: {l.strip()[:100]}')
