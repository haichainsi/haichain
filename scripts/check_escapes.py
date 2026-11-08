import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Check for \ followed by non-alpha (like \$, \-, \", \_, etc.)
    non_alpha_escapes = re.findall(r'\\[^a-zA-Z\s]', text)
    from collections import Counter
    c = Counter(non_alpha_escapes)
    print(f"{fname}: {c}")
