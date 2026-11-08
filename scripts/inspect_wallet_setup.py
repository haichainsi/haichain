import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("MetaMask matches in dashboard.html:")
for m in re.finditer(r'metamask', text, re.IGNORECASE):
    idx = m.start()
    print(text[idx-60:idx+150])
    print("-" * 40)

# Check phantom-deeplink.js
print("\nChecking assets/phantom-deeplink.js...")
try:
    with open('assets/phantom-deeplink.js', 'r', encoding='utf-8') as f:
        pjs = f.read()
    print("phantom-deeplink.js length:", len(pjs))
    print(pjs[:800])
except Exception as e:
    print("Error reading phantom-deeplink.js:", e)
