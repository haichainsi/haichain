import json

with open('scripts/dev_mcp_all_langs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

langs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he']

with open('scripts/all_translations_utf8.txt', 'w', encoding='utf-8') as out:
    for k, val in sorted(data.items()):
        if not (k.startswith('dev.') or k.startswith('mcp.')):
            continue
        out.write(f"\n==================== {k} ====================\n")
        for lang in langs:
            out.write(f"[{lang}]: {val.get(lang)}\n")

print("Wrote scripts/all_translations_utf8.txt")
