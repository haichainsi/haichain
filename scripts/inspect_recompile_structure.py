import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/recompile_all_10_pdfs.py', 'r', encoding='utf-8') as f:
    c = f.read()

print("recompile_all_10_pdfs.py structure:")
lines = c.splitlines()
for i, line in enumerate(lines[:120]):
    print(f"{i+1}: {line}")
