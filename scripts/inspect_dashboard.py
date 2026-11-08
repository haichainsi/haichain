import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

lucides = re.findall(r'lucide[^\"]*', text)
print('Lucide occurrences:', lucides[:10])

scripts = re.findall(r'<script[^>]*src=[\"\']([^\"\']+)[\"\']', text)
print('Scripts in dashboard.html:')
for s in scripts:
    print(' ', s)
