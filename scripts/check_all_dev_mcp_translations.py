import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/dev_mcp_all_langs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

langs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he']

for k, val in sorted(data.items()):
    if not (k.startswith('dev.') or k.startswith('mcp.')):
        continue
    print(f"\n==================== {k} ====================")
    for lang in langs:
        print(f"[{lang}]: {val.get(lang)}")
