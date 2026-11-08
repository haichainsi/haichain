import re, sys

with open("app/i18n.js", "r", encoding="utf-8") as f:
    text = f.read()

keys = ['marketplace.title', 'marketplace.badge', 'marketplace.subtitle', 'marketplace.registerBtn', 'marketplace.syncRegistries', 'marketplace.syncRegistriesShort']
for k in keys:
    matches = re.findall(r'"' + re.escape(k) + r'"\s*:\s*"((?:\\.|[^"\\])*)"', text)
    sys.stdout.buffer.write(f"Key {k} (count={len(matches)}):\n".encode('utf-8'))
    for m in matches[:2]:
        sys.stdout.buffer.write(f"   {m}\n".encode('utf-8'))
