import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

s = '<section id="tab-docs"'
e = '</section>'
idx_s = text.find(s)
idx_e = text.find(e, idx_s)
tab_docs = text[idx_s:idx_e+len(e)]
print(f"tab-docs length: {len(tab_docs)} chars")

# Find all data-i18n keys
keys = re.findall(r'data-i18n=["\']([^"\']+)["\']', tab_docs)
print(f"\n--- Found {len(keys)} data-i18n keys in tab-docs ---")
for k in keys:
    print(" ", k)

# Check all text nodes in tab-docs that do NOT have data-i18n and are not within pre/code/script
# Let's see lines that contain text outside code tags
print("\n--- Scanning for text lines without data-i18n in tab-docs ---")
lines = tab_docs.splitlines()
in_code = False
for line in lines:
    stripped = line.strip()
    if '<pre' in stripped or '<code' in stripped or '<script' in stripped:
        in_code = True
    if in_code:
        if '</pre>' in stripped or '</code>' in stripped or '</script>' in stripped:
            in_code = False
        continue
    
    # Check if there is plain text inside HTML tags
    clean = re.sub(r'<[^>]+>', ' ', stripped).strip()
    if clean and not stripped.startswith('<!--') and 'data-i18n' not in stripped:
        if len(clean) > 3 and not clean.startswith('{') and not clean.startswith('//'):
            print("  NO-I18N:", clean[:100])
