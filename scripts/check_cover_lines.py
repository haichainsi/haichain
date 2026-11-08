import sys, fitz
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
    pdf_path = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.pdf"
    doc = fitz.open(pdf_path)
    p0_text = doc[0].get_text()
    print(f"=== {lang} Page 1 Text Lines ===")
    for line in p0_text.splitlines():
        if "HAICHAIN" in line or "AI²" in line or "Superintelligence" in line or "Kinh Tế" in line:
            print("  ", repr(line))
