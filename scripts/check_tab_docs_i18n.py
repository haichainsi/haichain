import re

with open("dashboard.html", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('id="tab-docs"')
end_pos = text.find('</section>', pos)
docs_html = text[pos:end_pos]

keys = re.findall(r'data-i18n="([^"]+)"', docs_html)
print(f"Total data-i18n in tab-docs: {len(keys)}")
for k in keys:
    print("  ", k)

# Check for any untranslated Vietnamese text in tab-docs
# Let's strip out tags and check Vietnamese characters
stripped = re.sub(r'<[^>]+>', ' ', docs_html)
# common Vietnamese diacritics: à, á, ả, ã, ạ, ắ, ằ, ẳ, ẵ, ặ, ấ, ầ, ẩ, ẫ, ậ, è, é, ẻ, ẽ, ẹ, ê, ế, ề, ể, ễ, ệ, ì, í, ỉ, ĩ, ị, ò, ó, ỏ, õ, ọ, ô, ố, ồ, ổ, ỗ, ộ, ơ, ớ, ờ, ở, ỡ, ợ, ù, ú, ủ, ũ, ụ, ư, ứ, ừ, ử, ữ, ự, ỳ, ý, ỷ, ỹ, ỵ, đ
vi_chars = set("àáảãạắằẳẵặấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ")
lines_with_vi = []
for line in docs_html.splitlines():
    if any(c in vi_chars for c in line.lower()):
        lines_with_vi.append(line.strip())

print(f"\nLines with Vietnamese in tab-docs: {len(lines_with_vi)}")
for l in lines_with_vi:
    print("  VI LINE:", l[:100])
