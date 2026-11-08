import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'src=["\']([^"\']+\?v=[^"\']+)["\']', text)
print("Current script versions in dashboard.html:")
for m in sorted(set(matches)):
    print(" ", m)

# Bump version to v70_devhub_python_20261108
new_v = 'v70_devhub_python_20261108'
updated = re.sub(r'(\.js\?v=)[a-zA-Z0-9_\-]+', rf'\g<1>{new_v}', text)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(updated)
with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(updated)

print(f"Bumped script cachebusters to {new_v} in dashboard.html and app/dashboard.html")
