import re

files = ['dashboard.html', 'index.html', 'sale-controller.js', 'app/sale-controller.js']
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {fpath} ===")
    matches = re.finditer(r'(?:kết nối ví|connect\s*wallet|connect\s*web3|kết nối web3|web3)', text, re.IGNORECASE)
    lines = text.split('\n')
    for m in matches:
        line_no = text[:m.start()].count('\n') + 1
        line_content = lines[line_no - 1].strip()[:100]
        # filter noise
        if any(w in line_content.lower() for w in ['button', 'click', 'onclick', 'eventlistener', 'id=', 'class=']):
            print(f"  Line {line_no}: {line_content}")
