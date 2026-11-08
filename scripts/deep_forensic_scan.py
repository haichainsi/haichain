import urllib.request, time, re, sys
sys.stdout.reconfigure(encoding='utf-8')

ts = int(time.time())
print(f"=== DEEP FORENSIC SCAN ON LIVE HAICHAIN.SI ({ts}) ===\n")

# 1. SCAN HOMEPAGE
url_home = f"https://haichain.si/?t={ts}"
req_home = urllib.request.Request(url_home, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
with urllib.request.urlopen(req_home) as resp:
    home_html = resp.read().decode('utf-8', errors='ignore')

red_flags = [
    '100% Exploit Immune',
    '100% Cryptographic Immunity',
    '15/15 Audits Passed',
    '142x',
    '50x - 140x',
    '$15.9M ARR',
    'Bittensor ($TAO)',
    'Render / io.net',
    'ElizaOS / Virtuals'
]

print("1. HOMEPAGE RED FLAGS CHECK:")
all_cleared = True
for rf in red_flags:
    found = rf in home_html
    if found: all_cleared = False
    status = "CLEARED" if not found else "DETECTED"
    print(f"   [{status}] \"{rf}\"")

# 2. SCAN NEW COMPETITORS ON HOMEPAGE
new_features = [
    'Coinbase AgentKit (x402)',
    'Skyfire Protocol',
    'Stripe / Legacy Rails',
    '15/15 Test Vectors Verified',
    'Formally Verified Sub-PDA Invariants'
]

print("\n2. HOMEPAGE INSTITUTIONAL UPGRADES:")
for nf in new_features:
    found = nf in home_html
    status = "VERIFIED LIVE" if found else "MISSING"
    print(f"   [{status}] \"{nf}\"")

# 3. SCAN DASHBOARD
url_dash = f"https://haichain.si/dashboard.html?t={ts}"
req_dash = urllib.request.Request(url_dash, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
with urllib.request.urlopen(req_dash) as resp:
    dash_html = resp.read().decode('utf-8', errors='ignore')

dash_checks = [
    ('100% capital safety removed', '100% capital safety' not in dash_html),
    ('0.14ms Netting clarified', '0.14ms (Netting)' in dash_html),
    ('Emergency Stop present', 'Emergency Stop' in dash_html or 'emergency' in dash_html.lower())
]

print("\n3. DASHBOARD VERIFICATION:")
for label, ok in dash_checks:
    status = "PASS" if ok else "FAIL"
    print(f"   [{status}] {label}")

# 4. SCAN SALE CONTROLLER (CALCULATOR)
url_sale = f"https://haichain.si/app/sale-controller.js?t={ts}"
req_sale = urllib.request.Request(url_sale, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
with urllib.request.urlopen(req_sale) as resp:
    sale_js = resp.read().decode('utf-8', errors='ignore')

sale_checks = [
    ('142x Multiple removed', '142x Multiple' not in sale_js),
    ('142x Projected Multiple removed', '142x Projected Multiple' not in sale_js),
    ('28.5M Ticks present', '28.5M Ticks' in sale_js),
    ('Micro-Tx Capacity present', 'Micro-Tx Capacity' in sale_js),
    ('l1Value computation uses 200 ticks multiplier', 'executionCapacity = Math.round(totalTokens * 200)' in sale_js)
]

print("\n4. TERMINAL CALCULATOR VERIFICATION:")
for label, ok in sale_checks:
    status = "PASS" if ok else "FAIL"
    print(f"   [{status}] {label}")

# 5. SCAN MULTI-LANGUAGE ENGINE (I18N)
url_i18n = f"https://haichain.si/app/i18n.js?t={ts}"
req_i18n = urllib.request.Request(url_i18n, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
with urllib.request.urlopen(req_i18n) as resp:
    i18n_js = resp.read().decode('utf-8', errors='ignore')

i18n_checks = [
    ('100% Exploit Immune removed globally', '100% Exploit Immune' not in i18n_js),
    ('15/15 Kiểm Tra Vector An Toàn (VI)', '15/15 Kiểm Tra Vector An Toàn' in i18n_js),
    ('15/15 Test Vectors Verified (EN)', '15/15 Test Vectors Verified' in i18n_js),
    ('Coinbase AgentKit in i18n', 'Coinbase AgentKit (x402)' in i18n_js),
    ('Skyfire Protocol in i18n', 'Skyfire Protocol (EVM)' in i18n_js)
]

print("\n5. MULTI-LANGUAGE I18N VERIFICATION:")
for label, ok in i18n_checks:
    status = "PASS" if ok else "FAIL"
    print(f"   [{status}] {label}")

# 6. SCAN WHITEPAPER ROUTE
print("\n6. WHITEPAPER ACCESS CHECK:")
try:
    wp_req = urllib.request.Request("https://haichain.si/whitepaper", headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(wp_req) as wp_resp:
        print(f"   [PASS] https://haichain.si/whitepaper -> HTTP {wp_resp.status} (MIME: {wp_resp.headers.get('content-type')})")
except Exception as e:
    print(f"   [FAIL] Whitepaper error: {e}")
