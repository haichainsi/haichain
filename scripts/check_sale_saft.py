import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

print('btn-open-saft-pdf in sale-controller.js:', 'btn-open-saft-pdf' in text)
print('saft-pdf-modal in sale-controller.js:', 'saft-pdf-modal' in text)
print('saft' in text.lower())
