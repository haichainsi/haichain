with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('C3')
print('C3 snippet:')
print(repr(c[idx-150:idx+250]))

idx2 = c.find('hire-modal-agent-name')
print('hire modal snippet:')
print(repr(c[idx2-250:idx2+150]))
