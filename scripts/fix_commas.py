with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Replace string ending followed by new key without comma
fixed_content = re.sub(r'("[^"\n]+")(\s*\n\s*"[^"\n]+"\s*:)', r'\1,\2', content)

with open('i18n.js', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

with open('app/i18n.js', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print("Fixed missing commas in i18n.js and app/i18n.js")
