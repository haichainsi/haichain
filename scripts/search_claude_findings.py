import os

targets = ["createUsdtDepositSession", "handleX402Challenge", "pay.haichain.io", "HaiUsdt1111"]

for root, dirs, files in os.walk("."):
    # Skip node_modules, .git, .wrangler
    dirs[:] = [d for d in dirs if d not in ["node_modules", ".git", ".wrangler", "dist", "pdfjs"]]
    for f in files:
        if f.endswith(('.ts', '.js', '.json', '.md', '.html')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    c = fp.read()
                    for t in targets:
                        if t in c:
                            print(f"Found '{t}' in {p}")
            except Exception as e:
                pass
