with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find("fetch('/api/infer'")
if pos != -1:
    print('--- INFER FETCH ---')
    print(text[pos-100:pos+800])

pos2 = text.find("fetch('/api/wallet-relay'")
if pos2 != -1:
    print('--- WALLET RELAY FETCH ---')
    print(text[pos2-100:pos2+800])
