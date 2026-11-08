import re

def patch_dash(path):
    print(f"Patching {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_snippet = 'const personalizedUrl = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;'
    new_snippet = '''let personalizedUrl = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;
        if (typeof balance === 'number' && balance > 0) {
          personalizedUrl += `&bal=${balance.toFixed(2)}`;
        }'''

    old_copy = '''        const url = hasWallet && activeAddr 
          ? `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`
          : "https://mcp.haichain.si/api/mcp";'''

    new_copy = '''        let url = "https://mcp.haichain.si/api/mcp";
        if (hasWallet && activeAddr) {
          url = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;
          if (typeof balance === 'number' && balance > 0) {
            url += `&bal=${balance.toFixed(2)}`;
          }
        }'''

    if old_snippet in content:
        content = content.replace(old_snippet, new_snippet)
        print("Updated personalizedUrl to include &bal if balance > 0.")
    if old_copy in content:
        content = content.replace(old_copy, new_copy)
        print("Updated copy URL to include &bal if balance > 0.")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Finished {path}.")

patch_dash('dashboard.html')
patch_dash('app/dashboard.html')
