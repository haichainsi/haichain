import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's check where consecutive string quotes occur without a comma:
# e.g., "..."\n\s*"..."
import re

matches = list(re.finditer(r'("[^"\n]+")\s*\n\s*("[^"\n]+"\s*:)', content))
print(f"Found missing commas between string lines: {len(matches)}")
for m in matches[:10]:
    print(repr(m.group(0)))
