with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('nav class=')
if pos == -1:
    pos = c.find('<header')
print(c[pos:pos+2000])
