import os, re

target_file = 'scripts/recompile_all_10_pdfs.py'
with open(target_file, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace import line to include json
code = code.replace("import os, subprocess, markdown, shutil, sys, fitz, re, base64", "import os, subprocess, markdown, shutil, sys, fitz, re, base64, json")

compile_pdf_body = '''def compile_pdf(lang):
    c = cover_dict[lang]
    md_filename = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
    pdf_filename = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.pdf"
    
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, f"temp_{os.path.splitext(pdf_filename)[0]}.html")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # 1. Protect code blocks
    code_blocks = []
    def save_code(m):
        idx = len(code_blocks)
        code_blocks.append(m.group(0))
        return f"CODEBLOCKPLACEHOLDER{idx}END"

    clean_md = re.sub(r'```[\\s\\S]*?```', save_code, md_text)

    math_items = []

    # 2. Extract display math ($$...$$)
    def save_display_math(m):
        idx = len(math_items)
        formula = m.group(1).strip()
        math_items.append(('display', formula))
        return f"\\n\\nKATEXDISPLAYPLACEHOLDER{idx}END\\n\\n"

    clean_md = re.sub(r'\\$\\$([\\s\\S]*?)\\$\\$', save_display_math, clean_md)

    # 3. Extract inline math ($...$)
    def is_valid_inline_math(f):
        f = f.strip()
        if not f or len(f) > 300:
            return False
        if re.match(r'^\\d[\\d,.]*(?:\\s*(?:million|billion|trillion|[kKmMbB]))?\\+?$', f):
            return False
        if re.match(r'^(?:HAISI|SOL|USDT|BTC|ETH|USD)\\b', f):
            return False
        if '\\\\' in f or '_' in f or '^' in f or '{' in f or '}' in f:
            return True
        if re.search(r'\\b[a-zA-Z]\\b\\s*(=|<|>|\\\\le|\\\\ge|\\+|-|\\*|/)\\s*', f):
            return True
        if re.match(r'^[a-zA-Z](?:_[a-zA-Z0-9]+)?$', f):
            return True
        if re.match(r'^[a-zA-Z]\\s*,\\s*[a-zA-Z]$', f):
            return True
        if re.match(r'^[IT]_[1-9]$', f):
            return True
        return False

    def save_inline_math(m):
        formula = m.group(1).strip()
        if is_valid_inline_math(formula):
            idx = len(math_items)
            math_items.append(('inline', formula))
            return f"KATEXINLINEPLACEHOLDER{idx}END"
        return m.group(0)

    clean_md = re.sub(r'(?<!\\\\)\\$([^\\$\\n\\r]+?)\\$', save_inline_math, clean_md)

    # 4. Any remaining $ is plain currency! Protect them so HTML doesn't choke
    clean_md = re.sub(r'(?<!\\\\)\\$(?=[0-9A-Za-z])', r'&#36;', clean_md)

    # 5. Restore code blocks
    for i, cb in enumerate(code_blocks):
        clean_md = clean_md.replace(f"CODEBLOCKPLACEHOLDER{i}END", cb)

    # 6. Render math_items using node scripts/render_math_json.js
    temp_json_in = os.path.join(WORKSPACE_DIR, f"temp_math_in_{lang}.json")
    temp_json_out = os.path.join(WORKSPACE_DIR, f"temp_math_out_{lang}.json")
    with open(temp_json_in, "w", encoding="utf-8") as f:
        json.dump(math_items, f, ensure_ascii=False)

    subprocess.run(["node", "scripts/render_math_json.js", temp_json_in, temp_json_out], check=True)
    with open(temp_json_out, "r", encoding="utf-8") as f:
        rendered_math = json.load(f)

    if os.path.exists(temp_json_in):
        os.remove(temp_json_in)
    if os.path.exists(temp_json_out):
        os.remove(temp_json_out)

    # 7. Match TOC header and body
    toc_pattern = r'(^##[^\\n]*TABLE OF CONTENTS[^\\n]*\\n)(.*?)(\\n---\\n|\\n## 1|\\n# 1|\\n## [^\\n]*1\\.)'
    m = re.search(toc_pattern, clean_md, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    
    if m:
        toc_header_md = m.group(1).strip()
        toc_body_md = m.group(2).strip()
        
        before_toc_md = clean_md[:m.start()].strip()
        after_toc_md = clean_md[m.end():].strip()
        
        conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        toc_html = conv.convert(f"{toc_header_md}\\n\\n{toc_body_md}")
        # Strip code tags inside TOC links
        toc_html = re.sub(r'<code>(.*?)</code>', r'\\1', toc_html)
        
        conv2 = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        before_toc_html = conv2.convert(before_toc_md)
        
        conv3 = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        after_toc_html = conv3.convert(after_toc_md)
        
        content_html = f"""
        <div class="toc-page">
            {toc_html}
        </div>
        <div class="body-content">
            {before_toc_html}
            <hr />
            {after_toc_html}
        </div>
        """
    else:
        conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        body_html = conv.convert(clean_md)
        content_html = f'<div class="body-content">{body_html}</div>'

    # 8. Substitute pre-rendered KaTeX math
    for idx, r_html in enumerate(rendered_math):
        content_html = content_html.replace(f"<p>KATEXDISPLAYPLACEHOLDER{idx}END</p>", r_html)
        content_html = content_html.replace(f"KATEXDISPLAYPLACEHOLDER{idx}END", r_html)
        content_html = content_html.replace(f"KATEXINLINEPLACEHOLDER{idx}END", r_html)
'''

pattern = r'def compile_pdf\(lang\):.*?(?=direction = "rtl" if lang == "HE" else "ltr")'
m = re.search(pattern, code, flags=re.DOTALL)
if m:
    code = code[:m.start()] + compile_pdf_body + "\n    " + code[m.end():]
    print("Function body replaced successfully.")
else:
    print("Error: compile_pdf pattern not found!")

# Update edge call
old_edge = """    rendered_html_path = html_path.replace(".html", "_rendered.html")
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

new_edge = """    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(html_path):
        os.remove(html_path)"""

if old_edge in code:
    code = code.replace(old_edge, new_edge)
    print("Edge call replaced successfully.")
else:
    print("Note: old edge call already replaced or different.")

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("scripts/recompile_all_10_pdfs.py patched and ready!")
