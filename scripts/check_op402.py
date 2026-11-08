import re, sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['HAICHAIN_WHITEPAPER_V1.0_EN.md', 'HAICHAIN_WHITEPAPER_V1.0_VI.md']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    matches = re.findall(r'.*OP_402_PAY.*', c)
    print(f"=== {fname} ===")
    for m in matches[:10]:
        print(" ", m)
