with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
en_match = re.search(r'"en":\s*\{([\s\S]*?)\n\s*\},', text)
if en_match:
    lines = [l for l in en_match.group(1).split('\n') if 'aiHub' in l]
    print(f"Found {len(lines)} aiHub keys in 'en':")
    for l in lines:
        print(" ", l.strip())
