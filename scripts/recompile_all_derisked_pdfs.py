import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))

from generate_pdf_whitepapers import build_pdf_from_markdown

WORKSPACE_DIR = os.path.abspath(".")
APP_DIR = os.path.join(WORKSPACE_DIR, "app")

saft_files = [
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf", "en"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_VI.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI.pdf", "vi"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf", "vi"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_ZH.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_ZH.pdf", "zh"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_KO.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_KO.pdf", "ko"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_ES.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_ES.pdf", "es"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_FR.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_FR.pdf", "fr"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_RU.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_RU.pdf", "ru"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_KK.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_KK.pdf", "kk"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_HI.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_HI.pdf", "hi"),
    ("HAICHAIN_PRESEED_SAFT_AGREEMENT_HE.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_HE.pdf", "he"),
]

memo_files = [
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf", "en"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.pdf", "vi"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf", "vi"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_ZH.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_ZH.pdf", "zh"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_KO.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_KO.pdf", "ko"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.pdf", "es"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.pdf", "fr"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.pdf", "ru"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_KK.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_KK.pdf", "kk"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.pdf", "hi"),
    ("HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.pdf", "he"),
]

whitepaper_files = [
    ("HAICHAIN_WHITEPAPER_V1.0_EN.md", "HAICHAIN_WHITEPAPER_V1.0_EN.pdf", "en"),
    ("HAICHAIN_WHITEPAPER_V1.0_VI.md", "HAICHAIN_WHITEPAPER_V1.0_VI.pdf", "vi"),
    ("HAICHAIN_WHITEPAPER_V1.0_ZH.md", "HAICHAIN_WHITEPAPER_V1.0_ZH.pdf", "zh"),
    ("HAICHAIN_WHITEPAPER_V1.0_KO.md", "HAICHAIN_WHITEPAPER_V1.0_KO.pdf", "ko"),
    ("HAICHAIN_WHITEPAPER_V1.0_ES.md", "HAICHAIN_WHITEPAPER_V1.0_ES.pdf", "es"),
    ("HAICHAIN_WHITEPAPER_V1.0_FR.md", "HAICHAIN_WHITEPAPER_V1.0_FR.pdf", "fr"),
    ("HAICHAIN_WHITEPAPER_V1.0_RU.md", "HAICHAIN_WHITEPAPER_V1.0_RU.pdf", "ru"),
    ("HAICHAIN_WHITEPAPER_V1.0_KK.md", "HAICHAIN_WHITEPAPER_V1.0_KK.pdf", "kk"),
    ("HAICHAIN_WHITEPAPER_V1.0_HI.md", "HAICHAIN_WHITEPAPER_V1.0_HI.pdf", "hi"),
    ("HAICHAIN_WHITEPAPER_V1.0_HE.md", "HAICHAIN_WHITEPAPER_V1.0_HE.pdf", "he"),
]

def compile_group(file_list, group_name):
    print(f"\n==========================================")
    print(f"Compiling {group_name} ({len(file_list)} files)...")
    print(f"==========================================")
    for md, pdf, lang in file_list:
        md_path = os.path.join(WORKSPACE_DIR, md)
        pdf_path = os.path.join(WORKSPACE_DIR, pdf)
        if not os.path.exists(md_path):
            print(f"[!] Missing {md_path}")
            continue
        print(f"Rendering {pdf} ({lang})...")
        build_pdf_from_markdown(md, pdf, lang=lang)
        app_target = os.path.join(APP_DIR, pdf)
        shutil.copy2(pdf_path, app_target)
        size = os.path.getsize(pdf_path)
        print(f"[OK] {pdf} ({size:,} bytes) synced to app/")

if __name__ == "__main__":
    compile_group(saft_files, "SAFT Legal Agreements")
    compile_group(memo_files, "One-Pager Executive Memos")
    compile_group(whitepaper_files, "International Whitepapers")
    print("\n[SUCCESS] ALL 32 PDF ARTIFACTS RECOMPILED & SYNCED TO APP!")
