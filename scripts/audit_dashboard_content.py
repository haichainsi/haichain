import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

print(f"dashboard.html size: {len(dash)} bytes")

# Check all terms flagged by Claude
checks = [
    'production certified',
    'audited',
    '100% completed',
    'early backer',
    'fiat',
    'apple pay',
    'google pay',
    'credit card',
    'sandbox',
    'simulated',
    'vasp',
    'devnet',
    'mainnet',
    'ottersec',
    'neodyme',
    'unit test',
    'invariants',
    '72/72',
    'tau',
    '400ms',
    '0.05%',
    'mpp',
    'x402',
    'byok',
    'tee'
]

print("=== TERM FREQUENCY IN DASHBOARD.HTML ===")
for term in checks:
    count = len(re.findall(re.escape(term), dash, re.IGNORECASE))
    print(f"  '{term}': {count} occurrences")
