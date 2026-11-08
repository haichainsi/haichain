import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('"vault.activeInvariants"')
if pos != -1:
    print(c[pos-200:pos+300])
