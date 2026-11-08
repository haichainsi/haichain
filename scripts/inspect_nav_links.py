import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('id="nav-whitepaper-link"')
print("Nav pos:", pos)
print(c[pos-200:pos+600])

pos_mobile = c.find('id="mobile-nav-whitepaper-link"')
print("\nMobile nav pos:", pos_mobile)
print(c[pos_mobile-100:pos_mobile+500])
