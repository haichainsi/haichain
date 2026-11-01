# -*- coding: utf-8 -*-
"""
HAICHAIN International Whitepaper PDF Generator
Compiles Markdown Whitepapers into Institutional-Grade PDF Documents
Using Headless Browser Engine with Paged Media CSS
Style: 100% Borderless Minimalist Typography (Zero Borders, Zero Lines, Dedicated TOC Page)
Cover: Black Premium with Official White Logo (Zero Border Lines)
Token: $HAISI
"""

import os
import re
import base64
import subprocess
import markdown

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "haichain-official-logo-white.png")

def get_logo_base64():
    """Reads the official Haichain white logo and returns a base64 data URI."""
    if os.path.exists(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

def format_math(text):
    """Convert common LaTeX math expressions to clean semantic HTML."""
    def replace_display_math(match):
        expr = match.group(1).strip()
        expr_html = latex_to_html(expr)
        return f'<div class="math-display">{expr_html}</div>'

    def replace_inline_math(match):
        expr = match.group(1).strip()
        expr_html = latex_to_html(expr)
        return f'<span class="math-inline">{expr_html}</span>'

    # Display math $$ ... $$
    text = re.sub(r'\$\$(.*?)\$\$', replace_display_math, text, flags=re.DOTALL)
    # Inline math $ ... $
    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', replace_inline_math, text)
    return text

def latex_to_html(tex):
    """Substitutes LaTeX macros with clean Unicode/HTML entities."""
    s = tex
    s = re.sub(r'\\mathbf\{([^}]+)\}', r'<b>\1</b>', s)
    s = re.sub(r'\\textbf\{([^}]+)\}', r'<b>\1</b>', s)
    s = re.sub(r'\\text\{([^}]+)\}', r'<span class="math-text">\1</span>', s)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 &frasl; \2)', s)
    
    # Subscripts and superscripts
    s = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'_([a-zA-Z0-9])', r'<sub>\1</sub>', s)
    s = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', s)
    s = re.sub(r'\^([a-zA-Z0-9])', r'<sup>\1</sup>', s)
    
    # Symbols
    symbols = {
        r'\times': '&times;',
        r'\iff': '&hArr;',
        r'\implies': '&rArr;',
        r'\to': '&rarr;',
        r'\leftarrow': '&larr;',
        r'\forall': '&forall;',
        r'\exists': '&exist;',
        r'\ge': '&ge;',
        r'\le': '&le;',
        r'\ne': '&ne;',
        r'\approx': '&asymp;',
        r'\equiv': '&equiv;',
        r'\pm': '&plusmn;',
        r'\in': '&isin;',
        r'\cdot': '&middot;',
        r'\sum': '&sum;',
        r'\prod': '&prod;',
        r'\Delta': '&Delta;',
        r'\alpha': '&alpha;',
        r'\beta': '&beta;',
        r'\gamma': '&gamma;',
        r'\tau': '&tau;',
        r'\pi': '&pi;',
        r'\mu': '&mu;',
        r'\sigma': '&sigma;',
        r'\epsilon': '&epsilon;',
        r'\theta': '&theta;',
        r'\lambda': '&lambda;',
        r'\omega': '&omega;',
        r'\Omega': '&Omega;',
        r'\blacksquare': '&#9632;',
        r'\parallel': '||',
        r'\|': '||',
        r'\,': ' ',
        r'\quad': ' &nbsp; ',
        r'\qquad': ' &nbsp; &nbsp; '
    }
    for macro, rep in symbols.items():
        s = s.replace(macro, rep)
    return s

def process_callouts(html):
    """Transforms blockquote alerts into pure unboxed academic remarks."""
    html = re.sub(
        r'<blockquote>\s*<p>\s*\[!NOTE\]\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">NOTE</p><p class="remark-body">\1</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*\[!IMPORTANT\]\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">IMPORTANT NOTICE</p><p class="remark-body">\1</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*\[!WARNING\]\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">SYSTEM INVARIANT WARNING</p><p class="remark-body">\1</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*<strong>A Note to Institutional Allocators(.*?)</strong>\s*<br\s*/?>\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">STRATEGIC NOTE: INSTITUTIONAL ALLOCATORS & ARCHITECTS</p><p class="remark-body">\2</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*<strong>Thông Điệp Chiến Lược Dành Cho Các Nhà Đầu Tư Thể Chế(.*?)</strong>\s*<br\s*/?>\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">THÔNG ĐIỆP CHIẾN LƯỢC: NHÀ ĐẦU TƯ THỂ CHẾ & KỸ SƯ HỆ THỐNG</p><p class="remark-body">\2</p></div>',
        html, flags=re.DOTALL
    )
    return html

