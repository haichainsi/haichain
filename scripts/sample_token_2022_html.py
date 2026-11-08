import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Only search within the HTML markup before the main <script> tag
script_pos = c.find('<script>')
html_body = c[:script_pos]

for m in re.finditer(r'Token[ -]2022', html_body):
    start = max(0, m.start() - 50)
    end = min(len(html_body), m.end() + 50)
    print(html_body[start:end].replace('\n', ' '))
