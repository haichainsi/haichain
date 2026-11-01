import sys

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            modified = True
            print(f"Replaced '{old}' -> '{new}' in {filepath}")
        else:
            print(f"NOT FOUND: '{old}' in {filepath}")
            
    if modified:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f"Saved {filepath}")

# Update i18n.js and app/i18n.js
for path in ['i18n.js', 'app/i18n.js']:
    replace_in_file(path, [
        ('"nav.backToHome": "Back to Landing Page"', '"nav.backToHome": "Back to Home"')
    ])

# Update dashboard.html and app/dashboard.html
for path in ['dashboard.html', 'app/dashboard.html']:
    replace_in_file(path, [
        ('<!-- Back to Landing Page -->', '<!-- Back to Home -->'),
        ('<span data-i18n="nav.backToHome">Back to Landing Page</span>', '<span data-i18n="nav.backToHome">Back to Home</span>'),
        ('/app/i18n.js?v=v24_fast_mobile_wallet', '/app/i18n.js?v=v25_back_to_home')
    ])

# Update index.html and app/index.html cache version as well
for path in ['index.html', 'app/index.html']:
    replace_in_file(path, [
        ('/app/i18n.js?v=v24_fast_mobile_wallet', '/app/i18n.js?v=v25_back_to_home')
    ])

# Update temp_check.js if present
replace_in_file('temp_check.js', [
    ('<!-- Back to Landing Page -->', '<!-- Back to Home -->'),
    ('<span data-i18n="nav.backToHome">Back to Landing Page</span>', '<span data-i18n="nav.backToHome">Back to Home</span>')
])
