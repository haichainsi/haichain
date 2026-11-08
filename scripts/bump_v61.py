files = ['dashboard.html', 'index.html', 'app/dashboard.html', 'app/index.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('i18n.js?v=v60_federation_mesh_no_marketplace', 'i18n.js?v=v61_resilient_agent_hiring_zero_error')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Bumped version to v61 in {fn}")
