import urllib.request
import re
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Checking Cloudflare Pages deployment of v66...")
for attempt in range(1, 15):
    url = f"https://haichain.si/dashboard?t={int(time.time())}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'pdf-modal\.js\?v=([^"\'>\s]+)', data)
        ver = m.group(1) if m else 'None'
        print(f"Attempt {attempt}: ver={ver}")
        if 'v66' in ver:
            print(">>> SUCCESS! Latest commit with Dual Resend Email is LIVE on Cloudflare! <<<")
            sys.exit(0)
    except Exception as e:
        print(f"Attempt {attempt} error:", e)
    time.sleep(6)

print("Still waiting for propagation...")
