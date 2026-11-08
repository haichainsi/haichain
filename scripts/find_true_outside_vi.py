import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

v_start, v_end = 3994, 4525
d_start, d_end = 4528, 5069

vi_char_pattern = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]')

outside = []
for idx, l in enumerate(lines, 1):
    if v_start <= idx <= v_end:
        continue
    if d_start <= idx <= d_end:
        continue
    if idx < 300 and ('@context' in l or '"@type"' in l or '"name"' in l or '"text"' in l):
        continue
    if vi_char_pattern.search(l):
        outside.append((idx, l.strip()))

print(f"Total lines outside dictionaries with Vietnamese: {len(outside)}")
for idx, l in outside:
    print(f"L{idx}: {l}")
