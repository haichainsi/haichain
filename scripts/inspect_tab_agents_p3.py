with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Global Agent Federation Mesh')
if idx != -1:
    print(html[idx:idx+6000])
