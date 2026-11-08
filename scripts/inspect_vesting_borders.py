import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderVestingVaultPage')
end_idx = text.find('window.renderVestingVaultPage', idx)
vesting_code = text[idx:end_idx]

for line in vesting_code.splitlines():
    if 'border' in line and not line.strip().startswith('//'):
        print(line.strip())
