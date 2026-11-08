import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(580, 620):
    if i < len(lines):
        print(f"{i+1}: {repr(lines[i])}")
