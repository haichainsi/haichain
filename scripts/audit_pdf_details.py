# scripts/audit_pdf_details.py
import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

langs = ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']

print("=" * 80)
print("       FORENSIC TECHNICAL AUDIT OF 10 ONLINE WHITEPAPER PDFS")
print("=" * 80 + "\n")

results = {}

for l in langs:
    path = f"app/HAICHAIN_WHITEPAPER_V1.0_{l}.pdf"
    if not os.path.exists(path):
        print(f"[{l}] Missing PDF: {path}")
        continue

    doc = fitz.open(path)
    total_pages = len(doc)
    
    # 1. Check page 0 cover
    p0 = doc[0]
    p0_text = p0.get_text()
    drawings = [d for d in p0.get_drawings() if d['type'] == 'f' and d.get('fill') == (0.0, 0.0, 0.0)]
    has_fullbleed = bool(drawings)
    
    # 2. Check for LaTeX errors, raw LaTeX, and locate x402 section
    katex_errors = []
    raw_latex_pages = []
    x402_page = None
    x402_snippet = ""
    broken_chars_pages = []
    
    for idx, page in enumerate(doc):
        page_num = idx + 1
        text = page.get_text()
        
        # Check KaTeX errors
        if "katex parse error" in text.lower():
            katex_errors.append(page_num)
            
        # Check if raw unrendered LaTeX syntax leaked into text
        if ("\\Delta" in text or "\\text{" in text or "\\le" in text or "\\min(" in text):
            raw_latex_pages.append(page_num)
            
        # Check for unrendered unicode boxes / replacement chars
        if "\ufffd" in text:
            broken_chars_pages.append(page_num)
            
        # Locate the x402 section
        if "x402" in text.lower() and ("pay.sh" in text.lower() or "bounded loss" in text.lower() or "caip-2" in text.lower()):
            if x402_page is None:
                x402_page = page_num
                # Find line with heading
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                for line in lines:
                    if "4.6" in line or "6.6" in line or "x402" in line.lower():
                        x402_snippet = line
                        break

    file_size_kb = os.path.getsize(path) / 1024.0
    synced = os.path.getsize(path) == os.path.getsize(f"HAICHAIN_WHITEPAPER_V1.0_{l}.pdf")
    
    results[l] = {
        "pages": total_pages,
        "size_kb": file_size_kb,
        "synced": synced,
        "fullbleed": has_fullbleed,
        "katex_errors": katex_errors,
        "raw_latex_pages": raw_latex_pages,
        "broken_chars_pages": broken_chars_pages,
        "x402_page": x402_page,
        "x402_snippet": x402_snippet
    }

    print(f"[{l}] Total Pages: {total_pages} | Size: {file_size_kb:.1f} KB | Root/App Synced: {synced}")
    print(f"    - Cover Full-Bleed Black: {has_fullbleed}")
    print(f"    - KaTeX Render Errors: {len(katex_errors)} {katex_errors if katex_errors else '(Zero errors)'}")
    print(f"    - Raw Leaked LaTeX Code: {len(raw_latex_pages)} {raw_latex_pages if raw_latex_pages else '(Zero leaked code)'}")
    print(f"    - Broken / Missing Glyphs: {len(broken_chars_pages)} {broken_chars_pages if broken_chars_pages else '(Zero glyph errors)'}")
    print(f"    - x402 Section Located on Page: {x402_page}")
    print(f"    - Section Heading Found: {x402_snippet[:80]}")
    print("-" * 80)
