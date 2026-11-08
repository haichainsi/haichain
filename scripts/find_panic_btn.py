import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="panic-btn"')
if idx == -1:
    idx = text.find('Dừng Khẩn Cấp')
print("Panic btn:")
print(text[idx-100:idx+400])
