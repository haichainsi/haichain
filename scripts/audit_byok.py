import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('saveByokBtn.addEventListener')
print("saveByokBtn listener pos:", pos)
if pos != -1:
    print(text[pos:pos+2500])
