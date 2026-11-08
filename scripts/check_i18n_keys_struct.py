# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    s = l.strip()
    if s.endswith(': {') and (s.startswith("'") or s.startswith('"')):
        print(f'{i+1}: {s}')
