import urllib.request, re, time, os, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ts = int(time.time())

for path in ['/dashboard', '/dashboard.html', '/index.html']:
    url = f'https://haichain.si{path}?nocache={ts}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = resp.read().decode('utf-8', errors='ignore')
            m_i18n = re.search(r'i18n\.js\?v=([^"\'>\s]+)', data)
            m_sale = re.search(r'sale-controller\.js\?v=([^"\'>\s]+)', data)
            m_pdf = re.search(r'pdf-modal\.js\?v=([^"\'>\s]+)', data)
            print(f"URL: {path}")
            print(f"   i18n.js: {m_i18n.group(1) if m_i18n else 'None'}")
            print(f"   sale-controller.js: {m_sale.group(1) if m_sale else 'None'}")
            print(f"   pdf-modal.js: {m_pdf.group(1) if m_pdf else 'None'}")
    except Exception as e:
        print(f"URL: {path} Error: {e}")