def build_pdf_from_markdown(md_filename, pdf_filename, lang="en"):
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, md_filename.replace('.md', '_pdf_temp.html'))
    
    print(f"[*] Processing {md_filename} -> {pdf_filename}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Pre-process LaTeX math before Markdown parser treats it as markup
    text_with_math = format_math(raw_text)

    # Separate frontmatter, dedicated TOC page, and body
    if lang == "en":
        toc_pattern = r'(## TABLE OF CONTENTS\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    else:
        toc_pattern = r'(## M[^\n]*L[^\n]*C[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## |\n## T|\n## 1\.)'
    
    m = re.search(toc_pattern, text_with_math, re.DOTALL)
    md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    
    if m:
        frontmatter_text = text_with_math[:m.start()].strip()
        toc_text = m.group(1).strip()
        body_text = text_with_math[m.end():].strip()
        body_text = re.sub(r'^---\s*', '', body_text).strip()
        
        frontmatter_html = md_converter.convert(frontmatter_text)
        md_converter.reset()
        toc_html = md_converter.convert(toc_text)
        md_converter.reset()
        body_html = md_converter.convert(body_text)
        
        full_content_html = f"""
<div class="frontmatter-page">
{frontmatter_html}
</div>

<div class="toc-page">
{toc_html}
</div>

<div class="body-content">
{body_html}
</div>
"""
    else:
        full_content_html = md_converter.convert(text_with_math)

    full_content_html = process_callouts(full_content_html)
    logo_data_uri = get_logo_base64()

    # Document metadata and titles
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
    else:
        doc_title = "SÁCH TRẮNG CHÍNH THỨC HAICHAIN v1.0"
        doc_subtitle = "Hệ Điều Hành Tài Chính & Nhận Thức Phổ Quát Dành Cho Máy Móc Tự Hành - Nền Tảng Kiến Tạo Siêu Trí Tuệ Phi Tập Trung"
        doc_edition = "Sách Trắng v1.0 • Phiên Bản Tiêu Chuẩn Thể Chế Quốc Tế"
        brand_sub_text = "Hệ Điều Hành Tài Chính & Nhận Thức Phổ Quát Dành Cho Máy Móc Tự Hành"
        running_header_left = "SÁCH TRẮNG HAICHAIN v1.0"
        running_header_right = "haichain.si"
        running_footer_left = "BẢO LƯU MỌI QUYỀN • HỘI ĐỒNG KIẾN TRÚC HỆ THỐNG PHÂN TÁN HAICHAIN"
        tag_text = "HỆ ĐIỀU HÀNH SIÊU TRÍ TUỆ PHI TẬP TRUNG"
        lbl_settlement = "Tài Sản Quyết Toán Chính"
        val_settlement = "USDT (Tether USD SPL)"
        lbl_token = "Gas Chủ Quyền & Quản Trị"
        val_token = "$HAISI (Cố Định 1.000.000.000 Token)"
        lbl_domain = "Tên Miền Mạng Mục Tiêu"
        val_domain = "haichain.si (Superintelligence)"
        lbl_security = "Tiêu Chuẩn Xác Thực An Toàn"
        val_security = "Xác Thực Toán Học • Chuẩn Zero-Griefing"

    full_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{doc_title}</title>
<style>
/* CSS Paged Media Standards - 100% Borderless Pure Academic Typography */
@page {{
    size: A4;
    margin: 24mm 20mm 24mm 20mm;
    @top-left {{
        content: "{running_header_left}";
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 7.5pt;
        font-weight: 600;
        color: #52525b;
        letter-spacing: 0.5px;
    }}
    @top-right {{
        content: "{running_header_right}";
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 8pt;
        font-weight: 700;
        color: #52525b;
        letter-spacing: 0.5px;
    }}
    @bottom-left {{
        content: "{running_footer_left}";
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 7pt;
        color: #71717a;
        letter-spacing: 0.3px;
    }}
    @bottom-right {{
        content: "Page " counter(page);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 7.5pt;
        font-weight: 600;
        color: #52525b;
    }}
}}

@page:first {{
    margin: 0;
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

* {{
    border-color: transparent !important;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 9.6pt;
    line-height: 1.62;
    color: #18181b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}}

/* Universal Link Styling: NEVER Underline */
a, a:link, a:visited, a:hover, a:active {{
    text-decoration: none !important;
    color: inherit !important;
    border: none !important;
}}

/* Universal Horizontal Rules: Completely Hidden (Zero Border Lines) */
hr {{
    display: none !important;
    border: none !important;
    height: 0 !important;
    margin: 0 !important;
}}

/* Cover Page: Black Premium - Pure Borderless */
.cover-page {{
    page-break-after: always;
    break-after: page;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #050505;
    color: #ffffff;
    padding: 75px 60px;
    box-sizing: border-box;
    border: none !important;
}}

.cover-header {{
    border: none !important;
    padding-bottom: 24px;
}}

.cover-logo-img {{
    height: 38px;
    width: auto;
    display: block;
    margin-bottom: 12px;
    border: none !important;
}}

.cover-brand-sub {{
    font-size: 8.5pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a1a1aa;
    margin-top: 4px;
    font-weight: 500;
    border: none !important;
}}

.cover-title-container {{
    margin: auto 0;
    border: none !important;
}}

.cover-tag {{
    display: inline-block;
    border: none !important;
    color: #d4d4d8;
    font-size: 7.8pt;
    font-weight: 700;
    padding: 0;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
}}

.cover-title {{
    font-size: 26pt;
    font-weight: 800;
    line-height: 1.22;
    color: #ffffff;
    margin: 0 0 16px 0;
    letter-spacing: -0.5px;
    border: none !important;
}}

.cover-subtitle {{
    font-size: 12.5pt;
    font-weight: 400;
    line-height: 1.55;
    color: #a1a1aa;
    margin: 0 0 32px 0;
    max-width: 92%;
    border: none !important;
}}

.cover-badges {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px 24px;
    margin-top: 28px;
    border: none !important;
    padding: 10px 0;
}}

.cover-badge-item {{
    font-size: 8.5pt;
    border: none !important;
}}

.cover-badge-label {{
    color: #71717a;
    text-transform: uppercase;
    font-size: 7pt;
    letter-spacing: 1px;
    font-weight: 600;
    border: none !important;
}}

.cover-badge-val {{
    color: #f4f4f5;
    font-weight: 600;
    margin-top: 3px;
    border: none !important;
}}

.cover-footer {{
    border: none !important;
    padding-top: 20px;
    font-size: 8pt;
    color: #71717a;
    display: flex;
    justify-content: space-between;
}}

/* Page 2: Frontmatter (Title, Subtitle, Metadata, ASCII logo) */
.frontmatter-page {{
    page-break-after: always;
    break-after: page;
    padding-top: 10px;
}}

.frontmatter-page h1 {{
    font-size: 16pt;
    font-weight: 800;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 10px;
    margin-bottom: 12px;
    letter-spacing: -0.2px;
}}

.frontmatter-page h2 {{
    font-size: 11.5pt;
    font-weight: 600;
    color: #27272a;
    border: none !important;
    padding: 0;
    margin-top: 0;
    margin-bottom: 18px;
    line-height: 1.45;
}}

/* Page 3: Dedicated Standalone Table of Contents Page */
.toc-page {{
    page-break-before: always;
    page-break-after: always;
    break-before: page;
    break-after: page;
    padding-top: 14px;
}}

.toc-page h2 {{
    font-size: 14.5pt;
    font-weight: 800;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 0;
    margin-bottom: 22px;
    letter-spacing: -0.2px;
}}

.toc-page ol, .toc-page ul {{
    padding-left: 20px;
    margin: 0;
}}

.toc-page li {{
    margin-bottom: 6px;
    font-size: 8.8pt;
    line-height: 1.45;
    color: #18181b;
}}

.toc-page li li {{
    margin-top: 4px;
    margin-bottom: 4px;
    font-size: 8.2pt;
    color: #3f3f46;
}}

.toc-page a {{
    text-decoration: none !important;
    color: #18181b !important;
    border: none !important;
}}

.toc-page a:hover {{
    text-decoration: none !important;
}}

/* Typography Hierarchies - 100% Borderless */
h1 {{
    font-size: 16pt;
    font-weight: 800;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 34px;
    margin-bottom: 14px;
    letter-spacing: -0.2px;
    page-break-after: avoid;
    break-after: avoid;
}}

h1:first-of-type {{
    margin-top: 12px;
}}

h2 {{
    font-size: 12.5pt;
    font-weight: 700;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 24px;
    margin-bottom: 10px;
    page-break-after: avoid;
    break-after: avoid;
}}

h3 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #18181b;
    border: none !important;
    padding: 0;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
    break-after: avoid;
}}

h4 {{
    font-size: 9.6pt;
    font-weight: 700;
    color: #27272a;
    border: none !important;
    padding: 0;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
    break-after: avoid;
}}

p {{
    margin-top: 0;
    margin-bottom: 10px;
    text-align: justify;
    color: #18181b;
    border: none !important;
}}

ul, ol {{
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 22px;
}}

li {{
    margin-bottom: 5px;
}}

/* Tables - Borderless Modern Layout */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
    border: none !important;
}}

