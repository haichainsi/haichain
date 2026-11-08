with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('id="tab-vesting"')
e = c.find('id="tab-audit"')
if s != -1:
    print("Found tab-vesting at", s)
    print(c[s:s+3000])
else:
    print("tab-vesting not found")
