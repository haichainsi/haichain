import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Scripts in dashboard.html matching sale-controller:")
for m in re.finditer(r'src=["\'][^"\']*sale-controller[^"\']*["\']', text):
    print(m.group(0))
