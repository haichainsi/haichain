import re, time

ts = str(int(time.time() * 1000))
new_ver = f"v41_passkey_toast_fix_{ts}"

for path in ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'/app/i18n\.js\?v=[^"\'\s>]+', f'/app/i18n.js?v={new_ver}', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Bumped cache in {path}")
