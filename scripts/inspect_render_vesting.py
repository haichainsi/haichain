with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function renderVestingVaultPage')
if idx != -1:
    print("Found renderVestingVaultPage at", idx)
    print(c[idx:idx+3500])
else:
    idx2 = c.find('renderVestingVaultPage')
    print("renderVestingVaultPage at", idx2)
    print(c[idx2:idx2+1000])
