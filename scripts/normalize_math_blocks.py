import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

for fname in sorted(glob.glob("HAICHAIN_WHITEPAPER_V1.0_*.md")):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Normalize any sequence of 3 or more dollars to 2 dollars
    text = re.sub(r'\${3,}', '$$', text)
    
    # Ensure every $$ is preceded by \n\n if preceded by text, and followed by \n\n if followed by text
    # Let's cleanly format $$...$$ blocks
    def clean_math_blocks(t):
        lines = t.splitlines()
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            # If line is single-line display math e.g. $$...$$
            m = re.match(r'^\s*\$\$(.+?)\$\$\s*$', line)
            if m:
                formula = m.group(1).strip()
                # Ensure blank line before
                if new_lines and new_lines[-1].strip() != '':
                    new_lines.append('')
                new_lines.append(f"$${formula}$$")
                new_lines.append('')
                i += 1
                continue
            
            # If line starts a multi-line display math e.g. $$
            if line.strip() == '$$':
                if new_lines and new_lines[-1].strip() != '':
                    new_lines.append('')
                new_lines.append('$$')
                i += 1
                while i < len(lines) and lines[i].strip() != '$$':
                    new_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    new_lines.append('$$')
                    new_lines.append('')
                    i += 1
                continue

            new_lines.append(line)
            i += 1
            
        res = '\n'.join(new_lines)
        res = re.sub(r'\n{3,}', '\n\n', res) + '\n'
        return res

    cleaned = clean_math_blocks(text)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(cleaned)

print("[OK] Normalized all display math blocks in root files.")
