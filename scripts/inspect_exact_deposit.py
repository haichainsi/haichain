import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

s_idx = 0
for idx, l in enumerate(lines):
    if "const rawBalance = await solanaConnection.getBalance" in l:
        s_idx = idx
        break

print('\n'.join(lines[s_idx:s_idx+80]))
