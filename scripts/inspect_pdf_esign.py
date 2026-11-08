import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('HAICHAIN_ACTIVE_SAFT')
print(c[idx-800:idx+1500])
