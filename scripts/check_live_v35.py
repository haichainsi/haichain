import urllib.request
import re
import time

for attempt in range(1, 15):
    ts = str(int(time.time()))
    url = f"https://haichain.si/dashboard?t={ts}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'pdf-modal\.js\?v=([^"\'\s>]+)', data)
        ver = m.group(1) if m else 'Not found'
        print(f"Attempt {attempt}: live script tag version={ver}")
        if 'v35_solid_contrast' in ver:
            print("[+] SUCCESS! Version v35 (Solid Opaque & Ultra High Contrast) is LIVE on haichain.si!")
            break
    except Exception as e:
        print(f"Attempt {attempt} error:", e)
    time.sleep(3)
