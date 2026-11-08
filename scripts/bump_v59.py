files = ['dashboard.html', 'index.html', 'app/dashboard.html', 'app/index.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('i18n.js?v=v58_monochrome_marketplace_responsive', 'i18n.js?v=v59_fix_language_and_escrow_prompts')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Bumped version in {fn}")
