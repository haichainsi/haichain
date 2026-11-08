import urllib.request
import re
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0'}

req1 = urllib.request.Request('https://haichain.si/dashboard', headers=headers)
with urllib.request.urlopen(req1, context=ctx) as r:
    b1 = r.read().decode('utf-8', errors='ignore')
    m1 = re.findall(r'i18n\.js\?v=([^\s"\'>]+)', b1)
    print("Live dashboard i18n tag:", m1)

req2 = urllib.request.Request('https://haichain.si/', headers=headers)
with urllib.request.urlopen(req2, context=ctx) as r:
    b2 = r.read().decode('utf-8', errors='ignore')
    m2 = re.findall(r'i18n\.js\?v=([^\s"\'>]+)', b2)
    print("Live index.html i18n tag:", m2)

req3 = urllib.request.Request('https://haichain.si/app/i18n.js', headers=headers)
with urllib.request.urlopen(req3, context=ctx) as r:
    b3 = r.read().decode('utf-8', errors='ignore')
    print("Live /app/i18n.js length:", len(b3))
    print("Has 'Định Chế':", 'Định Chế' in b3)
    print("Has em-dash (\\u2014):", '\u2014' in b3)
    # Check Kazakh position
    m = re.search(r'const\s+LANGUAGES\s*=\s*\[(.*?)\];', b3, re.DOTALL)
    if m:
        codes = re.findall(r"code:\s*'([a-z]+)'", m.group(1))
        print("Live LANGUAGES order:", codes)
