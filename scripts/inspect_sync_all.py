import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer('"marketplace.syncRegistriesShort"', c)]
for pos in matches:
    print(c[pos-20:pos+150].replace('\n', ' '))
