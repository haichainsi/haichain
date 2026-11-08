import os, shutil

# 1. Update pdf-modal.js
for path in ['pdf-modal.js', 'app/pdf-modal.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("const versionParam = '?v=v31_perfect_10lang_audit';",
                              "const versionParam = '?v=v32_ai2_title_math_fixed';")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update index.html and app/index.html
for path in ['index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('/app/pdf-modal.js?v=v52_mobile_clean_and_cors',
                              '/app/pdf-modal.js?v=v53_ai2_title_math_fixed')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update dashboard.html and app/dashboard.html
for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('/app/pdf-modal.js?v=v52_mobile_clean_and_cors',
                              '/app/pdf-modal.js?v=v53_ai2_title_math_fixed')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("[OK] Successfully bumped version cache-busters across pdf-modal.js, index.html, and dashboard.html")
