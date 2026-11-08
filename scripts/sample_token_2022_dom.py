import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

script_pos = c.find('<script>')
script_body = c[script_pos:]

for m in re.finditer(r'Token[ -]2022', script_body):
    start = max(0, m.start() - 60)
    end = min(len(script_body), m.end() + 60)
    snippet = script_body[start:end].replace('\n', ' ')
    if 'innerHTML' in snippet or 'textContent' in snippet or '`' in snippet or '"' in snippet:
        print(snippet)
