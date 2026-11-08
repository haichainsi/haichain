import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

corruptions = [
    ('\x07lpha', 'alpha with bell'),
    (' lpha', ' lpha'),
    ('\x0cac', 'frac with formfeed'),
    ('\rac', 'frac with cr'),
    ('rac{', 'rac{'),
    ('\right', 'right with cr'),
    ('ight)', 'ight)'),
    ('ight]', 'ight]'),
    ('ight\\|', 'ight|'),
    ('eg\\text', 'eg\\text'),
    ('eg \text', 'eg \text'),
    ('imes', 'imes'),
    ('ceil', 'ceil'),
    ('floor', 'floor'),
]

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    found = []
    for pattern, name in corruptions:
        if pattern in text:
            found.append(name)
    if found:
        print(f"{fname}: {found}")
