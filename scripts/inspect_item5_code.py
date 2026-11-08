import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 44934
print(text[idx-200:idx+600])
