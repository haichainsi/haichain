import os, sys

with open('scripts/recompile_all_10_pdfs.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Define katex_style_tag near top
top_target = """with open(os.path.join(WORKSPACE_DIR, "assets/haichain-official-logo-white.png"), "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')"""

top_replacement = """with open(os.path.join(WORKSPACE_DIR, "assets/haichain-official-logo-white.png"), "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')

# Prepare local KaTeX CSS with absolute file:// font paths
katex_css_path = os.path.join(WORKSPACE_DIR, "node_modules", "katex", "dist", "katex.min.css")
with open(katex_css_path, "r", encoding="utf-8") as f:
    raw_katex_css = f.read()

fonts_dir = os.path.abspath(os.path.join(WORKSPACE_DIR, "node_modules", "katex", "dist", "fonts")).replace('\\\\', '/')
raw_katex_css = raw_katex_css.replace('fonts/', f'file:///{fonts_dir}/')
katex_style_tag = "<style>\\n" + raw_katex_css + "\\n.math-display-block { margin: 12px 0 !important; text-align: center !important; }\\n.katex { font-size: 1.05em !important; }\\n</style>"
"""

if top_target in code:
    code = code.replace(top_target, top_replacement)
    print("Top target replaced.")
else:
    print("Warning: top target not found!")

# 2. Add {katex_style_tag} to head
head_target = """<meta charset="utf-8">
<title>{c['title_pdf']}</title>"""

head_replacement = """<meta charset="utf-8">
<title>{c['title_pdf']}</title>
{katex_style_tag}"""

if head_target in code:
    code = code.replace(head_target, head_replacement)
    print("Head target replaced.")
else:
    print("Warning: head target not found!")

# 3. Add node render_math_cli.js execution before Edge call
edge_target = """    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(html_path):
        os.remove(html_path)"""

edge_replacement = """    rendered_html_path = html_path.replace(".html", "_rendered.html")
    subprocess.run(["node", "scripts/render_math_cli.js", html_path, rendered_html_path], check=True)
    
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file:///{rendered_html_path.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(html_path):
        os.remove(html_path)
    if os.path.exists(rendered_html_path):
        os.remove(rendered_html_path)"""

if edge_target in code:
    code = code.replace(edge_target, edge_replacement)
    print("Edge target replaced.")
else:
    print("Warning: edge target not found!")

with open('scripts/recompile_all_10_pdfs.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("scripts/recompile_all_10_pdfs.py updated successfully!")
