import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open("HAICHAIN_WHITEPAPER_V1.0_VI.pdf")
print("Total pages in VI:", len(doc))
for p in range(len(doc)-3, len(doc)):
    print(f"--- VI PAGE {p+1} ---")
    print(doc[p].get_text()[:1500])
