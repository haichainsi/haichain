with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if 'account-sync-browser-text' in l:
        print(f"L{idx}: {l.strip()}")
