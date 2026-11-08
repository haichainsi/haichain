import sys, re, glob, os
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob("HAICHAIN_WHITEPAPER_V1.0_*.md")):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Fix broken HaiChain formula
    text = re.sub(r'\$\$\\mathbf\{HaiChain\}\s*\\iff\s*\\mathbf\{AI²\}\s*=\s*\\text\{ARTIFICIAL INTELLIGENCE\}\s*\\times\s*\\text\{ACTUAL INTELLIGENCE(?:\s*\(.*?\))?\}\s*\n*\s*\$\$',
                  r'$$\\mathbf{HaiChain} \\iff \\mathbf{AI²} = \\text{ARTIFICIAL INTELLIGENCE} \\times \\text{ACTUAL INTELLIGENCE}$$', text)
    
    # Copy to app
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)
    
    app_f = os.path.join("app", fname)
    with open(app_f, 'w', encoding='utf-8') as f:
        f.write(text)

print("[OK] Cleaned HaiChain formula and synced to app/")
