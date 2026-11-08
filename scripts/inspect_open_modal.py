with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'window\.open\w+', c)]
for pos in matches:
    print(c[pos:pos+300])
    print('='*50)
