import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'id="pdf-modal-lang-dropdown".*?</div>', text, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("Not found")
