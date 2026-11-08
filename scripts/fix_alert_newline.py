import sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['dashboard.html', 'app/dashboard.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace the multi-line single quote string with '\n\n'
    bad_pattern = "alert(getVestingText('copiedToken2022Alert') + '\n\n' + TOKEN_2022_MINT);"
    bad_pattern_crlf = "alert(getVestingText('copiedToken2022Alert') + '\r\n\r\n' + TOKEN_2022_MINT);"
    good_pattern = "alert(getVestingText('copiedToken2022Alert') + '\\n\\n' + TOKEN_2022_MINT);"

    if bad_pattern in c:
        c = c.replace(bad_pattern, good_pattern)
        print(f"Fixed LF bad pattern in {fpath}")
    elif bad_pattern_crlf in c:
        c = c.replace(bad_pattern_crlf, good_pattern)
        print(f"Fixed CRLF bad pattern in {fpath}")
    else:
        # Regex fallback
        import re
        c, n = re.subn(r"alert\(getVestingText\('copiedToken2022Alert'\)\s*\+\s*'[\r\n]+'\s*\+\s*TOKEN_2022_MINT\);",
                       "alert(getVestingText('copiedToken2022Alert') + '\\n\\n' + TOKEN_2022_MINT);", c)
        print(f"Regex replaced in {fpath}: {n}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
