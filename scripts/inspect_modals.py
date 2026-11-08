import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

modals = re.findall(r'<div[^>]*id=["\']([^"\']*modal[^"\']*)["\']', text, re.IGNORECASE)
print("Modals found:", modals)

deposit_modal = text.find('deposit-modal')
if deposit_modal != -1:
    print("\nDeposit modal sample:")
    print(text[deposit_modal-100:deposit_modal+800])
