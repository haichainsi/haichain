import urllib.request, ssl, os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

langs = ['VI', 'EN', 'ZH', 'ES', 'FR', 'KO', 'RU', 'KK', 'HI', 'HE']

print("Checking /app/ paths:")
for l in langs:
    fname = f'HAICHAIN_WHITEPAPER_V1.0_{l}.pdf'
    local_path = os.path.join('app', fname)
    local_sz = os.path.getsize(local_path)
    url = f'https://haichain.si/app/{fname}'
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(r, context=ctx) as resp:
            remote_sz = int(resp.headers.get('Content-Length', 0))
            cf_cache = resp.headers.get('CF-Cache-Status')
            print(f"  /app/{fname}: Local={local_sz} | Remote={remote_sz} | Match={local_sz == remote_sz} | CF={cf_cache}")
    except Exception as e:
        print(f"  /app/{fname} Error: {e}")

for memo in ['HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf', 'HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf']:
    local_path = os.path.join('app', memo)
    local_sz = os.path.getsize(local_path)
    url = f'https://haichain.si/app/{memo}'
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(r, context=ctx) as resp:
            remote_sz = int(resp.headers.get('Content-Length', 0))
            cf_cache = resp.headers.get('CF-Cache-Status')
            print(f"  /app/{memo}: Local={local_sz} | Remote={remote_sz} | Match={local_sz == remote_sz} | CF={cf_cache}")
    except Exception as e:
        print(f"  /app/{memo} Error: {e}")
