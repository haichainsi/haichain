import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'const btnPayPhantom = container.querySelector(\'#btn-pay-phantom-1click\');' in line:
        print(f"Found btnPayPhantom at line {i+1}")
        print(''.join(lines[i:i+150]))
        break
