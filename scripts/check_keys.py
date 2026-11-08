import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()
matches = re.findall(r'"marketplace\.catAll":\s*"([^"]+)"', c)
for idx, m in enumerate(matches):
    print(idx, m)
