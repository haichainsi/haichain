import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"=== {fname} ===")
    for i, line in enumerate(lines):
        if re.search(r'(\$?A(?:I)?\^|AI\^2|AI²|\$\\mathbf\{AI\^2\})', line):
            print(f"  Line {i+1}: {line.strip()}")
