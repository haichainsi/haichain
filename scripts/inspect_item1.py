import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('btn-pay-phantom-1click')
print(text[idx-100:idx+600])
