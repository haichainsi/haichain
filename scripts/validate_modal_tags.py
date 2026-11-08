import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['dashboard.html', 'app/dashboard.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    s_idx = text.find('<div id="wallet-connect-modal"')
    e_idx = text.find('<div id="wallet-account-modal"')
    modal_str = text[s_idx:e_idx]

    tags = re.findall(r'(</?([a-zA-Z0-9]+)[^>]*>)', modal_str)
    stack = []
    has_err = False
    for full, name in tags:
        if full.endswith('/>') or name in ['input', 'img', 'br', 'hr']:
            continue
        if full.startswith('</'):
            if stack and stack[-1] == name:
                stack.pop()
            else:
                print(f"[{fpath}] ERROR: Mismatched tag {full}, top of stack was {stack[-1] if stack else 'EMPTY'}")
                has_err = True
        else:
            stack.append(name)

    if not has_err and not stack:
        print(f"[{fpath}] PERFECT: All tags matched and closed cleanly!")
    elif stack:
        print(f"[{fpath}] Unclosed tags: {stack}")
