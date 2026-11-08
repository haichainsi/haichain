import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
    c = f.read()

print("Length of HAICHAIN_WHITEPAPER_V1.0_EN.md:", len(c))
print(c[:2000])
