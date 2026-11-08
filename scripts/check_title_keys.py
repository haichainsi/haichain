import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r'"[^"]*title[^"]*":\s*"[^"]+"', text, re.I)
for line in m:
    if 'haichain' in line.lower() or 'economic' in line.lower() or 'superintelligence' in line.lower():
        print(line)
