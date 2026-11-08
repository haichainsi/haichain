import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('v6.9.3 L1 Core')
print(text[idx-300:idx+300])
