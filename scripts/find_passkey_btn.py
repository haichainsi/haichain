import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('vault.touchPasskey')
print("Surrounding HTML:")
print(text[idx-200:idx+300])

# Find the button ID or tag
btn_match = re.search(r'<button[^>]*>.*?vault\.touchPasskey.*?</button>', text, re.DOTALL)
if btn_match:
    print("\nFull Button Tag:")
    print(btn_match.group(0))

# Find script references to this button
for line in text.splitlines():
    if 'touchPasskey' in line or 'passkey-refresh' in line or 'refresh-passkey' in line or 'Touch Passkey' in line:
        print("Script line:", line.strip())
