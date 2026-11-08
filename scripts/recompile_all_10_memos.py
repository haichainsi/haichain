import sys, os, shutil
sys.path.insert(0, os.path.abspath("."))
from generate_pdf_whitepapers import build_pdf_from_markdown

all_memos = [
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf", "en"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.pdf", "vi"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf", "vi"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_ZH.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_ZH.pdf", "zh"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_KO.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_KO.pdf", "ko"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.pdf", "es"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.pdf", "fr"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.pdf", "ru"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.pdf", "he"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.pdf", "hi"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_KK.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_KK.pdf", "kk"),
]

for md, pdf, lang in all_memos:
    if os.path.exists(md):
        print(f"Building {pdf} ({lang})...")
        build_pdf_from_markdown(md, pdf, lang=lang)
        app_target = os.path.join("app", pdf)
        shutil.copy2(pdf, app_target)
        print(f"-> {pdf} ({os.path.getsize(pdf)} bytes) synced to app/")

print("ALL 11 PRE-SEED MEMO PDFS RECOMPILED AND SYNCED.")
