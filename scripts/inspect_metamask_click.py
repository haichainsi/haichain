import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('data-provider="metamask"')
print("Metamask button click handler search:")
idx2 = text.find("provider === 'metamask'")
if idx2 != -1:
    print(text[idx2-100:idx2+600])
else:
    idx3 = text.find("'metamask'")
    print("Found 'metamask' at", idx3)
    print(text[idx3-50:idx3+600])
