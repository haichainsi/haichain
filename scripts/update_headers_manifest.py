import re

with open('_headers', 'r', encoding='utf-8') as f:
    text = f.read()

# Update manifest cache control
text = re.sub(
    r'/manifest\.json\s+Content-Type:[^\n]+\s+Cache-Control:[^\n]+',
    '/manifest.json\n  Content-Type: application/manifest+json; charset=utf-8\n  Cache-Control: public, max-age=0, must-revalidate, no-cache',
    text
)
text = re.sub(
    r'/site\.webmanifest\s+Content-Type:[^\n]+\s+Cache-Control:[^\n]+',
    '/site.webmanifest\n  Content-Type: application/manifest+json; charset=utf-8\n  Cache-Control: public, max-age=0, must-revalidate, no-cache',
    text
)

with open('_headers', 'w', encoding='utf-8') as f:
    f.write(text)

with open('app/_headers', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated _headers and app/_headers")
