import urllib.request, re

req = urllib.request.Request('https://haichain.si/dashboard.html?buster=99999', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')
    print('Live Size:', len(html))
    scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', html)
    for s in scripts:
        print('Script:', s)
    idx = html.find('v4_metamask_relay_sync')
    print('v4 in live:', idx != -1)
    idx2 = html.find('btn-metamask-inapp-confirm')
    print('btn-metamask-inapp-confirm in live:', idx2 != -1)
