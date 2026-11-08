with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

print('renderTerminalContent occurrences:', text.count('renderTerminalContent'))
print('saft-referral-hub occurrences in sale-controller.js:', text.count('saft-referral-hub'))

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dtext = f.read()

print('saft-referral-hub occurrences in dashboard.html:', dtext.count('saft-referral-hub'))
