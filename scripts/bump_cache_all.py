import os, re

NEW_VERSION = "v62_institutional_tables_math_fixed_20261103_final"

# 1. Bump app/pdf-modal.js
pdf_modal_path = "app/pdf-modal.js"
with open(pdf_modal_path, "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r'const versionParam = [\'"][^\'"]*[\'"];', f"const versionParam = '?v={NEW_VERSION}';", text)
with open(pdf_modal_path, "w", encoding="utf-8") as f:
    f.write(text)
print(f"Updated {pdf_modal_path} with {NEW_VERSION}")

# 2. Bump dashboard.html and index.html
for fname in ["dashboard.html", "index.html"]:
    with open(fname, "r", encoding="utf-8") as f:
        t = f.read()

    t = re.sub(r'src=["\']/app/pdf-modal\.js(\?v=[^"\']*)?["\']', f'src="/app/pdf-modal.js?v={NEW_VERSION}"', t)
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(t)
    print(f"Updated {fname} with {NEW_VERSION}")
