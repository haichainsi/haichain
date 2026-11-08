with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

for name in ['claude-mcp-modal', 'ai-hub-modal']:
    idx = text.find(f'id="{name}"')
    if idx != -1:
        print(f"=== {name} ===")
        print(text[idx-50:idx+1500])
        print("\n" + "="*40 + "\n")
    else:
        print(f"Not found: {name}")
