import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('openSaftPdfModal in dashboard.html:', 'openSaftPdfModal' in text)
print('btn-open-saft-pdf in dashboard.html:', 'btn-open-saft-pdf' in text)
print('saft-pdf-modal in dashboard.html:', 'saft-pdf-modal' in text)
