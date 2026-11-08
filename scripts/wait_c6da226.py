import urllib.request, re, time

print("Waiting for commit c6da226 (v28_cloud_mcp_streamable_http) to finish deploying...")

for attempt in range(10):
    time.sleep(6)
    url = f'https://haichain.si/dashboard?t={int(time.time())}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', data)
        ver = m.group(1) if m else "None"
        print(f"Attempt {attempt+1}: current live version = {ver}")
        if 'v28_cloud_mcp_streamable_http' in ver:
            print(">>> SUCCESS! Latest commit is LIVE on Cloudflare! <<<")
            break
    except Exception as e:
        print(f"Attempt {attempt+1} error: {e}")
