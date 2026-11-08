import re

files = ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html']

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'pdf-modal\.js\?v=[^\'">\s]+', 'pdf-modal.js?v=v69_saft_resend_dual_email_20261104', content)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Bumped cachebuster in {fp}')
