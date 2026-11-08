import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for path in ['/', '/dashboard', '/app/dashboard.html', '/index.html']:
    try:
        url = f"https://haichain.si{path}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx) as res:
            txt = res.read().decode("utf-8", errors="ignore")
            vers = re.findall(r'[a-zA-Z0-9_\-]+\.js\?v=([^\s"\'>]+)', txt)
            has_func = "function renderGlobalAgentMarketplace()" in txt
            has_market = "Global Agent Labor Marketplace" in txt
            print(f"Path: {path}")
            print(f"  Length: {len(txt)}")
            print(f"  Versions: {set(vers)}")
            print(f"  Has Marketplace Section: {has_market}")
            print(f"  Has render function: {has_func}")
    except Exception as e:
        print(f"Path: {path} -> {e}")
