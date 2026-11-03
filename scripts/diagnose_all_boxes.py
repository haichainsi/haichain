import glob, sys, unicodedata, re

sys.stdout.reconfigure(encoding='utf-8')

def display_width(s):
    w = 0
    for c in s:
        ea = unicodedata.east_asian_width(c)
        if ea in ('W', 'F'):
            w += 2
        else:
            w += 1
    return w

def analyze_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    in_code = False
    block = []
    block_start = 0
    boxes_in_file = []
    
    for idx, line in enumerate(lines):
        if line.startswith('```'):
            if not in_code:
                in_code = True
                block_start = idx + 1
                block = []
            else:
                in_code = False
                # analyze block for boxes
                # A box is a contiguous group of lines where top/bottom are +---+ and middle are |...|
                i = 0
                while i < len(block):
                    l_str = block[i].rstrip()
                    if re.match(r'^\s*\+[-=+]+\+\s*$', l_str):
                        # Start of a box!
                        box_start_idx = block_start + i
                        box_lines = [l_str]
                        j = i + 1
                        while j < len(block):
                            lj = block[j].rstrip()
                            if re.match(r'^\s*\|.*\|\s*$', lj) or re.match(r'^\s*\+[-=+]+\+\s*$', lj):
                                box_lines.append(lj)
                                if re.match(r'^\s*\+[-=+]+\+\s*$', lj) and j > i + 1:
                                    # Could be a divider or bottom border
                                    # Check if subsequent line is not a box line
                                    if j + 1 >= len(block) or (not re.match(r'^\s*\|.*\|\s*$', block[j+1].rstrip()) and not re.match(r'^\s*\+[-=+]+\+\s*$', block[j+1].rstrip())):
                                        break
                                j += 1
                            else:
                                break
                        if len(box_lines) >= 3:
                            boxes_in_file.append((box_start_idx, box_lines))
                        i = j
                    i += 1
        else:
            if in_code:
                block.append(line)
                
    return boxes_in_file

for f in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    boxes = analyze_file(f)
    print(f"\n==========================================")
    print(f"FILE: {f} ({len(boxes)} boxes found)")
    print(f"==========================================")
    for b_idx, (start_line, b_lines) in enumerate(boxes):
        top_w = display_width(b_lines[0])
        bottom_w = display_width(b_lines[-1])
        all_widths = [display_width(l) for l in b_lines]
        min_w = min(all_widths)
        max_w = max(all_widths)
        title = ""
        for bl in b_lines:
            if '|' in bl and not re.match(r'^\s*\|?\s*$', bl):
                clean_title = bl.replace('|', '').strip()
                if len(clean_title) > 5:
                    title = clean_title[:50]
                    break
        
        status = "PERFECT" if min_w == max_w else f"MISALIGNED (range: {min_w} to {max_w}, top: {top_w})"
        print(f"  Box {b_idx+1} [Line {start_line}]: {status} | Title: {title}")
        if min_w != max_w:
            for l_i, bl in enumerate(b_lines):
                dw = display_width(bl)
                if dw != top_w:
                    print(f"     Line {start_line+l_i} (w={dw:3d} vs {top_w:3d}): {bl}")
