with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('hire-modal-agent-name')
print(c[idx-350:idx+250])
