import urllib.request
import time
import re

url = "https://haichain.si/?_ts=" + str(int(time.time()))
print("Polling", url)

for attempt in range(1, 30):
    try:
        req = urllib.request.Request(
            f"https://haichain.si/?_ts={int(time.time()*1000)}",
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # Check for v38 or text-xs
            has_v38 = "v38_sync_small_text_" in html
            has_text_xs_card = 'class="space-y-2.5 font-sans text-xs leading-relaxed"' in html
            has_old_1 = "1. Thanh toán siêu nhỏ" in html
            
            print(f"[{attempt}] has_v38={has_v38}, has_text_xs_card={has_text_xs_card}, has_old_1={has_old_1}")
            
            if has_v38 and has_text_xs_card and not has_old_1:
                print(">>> LIVE DEPLOYMENT CONFIRMED! <<<")
                break
    except Exception as e:
        print(f"[{attempt}] Error:", e)
    
    time.sleep(5)
