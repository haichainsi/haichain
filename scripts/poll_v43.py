import urllib.request
import re
import time

for i in range(12):
    try:
        url = f"https://haichain.si/dashboard?_nocache={int(time.time()*1000)}"
        req = urllib.request.Request(url, headers={'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            if 'v43_mobile_header_viewport_lock' in text:
                print(f"[SUCCESS] Cloudflare Pages deployed commit 9fa8a09 live! (attempt {i+1})")
                exit(0)
            else:
                print(f"[WAIT] Still building... (attempt {i+1})")
    except Exception as e:
        print(f"[ERR] {e}")
    time.sleep(5)
