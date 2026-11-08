with open('scripts/convert_all_10_languages_tables.py', 'r', encoding='utf-8') as f:
    text = f.read()

with open('scripts/apply_all_tables_multilingual.py', 'r', encoding='utf-8') as f2:
    text2 = f2.read()

idx = text.find("'ZH': {")
end = text.find("    }\n}", idx)
zh_code = text[idx:end+6]

text2 = text2.replace("TABLES = {", "TABLES = {\n    " + zh_code + ",")
with open('scripts/apply_all_tables_multilingual.py', 'w', encoding='utf-8') as f:
    f.write(text2)
print('Added ZH to TABLES successfully.')
