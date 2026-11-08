import urllib.request, re, time, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ts = int(time.time())
url = f'https://haichain.si/dashboard?nocache={ts}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
with urllib.request.urlopen(req, context=ctx) as resp:
    data = resp.read().decode('utf-8', errors='ignore')

for line in data.splitlines():
    if '.js?v=' in line:
        print(line.strip())
