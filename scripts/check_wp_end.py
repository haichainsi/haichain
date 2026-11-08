import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
    c = f.read()

lines = c.splitlines()
print(f'Total lines: {len(lines)}')
print('Last 30 lines:')
print('\n'.join(lines[-30:]))
