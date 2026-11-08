import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Cache-Control': 'no-cache, no-store, max-age=0',
    'Pragma': 'no-cache'
}

req = urllib.request.Request('https://haichain.si/index.html', headers=headers)
with urllib.request.urlopen(req) as res:
    print('CF-Cache-Status:', res.headers.get('CF-Cache-Status'))
    print('Age:', res.headers.get('Age'))
    html = res.read().decode('utf-8', errors='ignore')
    print('Versions found:', re.findall(r'i18n\.js\?v=([^\s"\'>]+)', html))
    print('Has space-y-2.5 font-sans text-xs:', 'space-y-2.5 font-sans text-xs' in html)
    print('Has v38:', 'v38_sync_small_text_' in html)
