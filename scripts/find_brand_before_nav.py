with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('nav class="hidden md:flex')
print(c[pos-1500:pos])
