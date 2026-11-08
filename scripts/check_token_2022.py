import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['dashboard.html', 'index.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    matches = re.findall(r'Token[ -]2022', c)
    print(f'{fname}: {len(matches)} occurrences of Token-2022')
