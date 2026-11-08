import urllib.request, re, time, os, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 1. Check local dashboard
with open('dashboard.html', encoding='utf-8') as f:
    local_dash = f.read()

local_script_matches = re.findall(r'src=["\']([^"\']+\.js\?v=[^"\']+)["\']', local_dash)
print("Local Dashboard Scripts:")
for s in local_script_matches:
    print("  ", s)

# 2. Check live dashboard
ts = int(time.time())
req = urllib.request.Request(f'https://haichain.si/dashboard?t={ts}', headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
with urllib.request.urlopen(req, context=ctx) as resp:
    live_dash = resp.read().decode('utf-8', errors='ignore')

live_script_matches = re.findall(r'src=["\']([^"\']+\.js\?v=[^"\']+)["\']', live_dash)
print("\nLive Dashboard Scripts:")
for s in live_script_matches:
    print("  ", s)

# 3. Check PDF sizes and MD content
langs = ['VI', 'EN', 'ZH', 'ES', 'FR', 'KO', 'RU', 'KK', 'HI', 'HE']
print("\nWhitepaper Status:")
for l in langs:
    fname = f'HAICHAIN_WHITEPAPER_V1.0_{l}.pdf'
    local_sz = os.path.getsize(fname) if os.path.exists(fname) else 0
    # Try fetching with cachebuster
    url = f'https://haichain.si/{fname}?t={ts}'
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r, context=ctx) as resp:
            remote_sz = int(resp.headers.get('Content-Length', 0))
            print(f"  {l}: Local={local_sz} | Remote(bust)={remote_sz} | Match={local_sz == remote_sz}")
    except Exception as e:
        print(f"  {l}: Error {e}")

# 4. Check Pre-Seed Memos
for memo in ['HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf', 'HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf']:
    local_sz = os.path.getsize(memo) if os.path.exists(memo) else 0
    url = f'https://haichain.si/{memo}?t={ts}'
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r, context=ctx) as resp:
            remote_sz = int(resp.headers.get('Content-Length', 0))
            print(f"  {memo}: Local={local_sz} | Remote(bust)={remote_sz} | Match={local_sz == remote_sz}")
    except Exception as e:
        print(f"  {memo}: Error {e}")
