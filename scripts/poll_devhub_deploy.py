import urllib.request, time, sys, re

sys.stdout.reconfigure(encoding='utf-8')
print("Polling Cloudflare Pages for deployment of commit a58125a (v61_devhub_vi_label_clean)...")

for attempt in range(1, 20):
    url = f"https://haichain.si/dashboard?t={int(time.time())}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        
        m_i18n = re.search(r'i18n\.js\?v=([^\'\"\s>]+)', data)
        ver_i18n = m_i18n.group(1) if m_i18n else 'None'
        
        print(f"[{attempt}/20] Live i18n version: {ver_i18n}")
        if 'v61_devhub_vi_label_clean' in ver_i18n:
            print("\n>>> DEPLOYMENT CONFIRMED: Commit a58125a is LIVE on haichain.si! <<<")
            sys.exit(0)
    except Exception as e:
        print(f"[{attempt}/20] Error: {e}")
    time.sleep(6)

print("Timeout waiting for Cloudflare Pages.")
sys.exit(1)
