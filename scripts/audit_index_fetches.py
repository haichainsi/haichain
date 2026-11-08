import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

fetches = re.findall(r'fetch\s*\(([^)]+)\)', text)
print(f"Total fetch calls in index.html: {len(fetches)}")
for f in set(fetches):
    print(" ", f.strip()[:100])
