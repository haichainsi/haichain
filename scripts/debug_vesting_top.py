import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'const VESTING_VAULT_I18N =' in line:
        print(''.join(lines[i:i+35]))
        break
