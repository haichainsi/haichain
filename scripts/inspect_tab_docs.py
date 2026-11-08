import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'(<div id="tab-docs"[\s\S]*?)(<div id="tab-private-round"|<div id="tab-vesting")', content)
if m:
    tab_docs = m.group(1)
    print(f"Length of tab-docs: {len(tab_docs)}")
    lines = tab_docs.splitlines()
    print(f"Total lines: {len(lines)}")
    # Print the lines in tab_docs with their line numbers
    for i, l in enumerate(lines):
        print(f"{i+1}: {l}")
else:
    print("tab-docs not found")
