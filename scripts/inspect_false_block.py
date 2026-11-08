import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'if (false) {' in line:
        print(f"Found if (false) at line {i+1}")
        print(''.join(lines[i-5:i+60]))
        break
