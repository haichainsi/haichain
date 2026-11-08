with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function renderVestingVaultPage')
if idx != -1:
    print(c[idx+3000:idx+8000])
