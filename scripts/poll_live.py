import time
import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Waiting for Cloudflare Pages build of commit 9dbab3f...")
for attempt in range(1, 15):
    time.sleep(4)
    url = f"https://haichain.si/dashboard?t={int(time.time())}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = resp.read().decode("utf-8", errors="ignore")
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', data)
        ver = m.group(1) if m else "None"
        has_func = "function renderGlobalAgentMarketplace()" in data
        print(f"Attempt {attempt}: ver={ver}, has_func={has_func}")
        if has_func or "v49_marketplace_phase1" in ver:
            print(">>> SUCCESS! Latest commit 9dbab3f is 100% LIVE on Cloudflare! <<<")
            break
    except Exception as e:
        print(f"Attempt {attempt} error:", e)
