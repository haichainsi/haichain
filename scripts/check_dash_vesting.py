import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Lines 6370-6430 in dashboard.html:')
for i in range(6365, min(len(lines), 6430)):
    print(f'{i+1}: {lines[i].rstrip()}')
