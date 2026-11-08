with open('scripts/dashboard_script_vi.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    # let's see which line numbers they are
    print(line.strip()[:140])
