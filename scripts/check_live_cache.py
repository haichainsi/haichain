import urllib.request, time, re

url = f'https://haichain.si/dashboard.html?t={int(time.time())}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
html = urllib.request.urlopen(req).read().decode('utf-8')
m = re.search(r'pdf-modal\.js\?v=([^">]+)', html)
print('Live cachebuster:', m.group(1) if m else 'none')
