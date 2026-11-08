with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('openPreseedSaftModal')
print(c[idx:idx+1500])
