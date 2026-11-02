# -*- coding: utf-8 -*-
import os

target = "pathname === '/'"
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['.git', 'node_modules', '__pycache__', '.gemini']):
        continue
    for f in files:
        if f.endswith('.js'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for i, l in enumerate(fp):
                    if target in l:
                        print(f'{p}:{i+1}: {l.strip()}')
