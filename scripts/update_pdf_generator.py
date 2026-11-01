# -*- coding: utf-8 -*-
import re

with open('generate_pdf_whitepapers.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TOC pattern
old_toc_block = """    # Separate frontmatter, dedicated TOC page, and body
    if lang == "en":
        toc_pattern = r'(## TABLE OF CONTENTS\\s*\\n\\n.*?)(?=\\n---\\s*\\n\\s*## 1\\.|\\n## 1\\. )'
    else:
        toc_pattern = r'(## M[^\\n]*L[^\\n]*C[^\\n]*\\s*\\n\\n.*?)(?=\\n---\\s*\\n\\s*## |\\n## T|\\n## 1\\.)'"""

new_toc_block = """    # Separate frontmatter, dedicated TOC page, and body
    if lang == "en":
        toc_pattern = r'(## TABLE OF CONTENTS\\s*\\n\\n.*?)(?=\\n---\\s*\\n\\s*## 1\\.|\\n## 1\\. )'
    elif lang == "zh":
        toc_pattern = r'(## 目录[^\\n]*\\s*\\n\\n.*?)(?=\\n---\\s*\\n\\s*## 1\\.|\\n## 1\\. )'
    elif lang == "ko":
        toc_pattern = r'(## 목차[^\\n]*\\s*\\n\\n.*?)(?=\\n---\\s*\\n\\s*## 1\\.|\\n## 1\\. )'
    else:
        toc_pattern = r'(## M[^\\n]*L[^\\n]*C[^\\n]*\\s*\\n\\n.*?)(?=\\n---\\s*\\n\\s*## |\\n## T|\\n## 1\\.)'"""

content = content.replace(old_toc_block, new_toc_block)

# 2. Update metadata block
old_meta_block = """    # Document metadata and titles
    if lang == "en":
        doc_title = "HAICHAIN WHITEPAPER v1.0"
        doc_subtitle = "Universal Autonomous Machine Financial & Cognitive Operating System - The Bedrock for Decentralized Superintelligence"
        doc_edition = "Official Whitepaper v1.0 • Institutional Standard Edition"
        brand_sub_text = "Universal Autonomous Machine Financial & Cognitive Operating System"
        running_header_left = "HAICHAIN WHITEPAPER v1.0"
        running_header_right = "haichain.si"
        running_footer_left = "CONFIDENTIAL & PROPRIETARY • HAICHAIN GLOBAL SYSTEMS TASKFORCE"
        tag_text = "DECENTRALIZED SUPERINTELLIGENCE OPERATING SYSTEM"
        lbl_settlement = "Primary Settlement Asset"
        val_settlement = "USDT (Tether USD SPL)"
        lbl_token = "Sovereign Gas & Governance"
        val_token = "$HAISI (1,000,000,000 Fixed Supply)"
        lbl_domain = "Autonomous Network Domain"
        val_domain = "haichain.si (Superintelligence)"
        lbl_security = "Cryptographic Verification"
        val_security = "Formal Verification • Zero-Griefing Standard"
    else:"""

new_meta_block = """    # Document metadata and titles
    if lang == "en":
        doc_title = "HAICHAIN WHITEPAPER v1.0"
        doc_subtitle = "Universal Autonomous Machine Financial & Cognitive Operating System - The Bedrock for Decentralized Superintelligence"
        doc_edition = "Official Whitepaper v1.0 • Institutional Standard Edition"
        brand_sub_text = "Universal Autonomous Machine Financial & Cognitive Operating System"
        running_header_left = "HAICHAIN WHITEPAPER v1.0"
        running_header_right = "haichain.si"
        running_footer_left = "CONFIDENTIAL & PROPRIETARY • HAICHAIN GLOBAL SYSTEMS TASKFORCE"
        tag_text = "DECENTRALIZED SUPERINTELLIGENCE OPERATING SYSTEM"
        lbl_settlement = "Primary Settlement Asset"
        val_settlement = "USDT (Tether USD SPL)"
        lbl_token = "Sovereign Gas & Governance"
        val_token = "$HAISI (1,000,000,000 Fixed Supply)"
        lbl_domain = "Autonomous Network Domain"
        val_domain = "haichain.si (Superintelligence)"
        lbl_security = "Cryptographic Verification"
        val_security = "Formal Verification • Zero-Griefing Standard"
    elif lang == "zh":
        doc_title = "HAICHAIN 官方技术白皮书 v1.0"
        doc_subtitle = "自主机器通用财务与认知操作系统 - 去中心化超级智能的基石"
        doc_edition = "官方技术白皮书 v1.0 • 国际机构标准版"
        brand_sub_text = "自主机器通用财务与认知操作系统"
        running_header_left = "HAICHAIN 白皮书 v1.0"
        running_header_right = "haichain.si"
        running_footer_left = "机密与专有技术 • HAICHAIN 全球系统特别工作组"
        tag_text = "去中心化超级智能操作系统 (ASI)"
        lbl_settlement = "核心结算资产"
        val_settlement = "USDT (Solana SPL 代币)"
        lbl_token = "网络 Gas 与主权治理代币"
        val_token = "$HAISI (固定总量 1,000,000,000 枚)"
        lbl_domain = "主权自主网络域名"
        val_domain = "haichain.si (去中心化超级智能)"
        lbl_security = "密码学形式化验证"
        val_security = "形式化数学验证 • 零恶意攻击标准"
    elif lang == "ko":
        doc_title = "HAICHAIN 공식 기술 백서 v1.0"
        doc_subtitle = "자율 기계를 위한 보편적 금융 및 인지 운영체제 - 탈중앙화 초지능을 구축하는 기반"
        doc_edition = "공식 기술 백서 v1.0 • 국제 기관 표준 에디션"
        brand_sub_text = "자율 기계를 위한 보편적 금융 및 인지 운영체제"
        running_header_left = "HAICHAIN 백서 v1.0"
        running_header_right = "haichain.si"
        running_footer_left = "기밀 및 독점 정보 • HAICHAIN 글로벌 시스템 태스크포스"
        tag_text = "탈중앙화 초지능 운영체제 (ASI)"
        lbl_settlement = "주요 정산 자산"
        val_settlement = "USDT (Solana SPL)"
        lbl_token = "네트워크 가스 및 거버넌스"
        val_token = "$HAISI (1,000,000,000 고정 공급량)"
        lbl_domain = "자율 네트워크 도메인"
        val_domain = "haichain.si (탈중앙화 초지능)"
        lbl_security = "암호학적 형식 검증"
        val_security = "수학적 형식 검증 • 제로 그리핑 표준"
    else:"""

content = content.replace(old_meta_block, new_meta_block)

# 3. Enhance CSS Font Family for Asian typography
content = re.sub(
    r'font-family:\s*-apple-system,\s*BlinkMacSystemFont,\s*"Segoe UI",\s*Roboto,\s*"Helvetica Neue",\s*Arial,\s*sans-serif;',
    'font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", "PingFang SC", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans SC", "Noto Sans KR", sans-serif;',
    content
)

# 4. Update __main__
old_main = """if __name__ == "__main__":
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_EN.md", "HAICHAIN_WHITEPAPER_V1.0_EN.pdf", lang="en")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_VI.md", "HAICHAIN_WHITEPAPER_V1.0_VI.pdf", lang="vi")"""

new_main = """if __name__ == "__main__":
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_EN.md", "HAICHAIN_WHITEPAPER_V1.0_EN.pdf", lang="en")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_VI.md", "HAICHAIN_WHITEPAPER_V1.0_VI.pdf", lang="vi")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_ZH.md", "HAICHAIN_WHITEPAPER_V1.0_ZH.pdf", lang="zh")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_KO.md", "HAICHAIN_WHITEPAPER_V1.0_KO.pdf", lang="ko")"""

content = content.replace(old_main, new_main)

# Strict check: 0 em-dashes
content = content.replace('\u2014', '-').replace('\u2013', '-')

with open('generate_pdf_whitepapers.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("[+] Successfully updated generate_pdf_whitepapers.py for Phase 1 (ZH & KO support)")
