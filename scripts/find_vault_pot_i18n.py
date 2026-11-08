import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    t = f.read()

for k in ['vault.activePot', 'vault.actionCredits']:
    ms = re.findall(rf'[\'"]{re.escape(k)}[\'"]\s*:\s*[\'"][^\'"]+[\'"]', t)
    print(k, ":")
    for m in set(ms):
        print("  ", m)
