import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function renderVestingVaultPage()')
idx_end = c.find('function getStoredAllocations', idx)
print(f"renderVestingVaultPage length: {idx_end - idx}")
s1 = c.find('// STATE 1:', idx)
s2 = c.find('// STATE 2:', idx)
s3 = c.find('// STATE 3:', idx)
print("State 1 at", s1, "State 2 at", s2, "State 3 at", s3, "End at", idx_end)
