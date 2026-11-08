import os
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.js') or f.endswith('.html'):
            p = os.path.join(root, f)
            try:
                t = open(p, encoding='utf-8').read()
                if 'HAICHAIN_ACTIVE_SAFT' in t:
                    print(f'{p}')
            except:
                pass
