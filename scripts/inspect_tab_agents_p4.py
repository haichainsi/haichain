with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="market-category-filters"')
if idx != -1:
    print(html[idx:idx+4000])
