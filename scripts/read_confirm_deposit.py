import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('dashConfirmDepositBtn.addEventListener')
print("Position:", pos)
if pos != -1:
    print(text[pos:pos+4000])
