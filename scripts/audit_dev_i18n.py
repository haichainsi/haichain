import re

with open("app/i18n.js", "r", encoding="utf-8") as f:
    text = f.read()

all_dev_keys = sorted(list(set(re.findall(r'"(dev\.[a-zA-Z0-9_]+)"\s*:', text))))
print("Total unique dev keys:", len(all_dev_keys))
for k in all_dev_keys:
    print("  ", k)

langs = ['kk', 'en', 'zh', 'fr', 'ko', 'es', 'ru', 'vi', 'hi', 'he']
for l in langs:
    l_marker = '"' + l + '": {'
    pos1 = text.find(l_marker)
    if pos1 == -1:
        print("Lang not found:", l)
        continue
    # find next
    next_pos = len(text)
    for l2 in langs:
        if l2 != l:
            p = text.find('"' + l2 + '": {', pos1 + len(l_marker))
            if p != -1 and p < next_pos:
                next_pos = p
    sub = text[pos1:next_pos]
    missing = [k for k in all_dev_keys if f'"{k}":' not in sub]
    print(f"Lang {l:2s}: has {len(all_dev_keys)-len(missing)}/{len(all_dev_keys)}. Missing: {missing}")
