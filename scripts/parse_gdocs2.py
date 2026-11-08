with open('scripts/gdocs.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Length:", len(text))
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print("Scripts count:", len(scripts))
body_match = re.search(r'<body[^>]*>(.*?)</body>', text, re.DOTALL)
if body_match:
    body = body_match.group(1)
    # remove scripts
    clean_body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
    print("Clean body:")
    print(clean_body[:1000])
