with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re

for l in ['kk', 'en', 'zh', 'fr', 'ko', 'es', 'ru', 'vi', 'hi', 'he']:
    pos = c.find(f'"{l}": {{\n')
    assert pos != -1, f"Missing {l}"
    # find where the injected keys end
    lines = c[pos:pos+10000].split('\n')
    injected_count = 0
    for line in lines[1:]:
        if any(line.strip().startswith(f'"{p}') for p in ['advantages.', 'agenticShift.']):
            injected_count += 1
        else:
            break
    print(f"Lang {l}: found {injected_count} consecutive injected keys right after declaration")
