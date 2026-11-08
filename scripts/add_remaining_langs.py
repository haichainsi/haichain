# -*- coding: utf-8 -*-
with open('generate_pdf_whitepapers.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_RU.md", "HAICHAIN_WHITEPAPER_V1.0_RU.pdf", lang="ru")'
replacement = """    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_RU.md", "HAICHAIN_WHITEPAPER_V1.0_RU.pdf", lang="ru")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_KK.md", "HAICHAIN_WHITEPAPER_V1.0_KK.pdf", lang="kk")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_HI.md", "HAICHAIN_WHITEPAPER_V1.0_HI.pdf", lang="hi")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_HE.md", "HAICHAIN_WHITEPAPER_V1.0_HE.pdf", lang="he")"""

if target in text:
    text = text.replace(target, replacement)
    with open('generate_pdf_whitepapers.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Added KK, HI, HE to generate_pdf_whitepapers.py")
else:
    print("Target not found")
