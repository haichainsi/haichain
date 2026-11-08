import sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('DOMContentLoaded')
if pos != -1:
    print(c[pos:pos+1500])
else:
    print("DOMContentLoaded not found")
