with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'dash-confirm-deposit-btn', text)]
print(f"Occurrences of dash-confirm-deposit-btn: {len(matches)}")

for i, pos in enumerate(matches):
    print(f"\n--- Occurrence {i} at character {pos} ---")
    start = max(0, pos - 100)
    end = min(len(text), pos + 2500)
    print(text[start:end])
