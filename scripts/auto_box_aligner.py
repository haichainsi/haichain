import unicodedata, re, sys, os, glob

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

def align_single_box(box_lines, target_w):
    out = []
    for l in box_lines:
        s = l.rstrip('\r\n')
        if re.match(r'^\s*\+[-=+]+\+\s*$', s):
            m_indent = re.match(r'^(\s*)\+', s)
            ind = m_indent.group(1) if m_indent else ''
            dashes = target_w - display_width(ind) - 2
            char = '-' if '-' in s else '='
            out.append(f"{ind}+{char * dashes}+")
        else:
            m = re.match(r'^(\s*\|)(.*?)(\s*\|\s*)$', s)
            if m:
                pref = m.group(1)
                inner = m.group(2).rstrip()
                cur_dw = display_width(pref) + display_width(inner) + 1
                needed = target_w - cur_dw
                if needed >= 0:
                    out.append(f"{pref}{inner}{' ' * needed}|")
                else:
                    # If it slightly exceeds (by 1-3 chars), see if there are internal multiple spaces to compress
                    # E.g. compress 2+ consecutive spaces in inner
                    excess = -needed
                    compressed_inner = re.sub(r' {2,}', lambda match: ' ' * max(1, len(match.group(0)) - excess), inner, count=excess)
                    cur_dw = display_width(pref) + display_width(compressed_inner) + 1
                    needed = target_w - cur_dw
                    if needed >= 0:
                        out.append(f"{pref}{compressed_inner}{' ' * needed}|")
                    else:
                        out.append(s)
            else:
                out.append(s)
    return out

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    in_code = False
    new_lines = []
    current_block = []
    
    for idx, line in enumerate(lines):
        if line.startswith('```'):
            if not in_code:
                in_code = True
                new_lines.append(line)
                current_block = []
            else:
                in_code = False
                # Process current_block for any ASCII boxes
                # Identify contiguous box chunks
                i = 0
                processed_block = []
                while i < len(current_block):
                    l_str = current_block[i].rstrip('\r\n')
                    if re.match(r'^\s*\+[-=+]+\+\s*$', l_str):
                        # Start of a box
                        box_lines = [l_str]
                        j = i + 1
                        while j < len(current_block):
                            lj = current_block[j].rstrip('\r\n')
                            if re.match(r'^\s*\|.*\|\s*$', lj) or re.match(r'^\s*\+[-=+]+\+\s*$', lj):
                                box_lines.append(lj)
                                if re.match(r'^\s*\+[-=+]+\+\s*$', lj) and j > i + 1:
                                    if j + 1 >= len(current_block) or (not re.match(r'^\s*\|.*\|\s*$', current_block[j+1].rstrip()) and not re.match(r'^\s*\+[-=+]+\+\s*$', current_block[j+1].rstrip())):
                                        break
                                j += 1
                            else:
                                break
                        if len(box_lines) >= 3:
                            # Decide target width: max of top width or standard width
                            top_w = display_width(box_lines[0])
                            # If top_w < 102 and any line is > 95, target is 102
                            all_w = [display_width(x) for x in box_lines]
                            if max(all_w) > 95 and top_w < 95:
                                target_w = 102
                            else:
                                target_w = top_w
                                
                            aligned = align_single_box(box_lines, target_w)
                            processed_block.extend([x + '\n' for x in aligned])
                        else:
                            processed_block.extend([x + '\n' for x in box_lines])
                        i = j
                    else:
                        processed_block.append(current_block[i])
                    i += 1
                new_lines.extend(processed_block)
                new_lines.append(line)
        else:
            if in_code:
                current_block.append(line)
            else:
                new_lines.append(line)
                
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Processed and aligned boxes in {filepath}")

if __name__ == '__main__':
    for f in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
        process_file(f)
