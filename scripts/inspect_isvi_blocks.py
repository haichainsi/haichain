with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'isVi' in l:
        print(f"\n=================== L{idx} ===================")
        start = max(0, idx - 3)
        end = min(len(lines), idx + 8)
        for i in range(start, end):
            print(f"{i+1}: {lines[i].rstrip()}")
