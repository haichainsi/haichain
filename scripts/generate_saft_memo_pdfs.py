import os
import re
import subprocess
import markdown

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"

def update_markdown_tokens():
    for fname in ["HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md"]:
        fpath = os.path.join(WORKSPACE_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Replace $HAI with $HAISI (ensure no $HAISISI)
        text = re.sub(r'\$HAI(?!SI)\b', '$HAISI', text)
        text = text.replace("$HAI (Solana", "$HAISI (Solana")
        text = text.replace("triệu $HAI", "triệu $HAISI")
        text = text.replace("tỷ $HAI", "tỷ $HAISI")
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[+] Updated {fname} to $HAISI")

def compile_pdf(md_filename, pdf_filename, title):
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, f"temp_{os.path.splitext(pdf_filename)[0]}.html")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    body_html = md_converter.convert(md_text)
    
    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
@page {{
    size: A4;
    margin: 20mm 18mm 20mm 18mm;
    @bottom-center {{
        content: counter(page);
        font-size: 8pt;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #71717a;
    }}
}}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #18181b;
    line-height: 1.6;
    font-size: 9.5pt;
    background: #ffffff;
    margin: 0;
    padding: 0;
}}
h1 {{
    font-size: 18pt;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-top: 0;
    margin-bottom: 6px;
    color: #09090b;
    border-bottom: 2px solid #18181b;
    padding-bottom: 8px;
}}
h2 {{
    font-size: 13pt;
    font-weight: 700;
    margin-top: 18px;
    margin-bottom: 6px;
    color: #18181b;
}}
h3 {{
    font-size: 10.5pt;
    font-weight: 600;
    margin-top: 14px;
    margin-bottom: 4px;
    color: #3f3f46;
}}
p, li {{
    color: #27272a;
    margin-bottom: 8px;
}}
ul, ol {{
    padding-left: 20px;
    margin-top: 4px;
    margin-bottom: 12px;
}}
strong {{
    font-weight: 700;
    color: #09090b;
}}
code {{
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 8.5pt;
    background-color: #f4f4f5;
    padding: 2px 5px;
    border-radius: 4px;
    color: #18181b;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 8.5pt;
}}
th, td {{
    padding: 8px 10px;
    border: 1px solid #e4e4e7;
    text-align: left;
}}
th {{
    background-color: #f4f4f5;
    font-weight: 700;
    color: #09090b;
}}
blockquote {{
    margin: 12px 0;
    padding: 8px 14px;
    background: #f4f4f5;
    border-left: 3px solid #18181b;
    color: #3f3f46;
}}
hr {{
    border: none;
    border-top: 1px solid #e4e4e7;
    margin: 20px 0;
}}
.header-badge {{
    display: inline-block;
    font-size: 7.5pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    background: #18181b;
    color: #ffffff;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 10px;
}}
</style>
</head>
<body>
<div class="header-badge">HAICHAIN INSTITUTIONAL LEGAL DOCUMENT</div>
{body_html}
</body>
</html>"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    
    print(f"[*] Compiling PDF: {pdf_filename}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"[+] Successfully generated {pdf_filename} ({size_kb:.1f} KB)")
        
        # Copy to app directory as well
        app_pdf = os.path.join(WORKSPACE_DIR, "app", pdf_filename)
        with open(pdf_path, "rb") as src, open(app_pdf, "wb") as dst:
            dst.write(src.read())
        print(f"[+] Synced to app/{pdf_filename}")
    else:
        print(f"[-] Error: {res.stderr}")
        
    if os.path.exists(html_path):
        os.remove(html_path)

if __name__ == "__main__":
    update_markdown_tokens()
    compile_pdf(
        "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md",
        "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf",
        "HAICHAIN Pre-Seed SAFT Agreement (VI & EN)"
    )
    compile_pdf(
        "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md",
        "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf",
        "HAICHAIN Pre-Seed 1-Pager Investment Teaser Memo"
    )
