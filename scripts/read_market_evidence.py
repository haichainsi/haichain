# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(915, min(len(lines), 960)):
    print(f'{i+1}: {lines[i]}', end='')
