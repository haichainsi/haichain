with open('app/pdf-modal.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'saft-sign-overlay' in l:
        print(f'{i+1}: {l.strip()[:100]}')
