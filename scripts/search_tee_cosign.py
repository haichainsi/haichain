import os

def search_text(term):
    results = []
    for root, dirs, files in os.walk('.'):
        if any(skip in root for skip in ['.git', 'node_modules', '.gemini', 'tmp']):
            continue
        for f in files:
            if f.endswith(('.rs', '.ts', '.js', '.py')):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                        if term in content:
                            results.append(path)
                except:
                    pass
    return results

print("Files containing REQUIRE_COSIGN:")
for f in search_text('REQUIRE_COSIGN'):
    print(f)

print("\nFiles containing cosign or TEE:")
for f in search_text('cosign'):
    print(f)
