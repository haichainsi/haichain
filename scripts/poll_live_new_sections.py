import urllib.request
import time
import re

print("Starting poll for live sections on haichain.si...")
for i in range(1, 15):
    url = f"https://haichain.si/index.html?t={int(time.time())}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', html)
        ver = m.group(1) if m else 'none'
        has_sections = 'agentic-shift' in html and 'haichain-advantages' in html
        print(f"Poll {i}: version={ver}, has_sections={has_sections}")
        if has_sections:
            print("SUCCESS! Both new sections are 100% verified LIVE on https://haichain.si!")
            break
    except Exception as e:
        print(f"Poll {i} error: {e}")
    time.sleep(5)
