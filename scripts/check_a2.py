import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    matches = re.findall(r'(\$?[Aa]\^\{?2\}?\$?)', text)
    if matches:
        print(f"{fname}: {matches}")
