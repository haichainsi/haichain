import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for i in range(min(50, len(lines))):
    if 'const' in lines[i] or 'let' in lines[i] or 'var' in lines[i] or 'window.' in lines[i]:
        print(f"L{i+1}: {lines[i].strip()}")

print("\n--- Last 50 lines variable declarations ---")
for i in range(max(0, len(lines)-50), len(lines)):
    if 'const' in lines[i] or 'let' in lines[i] or 'var' in lines[i] or 'window.' in lines[i]:
        print(f"L{i+1}: {lines[i].strip()}")
