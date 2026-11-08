import urllib.request, time, re

print("Polling for live commit bea7024 (v36_no_numbering)...")
for i in range(1, 15):
    try:
        url = f"https://haichain.si/?t={int(time.time())}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', html)
        ver = m.group(1) if m else 'none'
        has_new_ver = 'v36_no_numbering' in ver
        has_no_num1 = '1. Thanh toán siêu nhỏ' not in html
        print(f"Poll {i}: live_version={ver}, matches={has_new_ver}, no_num1={has_no_num1}")
        if has_new_ver and has_no_num1:
            print(">>> SUCCESS! Commit bea7024 is 100% LIVE on Cloudflare! <<<")
            break
    except Exception as e:
        print(f"Poll {i} error: {e}")
    time.sleep(5)
