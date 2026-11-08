import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'saft|contract|sign', c, re.IGNORECASE)]
print(f'Total matches: {len(matches)}')
found = set()
for pos in matches:
    snippet = c[max(0, pos-40):min(len(c), pos+60)]
    for word in ['openSaft', 'openPreseed', 'signSaft', 'saftDrawer', 'saft-modal', 'preseed']:
        if word.lower() in snippet.lower():
            found.add(snippet.strip().replace('\n', ' '))
for s in list(found)[:15]:
    print('-', s)
