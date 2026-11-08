# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(1000, 1150):
    if i < len(lines):
        line = lines[i].strip()
        if '<section' in line or '</section>' in line or 'id=' in line:
            print(f'{i+1}: {line[:100]}')
