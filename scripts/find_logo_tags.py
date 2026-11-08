import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'<[^>]+(?:logo|brand)[^>]+>', c[:15000], re.I)
for m in matches[:10]:
    print(m)
