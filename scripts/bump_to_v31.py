import re

for path in ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'pdf-modal\.js\?v=[^"\'>\s]+', 'pdf-modal.js?v=v31_perfect_10lang_audit', text)
    text = re.sub(r'i18n\.js\?v=[^"\'>\s]+', 'i18n.js?v=v31_perfect_10lang_audit', text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Bumped cachebusters in {path}')
