import urllib.request, time, sys, fitz

sys.stdout.reconfigure(encoding='utf-8')

url_html = "https://haichain.si/"
url_pdf = "https://haichain.si/HAICHAIN_WHITEPAPER_V1.0_VI.pdf?v=v33_global_no_qr_clean_math"

print("Polling https://haichain.si for deployment of commit ec4fa29...")

deployed = False
for attempt in range(1, 30):
    try:
        req = urllib.request.Request(url_html, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            if 'v63_global_no_qr_clean_math_20261103' in html:
                print(f"Attempt {attempt}: Found v63 script tag in live HTML!")
                deployed = True
                break
            else:
                print(f"Attempt {attempt}: Waiting for Cloudflare Pages build... (3s)")
    except Exception as e:
        print(f"Attempt {attempt}: Error fetching: {e}")
    time.sleep(3)

if not deployed:
    print("Warning: Timed out waiting for HTML update, checking live PDF directly...")

# Now fetch the live PDF and check for &#36; and regional keywords
print("\nVerifying live PDF: HAICHAIN_WHITEPAPER_V1.0_VI.pdf...")
try:
    req_pdf = urllib.request.Request(url_pdf, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req_pdf, timeout=20) as resp:
        pdf_bytes = resp.read()
    
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = len(doc)
    full_text = ""
    for p in doc:
        full_text += p.get_text() + "\n"
    
    has_36 = "&#36;" in full_text or "#36;" in full_text or "36;HAISI" in full_text
    has_regional = "việt nam & đông nam á" in full_text.lower() or "vietqr" in full_text.lower()
    has_haisi = "$HAISI" in full_text
    
    print(f"Live Online PDF Verified: {pages} pages | Size: {len(pdf_bytes)/1024:.1f} KB")
    print(f"Contains '&#36;': {has_36} (Should be False)")
    print(f"Contains 'Việt Nam & Đông Nam Á' / 'VietQR': {has_regional} (Should be False)")
    print(f"Contains '$HAISI': {has_haisi} (Should be True)")
    
    if not has_36 and not has_regional and has_haisi:
        print("\n>>> SUCCESS: LIVE ONLINE PDF IS FULLY UPDATED AND 100% CLEAN! <<<")
    else:
        print("\n>>> WARNING: Live PDF still showing old cache on Cloudflare. <<<")
except Exception as e:
    print(f"Error checking live PDF: {e}")
