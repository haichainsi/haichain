import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

keywords = [
    'việt nam', 'vietnam', 'viet nam', 'đông nam á', 'southeast asia', 'asia', 'châu á',
    'instant qr', 'mã qr', 'qr code', 'vietqr', 'qr'
]

for fname in sorted(glob.glob("HAICHAIN_WHITEPAPER_V1.0_*.md")):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    matches = []
    for i, line in enumerate(lines):
        line_lower = line.lower()
        for kw in keywords:
            if kw in line_lower:
                # Exclude purely language indicator like "(Tiếng Việt)"
                if kw in ['việt nam', 'vietnam', 'viet nam'] and ('tiếng việt' in line_lower or 'phiên bản tiếng việt' in line_lower or 'bản tiếng việt' in line_lower):
                    continue
                matches.append((i + 1, kw, line.strip()))
                break
    
    print(f"=== {fname} ({len(matches)} matches) ===")
    for line_num, kw, txt in matches:
        print(f"  Line {line_num} [{kw}]: {txt[:120]}")
