import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/dev_mcp_all_langs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total keys: {len(data)}")
for k, langs in sorted(data.items()):
    if k.startswith('dev.') or k.startswith('mcp.'):
        print(f"\nKEY: {k}")
        print(f"  EN: {langs.get('en')}")
        print(f"  VI: {langs.get('vi')}")
        print(f"  ZH: {langs.get('zh')}")
