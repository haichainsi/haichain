import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://haichain.si/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        print("SAFT PDF STATUS:", r.status, len(r.read()))
except Exception as e:
    print("Error:", e)
