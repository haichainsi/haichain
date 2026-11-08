import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_lang = None
for i, line in enumerate(lines):
    m = re.match(r'^\s*"([a-z]{2})":\s*\{\s*$', line)
    if m:
        current_lang = m.group(1)
    if current_lang and any(k in line for k in ['"hero.badge"', '"hero.title"', '"hero.subtitle"', '"meta.title"', '"meta.description"']):
        print(f'{current_lang} | Line {i+1}: {line.strip()[:90]}')
