import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if line.strip().startswith('"vi": {') and i > 4000:
        print(''.join(lines[i:i+45]))
        break
