import re, time

ts = str(int(time.time()*1000))
new_v = f"v39_exact_small_text_{ts}"

for path in ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = re.sub(r'/app/i18n\.js\?v=[^"\'\s>]+', f'/app/i18n.js?v={new_v}', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f"Updated {path} -> {new_v}")
