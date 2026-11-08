import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_dict = False
langs = []
for line in lines:
    if 'const VESTING_VAULT_I18N =' in line:
        in_dict = True
        continue
    if in_dict:
        if line.strip().startswith('function ') or line.strip() == '};':
            break
        stripped = line.strip()
        if stripped.endswith('{') and len(stripped) <= 8 and ':' in stripped:
            langs.append(stripped.split(':')[0].strip(' "\''))

print("Found langs in VESTING_VAULT_I18N:", langs)
