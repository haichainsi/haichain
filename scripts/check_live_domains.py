import urllib.request
import json
import time

for domain in ['https://haichain.si', 'https://haichainsi.pages.dev']:
    try:
        url = f"{domain}/?_nocache={int(time.time()*1000)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            body = res.read().decode('utf-8', errors='ignore')
            import re
            m = re.findall(r'i18n\.js\?v=([^\s"\'>]+)', body)
            has_v38 = "v38_sync_small_text_" in body
            has_old_1 = "1. Thanh toán" in body
            print(f"Domain: {domain}")
            print(f"  i18n script version found: {m}")
            print(f"  has_v38: {has_v38}")
            print(f"  has_old_1: {has_old_1}")
            # check commit hash in headers if any
            headers = dict(res.headers)
            print(f"  cf-ray: {headers.get('cf-ray')}")
            print(f"  age: {headers.get('age')}")
            print(f"  cf-cache-status: {headers.get('cf-cache-status')}")
    except Exception as e:
        print(f"Domain {domain} error: {e}")
