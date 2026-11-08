import urllib.request
import time
import sys

url_dash = "https://haichain.si/dashboard"
url_i18n = "https://haichain.si/i18n.js?v=v72_devhub_i18n_clean_20261108"
target_str = "v72_devhub_i18n_clean_20261108"
target_key = "dev.watchtowerTitle"

print(f"Polling Cloudflare Pages live deployment for {target_str}...")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

max_attempts = 30
for i in range(1, max_attempts + 1):
    try:
        req = urllib.request.Request(url_dash, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8')
            if target_str in content:
                print(f"[{i}/{max_attempts}] SUCCESS! Found {target_str} on {url_dash}")
                
                # Check i18n
                req_i18n = urllib.request.Request(url_i18n, headers=headers)
                with urllib.request.urlopen(req_i18n, timeout=10) as resp_i18n:
                    i18n_content = resp_i18n.read().decode('utf-8')
                    if target_key in i18n_content:
                        print(f"SUCCESS! Found {target_key} in live {url_i18n}")
                        print("Production deployment is LIVE and fully verified!")
                        sys.exit(0)
            else:
                print(f"[{i}/{max_attempts}] Still old version on edge, waiting 5s...")
    except Exception as e:
        print(f"[{i}/{max_attempts}] Error fetching: {e}")
    time.sleep(5)

print("Timeout waiting for Cloudflare deployment")
sys.exit(1)
