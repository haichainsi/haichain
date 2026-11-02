import os, re, time

def update_file(path, func):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = func(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")
    else:
        print(f"No changes in {path}")

# 1. Update hero font size and remove emoji in index.html & app/index.html
def patch_html(content):
    # Change hero h1 text-2xl to text-3xl
    # Target: <h1 class="text-2xl sm:text-4xl md:text-5xl
    content = content.replace(
        '<h1 class="text-2xl sm:text-4xl md:text-5xl',
        '<h1 class="text-3xl sm:text-4xl md:text-5xl'
    )
    # Remove emoji 👉 and surrounding space if present
    content = content.replace('👉 ', '')
    content = content.replace('👉', '')
    return content

update_file('index.html', patch_html)
update_file('app/index.html', patch_html)

# 2. Remove emoji in i18n.js & app/i18n.js
def patch_js(content):
    content = content.replace('👉 ', '')
    content = content.replace('👉', '')
    return content

update_file('i18n.js', patch_js)
update_file('app/i18n.js', patch_js)

# 3. Bump cachebuster
ts = int(time.time() * 1000)
new_ver = f"?v=v34_hero_text3xl_noemoji_{ts}"

def bump_cache(content):
    return re.sub(r'i18n\.js(\?v=[a-zA-Z0-9_\.]*)?', f'i18n.js{new_ver}', content)

update_file('index.html', bump_cache)
update_file('app/index.html', bump_cache)
update_file('dashboard.html', bump_cache)
update_file('app/dashboard.html', bump_cache)

print(f"Successfully bumped cache to {new_ver}")
