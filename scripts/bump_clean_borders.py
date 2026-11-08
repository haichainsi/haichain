import re, time

ts = str(int(time.time() * 1000))
new_sc_ver = f"v28_borderless_clean_{ts}"
new_i18n_ver = f"v40_borderless_{ts}"

for path in ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'sale-controller\.js(\?v=[a-zA-Z0-9_\.]*)?', f'sale-controller.js?v={new_sc_ver}', content)
    content = re.sub(r'/app/i18n\.js\?v=[^"\'\s>]+', f'/app/i18n.js?v={new_i18n_ver}', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Bumped cache in {path}")
