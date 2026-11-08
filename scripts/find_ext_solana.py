with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if 'external solana' in line.lower():
        print(line.strip())
