import os
import subprocess
import markdown
import shutil

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
APP_DIR = os.path.join(WORKSPACE_DIR, "app")

def compile_pdf(md_filename, pdf_filename, title):
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, f"temp_{os.path.splitext(pdf_filename)[0]}.html")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    body_html = md_converter.convert(md_text)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
@page {{
    size: A4;
    margin: 18mm 18mm 18mm 18mm;
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
    line-height: 1.55;
    font-size: 9.5pt;
    background: #ffffff;
    margin: 0;
    padding: 0;
}}
h1 {{
    font-size: 17pt;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-top: 0;
    margin-bottom: 5px;
    color: #09090b;
    border-bottom: 2px solid #18181b;
    padding-bottom: 6px;
}}
h2 {{
    font-size: 12pt;
    font-weight: 700;
    margin-top: 14px;
    margin-bottom: 4px;
    color: #18181b;
}}
h3 {{
    font-size: 10pt;
    font-weight: 600;
    margin-top: 12px;
    margin-bottom: 4px;
    color: #3f3f46;
}}
p, li {{
    color: #27272a;
    margin-bottom: 6px;
}}
ul, ol {{
    padding-left: 20px;
    margin-top: 3px;
    margin-bottom: 10px;
}}
strong {{
    font-weight: 700;
    color: #09090b;
}}
code {{
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 8.5pt;
    background-color: #f4f4f5;
    padding: 2px 4px;
    border-radius: 4px;
    border: 1px solid #e4e4e7;
    color: #09090b;
}}
pre {{
    background-color: #09090b;
    color: #f4f4f5;
    padding: 10px 14px;
    border-radius: 6px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 8pt;
    line-height: 1.4;
    overflow-x: auto;
    margin: 10px 0;
}}
pre code {{
    background-color: transparent;
    padding: 0;
    border: none;
    color: inherit;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 8.5pt;
}}
th, td {{
    border: 1px solid #d4d4d8;
    padding: 6px 10px;
    text-align: left;
}}
th {{
    background-color: #f4f4f5;
    font-weight: 700;
    color: #09090b;
}}
hr {{
    border: none;
    border-top: 1px solid #e4e4e7;
    margin: 12px 0;
}}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""
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
    subprocess.run(cmd, check=True)
    if os.path.exists(html_path):
        os.remove(html_path)
    
    # Mirror to app/ directory
    app_pdf_path = os.path.join(APP_DIR, pdf_filename)
    shutil.copy2(pdf_path, app_pdf_path)
    print(f"[OK] Successfully compiled {pdf_filename} and mirrored to app/")

if __name__ == "__main__":
    compile_pdf(
        "HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.md",
        "HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf",
        "HAICHAIN Pre-Seed SAFT Agreement (Official English Standard)"
    )
    compile_pdf(
        "HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md",
        "HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf",
        "HAICHAIN Pre-Seed 1-Pager Investment Memo (English Edition)"
    )
    
    # Also overwrite the VI_EN files with English default so legacy routes immediately serve English
    compile_pdf(
        "HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.md",
        "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf",
        "HAICHAIN Pre-Seed SAFT Agreement (Official English Standard)"
    )
    compile_pdf(
        "HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md",
        "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf",
        "HAICHAIN Pre-Seed 1-Pager Investment Memo (English Edition)"
    )
