# -*- coding: utf-8 -*-
import os

target = '"version": "6.9.3"'
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['.git', 'node_modules', '__pycache__', '.gemini']):
        continue
    for f in files:
        if f.endswith(('.js', '.json', '.toml', '.txt')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if target in c:
                    print(p)
