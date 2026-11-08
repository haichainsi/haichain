import sys, re, glob, os
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob("HAICHAIN_WHITEPAPER_V1.0_*.md")):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Ensure blank line after $$...$$
    text = re.sub(r'(\$\$.*?\$\$)\n(?!\n)', r'\1\n\n', text)
    # Ensure blank line before $$...$$
    text = re.sub(r'(?<!\n)\n(\$\$.*?\$\$)', r'\n\n\1', text)
    # Normalize 3+ newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)
    
    app_f = os.path.join("app", fname)
    with open(app_f, 'w', encoding='utf-8') as f:
        f.write(text)

print("[OK] Enforced blank lines around all $$...$$ display math.")
