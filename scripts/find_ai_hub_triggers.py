import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'ai-hub', text)
print("ai-hub mentions:", len(matches))

# Find buttons that trigger ai hub
btns = re.findall(r'<button[^>]*ai-hub[^>]*>.*?</button>', text, re.DOTALL)
for b in btns:
    print("Button:", b[:200])

# Check JS handlers for ai-hub
js_handlers = re.findall(r'.*ai-hub.*', text)
for j in js_handlers[:10]:
    print("JS:", j.strip())
