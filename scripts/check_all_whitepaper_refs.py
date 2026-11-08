import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or '__pycache__' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.js')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fl:
                c = fl.read()
                matches = re.findall(r'HAICHAIN_WHITEPAPER[^\'"\s]+', c)
                if matches:
                    print(f'{path}: {set(matches)}')
