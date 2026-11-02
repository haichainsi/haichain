import time

ts = int(time.time() * 1000)
new_ver = f"?v=v33_landing_agentic_{ts}"

def bump_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    import re
    # replace i18n.js?v=... with new_ver
    new_content = re.sub(r'i18n\.js(\?v=[a-zA-Z0-9_\.]*)?', f'i18n.js{new_ver}', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Bumped {path} to {new_ver}')

bump_file('index.html')
bump_file('app/index.html')
bump_file('dashboard.html')
bump_file('app/dashboard.html')
