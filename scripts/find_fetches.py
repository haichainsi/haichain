import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

fetches = re.findall(r'fetch\([\'"`]([^\'")`]+)[\'"`]', text)
print('Fetches in dashboard.html:')
for u in set(fetches):
    print(' ', u)

with open('app/pdf-modal.js', 'r', encoding='utf-8') as f:
    pdf_text = f.read()

fetches_pdf = re.findall(r'fetch\([\'"`]([^\'")`]+)[\'"`]', pdf_text)
print('Fetches in app/pdf-modal.js:')
for u in set(fetches_pdf):
    print(' ', u)
