import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'copiedToken2022Alert' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[i-5:i+15]))
        break