th, td {{
    border: none !important;
    padding: 7px 10px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: #f4f4f5;
    color: #000000;
    font-weight: 700;
    letter-spacing: 0.3px;
    border: none !important;
}}

tr:nth-child(even) td {{
    background-color: #fafafa;
}}

/* Code Blocks & ASCII Architecture - 100% Borderless */
pre {{
    background-color: transparent !important;
    color: #000000;
    padding: 8px 0;
    border: none !important;
    border-radius: 0 !important;
    font-family: Consolas, "Courier New", monospace;
    font-size: 7.6pt;
    line-height: 1.35;
    overflow: hidden;
    margin: 14px 0;
    page-break-inside: avoid;
    break-inside: avoid;
}}

code {{
    font-family: Consolas, "Courier New", monospace;
    font-size: 8.8pt;
    background: transparent !important;
    color: #000000;
    padding: 0 !important;
    border: none !important;
}}

pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
}}

/* Academic Remarks / Notes - Pure Typography (Zero Borders) */
.academic-remark {{
    margin: 16px 20px;
    padding: 0;
    border: none !important;
    background: transparent !important;
    page-break-inside: avoid;
    break-inside: avoid;
}}

.academic-remark .remark-lead {{
    font-size: 8.5pt;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #000000;
    margin: 0 0 4px 0;
    text-align: left;
    border: none !important;
}}

