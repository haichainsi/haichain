with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

is_vi_lines = []
for idx, l in enumerate(lines, 1):
    if 'isVi' in l:
        is_vi_lines.append((idx, l.strip()))

print(f"Total lines with isVi in dashboard.html: {len(is_vi_lines)}")
for idx, l in is_vi_lines[:50]:
    print(f"L{idx}: {l[:120]}")
