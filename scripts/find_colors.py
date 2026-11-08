with open('scripts/gdocs.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'#[0-9a-fA-F]{3,6}|rgb\([^)]+\)', text)
print("Found colors:", set(matches[:30]))
