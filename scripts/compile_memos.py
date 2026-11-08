import sys, os, shutil
sys.path.insert(0, os.path.abspath("."))
from generate_pdf_whitepapers import build_pdf_from_markdown

memos = [
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf", "en"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf", "vi"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf", "en"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf", "vi")
]

for md, pdf, lang in memos:
    if os.path.exists(md):
        print(f"Building {pdf}...")
        build_pdf_from_markdown(md, pdf, lang=lang)
        app_target = os.path.join("app", pdf)
        shutil.copy2(pdf, app_target)
        print(f"Copied {pdf} to {app_target} ({os.path.getsize(pdf)} bytes)")
