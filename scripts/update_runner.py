with open('scripts/test_browser_modal2.py', 'r', encoding='utf-8') as f:
    code = f.read()

code += """
import re
m = re.search(r'<pre id="test-output"[^>]*>(.*?)</pre>', out_text, re.DOTALL)
if m:
    print("LOGS IN DOM:")
    print(m.group(1))
"""

with open('scripts/test_browser_modal2.py', 'w', encoding='utf-8') as f:
    f.write(code)
