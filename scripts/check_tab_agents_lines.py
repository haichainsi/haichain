import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_tab_agents = False
for idx, line in enumerate(lines, 1):
    if 'id="tab-agents"' in line:
        in_tab_agents = True
    if in_tab_agents:
        if re.search(r'\b(?:emerald|green)-\d+', line):
            print(f"Line {idx}: {line.strip()[:100]}")
        if '</section>' in line:
            break
