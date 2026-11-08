import urllib.request, time, sys, re
sys.stdout.reconfigure(encoding='utf-8')

print("Waiting for Cloudflare Pages build & deployment of commit 7b2fd8c...")
for attempt in range(1, 30):
    url = f"https://haichain.si/dashboard?t={int(time.time())}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        
        m_modal = re.search(r'pdf-modal\.js\?v=([^\'\"\s>]+)', data)
        ver_modal = m_modal.group(1) if m_modal else 'None'
        
        print(f"[{attempt}/30] Live modal version: {ver_modal}")
        if 'v53_ai2_title_math_fixed' in ver_modal:
            print("\n>>> DEPLOYMENT CONFIRMED: Commit 7b2fd8c is LIVE on haichain.si! <<<")
            break
    except Exception as e:
        print(f"[{attempt}/30] Error: {e}")
    time.sleep(5)
