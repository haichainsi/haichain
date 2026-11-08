import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_v = 'v71_devhub_fixed_20261108'
updated = re.sub(r'(\.js\?v=)[a-zA-Z0-9_\-]+', rf'\g<1>{new_v}', text)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(updated)
with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(updated)

print(f"Bumped script cachebusters to {new_v} in dashboard.html and app/dashboard.html")
