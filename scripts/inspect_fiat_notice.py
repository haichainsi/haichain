import re, sys
sys.stdout.reconfigure(encoding='utf-8')

i18n = open('app/i18n.js', encoding='utf-8').read()
for m in re.finditer(r'[\'\"]fiatSandboxNotice[\'\"]\s*:\s*[\'\"]([^\'\"]+)[\'\"]', i18n):
    print(m.group(0))
