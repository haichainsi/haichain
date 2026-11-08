with open("dashboard.html", "r", encoding="utf-8") as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'function.*passkey|passkey.*click|authenticateWithPasskey', c, re.I)]
print("Matches found:", len(matches))
for pos in matches[:5]:
    print("--- SNIPPET ---")
    print(c[max(0, pos-100):min(len(c), pos+300)])
