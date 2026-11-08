import os, re

matches = []
for f in os.listdir('.'):
    if f.endswith('.js') or f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            if 'openPdfViewerModal' in content:
                for line_no, line in enumerate(content.splitlines()):
                    if 'openPdfViewerModal' in line and ('function' in line or '=' in line):
                        matches.append((f, line_no, line.strip()))

for m in matches:
    print(m)
