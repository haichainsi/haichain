with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'HAICHAIN_ACTIVE_SAFT|HAICHAIN_SIGNED', c)]
for pos in matches:
    print(c[pos-200:pos+400])
    print('='*50)
