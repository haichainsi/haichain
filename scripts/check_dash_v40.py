import urllib.request, re, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ts = int(time.time() * 1000)
url = f"https://haichain.si/dashboard?t={ts}"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')
    m = re.findall(r'pdf-modal\.js\?v=([^\"]+)', html)
    print("Dashboard live pdf-modal script version:", m)
