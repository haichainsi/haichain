import sys
import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1809, 2008):
    line = lines[i]
    # Check if there is any </div>
    div_opens = len(re.findall(r'<div\b', line))
    div_closes = len(re.findall(r'</div>', line))
    btn_opens = len(re.findall(r'<button\b', line))
    btn_closes = len(re.findall(r'</button>', line))
    if div_opens != div_closes or btn_opens != btn_closes or 'Custom Solana' in line:
        print(f"L{i+1:4d} (div:+{div_opens}/-{div_closes}, btn:+{btn_opens}/-{btn_closes}): {line.strip()[:80]}")
