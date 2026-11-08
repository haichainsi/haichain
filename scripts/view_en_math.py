import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if i >= 1330 and '$$' in line:
        print(f"EN L{i+1}: {repr(line)}")
