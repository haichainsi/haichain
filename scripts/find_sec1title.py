import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, line in enumerate(lines):
    if 'dev.sec1Title' in line:
        print(f"Line {i+1}: {line.strip()[:120]}")
