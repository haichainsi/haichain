import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://haichain.si/app/pdf-modal.js?v=v40_fluid_signature_validated_1793646000000"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    txt = r.read().decode('utf-8', errors='ignore')
    print("Length:", len(txt))
    print("Has isSigValid:", "isSigValid" in txt)
    print("Has old strokeCount < 3:", "strokeCount < 3" in txt)
    print("CF-Cache-Status:", r.headers.get('cf-cache-status'))
