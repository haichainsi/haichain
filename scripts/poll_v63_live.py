import urllib.request, re, time

for i in range(10):
    url = f'https://haichain.si/dashboard?t={int(time.time())}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', data)
        ver = m.group(1) if m else 'None'
        has_airdrop = 'requestAirdrop' in data
        has_sign = 'signAndSendTransaction' in data
        print(f"Poll {i+1}: ver={ver}, has_airdrop={has_airdrop}, has_sign={has_sign}")
        if has_airdrop and has_sign:
            print(">>> VERIFIED: v63 is LIVE on Cloudflare! <<<")
            break
    except Exception as e:
        print("Error:", e)
    time.sleep(5)
