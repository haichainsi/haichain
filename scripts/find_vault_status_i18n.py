import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['dashboard.html', 'app/dashboard.html', 'i18n.js', 'app/i18n.js']:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            t = f.read()
        ms = re.findall(r'[\'"]vault\.status\.[^\'"]+[\'"]\s*:\s*[\'"][^\'"]+[\'"]', t)
        print(f"{fpath}: found {len(ms)} matches")
        for m in sorted(set(ms)):
            print("  ", m)
    except Exception as e:
        print(fpath, e)
