import sys

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
for m in re.finditer(r'.{0,40}\U0001f449.{0,80}', c):
    sys.stdout.buffer.write(b"Match in index.html: " + m.group(0).encode('utf-8') + b"\n")

with open('i18n.js', 'r', encoding='utf-8') as f:
    js = f.read()

for m in re.finditer(r'.{0,40}\U0001f449.{0,80}', js):
    sys.stdout.buffer.write(b"Match in i18n.js: " + m.group(0).encode('utf-8') + b"\n")
