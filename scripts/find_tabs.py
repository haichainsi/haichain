import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

tabs = re.findall(r'<div id="(tab-[^"]+)"', content)
print("Tabs found:", tabs)

matches = re.findall(r'Developer & MCP Hub', content)
print("Developer & MCP Hub mentions:", len(matches))

# Find lines with Developer & MCP Hub
lines = content.splitlines()
for i, line in enumerate(lines):
    if 'Developer & MCP Hub' in line or 'tab-mcp' in line or 'tab-developer' in line:
        print(f"Line {i+1}: {line}")
