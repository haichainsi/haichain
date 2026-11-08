import re
from bs4 import BeautifulSoup, Comment

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
body = soup.find('body')

# Remove comments
for c in body.find_all(text=lambda text: isinstance(text, Comment)):
    c.extract()

untranslated = []
for tag in body.find_all(True):
    if tag.name in ['script', 'style', 'svg', 'path', 'code']:
        continue
    if tag.get('data-i18n'):
        continue
    for child in tag.children:
        if isinstance(child, str):
            text = child.strip()
            if len(text) > 2 and not text.startswith('$') and not re.match(r'^[0-9\.\,\s\/\%\+\-\:\*\#\(\)]+$', text):
                # Check ancestor
                has_ancestor = False
                p = tag
                while p and p.name != 'body':
                    if p.get('data-i18n'):
                        has_ancestor = True
                        break
                    p = p.parent
                if not has_ancestor:
                    untranslated.append((tag.name, tag.get('id', ''), tag.get('class', []), text))

print(f"Total REAL untranslated text nodes: {len(untranslated)}")
for t in untranslated:
    print(f"<{t[0]} id='{t[1]}'>: {t[3]}")
