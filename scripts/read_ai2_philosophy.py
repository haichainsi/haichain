# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(805, 835):
    print(f'{i+1}: {lines[i]}', end='')
print('...')
for i in range(900, 925):
    print(f'{i+1}: {lines[i]}', end='')
