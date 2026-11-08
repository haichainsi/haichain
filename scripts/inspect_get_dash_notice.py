with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'function getDashNotice' in l or 'const getDashNotice' in l:
        print(f"L{idx}: {l.strip()}")
        for j in range(idx, min(idx + 25, len(lines))):
            print(f"  L{j+1}: {lines[j].rstrip()}")
        break
