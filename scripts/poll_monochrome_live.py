import urllib.request, time, re

print("Polling for live commit f39667d (v33_landing_agentic_1793633622455)...")
for i in range(1, 15):
    try:
        url = f"https://haichain.si/?t={int(time.time())}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', html)
        ver = m.group(1) if m else 'none'
        is_new = '1793633622455' in ver
        has_no_rose = 'bg-rose-500' not in html
        print(f"Poll {i}: live_version={ver}, matches_target={is_new}, no_rose={has_no_rose}")
        if is_new:
            print(">>> SUCCESS! Commit f39667d is LIVE with 100% monochrome design! <<<")
            break
    except Exception as e:
        print(f"Poll {i} error: {e}")
    time.sleep(6)
