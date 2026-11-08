import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'fetch\([\'"`][^\'"`]*api[^\'"`]*[\'"`]', text)
for m in set(matches):
    print(m)
