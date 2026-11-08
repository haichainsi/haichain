import urllib.request, re, time, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("[*] Polling Cloudflare Pages for unblocked deployment (commit 4a85153)...")
max_attempts = 20

for attempt in range(1, max_attempts + 1):
    ts = int(time.time())
    url = f"https://haichain.si/dashboard.html?t={ts}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
            has_v19 = 'v19_cachebust_institutional_1793600000' in data
            has_memo = 'openPreseedMemoModal' in data
            cf_cache = resp.headers.get('CF-Cache-Status')
            
            print(f"Attempt {attempt}/{max_attempts}: v19_in_html={has_v19}, memo_func={has_memo}, cf_cache={cf_cache}")
            if has_v19 or has_memo:
                print("\n[+] SUCCESS! Latest build is LIVE on https://haichain.si!")
                break
    except Exception as e:
        print(f"Attempt {attempt} error: {e}")
    time.sleep(6)
