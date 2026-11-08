import sys

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\b(?:en|fr|es|ru|zh|ko|hi|he|vi|kk)\b\s*:\s*\{)', text)
print("Language block headers found:", matches)
