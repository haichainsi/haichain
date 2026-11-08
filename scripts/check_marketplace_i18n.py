import sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('app/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Look for marketplace keys in i18n
print("Finding marketplace in i18n.js...")
for m in re.finditer(r'marketplace', content):
    print(content[max(0, m.start()-30):min(len(content), m.end()+100)])
    break
