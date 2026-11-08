import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find("fetch('/api/saft/submit'")
print(c[idx:idx+2500])
