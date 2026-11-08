import urllib.request, time, sys, re
sys.stdout.reconfigure(encoding='utf-8')

print("Waiting for Cloudflare Pages build & deployment of commit 756871c...")
for attempt in range(1, 30):
    url = f"https://haichain.si/dashboard?t={int(time.time())}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        
        has_python = 'haichain-agent-pay' in data
        m_v = re.search(r'i18n\.js\?v=([^\'\"\s>]+)', data)
        ver = m_v.group(1) if m_v else 'None'
        
        print(f"[{attempt}/30] Live i18n version: {ver} | Python SDK present: {has_python}")
        if has_python or 'v70_devhub_python_20261108' in ver:
            print("\n>>> DEPLOYMENT CONFIRMED: Commit 756871c is LIVE on haichain.si! <<<")
            break
    except Exception as e:
        print(f"[{attempt}/30] Error: {e}")
    time.sleep(5)
