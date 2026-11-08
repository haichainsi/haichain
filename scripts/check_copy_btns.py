import json

with open('scripts/dev_mcp_all_langs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k in ['btn.copy', 'btn.copyCode', 'btn.copyCurl', 'btn.copyJson']:
    print(k, data.get(k))
