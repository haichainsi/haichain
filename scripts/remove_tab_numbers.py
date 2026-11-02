import os, re

files_i18n = ['i18n.js', 'app/i18n.js']
files_html = ['dashboard.html', 'app/dashboard.html']

# 1. Patch i18n files across all 10 languages
for fp in files_i18n:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove "1. ", "2. ", "3. " from aiHub.tabDesktop, aiHub.tabOnline, aiHub.tabWeb
    content = re.sub(r'("aiHub\.tabDesktop":\s*")[0-9]+\.\s*', r'\1', content)
    content = re.sub(r'("aiHub\.tabOnline":\s*")[0-9]+\.\s*', r'\1', content)
    content = re.sub(r'("aiHub\.tabWeb":\s*")[0-9]+\.\s*', r'\1', content)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated i18n:", fp)

# 2. Patch HTML files fallback text
for fp in files_html:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('data-i18n="aiHub.tabDesktop">1. Desktop App<', 'data-i18n="aiHub.tabDesktop">Desktop App<')
    content = content.replace('data-i18n="aiHub.tabOnline">2. Claude Mobile<', 'data-i18n="aiHub.tabOnline">Claude Mobile<')
    content = content.replace('data-i18n="aiHub.tabWeb">3. Web Direct<', 'data-i18n="aiHub.tabWeb">Web Direct<')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated HTML:", fp)
