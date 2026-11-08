with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'function renderVestingVaultPage' in l:
        print(f"L{idx}: {l.strip()}")
        for j in range(idx, min(idx + 60, len(lines))):
            print(f"  L{j+1}: {lines[j].rstrip()}")
        break
