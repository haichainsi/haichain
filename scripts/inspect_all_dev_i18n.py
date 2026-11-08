import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract TRANSLATIONS object
start = text.find('const TRANSLATIONS = {')
end = text.rfind('};')
trans_str = text[start + len('const TRANSLATIONS = '):end + 1]

# Let's inspect dev keys in all languages
import re
langs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he']
for lang in langs:
    pos = text.find(f'"{lang}": {{')
    next_pos = text.find('};\n', pos) if pos != -1 else -1
    print(f"\n================ LANG: {lang} ================")
    if pos != -1:
        block = text[pos:pos+2500]
        for line in block.splitlines()[:25]:
            if any(k in line for k in ['dev.', 'mcp.', 'nav.devHub']):
                print(line.strip())
