import urllib.request, time, re

print("Polling for Cloudflare Pages build of commit 301f51c...")
for i in range(12):
    ts = int(time.time())
    try:
        url = f"https://haichain.si/index.html?t={ts}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
        if "v30_architectural_tradeoffs" in content or "Architectural Dimension" in content:
            print(f">>> DEPLOY CONFIRMED LIVE at attempt {i+1} ({ts})! <<<")
            break
        else:
            print(f"Attempt {i+1}: still deploying/cached...")
    except Exception as e:
        print(f"Attempt {i+1} error: {e}")
    time.sleep(5)
