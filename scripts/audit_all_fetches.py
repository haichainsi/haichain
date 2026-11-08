import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

fetches = re.findall(r'fetch\s*\(([^)]+)\)', text)
print(f"Total fetch calls in dashboard.html: {len(fetches)}")
for f in set(fetches):
    print(" ", f.strip()[:100])
