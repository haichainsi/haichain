import urllib.request, time, re

t = int(time.time())
for url in ['https://haichain.si/?t=' + str(t), 'https://haichain.si/index.html?t=' + str(t), 'https://haichain.si/app/index.html?t=' + str(t)]:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store, must-revalidate'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', body)
            ver = m.group(1) if m else 'none'
            print(url.split('?')[0], '-> ver:', ver, 'agentic:', 'agentic-shift' in body)
    except Exception as e:
        print(url, 'error:', e)
