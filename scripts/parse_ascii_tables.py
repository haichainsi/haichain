import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# We can define a generic table converter that parses an ASCII table with "+---" and "|" into a clean Markdown table!
def parse_ascii_table_to_markdown(ascii_text):
    lines = [l.strip() for l in ascii_text.strip().splitlines() if l.strip()]
    # remove outer code block fences
    if lines and lines[0].startswith('```'):
        lines = lines[1:]
    if lines and lines[-1].startswith('```'):
        lines = lines[:-1]
    
    # Filter out pure border lines like +--------------------+
    content_lines = []
    for l in lines:
        if re.match(r'^\+[ -]+\+$', l):
            continue
        if l.startswith('|') and l.endswith('|'):
            # inner line
            content_lines.append(l[1:-1])
        elif l.startswith('|'):
            content_lines.append(l[1:])
    
    if not content_lines:
        return ascii_text

    # First content line is often title
    title = content_lines[0].strip()
    
    # Find header row
    header_idx = 1
    while header_idx < len(content_lines) and not content_lines[header_idx].strip():
        header_idx += 1
        
    if header_idx >= len(content_lines):
        return ascii_text

    raw_header = content_lines[header_idx]
    
    # Determine column boundaries by scanning multiple whitespace separators in header
    # or by known column headers
    cols = [c.strip() for c in re.split(r'\s{2,}', raw_header.strip()) if c.strip()]
    if len(cols) < 2:
        return ascii_text

    # Parse rows
    rows = []
    current_row = None
    
    for l in content_lines[header_idx+1:]:
        s = l.strip()
        if not s:
            if current_row:
                rows.append(current_row)
                current_row = None
            continue
            
        parts = [p.strip() for p in re.split(r'\s{2,}', s) if p.strip()]
        
        # If parts match column count, it's a new row
        if len(parts) == len(cols):
            if current_row:
                rows.append(current_row)
            current_row = parts
        elif len(parts) > 0:
            if current_row:
                # append to current row cells if multiline continuation
                if len(parts) <= len(current_row):
                    for idx, p in enumerate(parts):
                        current_row[idx] += " " + p
                else:
                    current_row[-1] += " " + " ".join(parts)
            else:
                # new row with fewer parts
                padded = parts + [""] * (len(cols) - len(parts))
                current_row = padded
                
    if current_row:
        rows.append(current_row)

    if not rows:
        return ascii_text

    # Build markdown table
    header_line = "| " + " | ".join(cols) + " |"
    sep_line = "| " + " | ".join([":---" for _ in cols]) + " |"
    row_lines = []
    for r in rows:
        clean_cells = [c.replace("|", "\\|").strip() for c in r]
        # bold first cell
        if clean_cells and not clean_cells[0].startswith('**'):
            clean_cells[0] = f"**{clean_cells[0]}**"
        row_lines.append("| " + " | ".join(clean_cells) + " |")

    md_table = header_line + "\n" + sep_line + "\n" + "\n".join(row_lines)
    return md_table

print("ASCII Parser module ready.")
