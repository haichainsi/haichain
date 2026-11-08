with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'isVi' in l:
        print(f"L{idx}: {l.strip()[:100]}")
        # print next 3 lines
        for j in range(idx, min(idx + 4, len(lines))):
            print(f"   {lines[j].rstrip()[:100]}")
