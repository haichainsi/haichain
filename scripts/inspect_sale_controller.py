import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app/sale-controller.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(''.join(lines[1150:1280]))
