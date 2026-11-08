import urllib.request, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://haichain.si/app/pdf-modal.js?v=v40_fluid_signature_validated_1793646000000"
print("Polling Cloudflare Pages for v40 signature fix...")
for i in range(1, 21):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            txt = r.read().decode('utf-8', errors='ignore')
            has_isSigValid = "isSigValid" in txt
            has_pointer = "PointerEvent" in txt
            has_old_stroke = "strokeCount < 3" in txt
            cf_cache = r.headers.get('cf-cache-status')
            print(f"[{i}] len={len(txt)}, has_isSigValid={has_isSigValid}, has_old_stroke={has_old_stroke}, cf_cache={cf_cache}")
            if has_isSigValid and not has_old_stroke:
                print("SUCCESS: v40 signature fix is LIVE on Cloudflare Pages!")
                exit(0)
    except Exception as e:
        print(f"[{i}] Error: {e}")
    time.sleep(3)

print("Still deploying...")
