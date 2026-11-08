import re

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect vi and en dev keys
for lang in ['en', 'vi']:
    m = re.search(r'\b' + lang + r':\s*\{([^}]+dev\.sec1Title[^\}]+)\}', text)
    if m:
        block = m.group(1)
        for line in block.splitlines():
            if 'dev.' in line:
                print(f"[{lang}] {line.strip()[:100]}")
