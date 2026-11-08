with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Web SERP Scraper Swarm')
print(repr(c[idx-250:idx+250]))
