import urllib.request
import re
import time

for attempt in range(1, 12):
    url = f'https://haichain.si/dashboard?t={int(time.time())}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', data)
        ver = m.group(1) if m else 'None'
        has_new = 'btn-continue-in-metamask' in data
        has_intent = 'intent://' in data
        print(f"Attempt {attempt}: version={ver}, has_new_btn={has_new}, has_intent={has_intent}")
        if 'v29_institutional_audit_upgrade' in ver or has_new:
            print(">>> SUCCESS! Latest commit 246b399 is LIVE on Cloudflare! <<<")
            break
    except Exception as e:
        print(f"Attempt {attempt} error:", e)
    time.sleep(5)
