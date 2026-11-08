import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('dashboard.html length:', len(text))
print('Has VESTING_VAULT_I18N:', 'const VESTING_VAULT_I18N =' in text)
print('Has renderVestingVaultPage:', 'function renderVestingVaultPage()' in text)
