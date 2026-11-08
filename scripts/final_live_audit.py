import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')

def test_url(url, checks):
    print(f'=== Testing {url} ===')
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
    all_passed = True
    for label, fn in checks.items():
        ok = fn(content)
        if not ok: all_passed = False
        status = 'PASS' if ok else 'FAIL'
        print(f'  [{status}] {label}')
    return all_passed

p1 = test_url('https://haichain.si/?t=final_check', {
    'Coinbase AgentKit present': lambda c: 'Coinbase AgentKit (x402)' in c,
    'Skyfire Protocol present': lambda c: 'Skyfire Protocol' in c,
    'Stripe Legacy Rails present': lambda c: 'Stripe / Legacy Rails' in c,
    '15/15 Test Vectors present': lambda c: '15/15 Test Vectors Verified' in c,
    '100% Exploit Immune removed': lambda c: '100% Exploit Immune' not in c,
    '50x - 140x removed': lambda c: '50x - 140x' not in c,
    'Whitepaper direct href present': lambda c: '/HAICHAIN_WHITEPAPER_V1.0_EN.pdf' in c
})

p2 = test_url('https://haichain.si/dashboard.html?t=final_check', {
    'v29 cache buster present': lambda c: 'v29_institutional_audit_upgrade' in c,
    '100% capital safety removed': lambda c: '100% capital safety' not in c,
    '0.14ms Netting clarified': lambda c: '0.14ms (Netting)' in c
})

p3 = test_url('https://haichain.si/app/sale-controller.js?v=v29', {
    '142x Multiple removed': lambda c: '142x Multiple' not in c,
    '28.5M Ticks present': lambda c: '28.5M Ticks' in c,
    'Micro-Tx Capacity present': lambda c: 'Micro-Tx Capacity' in c
})

print(f'\nOVERALL AUDIT RESULT: {"ALL CHECKS PASSED 100%" if (p1 and p2 and p3) else "SOME CHECKS FAILED"}')
