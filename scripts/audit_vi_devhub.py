import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

vi_chars = r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]'

# Check pre and code
pre_code = re.findall(r'<(?:pre|code)\b[^>]*>(.*?)</(?:pre|code)>', content, re.DOTALL | re.IGNORECASE)
found_in_code = [b.strip() for b in pre_code if re.search(vi_chars, b, re.IGNORECASE)]
print('Vietnamese in <pre>/<code> blocks count:', len(found_in_code))
for item in found_in_code:
    print('CODE ITEM WITH VI:\n', item[:120])

# Check tab-docs section
tab_docs_match = re.search(r'id=[\"\']tab-docs[\"\'].*?(?=id=[\"\']tab-[a-z]|\Z)', content, re.DOTALL)
if tab_docs_match:
    tab_text = tab_docs_match.group(0)
    steps = re.findall(r'Step\s+\d+:[^<]+', tab_text)
    print('Found steps in tab-docs:', len(steps))
    for s in steps:
        has_vi = bool(re.search(vi_chars, s, re.IGNORECASE))
        print(s.strip(), '| Has VI:', has_vi)
else:
    print('tab-docs not found')
