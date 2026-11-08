import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

keys = ['tech.done1', 'tech.done2', 'roadmap.stage1Item1', 'footer.certified']
for k in keys:
    matches = re.findall(rf'"{re.escape(k)}":\s*"([^"]*)"', c)
    print(f'{k}: {len(matches)} occurrences, sample: {matches[0] if matches else None}')
