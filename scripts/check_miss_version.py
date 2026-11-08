import urllib.request
import time
import re

url = f'https://haichain.si/?cf_bypass={int(time.time()*1000)}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as res:
    print('URL:', url)
    print('CF-Cache-Status:', res.headers.get('CF-Cache-Status'))
    html = res.read().decode('utf-8', errors='ignore')
    print('Versions in MISS response:', re.findall(r'i18n\.js\?v=([^\s"\'>]+)', html))
    print('Has space-y-2.5 font-sans text-xs:', 'space-y-2.5 font-sans text-xs' in html)
    print('Has v38:', 'v38_sync_small_text_' in html)
