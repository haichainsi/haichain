import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

srcs = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', text)
print(f"External scripts in dashboard.html ({len(srcs)}):")
for s in srcs:
    print(" ", s)
