import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

s_idx = 0
for idx, l in enumerate(lines):
    if "STATE 3: Active Allocation found" in l or "const haiTotal = alloc.haiTokens" in l:
        s_idx = idx
        break

print('\n'.join(lines[s_idx:s_idx+120]))
