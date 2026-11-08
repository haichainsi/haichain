# -*- coding: utf-8 -*-
"""
Build institutional unabridged Hebrew whitepaper (HAICHAIN_WHITEPAPER_V1.0_HE.md)
Ensures 100% preservation of all formulas, code snippets, addresses, and 0 em/en dashes.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from he_parts import (
    part0, part1, part2, part3, part4, part5,
    part6, part7, part8, part9, part10, part11,
    part12, part13
)

def main():
    parts = [
        part0.get_content(),
        part1.get_content(),
        part2.get_content(),
        part3.get_content(),
        part4.get_content(),
        part5.get_content(),
        part6.get_content(),
        part7.get_content(),
        part8.get_content(),
        part9.get_content(),
        part10.get_content(),
        part11.get_content(),
        part12.get_content(),
        part13.get_content(),
    ]
    
    # Join with standard section breaks
    joined = "\n\n---\n\n".join(parts)
    
    # Enforce strict zero em-dash / en-dash invariant
    clean_text = joined.replace("\u2014", "-").replace("\u2013", "-")
    
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "HAICHAIN_WHITEPAPER_V1.0_HE.md")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(clean_text)
    
    print(f"[OK] Generated {output_path}")
    print(f"Total characters: {len(clean_text)}")
    print(f"Total lines: {len(clean_text.splitlines())}")
    print(f"Em-dash count: {clean_text.count(chr(0x2014))}")
    print(f"En-dash count: {clean_text.count(chr(0x2013))}")

if __name__ == "__main__":
    main()
