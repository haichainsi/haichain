import urllib.request
import re

for path in ['/', '/index.html', '/dashboard', '/dashboard.html', '/app/dashboard.html']:
    try:
        url = f'https://haichain.si{path}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', text)
            v = m.group(1) if m else 'no-i18n'
            has_new = 'btn-continue-in-metamask' in text
            print(f"{path:20} -> {len(text)} bytes, i18n={v}, has_new={has_new}")
    except Exception as e:
        print(f"{path:20} -> err: {e}")
