import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# We will define the high-fidelity markdown tables for VI and EN first, and map them to all 10 languages!
# Table 1: Cross-Paradigm Infrastructure Comparison Matrix (Chapter 1 / 3)
# Table 2: Empirical Competitor Audit (Chapter 1 / 3.2)
# Table 3: Invisible Web3 Onboarding Topology (Chapter 3 / 4)
# Table 4: Six Invariants Exploit Defense Matrix (Chapter 6)
# Table 5: Strategic Engineering Roadmap Matrix (Chapter 11)

def patch_file(lang):
    filename = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
    if not os.path.exists(filename):
        return
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    original_len = len(text)
    
    # 1. Update Competitor Table in Chapter 1
    # Find code block with BẢNG SO SÁNH ĐỐI THỦ THỰC NGHIỆM or EMPIRICAL ARCHITECTURAL MATRIX
    comp_block_pattern = r'```[^\n]*\n\+[ -]+\+\n[^\n]*?(?:BẢNG SO SÁNH ĐỐI THỦ|EMPIRICAL ARCHITECTURAL MATRIX|EMPIRICAL COMPETITOR AUDIT|CROSS-PARADIGM|СРАВНИТЕЛЬН|对比|비교|COMPARATIV)[^\n]*?\n[\s\S]*?\n\+[ -]+\+\n```'
    
    # Check if this matches
    m = re.search(comp_block_pattern, text)
    if m:
        print(f"[{lang}] Found competitor ASCII table at {m.start()}..{m.end()} ({len(m.group(0))} chars)")
    else:
        print(f"[{lang}] Note: Competitor ASCII table pattern didn't match via generic regex; checking specific headers.")

print("Patch script ready to inspect all languages.")
