import glob

terms = [
    '100% Exploit Immune',
    '100% Cryptographic',
    '142x',
    '50x - 140x',
    '15.9M',
    'Bittensor',
    'Render / io.net',
    'ElizaOS'
]

md_files = glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')
print(f"Scanning {len(md_files)} Whitepaper markdown files...\n")

for f in sorted(md_files):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    matches = []
    for t in terms:
        if t.lower() in content.lower():
            matches.append(t)
    if matches:
        print(f"[{f}] FOUND: {matches}")
    else:
        print(f"[{f}] CLEAN: No red flags.")
