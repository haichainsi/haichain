import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/recompile_all_10_pdfs.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Update the titles in langs array to reflect v1.1
c = c.replace("Whitepaper v1.0", "Whitepaper v1.1 (CapLeaf & 9 Invariants Edition)")
c = c.replace("Sách Trắng Chính Thức HAICHAIN v1.0", "Sách Trắng Kỹ Thuật HAICHAIN v1.1 (Bản CapLeaf & 9 Bất Biến)")
c = c.replace("官方白皮书 v1.0", "官方白皮书 v1.1（CapLeaf 与 9 大不变量正式版）")
c = c.replace("공식 백서 v1.0", "공식 백서 v1.1 (CapLeaf 및 9대 불변성 에디션)")
c = c.replace("Libro Blanco Oficial HAICHAIN v1.0", "Libro Blanco Oficial HAICHAIN v1.1 (CapLeaf y 9 Invariantes)")
c = c.replace("Livre Blanc Officiel HAICHAIN v1.0", "Livre Blanc Officiel HAICHAIN v1.1 (CapLeaf & 9 Invariants)")
c = c.replace("Официальный Whitepaper HAICHAIN v1.0", "Официальный Whitepaper HAICHAIN v1.1 (CapLeaf и 9 Инвариантов)")
c = c.replace("Ресми Ақ Қағазы v1.0", "Ресми Ақ Қағазы v1.1 (CapLeaf және 9 Инвариант)")
c = c.replace("आधिकारिक श्वेतपत्र v1.0", "आधिकारिक श्वेतपत्र v1.1 (CapLeaf और 9 नियम)")
c = c.replace("הספר הלבן הרשמי של HAICHAIN v1.0", "הספר הלבן הרשמי של HAICHAIN v1.1 (מהדורת CapLeaf ו-9 אינווריאנטים)")

with open('scripts/recompile_all_10_pdfs.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated titles in recompile_all_10_pdfs.py")
