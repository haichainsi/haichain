import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Let's inspect where DASH_NOTICES_I18N is defined
start_dict = None
end_dict = None
for idx, l in enumerate(lines, 1):
    if 'const DASH_NOTICES_I18N =' in l or 'var DASH_NOTICES_I18N =' in l or 'let DASH_NOTICES_I18N =' in l:
        start_dict = idx
    if start_dict and end_dict is None and idx > start_dict:
        if l.strip().startswith('};'):
            end_dict = idx

print(f"DASH_NOTICES_I18N defined between L{start_dict} and L{end_dict}")

vi_char_pattern = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]')

# Lines outside this dictionary that have Vietnamese
outside_dict_vi = []
for idx, l in enumerate(lines, 1):
    if start_dict and end_dict and start_dict <= idx <= end_dict:
        continue
    # skip JSON-LD schema lines in <head>
    if idx < 300 and ('@context' in l or '"@type"' in l or '"name"' in l or '"text"' in l):
        continue
    if vi_char_pattern.search(l):
        outside_dict_vi.append((idx, l.strip()))

print(f"Found {len(outside_dict_vi)} lines with Vietnamese OUTSIDE DASH_NOTICES_I18N and schema:")
for idx, l in outside_dict_vi:
    print(f"L{idx}: {l[:130]}")
