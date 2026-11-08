import re

files = ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html']

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    
    txt = re.sub(r'pdf-modal\.js\?v=[^\"]+', 'pdf-modal.js?v=v42_saft_telegram_live_1793650000000', txt)
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(txt)
    print("Bumped cache in", p)
