import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Search for variations of AI^2, $AI^2$, $A^2$, $\mathbf{AI^2}$, etc.
    ai2_matches = re.findall(r'(\$?A(?:I)?\^\{?2\}?\$?|\$\\mathbf\{AI\^2\}\$|\$\\mathbf\{A\^2\}\$)', text)
    
    # 2. Search for escaped dollar signs e.g. \$0.0001
    esc_dollars = re.findall(r'\\\$[0-9]+(?:\.[0-9]+)?', text)
    
    # 3. Check for raw LaTeX math
    raw_latex = re.findall(r'(\$\$.*?\$\$|\$[a-zA-Z\\]+.*?\$)', text)
    
    print(f"=== {fname} ===")
    print(f"  AI^2 variants: {len(ai2_matches)} -> {set(ai2_matches)}")
    print(f"  Escaped dollars (\\$...): {len(esc_dollars)} (sample: {esc_dollars[:5]})")
    print(f"  Raw LaTeX count: {len(raw_latex)}")
