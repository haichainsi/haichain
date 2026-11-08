import urllib.request
import time
import re

print("Checking for commit 2746dc0 on live site...")

for i in range(1, 15):
    url = f'https://haichain.si/?cf_build_poll={int(time.time()*1000)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            has_p5 = 'p-5 sm:p-6 rounded-2xl' in html
            has_xs_body = 'space-y-2.5 font-sans text-xs leading-relaxed' in html
            print(f"[{i}] has_p5={has_p5}, has_xs_body={has_xs_body}")
            if has_p5 and has_xs_body:
                print(">>> 2746dc0 IS FULLY LIVE ON CLOUDFLARE! <<<")
                break
    except Exception as e:
        print(f"[{i}] error:", e)
    time.sleep(5)
