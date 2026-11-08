import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_idx = text.find('function renderVestingVaultPage()')
print(text[s_idx+2500:s_idx+5500])
