with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="tab-vesting"')
print(text[pos-200:pos+300])
