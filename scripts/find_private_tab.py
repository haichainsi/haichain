import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

tabs = set(re.findall(r'data-tab="([^"]*)"', text))
print("All data-tabs in dashboard.html:", tabs)

# Search for "SAFT"
print("\nSAFT occurrences:")
for m in re.finditer(r'SAFT', text, re.IGNORECASE):
    idx = m.start()
    print(text[idx-50:idx+150])
    print("-" * 40)
