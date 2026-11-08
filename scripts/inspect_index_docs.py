import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'href=["\'][^"\']*(?:whitepaper|pdf|doc)[^"\']*["\']', c, re.I)
print('Whitepaper/PDF/doc hrefs in index.html:', set(matches))

onclicks = re.findall(r'onclick=["\'][^"\']*(?:whitepaper|pdf|doc)[^"\']*["\']', c, re.I)
print('Onclick calls:', set(onclicks))

data_docs = re.findall(r'data-doc=["\'][^"\']+["\']', c, re.I)
print('Data doc attributes:', set(data_docs))

# Check for document modals or viewer
pdf_modals = re.findall(r'id=["\'][^"\']*(?:pdf|modal|viewer|doc)[^"\']*["\']', c, re.I)
print('PDF/Doc Modals:', set(pdf_modals))
