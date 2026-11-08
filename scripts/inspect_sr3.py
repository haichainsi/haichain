with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('agent_serp_crawler_03')
print(repr(c[idx:idx+350]))
