with open('scripts/recompile_all_10_pdfs.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add @page :first
old_page = """@page {{
    size: A4;
    margin: 0;
}}
@page cover {{"""

new_page = """@page {{
    size: A4;
    margin: 0;
}}
@page :first {{
    size: A4;
    margin: 0 !important;
}}
@page cover {{"""

text = text.replace(old_page, new_page)

# 2. Update cover page styling
old_cover = """/* COVER PAGE (100% TRUE FULL-BLEED BLACK PREMIUM) */
.cover-page {{
    page: cover;
    width: 210mm;
    height: 297mm;
    box-sizing: border-box;
    background: #000000 !important;"""

new_cover = """/* COVER PAGE (100% TRUE FULL-BLEED BLACK PREMIUM) */
.cover-page {{
    page: cover;
    width: 210mm;
    min-width: 210mm;
    height: 297mm;
    min-height: 297mm;
    box-sizing: border-box;
    background-color: #000000 !important;
    background: #000000 !important;"""

text = text.replace(old_cover, new_cover)

# 3. Update pre & table styling
old_pre_table = """pre {{
    background-color: #09090b;
    color: #f4f4f5;
    padding: 7px 9px;
    border-radius: 4px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 5.1pt;
    line-height: 1.22;
    letter-spacing: -0.28px;
    white-space: pre !important;
    overflow: hidden !important;
    margin: 8px 0;
    max-width: 100% !important;
    box-sizing: border-box !important;
}}
pre code {{
    background-color: transparent !important;
    padding: 0 !important;
    border: none !important;
    color: inherit !important;
    font-size: inherit !important;
    letter-spacing: inherit !important;
    white-space: pre !important;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8pt;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
}}
th, td {{
    border: 1px solid #d4d4d8;
    padding: 5px 8px;
    text-align: left;
}}
th {{
    background-color: #f4f4f5;
    font-weight: 700;
    color: #09090b;
}}"""

new_pre_table = """pre {{
    background-color: #09090b !important;
    color: #f4f4f5 !important;
    padding: 8px 10px !important;
    border-radius: 4px !important;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace !important;
    font-size: 5.8pt !important;
    line-height: 1.28 !important;
    letter-spacing: 0 !important;
    white-space: pre !important;
    overflow: hidden !important;
    margin: 10px 0 !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
}}
pre code {{
    background-color: transparent !important;
    padding: 0 !important;
    border: none !important;
    color: inherit !important;
    font-size: inherit !important;
    letter-spacing: 0 !important;
    white-space: pre !important;
}}
table {{
    width: 100% !important;
    border-collapse: collapse !important;
    margin: 12px 0 16px 0 !important;
    font-size: 7.6pt !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
}}
thead {{
    display: table-header-group !important;
}}
tr {{
    page-break-inside: avoid !important;
    break-inside: avoid !important;
}}
th {{
    background-color: #09090b !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    font-size: 7.2pt !important;
    letter-spacing: 0.5px !important;
    padding: 6px 8px !important;
    border: 1px solid #27272a !important;
}}
td {{
    border: 1px solid #e4e4e7 !important;
    padding: 6px 8px !important;
    text-align: left !important;
    vertical-align: top !important;
    color: #27272a !important;
    line-height: 1.4 !important;
}}
tr:nth-child(even) td {{
    background-color: #fafafa !important;
}}"""

text = text.replace(old_pre_table, new_pre_table)

with open('scripts/recompile_all_10_pdfs.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("scripts/recompile_all_10_pdfs.py updated successfully.")
