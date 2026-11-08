import urllib.request, time, re

req = urllib.request.Request(f'https://haichain.si/?v={int(time.time())}', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

m = re.search(r'data-i18n="comp\.row6Hai">([^<]+)<', html)
if m:
    print('Row6Hai content:', m.group(1))
else:
    print('Row6Hai not found')

m2 = re.search(r'data-i18n="aud\.investorNowDesc">([^<]+)<', html)
if m2:
    print('InvestorNowDesc content:', m2.group(1))
else:
    print('InvestorNowDesc not found')

# Also check i18n.js
req_i18n = urllib.request.Request(f'https://haichain.si/i18n.js?v={int(time.time())}', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req_i18n, timeout=10) as r:
    i18n_text = r.read().decode('utf-8', errors='ignore')

print('i18n has Ve-Governance staking:', 'Ve-Governance staking' in i18n_text)
print('i18n has old Real Yield in USDT (40%:', 'Real Yield in USDT (40%' in i18n_text)
