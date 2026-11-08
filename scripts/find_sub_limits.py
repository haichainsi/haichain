import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('subscriptionLimits')
while idx != -1:
    print("Found subscriptionLimits at", idx)
    print(text[idx-50:idx+350])
    print("="*40)
    idx = text.find('subscriptionLimits', idx+1)
