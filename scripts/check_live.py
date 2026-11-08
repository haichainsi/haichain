import urllib.request, time

time.sleep(10)
url = 'https://haichain.si/dashboard.html?cache_bust=' + str(int(time.time()))
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        print('Live dashboard fetched, size:', len(html))
        print('startMetaMaskSessionPoller in live:', 'startMetaMaskSessionPoller' in html)
        print('btn-metamask-inapp-confirm in live:', 'btn-metamask-inapp-confirm' in html)
        print('v4_metamask_relay_sync in live:', 'v4_metamask_relay_sync' in html)
except Exception as e:
    print('Fetch error:', e)
