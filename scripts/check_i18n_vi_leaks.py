import re

with open('i18n.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where TRANSLATIONS is defined and each language section
# In i18n.js, each language is usually a key in TRANSLATIONS: en: { ... }, vi: { ... }, etc.
vi_char_pattern = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]')

# Distinct Vietnamese-only characters (not in French/Spanish like à, á, è, é):
vi_only_pattern = re.compile(r'[ăắằẳẵặâấầẩẫậđđêếềểễệơớờởỡợưứừửữựảãạẻẽẹỉĩịỏõọủũụỳỷỹỵĐ]')

# Split by lang keys in TRANSLATIONS
# Let's find language blocks
lang_matches = list(re.finditer(r'^\s*([a-z]{2}):\s*\{', text, re.MULTILINE))
print(f"Found {len(lang_matches)} language blocks in i18n.js:")
for i, m in enumerate(lang_matches):
    start = m.start()
    end = lang_matches[i+1].start() if i+1 < len(lang_matches) else text.find('window.haichainI18n')
    lang = m.group(1)
    block = text[start:end]
    if lang != 'vi':
        # Check if vi_only_pattern matches any line in this block
        vi_lines = []
        for line_num, l in enumerate(block.split('\n'), 1):
            if vi_only_pattern.search(l):
                vi_lines.append(l.strip())
        if vi_lines:
            print(f"  [WARNING] Language '{lang}' has {len(vi_lines)} lines with VIETNAMESE-only characters! Sample:")
            for s in vi_lines[:5]:
                print(f"    {s[:100]}")
        else:
            print(f"  Language '{lang}': CLEAN (0 Vietnamese lines)")
