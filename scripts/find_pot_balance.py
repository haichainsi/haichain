import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for KHO QUỸ or 20.0000 or spending pot
for line_no, line in enumerate(text.splitlines(), 1):
    if any(k in line for k in ['20.0000', '25.0000', 'Kho Quỹ Đang Hoạt Động', 'dash.activePot', 'spending_pot', 'haichain_vault_balance', 'localStorage']):
        print(f"{line_no}: {line.strip()[:140]}")
