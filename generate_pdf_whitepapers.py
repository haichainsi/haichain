# -*- coding: utf-8 -*-
"""
HAICHAIN International Whitepaper PDF Generator
Compiles Markdown Whitepapers into Institutional-Grade PDF Documents
Using Headless Browser Engine with Paged Media CSS
Style: Pure Academic Minimalist Typography (Zero Boxes, Zero Vertical Accent Bars)
Cover: Black Premium with Official White Logo
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

    # Convert Markdown to HTML
    md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    body_html = md_converter.convert(text_with_math)
    body_html = process_callouts(body_html)

    logo_data_uri = get_logo_base64()

    # Document metadata and titles
    if lang == "en":
        doc_title = "HAICHAIN WHITEPAPER v1.0"
        doc_subtitle = "Universal Autonomous Machine Financial & Cognitive Operating System"
        doc_edition = "Official Whitepaper v1.0 • Institutional Standard Edition"
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
        doc_subtitle = "Hệ Điều Hành Tài Chính & Nhận Thức Toàn Cầu Cho Tác Tử Trí Tuệ Nhân Tạo"
        doc_edition = "Sách Trắng v1.0 • Phiên Bản Tiêu Chuẩn Thể Chế Quốc Tế"
        running_header_left = "SÁCH TRẮNG HAICHAIN v1.0"
        running_header_right = "haichain.si"
        running_footer_left = "BẢO LƯU MỌI QUYỀN • HỘI ĐỒNG KIẾN TRÚC HỆ THỐNG PHÂN TÁN HAICHAIN"
        tag_text = "GIAO THỨC HỆ ĐIỀU HÀNH SIÊU TRÍ TUỆ NHÂN TẠO"
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
/* CSS Paged Media Standards - Pure Academic Monochrome (Zero Boxes / Zero Accent Bars) */
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

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 9.6pt;
    line-height: 1.62;
    color: #18181b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}}

/* Cover Page: Black Premium Minimalist */
.cover-page {{
    page-break-after: always;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #050505;
    color: #ffffff;
    padding: 75px 60px;
    box-sizing: border-box;
}}

.cover-header {{
    border-bottom: 1px solid #27272a;
    padding-bottom: 24px;
}}

.cover-logo-img {{
    height: 38px;
    width: auto;
    display: block;
    margin-bottom: 12px;
}}

.cover-brand-sub {{
    font-size: 8.5pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a1a1aa;
    margin-top: 4px;
    font-weight: 500;
}}

.cover-title-container {{
    margin: auto 0;
}}

.cover-tag {{
    display: inline-block;
    border-bottom: 1px solid #3f3f46;
    color: #d4d4d8;
    font-size: 7.8pt;
    font-weight: 700;
    padding-bottom: 4px;
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
}}

.cover-subtitle {{
    font-size: 12.5pt;
    font-weight: 400;
    line-height: 1.55;
    color: #a1a1aa;
    margin: 0 0 32px 0;
    max-width: 92%;
}}

.cover-badges {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px 24px;
    margin-top: 28px;
    border-top: 1px solid #27272a;
    border-bottom: 1px solid #27272a;
    padding: 20px 0;
}}

.cover-badge-item {{
    font-size: 8.5pt;
}}

.cover-badge-label {{
    color: #71717a;
    text-transform: uppercase;
    font-size: 7pt;
    letter-spacing: 1px;
    font-weight: 600;
}}

.cover-badge-val {{
    color: #f4f4f5;
    font-weight: 600;
    margin-top: 3px;
}}

.cover-footer {{
    border-top: 1px solid #27272a;
    padding-top: 20px;
    font-size: 8pt;
    color: #71717a;
    display: flex;
    justify-content: space-between;
}}

/* Typography Hierarchies - Pure Academic Clean (Zero Vertical Accent Bars) */
h1 {{
    font-size: 16pt;
    font-weight: 800;
    color: #000000;
    border-bottom: 1px solid #000000;
    padding-bottom: 5px;
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
    border: none;
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
    border: none;
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
    border: none;
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
}}

ul, ol {{
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 22px;
}}

li {{
    margin-bottom: 5px;
}}

a {{
    color: #000000;
    text-decoration: underline;
}}

/* Academic Booktabs Tables (Classic LaTeX Style) */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
    border-top: 1.5px solid #000000;
    border-bottom: 1.5px solid #000000;
}}

th, td {{
    border: none;
    border-bottom: 1px solid #e4e4e7;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: transparent;
    color: #000000;
    font-weight: 700;
    border-bottom: 1px solid #000000;
    letter-spacing: 0.3px;
}}

/* Technical Blocks / ASCII Architecture (Academic Hairline Style, No Dark Background) */
pre {{
    background-color: #fafafa;
    color: #000000;
    padding: 12px 14px;
    border-top: 1px solid #000000;
    border-bottom: 1px solid #000000;
    border-left: none;
    border-right: none;
    border-radius: 0;
    font-family: Consolas, "Courier New", monospace;
    font-size: 7.6pt;
    line-height: 1.35;
    overflow: hidden;
    margin: 16px 0;
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

/* Academic Remarks / Notes - Pure Typography (Zero Boxes, Zero Bars, Zero Backgrounds) */
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
}}

.academic-remark .remark-body {{
    font-style: italic;
    color: #18181b;
    line-height: 1.6;
    margin: 0;
    text-align: justify;
}}

/* Mathematical Formulas - Pure Academic (Zero Boxes, Zero Bars, Zero Backgrounds) */
.math-display {{
    background: transparent !important;
    border: none !important;
    border-left: none !important;
    border-radius: 0 !important;
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
}}

hr {{
    border: none;
    border-top: 1px solid #e4e4e7;
    margin: 24px 0;
}}
</style>
</head>
<body>

<!-- Institutional Black Premium Cover Page -->
<div class="cover-page">
    <div class="cover-header">
        <img src="{logo_data_uri}" class="cover-logo-img" alt="HAICHAIN Logo" />
        <div class="cover-brand-sub">Universal Autonomous Machine Financial & Cognitive Operating System</div>
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

<!-- Main Body Content -->
<div class="document-content">
{body_html}
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
