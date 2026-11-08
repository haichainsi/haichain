import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.haichain-action-btn.has-label')
if idx != -1:
    print(text[idx-50:idx+400])
else:
    idx2 = text.find('has-label')
    print("has-label:", text[idx2-50:idx2+400])
