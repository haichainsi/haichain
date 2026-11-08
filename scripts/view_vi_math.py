import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if i >= 1180 and '$$' in line:
        print(f"L{i+1}: {repr(line)}")
