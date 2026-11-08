import re

ts = "1793637895707"
new_v = f"v38_sync_small_text_{ts}"

for path in ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = re.sub(r'/app/i18n\.js\?v=[^"\'\s>]+', f'/app/i18n.js?v={new_v}', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f"Updated {path} -> {new_v}")
