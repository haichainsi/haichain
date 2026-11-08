import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
keys = ['syncRegistriesShort', 'devDocsBtn', 'marketplace.badge', 'marketplace.title']
for k in keys:
    matches = [m.start() for m in re.finditer(k, c)]
    for pos in matches[:3]:
        print(f"Key {k}:", c[pos-20:pos+120].replace('\n', ' '))
