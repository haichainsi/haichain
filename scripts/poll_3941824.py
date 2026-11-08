import urllib.request
import time
import re

print("Polling haichain.si for commit 3941824 (v39_exact_small_text_)...")

for attempt in range(1, 40):
    url = f"https://haichain.si/?_ts={int(time.time()*1000)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            has_v39 = "v39_exact_small_text_" in html
            has_p5 = 'p-5 sm:p-6 rounded-2xl' in html
            has_text_xs = 'space-y-2.5 font-sans text-xs leading-relaxed' in html
            print(f"[{attempt}] has_v39={has_v39}, has_p5={has_p5}, has_text_xs={has_text_xs}")
            if has_v39 and has_p5 and has_text_xs:
                print(">>> 3941824 IS OFFICIALLY LIVE ON CLOUDFLARE PAGES! <<<")
                break
    except Exception as e:
        print(f"[{attempt}] Error:", e)
    time.sleep(5)
