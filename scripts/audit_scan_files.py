import os

def find_files():
    targets = []
    for root, dirs, files in os.walk('.'):
        # skip node_modules, .git, etc.
        if any(skip in root for skip in ['.git', 'node_modules', '.gemini', 'tmp']):
            continue
        for f in files:
            ext = os.path.splitext(f)[1]
            if ext in ['.rs', '.ts', '.js', '.py', '.toml', '.json'] and not f.endswith('.db.json'):
                targets.append(os.path.join(root, f))
    return targets

files = find_files()
print(f"Total relevant files: {len(files)}")
for f in sorted(files):
    if any(k in f for k in ['program', 'contract', 'capleaf', 'channel', 'vault', 'sdk', 'agent-pay', 'relayer', 'watchtower']):
        print(f)
