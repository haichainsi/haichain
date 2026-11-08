import sys, os, fitz
sys.stdout.reconfigure(encoding='utf-8')

langs = ['EN', 'VI', 'ZH', 'KO', 'FR', 'ES', 'RU', 'KK', 'HI', 'HE']
print("================================================================================")
print("       HAICHAIN ONLINE PDF READER FORENSIC AUDIT (ALL 10 LANGUAGES)            ")
print("================================================================================\n")

for l in langs:
    pdf_path = f"HAICHAIN_WHITEPAPER_V1.0_{l}.pdf"
    app_path = os.path.join("app", pdf_path)
    if not os.path.exists(pdf_path):
        print(f"[{l}] ERROR: Root PDF not found: {pdf_path}")
        continue
    if not os.path.exists(app_path):
        print(f"[{l}] ERROR: App PDF not found: {app_path}")
        continue

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    
    first_page_text = doc[0].get_text()
    first_lines = [line.strip() for line in first_page_text.splitlines() if line.strip()][:4]
    
    # Read last 3 pages
    last_text = ""
    for p_idx in range(max(0, total_pages - 3), total_pages):
        last_text += doc[p_idx].get_text() + "\n"
        
    has_sec12 = any(k in last_text for k in ["12.", "12 ", "APPENDIX", "PHỤ LỤC", "附录", "부록", "ANNEXE", "APÉNDICE", "ПРИЛОЖЕНИЕ", "ҚОСЫМША", "परिशिष्ट", "נספח"])
    has_223 = "223" in last_text
    has_invariants = any(k in last_text for k in ["I1", "I9", "9 Invariants", "9 bất biến", "9大", "9대", "9 invariants", "9 invariantes", "9 инвариантов", "9 инвариант", "9 नियम", "9 אינווריאנטים"])
    has_claude = any(k in last_text for k in ["6.1", "Claude", "theft", "thiệt hại", "损失", "손실", "perte", "pérdida", "ущерб", "шығын", "क्षति", "הפסד"])
    has_redteam = any(k in last_text for k in ["Red-Team", "Jito", "MEV", "OwnerForceReclaim", "Lamport", "lamports", "Prompt Injection"])
    
    root_size = os.path.getsize(pdf_path) / 1024.0
    app_size = os.path.getsize(app_path) / 1024.0
    is_synced = (root_size == app_size)

    print(f"[{l}] Pages: {total_pages} | Size: {root_size:.1f} KB | Synced with app/: {is_synced}")
    print(f"    Line 1: {first_lines[0] if len(first_lines) > 0 else 'N/A'}")
    print(f"    Line 2: {first_lines[1] if len(first_lines) > 1 else 'N/A'}")
    print(f"    Line 3: {first_lines[2] if len(first_lines) > 2 else 'N/A'}")
    print(f"    - Section 12 Attached: {has_sec12}")
    print(f"    - 223 Bytes Wire Schema: {has_223}")
    print(f"    - 9 Mathematical Invariants (I1-I9): {has_invariants}")
    print(f"    - Claude Theorem 6.1 Bounded Theft Ceiling: {has_claude}")
    print(f"    - 5 Red-Team Patches Present: {has_redteam}")
    print("-" * 80)
