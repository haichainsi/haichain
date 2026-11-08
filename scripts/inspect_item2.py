import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('calc-input')
if idx == -1:
    idx = text.find('calc-amount')
if idx == -1:
    idx = text.find('Subscription Amount')
if idx == -1:
    idx = text.find('2500')
print("Calculator section in sale-controller.js:")
print(text[idx-100:idx+800])
