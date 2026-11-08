import urllib.request
import time

for attempt in range(1, 10):
    time.sleep(8)
    url = f"https://haichain.si/dashboard.html?buster={attempt}_{int(time.time())}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
            has_chrome = 'googlechrome://navigate' in data
            has_relay = '/api/wallet-relay' in data
            print(f"Check {attempt}: has_chrome={has_chrome}, has_relay={has_relay}")
            if has_chrome and has_relay:
                print(">>> SUCCESS! Latest commit 8300757 is LIVE on Cloudflare! <<<")
                break
    except Exception as e:
        print(f"Check {attempt} error:", e)
