import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'vault.status.frozen' in line or 'vault.status.active' in line:
        print(f"Line {i+1}: {line.strip()}")
