import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()[:60]
for i, l in enumerate(lines):
    print(f'{i+1}: {l.rstrip()}')
