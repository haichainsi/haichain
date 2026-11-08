with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re, sys
for m in re.finditer(r'data-i18n="advantages\.item\dTitle">\s*([^<]+)', c):
    sys.stdout.buffer.write((m.group(1).strip() + '\n').encode('utf-8'))
