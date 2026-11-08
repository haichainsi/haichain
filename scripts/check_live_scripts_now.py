import urllib.request, time, re

ts = int(time.time())
url = f'https://haichain.si/index.html?t={ts}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
for s in scripts:
    if 'v=' in s:
        print('Live index.html script:', s)

url_dash = f'https://haichain.si/dashboard.html?t={ts}'
req_dash = urllib.request.Request(url_dash, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
with urllib.request.urlopen(req_dash, timeout=10) as resp:
    html_dash = resp.read().decode('utf-8', errors='ignore')

scripts_dash = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html_dash)
for s in scripts_dash:
    if 'v=' in s:
        print('Live dashboard.html script:', s)
