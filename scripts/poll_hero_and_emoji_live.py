import urllib.request, time, re

print("Polling for live commit a24896e (v34_hero_text3xl_noemoji)...")
for i in range(1, 15):
    try:
        url = f"https://haichain.si/?t={int(time.time())}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        has_new_hero = 'text-3xl sm:text-4xl md:text-5xl font-bold' in html
        has_no_emoji = '\U0001f449' not in html
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', html)
        ver = m.group(1) if m else 'none'
        print(f"Poll {i}: ver={ver}, text3xl={has_new_hero}, no_emoji={has_no_emoji}")
        if has_new_hero and has_no_emoji and 'v34_hero_text3xl_noemoji' in ver:
            print(">>> SUCCESS! Commit a24896e is 100% LIVE on Cloudflare! <<<")
            break
    except Exception as e:
        print(f"Poll {i} error: {e}")
    time.sleep(5)
