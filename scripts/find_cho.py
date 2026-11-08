import re, sys

for fname in ["app/i18n.js", "i18n.js", "dashboard.html", "app/dashboard.html"]:
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    matches = re.findall(r'[^"\n]*chợ[^"\n]*', text, re.IGNORECASE)
    sys.stdout.buffer.write(f"File {fname}: found {len(matches)} occurrences of 'chợ'\n".encode('utf-8'))
    for m in matches:
        sys.stdout.buffer.write(f"  -> {m.strip()}\n".encode('utf-8'))
