import re, sys, os

with open('scripts/recompile_all_10_pdfs.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add KaTeX CSS loading near top
katex_load_snippet = """
with open(os.path.join(WORKSPACE_DIR, "assets/haichain-official-logo-white.png"), "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')

# Prepare local KaTeX CSS with absolute file:// font paths
katex_css_path = os.path.join(WORKSPACE_DIR, "node_modules", "katex", "dist", "katex.min.css")
with open(katex_css_path, "r", encoding="utf-8") as f:
    raw_katex_css = f.read()

fonts_dir = os.path.abspath(os.path.join(WORKSPACE_DIR, "node_modules", "katex", "dist", "fonts")).replace('\\\\', '/')
raw_katex_css = raw_katex_css.replace('fonts/', f'file:///{fonts_dir}/')
katex_style_tag = f"<style>\\n{raw_katex_css}\\n.math-display-block {{ margin: 12px 0 !important; text-align: center !important; }}\\n.katex {{ font-size: 1.05em !important; }}\\n</style>"
"""

target1 = """with open(os.path.join(WORKSPACE_DIR, "assets/haichain-official-logo-white.png"), "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')"""

code = code.replace(target1, katex_load_snippet.strip())

# 2. Inject {katex_style_tag} inside <head>
head_target = """<head>
<meta charset="utf-8">"""

head_replacement = """<head>
<meta charset="utf-8">
{katex_style_tag}"""

code = code.replace(head_target, head_replacement)

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

code = code.replace(edge_target, edge_replacement)

with open('scripts/recompile_all_10_pdfs.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("scripts/recompile_all_10_pdfs.py patched safely!")
