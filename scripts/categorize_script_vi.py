import re

with open('scripts/dashboard_script_vi.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check which lines belong to DASH_NOTICES_I18N['vi'] or other dictionaries
in_vi_dict = False
dict_lines = []
non_dict_lines = []

for l in lines:
    if "vi: {" in l or "'vi': {" in l or '"vi": {' in l:
        in_vi_dict = True
    if in_vi_dict:
        dict_lines.append(l)
        if re.search(r'^\s*},?\s*$', l) or "zh: {" in l or "'zh': {" in l:
            in_vi_dict = False
    else:
        non_dict_lines.append(l)

print(f"Total script lines with VI: {len(lines)}")
print(f"Lines inside dictionary definition: {len(dict_lines)}")
print(f"Lines OUTSIDE dictionary definition: {len(non_dict_lines)}")

print("\n--- SAMPLE OUTSIDE DICTIONARY LINES ---")
for l in non_dict_lines[:40]:
    print(l.strip()[:140])
