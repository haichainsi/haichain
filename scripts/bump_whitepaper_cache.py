import sys, re

NEW_PDF_VERSION = "?v=v33_global_no_qr_clean_math"
NEW_SCRIPT_TAG_VERSION = "?v=v63_global_no_qr_clean_math_20261103"

# 1. Update pdf-modal.js and app/pdf-modal.js
for fn in ['pdf-modal.js', 'app/pdf-modal.js']:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'const versionParam = \'\?v=[^\']+\';', f"const versionParam = '{NEW_PDF_VERSION}';", content)
    
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated version in {fn}")

# 2. Update html files script tags for pdf-modal.js
for fn in ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<script src="(/app/)?pdf-modal\.js\?v=[^"]+"></script>',
        f'<script src="/app/pdf-modal.js{NEW_SCRIPT_TAG_VERSION}"></script>',
        content
    )
    
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated pdf-modal script tag in {fn}")

print("Cache bump complete.")
