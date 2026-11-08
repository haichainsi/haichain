import os, re

files = ['dashboard.html', 'index.html', 'sale-controller.js', 'i18n.js']
for fname in files:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, l in enumerate(lines):
        if re.search(r'kết\s*nối.*ví|connect.*wallet|ví\s*web3', l, re.IGNORECASE):
            print(f"{fname}:{idx+1}: {l.strip()[:110]}")
