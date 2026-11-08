import re
import json

with open('i18n.js', 'r', encoding='utf-8') as f:
    i18n_content = f.read()

# We can search for the languages object or keys
langs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he']

for lang in langs:
    print(f"\n=================== LANG: {lang} ===================")
    # find keys under this lang starting with 'dev.' or 'mcp.'
    pattern = rf"['\"]?{lang}['\"]?\s*:\s*\{{([\s\S]*?)\n\s*\}},?\s*(?:['\"]?[a-z]{{2}}['\"]?\s*:|$)"
    # Alternative: search line by line in the file
    pass

# Better approach: parse the JS file using a small node script to output JSON of dev.* and mcp.* keys
