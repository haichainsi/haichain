import re, sys
sys.stdout.reconfigure(encoding='utf-8')

dash = open('dashboard.html', encoding='utf-8').read()

print("=== APPLE PAY OCCURRENCES ===")
for m in re.finditer(r'.{0,100}apple pay.{0,100}', dash, re.IGNORECASE):
    print("MATCH:", repr(m.group(0).strip()))

print("\n=== FIAT TOP UP / ON RAMP MODAL ===")
for m in re.finditer(r'id=[\"\'][^\"\']*fiat[^\"\']*[\"\']|id=[\"\'][^\"\']*deposit[^\"\']*[\"\']', dash, re.IGNORECASE):
    print("ID:", m.group(0))
