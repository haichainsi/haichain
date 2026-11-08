import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function renderVestingVaultPage()')
print(c[idx:idx+1500])
