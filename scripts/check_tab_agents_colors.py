with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('id="tab-agents"')
e = c.find('id="tab-playground"')
tab = c[s:e] if s != -1 and e != -1 else ''

import re
matches = [(m.start(), tab[max(0, m.start()-50):min(len(tab), m.start()+50)]) for m in re.finditer(r'(emerald|green-\d+|teal-\d+)', tab)]
print(f'Found {len(matches)} occurrences in tab-agents:')
for pos, snippet in matches:
    print(snippet.replace('\n', ' '))
