import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request("https://haichain.si/app/pdf-modal.js?v=v38_inmodal_lang_sync_1793642000000", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    txt = r.read().decode('utf-8', errors='ignore')
    print("Length of /app/pdf-modal.js:", len(txt))
    print("Has SAFT_DRAWER_I18N:", "SAFT_DRAWER_I18N" in txt)
    print("Has pdf-modal-lang-toggle:", "pdf-modal-lang-toggle" in txt)
    print("First 300 chars:", txt[:300])
