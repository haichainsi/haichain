with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('function openPdfViewerModal')
if pos == -1:
    pos = c.find('window.openPdfViewerModal =')
print("Definition pos:", pos)
if pos != -1:
    print(c[pos:pos+1500])
