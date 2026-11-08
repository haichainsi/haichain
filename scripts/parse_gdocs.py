import re

with open('scripts/gdocs.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<[^>]+>', text):
    snippet = m.group(0)
    if any(k in snippet.lower() for k in ['popout', 'target="_blank"', 'viewer-icon', 'drive-viewer-toolstrip']):
        print(snippet)
