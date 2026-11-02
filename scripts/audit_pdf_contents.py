import glob, os, re, sys, fitz

sys.stdout.reconfigure(encoding='utf-8')

app_pdfs = sorted(glob.glob('app/*.pdf'))
print(f"Total PDFs found in app/: {len(app_pdfs)}")

bad_patterns = [
    re.compile(r'real\s+yield', re.IGNORECASE),
    re.compile(r'15[\.,]9\s*M', re.IGNORECASE),
    re.compile(r'40%.{0,30}(?:usdt|dividend|real\s+yield|distribut)', re.IGNORECASE),
    re.compile(r'60%.{0,30}buyback', re.IGNORECASE),
    re.compile(r'дивиденд', re.IGNORECASE),
    re.compile(r'rendimiento\s+real', re.IGNORECASE),
    re.compile(r'rendement\s+r[eé]el', re.IGNORECASE)
]

total_violations = 0

for pdf_path in app_pdfs:
    doc = fitz.open(pdf_path)
    pdf_name = os.path.basename(pdf_path)
    file_violations = []
    
    for page_idx in range(len(doc)):
        text = doc[page_idx].get_text()
        for pat in bad_patterns:
            matches = list(pat.finditer(text))
            for m in matches:
                # Exclude explicit negative/disclaimer statements like "Zero passive dividend" or "eliminating dividend"
                start = max(0, m.start() - 30)
                end = min(len(text), m.end() + 30)
                snippet = text[start:end].replace('\n', ' ')
                
                # Check if it's a disclaimer
                is_disclaimer = any(d in snippet.lower() for d in [
                    'zero passive dividend', 'sin distribución de dividendos', 
                    'sans aucune distribution', 'без пассивных дивиденд',
                    '수동적 배당', '零被动股息', 'không chia cổ tức', 'rather than distributing direct cash dividend'
                ])
                if not is_disclaimer:
                    file_violations.append((page_idx + 1, snippet))
                    
    if file_violations:
        print(f"\n[X] VIOLATION in {pdf_name}:")
        for pnum, snip in file_violations:
            print(f"    Page {pnum}: ...{snip.strip()}...")
        total_violations += len(file_violations)

print(f"\n==========================================")
print(f"FINAL AUDIT RESULT: {total_violations} illegal promise violations across all {len(app_pdfs)} PDFs.")
print(f"==========================================")
