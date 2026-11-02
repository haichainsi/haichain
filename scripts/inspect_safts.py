import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

saft_files = sorted(glob.glob('HAICHAIN_PRESEED_SAFT_AGREEMENT_*.md'))
print(f"Total SAFT files: {len(saft_files)}")

for sf in saft_files:
    with open(sf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check lines around veHAI or staking
    lines = content.split('\n')
    print(f"\n--- {sf} ---")
    for idx, line in enumerate(lines):
        if any(w in line.lower() for w in ['vehại', 'vehai', 'real yield', 'cash flow', 'usdt', 'stak']):
            print(f"L{idx+1}: {line}")
