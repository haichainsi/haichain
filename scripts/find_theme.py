with open('app/dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'theme' in l.lower() and ('dark' in l.lower() or 'light' in l.lower()):
        if len(l.strip()) < 120:
            print(f'{i+1}: {l.strip()}')
