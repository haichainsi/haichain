with open('generate_pdf_whitepapers.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'class="cover-page".*?(?=class="page"|\Z)', text, re.DOTALL)
if m:
    print(m.group(0)[:1500])
else:
    print("Cover page not found with that class, searching for cover")
    m2 = re.search(r'<div class="cover[^"]*".*?</div>', text, re.DOTALL)
    if m2:
        print(m2.group(0)[:1000])
