import re, sys
sys.stdout.reconfigure(encoding='utf-8')

dash = open('dashboard.html', encoding='utf-8').read()
idx = dash.find('FIAT MODES (Apple Pay & Credit Card)')
if idx != -1:
    print(dash[idx:idx+900])
