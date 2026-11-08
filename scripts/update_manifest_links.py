import re

targets = ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html']

for path in targets:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace manifest link with cachebusted version
    text = re.sub(
        r'<link\s+rel=[\"\']manifest[\"\']\s+href=[\"\'][^\"\']+[\"\']>',
        '<link rel="manifest" href="/manifest.json?v=v33_symbiotic_ai2_title">',
        text
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated manifest link in {path}")
