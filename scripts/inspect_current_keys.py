import json, re, sys

with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

keys = [
    'agenticShift.badge', 'agenticShift.title', 'agenticShift.subtitle',
    'agenticShift.card1Title', 'agenticShift.card1Desc',
    'agenticShift.card2Title', 'agenticShift.card2Desc',
    'agenticShift.card3Title', 'agenticShift.card3Desc',
    'advantages.badge', 'advantages.title', 'advantages.subtitle',
    'advantages.item1Title', 'advantages.item1Rival', 'advantages.item1Hai',
    'advantages.item2Title', 'advantages.item2Rival', 'advantages.item2Hai',
    'advantages.item3Title', 'advantages.item3Rival', 'advantages.item3Hai',
    'advantages.item4Title', 'advantages.item4Desc'
]

# find within "vi": {
vi_idx = c.find('"vi": {')
block_vi = c[vi_idx:vi_idx+8000]

for k in keys:
    m = re.search(r'"' + re.escape(k) + r'":\s*"([^"]+)"', block_vi)
    if m:
        line = f"[{k}] => {m.group(1)}\n"
        sys.stdout.buffer.write(line.encode('utf-8'))
