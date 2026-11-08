import re

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'(\"[a-z]{2}\":\s*\{)', text)
print('Double quoted lang keys:', len(matches), matches)

matches2 = re.findall(r'(\'[a-z]{2}\':\s*\{)', text)
print('Single quoted lang keys:', len(matches2), matches2)

matches3 = re.findall(r'(\b[a-z]{2}:\s*\{)', text)
print('Bare lang keys:', len(matches3), matches3[:10])
