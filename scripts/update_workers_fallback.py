import os

files = ['app/_worker.js', 'server/haichain-mcp-worker.js']
target = "return new Response('Not Found', { status: 404 });"
replacement = "return await fetch(request);"

for fn in files:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        if target in c:
            c = c.replace(target, replacement)
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated {fn}")
        else:
            print(f"Target not found in {fn}")
