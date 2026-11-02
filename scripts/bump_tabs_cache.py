import os, time

files = ['dashboard.html', 'app/dashboard.html']
new_ver = f"v37_clean_tabs_{int(time.time() * 1000)}"

for fp in files:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace i18n.js?v=...
    old_tag = '<script src="/app/i18n.js?v=v36_no_numbering_1793635991842"></script>'
    new_tag = f'<script src="/app/i18n.js?v={new_ver}"></script>'

    if old_tag in c:
        c = c.replace(old_tag, new_tag)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Bumped cache-buster in:", fp)
    else:
        # Fallback regex
        import re
        c = re.sub(r'src="(/app/i18n\.js\?v=[^"]+)"', f'src="/app/i18n.js?v={new_ver}"', c)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Bumped with regex in:", fp)
