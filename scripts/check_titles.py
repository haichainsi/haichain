import re, sys

with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('"en": {')
block = c[pos:pos+4000]
for i in range(1, 5):
    m = re.search(rf'"advantages\.item{i}Title":\s*"([^"]+)"', block)
    if m:
        sys.stdout.buffer.write(f"EN item{i}Title: {m.group(1)}\n".encode('utf-8'))
