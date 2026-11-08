import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request("https://haichain.si/dashboard", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    for k, v in r.headers.items():
        if any(x in k.lower() for x in ['age', 'date', 'cf', 'cache', 'etag', 'last-modified']):
            print(f"{k}: {v}")
