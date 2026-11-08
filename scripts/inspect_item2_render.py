import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('${t.subscriptionAmount}')
if idx == -1:
    idx = text.find('t.subscriptionLimits')
print("Render calculator:")
print(text[idx-200:idx+1200])
