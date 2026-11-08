import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sub = text[text.find('hub-tab-gateway'):text.find('hub-tab-gateway')+2500]
print("JS logic for hub-tab:")
print(sub)
