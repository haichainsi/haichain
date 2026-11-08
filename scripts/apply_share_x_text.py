import sys
import time
import re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update sale-controller.js and app/sale-controller.js
with open('sale-controller.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = "refShareX: 'Chia sẻ lên X',"
replacement = "refShareX: 'Chia sẻ X',"

if target in content:
    content = content.replace(target, replacement, 1)
    with open('sale-controller.js', 'w', encoding='utf-8') as f:
        f.write(content)
    with open('app/sale-controller.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated refShareX in sale-controller.js and app/sale-controller.js!")
else:
    print("Target not found!")
    sys.exit(1)

# 2. Bump cachebuster in dashboard.html and app/dashboard.html
new_ver = f"v46_share_x_text_{int(time.time()*1000)}"

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dhtml = f.read()

dhtml = re.sub(
    r'/app/sale-controller\.js\?v=[^\"]+',
    f'/app/sale-controller.js?v={new_ver}',
    dhtml
)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)
with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)

print("Bumped cachebuster to:", new_ver)
