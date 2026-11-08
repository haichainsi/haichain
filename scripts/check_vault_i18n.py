with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'"(vault\.[^"]+)"', c)
print('Unique vault keys in i18n:', set(matches))
