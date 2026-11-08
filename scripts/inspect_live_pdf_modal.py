import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request("https://haichain.si/app/pdf-modal.js?nocache=123", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    txt = r.read().decode('utf-8', errors='ignore')
    print("Length:", len(txt))
    print("Has SAFT_DRAWER_I18N:", "SAFT_DRAWER_I18N" in txt)
    print("Has zh in SAFT_DRAWER_I18N:", "zh:" in txt)
    print("Has ko in SAFT_DRAWER_I18N:", "ko:" in txt)
    print("Has pdf-modal-lang-toggle:", "pdf-modal-lang-toggle" in txt)
    print("Has haichain:languageChanged:", "haichain:languageChanged" in txt)
    print("Has refreshSaftDrawerI18n:", "refreshSaftDrawerI18n" in txt)
