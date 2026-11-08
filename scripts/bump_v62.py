files = ['dashboard.html', 'index.html', 'app/dashboard.html', 'app/index.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    import re
    content = re.sub(r'i18n\.js\?v=[^\s"\'<>]+', 'i18n.js?v=v62_zero_downtime_agent_escrow', content)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Bumped version to v62 in {fn}")
