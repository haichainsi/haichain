import urllib.request
import time
import re

print("Polling haichain.si for commit 3ac032a...")

for attempt in range(1, 40):
    url = f"https://haichain.si/dashboard.html?_ts={int(time.time()*1000)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            has_borderless = 'rounded-3xl bg-white dark:bg-[#0a0a0a] space-y-6' in html
            has_old_border = 'border border-neutral-200/60 dark:border-white/[0.06]' in html
            print(f"[{attempt}] has_borderless={has_borderless}, has_old_border={has_old_border}")
            if has_borderless and not has_old_border:
                print(">>> 3ac032a IS CONFIRMED LIVE ON CLOUDFLARE! <<<")
                break
    except Exception as e:
        print(f"[{attempt}] Error:", e)
    time.sleep(5)
