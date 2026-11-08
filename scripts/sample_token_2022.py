import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

for m in re.finditer(r'Token[ -]2022', c):
    start = max(0, m.start() - 40)
    end = min(len(c), m.end() + 40)
    print(c[start:end].replace('\n', ' '))
    if m.start() > 100000:
        break
