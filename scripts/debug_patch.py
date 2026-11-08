import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('guaranteeTitle in c:', 'guaranteeTitle' in c)
print('<!-- 4 Executive KPI Cards -->' in c)
