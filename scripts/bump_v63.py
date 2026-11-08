files = ['dashboard.html', 'index.html', 'app/dashboard.html', 'app/index.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    import re
    content = re.sub(r'i18n\.js\?v=[^\s"\'<>]+', 'i18n.js?v=v63_real_solana_wallet_signing_devnet', content)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Bumped version to v63 in {fn}")
