import urllib.request, time, re

print("Polling for live commit 4b65f9d (v35_streamlined_unboxed)...")
for i in range(1, 15):
    try:
        url = f"https://haichain.si/?t={int(time.time())}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', html)
        ver = m.group(1) if m else 'none'
        has_new_ver = 'v35_streamlined_unboxed' in ver
        print(f"Poll {i}: live_version={ver}, matches={has_new_ver}")
        if has_new_ver:
            print(">>> SUCCESS! Commit 4b65f9d is 100% LIVE on Cloudflare! <<<")
            break
    except Exception as e:
        print(f"Poll {i} error: {e}")
    time.sleep(5)
