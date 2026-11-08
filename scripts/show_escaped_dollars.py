import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    matches = [m.start() for m in re.finditer(r'\\\$', text)]
    if matches:
        print(f"=== {fname} ({len(matches)}) ===")
        for pos in matches[:8]:
            snippet = text[max(0, pos-20):min(len(text), pos+30)].replace('\n', ' ')
            print(f"   ...{snippet}...")
