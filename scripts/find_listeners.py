import sys, re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'window\.addEventListener\([^\)]+\)', c)
print('Window event listeners:', matches)
matches2 = re.findall(r'document\.addEventListener\([^\)]+\)', c)
print('Document event listeners:', matches2)
