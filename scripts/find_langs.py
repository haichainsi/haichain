import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    m = re.match(r'^\s*"([a-z]{2})":\s*\{\s*$', l)
    if m:
        print(f'Line {i+1}: Lang {m.group(1)}')
