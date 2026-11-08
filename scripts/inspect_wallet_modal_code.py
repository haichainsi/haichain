import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'id="wallet-btn"' in line or 'id="wallet-modal"' in line or 'wallet-btn' in line:
        print(f"Line {idx+1}: {line.strip()}")
        # print next 20 lines
        for j in range(idx, min(len(lines), idx+30)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        print("-" * 50)
