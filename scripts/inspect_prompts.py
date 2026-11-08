import re, sys

with open("app/i18n.js", "r", encoding="utf-8") as f:
    text = f.read()

langs = ['kk', 'en', 'zh', 'fr', 'ko', 'es', 'ru', 'vi', 'hi', 'he']
for l in langs:
    l_marker = '"' + l + '": {'
    pos1 = text.find(l_marker)
    next_pos = len(text)
    for l2 in langs:
        if l2 != l:
            p = text.find('"' + l2 + '": {', pos1 + len(l_marker))
            if p != -1 and p < next_pos:
                next_pos = p
    sub = text[pos1:next_pos]
    p1 = re.search(r'"dev\.sec2Prompt1":\s*"((?:\\.|[^"\\])*)"', sub)
    p2 = re.search(r'"dev\.sec2Prompt2":\s*"((?:\\.|[^"\\])*)"', sub)
    p3 = re.search(r'"dev\.sec2Prompt3":\s*"((?:\\.|[^"\\])*)"', sub)
    sys.stdout.buffer.write(f"=== {l.upper()} ===\n".encode('utf-8'))
    if p1: sys.stdout.buffer.write(f"  P1: {p1.group(1)}\n".encode('utf-8'))
    if p2: sys.stdout.buffer.write(f"  P2: {p2.group(1)}\n".encode('utf-8'))
    if p3: sys.stdout.buffer.write(f"  P3: {p3.group(1)}\n".encode('utf-8'))
