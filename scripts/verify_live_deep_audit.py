import urllib.request, ssl, sys, time

sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()

urls = [
    ("Landing Page", "https://haichain.si/"),
    ("Dashboard", "https://haichain.si/dashboard.html"),
    ("i18n Master JS", "https://haichain.si/i18n.js"),
    ("Whitepaper EN PDF", "https://haichain.si/HAICHAIN_WHITEPAPER_V1.0_EN.pdf"),
    ("Whitepaper VI PDF", "https://haichain.si/HAICHAIN_WHITEPAPER_V1.0_VI.pdf"),
    ("Whitepaper ES PDF", "https://haichain.si/HAICHAIN_WHITEPAPER_V1.0_ES.pdf"),
    ("SAFT EN PDF", "https://haichain.si/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf"),
    ("SAFT VI PDF", "https://haichain.si/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI.pdf"),
    ("Memo EN PDF", "https://haichain.si/HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf"),
    ("Memo VI PDF", "https://haichain.si/HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.pdf"),
]

print("Verifying live HTTP endpoints on Cloudflare Edge (https://haichain.si)...")
for label, url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            status = resp.status
            size = len(resp.read())
            print(f"[OK] {label:<20} | Status: {status} | Size: {size:,} bytes | {url}")
    except Exception as e:
        print(f"[FAIL] {label:<20} | Error: {e}")

print("Live endpoint verification complete.")
