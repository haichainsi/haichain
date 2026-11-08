import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if any(k in l for k in ['"hero.badge"', '"hero.title"', '"hero.subtitle"']):
        print(f'{i+1}: {l.strip()[:140]}')
