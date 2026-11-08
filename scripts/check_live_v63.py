import urllib.request, re, time, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for i in range(8):
    ts = int(time.time())
    req = urllib.request.Request(f'https://haichain.si/dashboard?cache_bust={ts}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', data)
        ver = m.group(1) if m else 'None'
        print(f"Check {i+1}: ver={ver}")
        if 'v63' in ver:
            print(">>> CLOUDFLARE DEPLOYED COMMIT e8390e4 LIVE! <<<")
            break
    except Exception as e:
        print("Error:", e)
    time.sleep(10)
