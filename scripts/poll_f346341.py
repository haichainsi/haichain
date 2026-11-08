import urllib.request
import time
import re

print("Polling haichain.si for commit f346341 (v41_passkey_toast_fix_)...")

for attempt in range(1, 35):
    url = f"https://haichain.si/dashboard.html?_ts={int(time.time()*1000)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            has_v41 = "v41_passkey_toast_fix_" in html
            has_toast_fix = "function showToast(options, secondaryMsg, customIcon)" in html
            print(f"[{attempt}] has_v41={has_v41}, has_toast_fix={has_toast_fix}")
            if has_v41 and has_toast_fix:
                print(">>> f346341 IS LIVE ON CLOUDFLARE PAGES! <<<")
                break
    except Exception as e:
        print(f"[{attempt}] Error:", e)
    time.sleep(5)
