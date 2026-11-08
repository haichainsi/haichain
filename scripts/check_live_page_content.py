import urllib.request, re, time

url = f'https://haichain.si/index.html?t={int(time.time())}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', html)
if m:
    print('Live i18n cachebuster:', m.group(1))

m_pdf = re.search(r'pdf-modal\.js\?v=([^"\'>\s]+)', html)
if m_pdf:
    print('Live pdf-modal cachebuster:', m_pdf.group(1))

print('Has v30_architectural_tradeoffs:', 'v30_architectural_tradeoffs' in html)
print('Has v29_institutional_audit_upgrade:', 'v29_institutional_audit_upgrade' in html)
