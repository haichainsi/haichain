import json

with open('scripts/dev_mcp_all_langs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k in sorted(data.keys()):
    if k.startswith('btn.'):
        print(f"{k}: {data[k].get('en')}")
