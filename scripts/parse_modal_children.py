import sys
import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract content inside <div id="wallet-connect-modal"...> ... </div>
m = re.search(r'<div id="wallet-connect-modal"[^>]*>(.*?)</div>\s*<!--\s*5\.\s*CONNECTED', text, re.DOTALL)
if m:
    content = m.group(1)
    print("Found wallet-connect-modal content length:", len(content))
    # Count top-level divs inside #wallet-connect-modal
    # Let's see:
    pos = 0
    top_children = []
    # parse html tags
    depth = 0
    start_tag = None
    for match in re.finditer(r'(<div\b[^>]*>)|(</div>)', content):
        if match.group(1):
            if depth == 0:
                start_tag = match.group(1)
                start_pos = match.start()
            depth += 1
        elif match.group(2):
            depth -= 1
            if depth == 0:
                top_children.append((start_tag, content[start_pos:match.end()]))
    print(f"Top level children count in wallet-connect-modal: {len(top_children)}")
    for i, (tag, child_text) in enumerate(top_children):
        print(f"Child {i+1}: tag={tag[:60]}... text_len={len(child_text)}")
        first_few = child_text[:120].replace('\n', ' ')
        last_few = child_text[-120:].replace('\n', ' ')
        print(f"   First: {first_few}")
        print(f"   Last: {last_few}")
else:
    print("Could not match wallet-connect-modal regex")
