import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open("HAICHAIN_WHITEPAPER_V1.0_EN.pdf")
print("Total pages:", len(doc))
print("--- PAGE 30 ---")
print(doc[29].get_text())
print("--- PAGE 31 ---")
print(doc[30].get_text())
print("--- PAGE 32 ---")
print(doc[31].get_text())
