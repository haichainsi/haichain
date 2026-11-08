import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read EXTRA_NOTICES from eliminate_all_remaining_isvi.js
with open('scripts/eliminate_all_remaining_isvi.js', 'r', encoding='utf-8') as f:
    el_code = f.read()

p1 = el_code.find('const EXTRA_NOTICES =')
pEnd1 = el_code.find('function patchFile', p1)
extra_snippet = el_code[p1:pEnd1].replace('const EXTRA_NOTICES =', 'EXTRA_NOTICES =').strip()
if extra_snippet.endswith(';'):
    extra_snippet = extra_snippet[:-1]

# Read MM_KEYS from patch_final_isvi.js
with open('scripts/patch_final_isvi.js', 'r', encoding='utf-8') as f:
    mm_code = f.read()

p2 = mm_code.find('const MM_KEYS =')
pEnd2 = mm_code.find('function patchFinal', p2)
mm_snippet = mm_code[p2:pEnd2].replace('const MM_KEYS =', 'MM_KEYS =').strip()
if mm_snippet.endswith(';'):
    mm_snippet = mm_snippet[:-1]

# Execute snippets to get dictionaries
scope = {}
exec(extra_snippet, scope)
exec(mm_snippet, scope)

extra_notices = scope['EXTRA_NOTICES']
mm_keys = scope['MM_KEYS']

langs = ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he']
all_extra = {}
for lang in langs:
    all_extra[lang] = {}
    if lang in extra_notices:
        all_extra[lang].update(extra_notices[lang])
    if lang in mm_keys:
        all_extra[lang].update(mm_keys[lang])

print('Total extra keys per lang:')
for l in langs:
    print(l, len(all_extra[l]))

def inject_into_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # In content, for each language block inside DASH_NOTICES_I18N, inject missing keys
    dash_start = content.find('const DASH_NOTICES_I18N =')
    dash_end = content.find('function getDashNotice', dash_start)
    dash_block = content[dash_start:dash_end]

    for lang in langs:
        token = f'"{lang}": {{\n'
        pos = dash_block.find(token)
        if pos != -1:
            inject_str = ""
            for k, v in all_extra[lang].items():
                if f'"{k}":' not in dash_block[pos:pos+15000]:
                    inject_str += f'      "{k}": {json.dumps(v, ensure_ascii=False)},\n'
            if inject_str:
                insert_idx = pos + len(token)
                dash_block = dash_block[:insert_idx] + inject_str + dash_block[insert_idx:]
                print(f'{filepath}: Injected {len(inject_str.splitlines())} keys into {lang}')

    content = content[:dash_start] + dash_block + content[dash_end:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

inject_into_file('dashboard.html')
inject_into_file('app/dashboard.html')
print('DONE INJECTION!')
