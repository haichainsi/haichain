import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'data-i18n=["\'](hero\.[^"\']+)["\']', text):
    pos = m.start()
    line_num = text[:pos].count('\n') + 1
    snippet = text[max(0, pos-80):min(len(text), pos+160)].replace('\n', ' ')
    print(f'Line {line_num}: {m.group(1)} | {snippet}')
