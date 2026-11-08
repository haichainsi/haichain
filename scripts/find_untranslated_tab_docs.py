import sys
from bs4 import BeautifulSoup

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
tab_docs = soup.find('section', {'id': 'tab-docs'})

if not tab_docs:
    print("tab-docs not found!")
    exit(1)

untranslated = []
for el in tab_docs.descendants:
    if el.name in ['script', 'style', 'code', 'pre']:
        continue
    if hasattr(el, 'contents') and len(el.contents) == 1 and isinstance(el.contents[0], str):
        text = el.text.strip()
        if len(text) > 3 and not el.has_attr('data-i18n'):
            parent_names = [p.name for p in el.parents]
            if 'pre' in parent_names or 'code' in parent_names:
                continue
            untranslated.append((el.name, text))

with open('scripts/untranslated_nodes.txt', 'w', encoding='utf-8') as out:
    out.write(f"Total untranslated text nodes in tab-docs: {len(untranslated)}\n")
    for tag, txt in untranslated:
        out.write(f"[{tag}]: {txt}\n")

print(f"Total untranslated: {len(untranslated)}")
