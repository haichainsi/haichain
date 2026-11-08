# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'"ai2\.badge":\s*"([^"]+)"', text)
for m in matches:
    print('-', m)
