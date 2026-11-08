import sys, re
sys.stdout.reconfigure(encoding='utf-8')

OLD_V = '?v=v33_global_no_qr_clean_math'
NEW_V = '?v=v65_institutional_tables_math_fixed_20261103'

# 1. Update pdf-modal.js and app/pdf-modal.js
for path in ['pdf-modal.js', 'app/pdf-modal.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if OLD_V in content:
        content = content.replace(OLD_V, NEW_V)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {path} with {NEW_V}')
    else:
        print(f'Pattern not found in {path}')

# 2. Update script tags in index.html, dashboard.html, app/index.html, app/dashboard.html
files_to_update = ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html']
for path in files_to_update:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace pdf-modal.js?v=...
    new_content = re.sub(r'pdf-modal\.js\?v=[^\"]+', f'pdf-modal.js{NEW_V}', content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated script tag in {path}')
    else:
        print(f'No script tag changed in {path}')
