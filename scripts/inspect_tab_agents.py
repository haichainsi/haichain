with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="tab-agents"')
if idx != -1:
    print("Found tab-agents at", idx)
    print(html[idx:idx+3500])
else:
    print("tab-agents not found")
