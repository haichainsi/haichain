import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

vi_char_pattern = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]')

in_script = False
markup_vi = []
script_vi = []

for idx, line in enumerate(lines, 1):
    if '<script' in line:
        in_script = True
    if '</script>' in line:
        in_script = False
        continue
    
    if vi_char_pattern.search(line):
        if in_script:
            script_vi.append((idx, line.strip()))
        else:
            markup_vi.append((idx, line.strip()))

print(f"Total HTML markup lines with Vietnamese: {len(markup_vi)}")
print(f"Total Script lines with Vietnamese: {len(script_vi)}")

print("\n--- ALL HTML MARKUP LINES ---")
for idx, l in markup_vi:
    print(f"L{idx}: {l[:120]}")

with open('scripts/dashboard_script_vi.txt', 'w', encoding='utf-8') as out:
    for idx, l in script_vi:
        out.write(f"L{idx}: {l}\n")
print(f"Saved {len(script_vi)} script lines to scripts/dashboard_script_vi.txt")
