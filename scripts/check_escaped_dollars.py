import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Find all instances of \$
    escaped_dollars = re.findall(r'\\\$', text)
    print(f"{fname}: {len(escaped_dollars)} occurrences of \\$")
