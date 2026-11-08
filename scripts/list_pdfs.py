import os

pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]
print('PDFs in root:', pdfs)

if os.path.exists('assets'):
    assets_pdfs = [f for f in os.listdir('assets') if f.endswith('.pdf')]
    print('PDFs in assets:', assets_pdfs)
