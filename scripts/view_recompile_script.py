import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/recompile_all_10_pdfs.py', 'r', encoding='utf-8') as f:
    c = f.read()

print(c)
