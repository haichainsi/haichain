import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')

wps = sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md'))
for wp in wps:
    with open(wp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # search for chapter 8.2 or 40% or real yield
    matches = re.findall(r'.{0,60}(?:40%|real yield|rendimiento real|rendement réel|доходност|실제 수익|真实收益).{0,60}', content, re.IGNORECASE)
    print(f"\n=== {wp} (Matches: {len(matches)}) ===")
    for m in matches[:6]:
        print("  ...", m.strip().replace('\n', ' '), "...")
