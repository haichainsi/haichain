for path in ['i18n.js', 'app/i18n.js']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('AI रोbोटों', 'AI रोबोटों')
    c = c.replace('richesse và la souveraineté', 'richesse et la souveraineté')
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(c)
    print(f'Fixed polish typos in {path}')
