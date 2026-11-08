import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all buttons
button_tags = re.findall(r'<button([^>]*)>', text)
print(f"Total buttons found: {len(button_tags)}")

button_ids = []
for b in button_tags:
    m = re.search(r'id=["\']([^"\']+)["\']', b)
    if m:
        button_ids.append(m.group(1))

print(f"Buttons with IDs ({len(button_ids)}):")
for bid in button_ids:
    # Check if there is an addEventListener or onclick for this ID in text
    has_listener = f"'{bid}'" in text or f'"{bid}"' in text
    print(f"  - {bid} (found in script: {has_listener})")

print("\n--- Wallet Connection Logic ---")
for line in text.splitlines():
    if any(k in line.lower() for k in ['window.solana', 'phantom', 'solflare', 'connectwallet', 'disconnect', 'getbalance']):
        print(" ", line.strip()[:140])
