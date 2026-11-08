import sys

with open('scripts/recompile_all_10_pdfs.py', 'r', encoding='utf-8') as f:
    c = f.read()

target = "clean_md = re.sub(r'(?<!\\\\)\\$(?=[0-9A-Za-z])', r'&#36;', clean_md)"
replacement = "# Currency signs remain literal $ without &#36;\n    # clean_md = re.sub(r'(?<!\\\\)\\$(?=[0-9A-Za-z])', r'&#36;', clean_md)"

if target in c:
    c = c.replace(target, replacement)
    target2 = 'with open(html_path, "w", encoding="utf-8") as f:'
    replacement2 = 'full_html = full_html.replace("&#36;", "$").replace("&amp;#36;", "$")\n    with open(html_path, "w", encoding="utf-8") as f:'
    c = c.replace(target2, replacement2)
    with open('scripts/recompile_all_10_pdfs.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Successfully patched scripts/recompile_all_10_pdfs.py')
else:
    print('Target not found in recompile_all_10_pdfs.py')

# Also patch render_math_cli.js
with open('scripts/render_math_cli.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("&#36;$1", "___HAICHAIN_DOLLAR_TEMP___$1")
js = js.replace(
    "fs.writeFileSync(outputFile, parts.join(''), 'utf-8');",
    "let out = parts.join('').replace(/___HAICHAIN_DOLLAR_TEMP___/g, '$').replace(/&#36;/g, '$').replace(/&amp;#36;/g, '$');\nfs.writeFileSync(outputFile, out, 'utf-8');"
)

with open('scripts/render_math_cli.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Successfully patched scripts/render_math_cli.js')