.academic-remark .remark-body {{
    font-style: italic;
    color: #18181b;
    line-height: 1.6;
    margin: 0;
    text-align: justify;
    border: none !important;
}}

/* Mathematical Formulas - Pure Academic (Zero Borders) */
.math-display {{
    background: transparent !important;
    border: none !important;
    padding: 10px 0 !important;
    margin: 14px 0 !important;
    text-align: center;
    font-family: "Cambria Math", "Times New Roman", Times, serif;
    font-size: 11pt;
    color: #000000;
    page-break-inside: avoid;
    break-inside: avoid;
}}

.math-inline {{
    font-family: "Cambria Math", "Times New Roman", Times, serif;
    font-size: 9.8pt;
    color: #000000;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}}

.math-text {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-style: normal;
}}

/* Blockquotes */
blockquote {{
    margin: 14px 20px;
    padding: 0;
    border: none !important;
    background: transparent !important;
    color: #18181b;
    font-style: italic;
    page-break-inside: avoid;
    break-inside: avoid;
}}

blockquote p {{
    margin: 0;
    text-align: justify;
    border: none !important;
}}
</style>
</head>
<body>

<!-- Institutional Black Premium Cover Page (Zero Border Lines) -->
<div class="cover-page">
    <div class="cover-header">
        <img src="{logo_data_uri}" class="cover-logo-img" alt="HAICHAIN Logo" />
        <div class="cover-brand-sub">{brand_sub_text}</div>
    </div>
    
    <div class="cover-title-container">
        <div class="cover-tag">{tag_text}</div>
        <div class="cover-title">{doc_title}</div>
        <div class="cover-subtitle">{doc_subtitle}</div>
        
        <div class="cover-badges">
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_settlement}</div>
                <div class="cover-badge-val">{val_settlement}</div>
            </div>
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_token}</div>
                <div class="cover-badge-val">{val_token}</div>
            </div>
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_domain}</div>
                <div class="cover-badge-val">{val_domain}</div>
            </div>
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_security}</div>
                <div class="cover-badge-val">{val_security}</div>
            </div>
        </div>
    </div>
    
    <div class="cover-footer">
        <div>{doc_edition}</div>
        <div>haichain.si</div>
    </div>
</div>

<!-- Main Body Content with Isolated Frontmatter and Dedicated TOC Page -->
<div class="document-content">
{full_content_html}
</div>

</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    # Command line invocation of Microsoft Edge in headless print-to-pdf mode
    edge_cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    
    print(f"[*] Compiling PDF via Edge Engine to: {pdf_path}")
    result = subprocess.run(edge_cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"[+] Successfully generated: {pdf_filename} ({size_kb:.1f} KB)")
    else:
        print(f"[-] Error generating PDF: {result.stderr}")
    
    # Clean up temporary HTML file
    if os.path.exists(html_path):
        os.remove(html_path)

if __name__ == "__main__":
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_EN.md", "HAICHAIN_WHITEPAPER_V1.0_EN.pdf", lang="en")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_VI.md", "HAICHAIN_WHITEPAPER_V1.0_VI.pdf", lang="vi")
