import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('btn-tray-metamask')
print("btn-tray-metamask HTML:")
print(text[idx-100:idx+800])

idx_js = text.find('btn-tray-metamask-app')
print("\nJS for btn-tray-metamask-app:")
print(text[idx_js-100:idx_js+800])
