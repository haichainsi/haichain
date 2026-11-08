with open('scripts/gdocs.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
links = re.findall(r'<link[^>]+>', text)
for l in links:
    print(l)
