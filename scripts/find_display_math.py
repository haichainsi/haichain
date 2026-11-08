import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'r', encoding='utf-8') as f:
    text = f.read()

display_math = re.findall(r'(\$\$.*?\$\$)', text, flags=re.DOTALL)
print(f"Total display math blocks in VI: {len(display_math)}")
for i, dm in enumerate(display_math):
    print(f"--- Block {i+1} ---")
    print(dm.strip())
