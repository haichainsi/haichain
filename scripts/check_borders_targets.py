import re

files = ['dashboard.html', 'app/dashboard.html', 'sale-controller.js', 'app/sale-controller.js']

print("Checking targets:")
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Check VIP gatekeeper
    gatekeeper_matches = re.findall(r'<div[^>]*rounded-3xl[^>]*border[^>]*>[^<]*<div[^>]*rounded-2xl[^>]*>[^<]*<i data-lucide="shield-check"', c)
    # Check Vesting Vault
    vesting_matches = re.findall(r'<div[^>]*rounded-3xl border border-neutral-200/60[^>]*>', c)
    # Check divider lines
    divider1 = c.count('border-t border-neutral-100 dark:border-neutral-800/80')
    divider2 = c.count('border-b border-neutral-100 dark:border-white/[0.04]')
    
    print(f"\n{f}:")
    print(f"  VIP Gatekeeper box matches: {len(gatekeeper_matches)}")
    print(f"  Vesting Vault container matches: {len(vesting_matches)}")
    print(f"  VIP divider line (border-t) matches: {divider1}")
    print(f"  Vesting divider line (border-b) matches: {divider2}")
