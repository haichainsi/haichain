import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderVestingVaultPage')
if idx != -1:
    print("Found in dashboard.html at", idx)
    print(text[idx:idx+1500])
else:
    print("Not in dashboard.html, checking other files...")
    import os
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.js') and not 'node_modules' in root and not '.git' in root:
                p = os.path.join(root, file)
                try:
                    c = open(p, 'r', encoding='utf-8').read()
                    if 'renderVestingVaultPage' in c:
                        print(f"FOUND IN: {p}")
                except:
                    pass
