import re

print("Inspecting dashboard.html lines 3845-4040...")
with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's locate the exact section
start_idx = text.find("// 2. PHANTOM WALLET")
end_idx = text.find("// 4. MANUAL ADDRESS (Show/Hide Input with Clipboard Paste)")

print("Found section:", start_idx, end_idx)
print("Section snippet:\n", text[start_idx:start_idx+300])
