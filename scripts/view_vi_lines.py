import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(965, 985):
    print(f"{i+1}: {repr(lines[i])}")
