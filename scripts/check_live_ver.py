import urllib.request
import re
import time

url = f'https://haichain.si/dashboard.html?nocache={int(time.time()*1000)}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as res:
        content = res.read().decode('utf-8')
        m = re.findall(r'/app/sale-controller\.js\?v=[^\"]+', content)
        print('Live sale-controller script version:', m)
except Exception as e:
    print('Error:', e)
