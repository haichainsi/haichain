import urllib.request, re, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(f"https://haichain.pages.dev/dashboard?t={int(time.time())}", headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
try:
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
        m = re.findall(r'i18n\.js\?v=([^"]+)', html)
        print("pages.dev i18n:", m)
        print("pages.dev requestAirdrop:", 'requestAirdrop' in html)
        print("pages.dev cf-cache:", r.headers.get('cf-cache-status'))
except Exception as e:
    print("pages.dev error:", e)
