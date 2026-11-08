import re

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

keys = re.findall(r'"(dev\.[^"]+)"', text)
print(f"Total dev keys found: {len(keys)}")
for k in sorted(set(keys))[:20]:
    print(" ", k)
