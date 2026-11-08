import urllib.request, time, re

url = f"https://haichain.si/?t={int(time.time())}"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

m = re.search(r'<section id="comparison"[\s\S]*?</section>', html)
if m:
    print("Found comparison section on live:\n")
    print(m.group(0)[:600])
else:
    print("Comparison section NOT found!")

m_title = re.search(r'<h2[^>]*data-i18n="comp\.title"[^>]*>([\s\S]*?)</h2>', html)
if m_title:
    print("\nLive h2 text:")
    print(m_title.group(1).strip())
