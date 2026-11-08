import re

for fname in ['dashboard.html', 'index.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        t = f.read()
    matches = re.findall(r'<script[^>]*src=[\'"][^\'"]+\?v=[^\'"]+[\'"][^>]*>', t)
    print(f"=== {fname} ({len(matches)} versioned scripts) ===")
    for m in matches:
        print(" ", m)
