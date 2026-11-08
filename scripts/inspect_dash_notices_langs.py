with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'const DASH_NOTICES_I18N = \{([\s\S]*?)\n\s*\};', text)
if m:
    dict_content = m.group(1)
    langs = re.findall(r'^\s*["\']?([a-z]{2})["\']?:\s*\{', dict_content, re.MULTILINE)
    print("Languages in DASH_NOTICES_I18N:", langs)
else:
    print("DASH_NOTICES_I18N not found")
