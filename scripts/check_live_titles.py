import urllib.request
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://haichain.si', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as res:
    html = res.read().decode('utf-8', errors='ignore')

m = re.findall(r'<h3[^>]*data-i18n="advantages\.item\dTitle"[^>]*>([^<]+)</h3>', html)
print("Advantage titles in live HTML:")
for t in m:
    print(" -", t.strip())

req_js = urllib.request.Request('https://haichain.si/app/i18n.js?v=v36_no_numbering_1793635991842', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req_js) as res:
    js = res.read().decode('utf-8', errors='ignore')

print("\nAdvantage titles in live i18n.js (vi):")
for k in ['advantages.item1Title', 'advantages.item2Title', 'advantages.item3Title', 'advantages.item4Title']:
    matches = re.findall(rf'"{k}": "([^"]+)"', js)
    print(k, matches)
