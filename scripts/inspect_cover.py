with open('generate_pdf_whitepapers.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# look for cover or title page
cover_match = re.search(r'cover.*?(?=</section>|</div>|$)', text, re.DOTALL | re.IGNORECASE)
if cover_match:
    print("Cover snippet:")
    print(cover_match.group(0)[:800])
else:
    print("No cover section, searching for logo")
    for m in re.finditer(r'<div[^>]*class="[^"]*cover[^"]*"[^>]*>.*?(?=</div>)', text, re.DOTALL | re.IGNORECASE):
        print(m.group(0)[:400])
