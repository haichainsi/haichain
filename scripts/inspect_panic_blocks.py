import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('=== BLOCK 1 (Lines 2200-2245) ===')
print(''.join(lines[2200:2245]))

print('=== BLOCK 2 (Lines 2610-2665) ===')
print(''.join(lines[2610:2665]))
