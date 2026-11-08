import re

for filepath in ['i18n.js', 'app/i18n.js']:
    print(f"=== {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(r'"(playground\.demo[^"]+)":\s*"([^"]+)"', text)
    for k, v in matches:
        print(f"  {k}: {v}")
