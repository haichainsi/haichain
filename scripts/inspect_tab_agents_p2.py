with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="tab-agents"')
if idx != -1:
    print(html[idx+3500:idx+12000])
