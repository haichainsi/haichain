import urllib.request
import ssl
import re
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for i in range(40):
    try:
        req = urllib.request.Request('https://haichain.si/dashboard?lang=en', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
            body = res.read().decode('utf-8', errors='ignore')
        m = re.search(r'pdf-modal\.js\?v=([^"\']+)', body)
        ver = m.group(1) if m else "NONE"
        print(f"Attempt {i+1}: {ver}")
        if 'v38' in ver:
            print("SUCCESS! v38 is live!")
            exit(0)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(3)
