import re, sys
sys.stdout.reconfigure(encoding='utf-8')

dash = open('dashboard.html', encoding='utf-8').read()
idx = dash.find('id="deposit-fiat-banner"')
if idx != -1:
    print(dash[idx-100:idx+600])
