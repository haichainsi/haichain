with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('openPdfViewerModal')
print(c[pos-200:pos+1500])
