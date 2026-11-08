with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'languageChanged' in l:
        print(f"L{idx}: {l.strip()}")
        # print next 25 lines
        for j in range(idx, min(idx + 35, len(lines))):
            print(f"  L{j+1}: {lines[j].rstrip()}")
