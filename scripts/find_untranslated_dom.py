import re
from bs4 import BeautifulSoup

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all tags in body
body = soup.find('body')
if not body:
    print("No body found")
    exit()

# Traverse elements and find text nodes that are not inside <script> or <style>
# and check if the element or any ancestor has data-i18n
untranslated_texts = []

for tag in body.find_all(True):
    if tag.name in ['script', 'style', 'svg', 'path', 'code']:
        continue
    # If the tag itself has data-i18n, its children are replaced by i18n
    if tag.get('data-i18n'):
        continue
    # If an ancestor has data-i18n, it will be replaced by i18n (unless ancestor's translation contains html)
    # Check direct text children
    for child in tag.children:
        if isinstance(child, str):
            text = child.strip()
            if len(text) > 2 and not text.startswith('{') and not text.startswith('$') and not text.isdigit():
                # Check if this tag has an ancestor with data-i18n
                has_i18n_ancestor = False
                p = tag
                while p and p.name != 'body':
                    if p.get('data-i18n'):
                        has_i18n_ancestor = True
                        break
                    p = p.parent
                if not has_i18n_ancestor:
                    untranslated_texts.append((tag.name, tag.get('id', ''), tag.get('class', []), text))

print(f"Total untranslated text nodes found: {len(untranslated_texts)}")
for item in untranslated_texts[:50]:
    print(f"<{item[0]} id='{item[1]}'>: {item[3][:80]}")

with open('scripts/untranslated_dom_nodes.txt', 'w', encoding='utf-8') as out:
    for item in untranslated_texts:
        out.write(f"<{item[0]} id='{item[1]}' class='{' '.join(item[2])}'>: {item[3]}\n")
