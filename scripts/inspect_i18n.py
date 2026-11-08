import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'refProgramTitle' in l and i > 125:
        for j in range(max(0, i-5), min(len(lines), i+30)):
            print(f'{j+1}: {lines[j].rstrip()}')
        break
