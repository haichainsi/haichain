import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"=== {fname} ===")
    for i, line in enumerate(lines):
        if any(c in line for c in ['rac{', 'ight)', '\x07lpha', 'ceil', 'floor']):
            # Filter out genuine english words like 'times', 'ceiling', etc.
            if 'frac{' not in line or 'right)' not in line or 'alpha' not in line:
                print(f"  Line {i+1}: {repr(line.strip())}")
