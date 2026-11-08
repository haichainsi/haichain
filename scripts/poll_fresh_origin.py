import urllib.request, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Waiting for Cloudflare Pages to finish building commit b9a6a5a...")
for attempt in range(1, 25):
    ts = int(time.time() * 1000)
    url = f"https://haichain.si/app/pdf-modal.js?cb={ts}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            txt = r.read().decode('utf-8', errors='ignore')
            has_isSigValid = "isSigValid" in txt
            has_old = "strokeCount < 3" in txt
            cf_cache = r.headers.get('cf-cache-status')
            print(f"[{attempt}] len={len(txt)}, has_isSigValid={has_isSigValid}, has_old_stroke={has_old}, cf_cache={cf_cache}")
            if has_isSigValid and not has_old:
                print("\n>>> SUCCESS! Commit b9a6a5a with fluid signature validation is LIVE on Cloudflare! <<<")
                exit(0)
    except Exception as e:
        print(f"[{attempt}] error: {e}")
    time.sleep(5)
