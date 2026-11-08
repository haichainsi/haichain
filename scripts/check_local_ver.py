import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()
m = re.search(r'i18n\.js\?v=([^"\'>\s]+)', c)
print("Local dashboard i18n:", m.group(1) if m else "None")
