import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'vaultStatusBadge' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[max(0, i-2):min(len(lines), i+8)]))
