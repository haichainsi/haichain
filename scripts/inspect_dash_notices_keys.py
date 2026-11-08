with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re, json
m = re.search(r'const DASH_NOTICES_I18N = (\{[\s\S]*?\n\s*\});', text)
if m:
    dict_str = m.group(1)
    # Parse keys of 'en'
    en_m = re.search(r'["\']en["\']:\s*\{([\s\S]*?)\n\s*\},', dict_str)
    if en_m:
        keys = re.findall(r'["\']?([a-zA-Z0-9_]+)["\']?:\s*', en_m.group(1))
        print(f"Total keys in DASH_NOTICES_I18N['en']: {len(keys)}")
        print("Keys:", sorted(list(set(keys))))
