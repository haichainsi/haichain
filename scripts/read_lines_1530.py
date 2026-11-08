# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(1530, 1560):
    print(f'{i+1}: {lines[i]}', end='')
