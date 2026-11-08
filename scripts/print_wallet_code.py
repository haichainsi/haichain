import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== LINES 4150 - 4210 ===")
print(''.join(lines[4149:4210]))
