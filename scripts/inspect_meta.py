import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

# search for document.title or meta in i18n.js
for line in text.splitlines():
    if 'document.title' in line or 'meta' in line.lower() and ('description' in line.lower() or 'og:' in line.lower()):
        print(line.strip())
