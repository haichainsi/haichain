import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(6390, 6405):
    print(f'{j+1}: {lines[j].rstrip()}')
