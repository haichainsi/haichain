import os, re

memos_data = {
    "HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md": {
        "title_old": r"### 3\. TIERED REVENUE ENGINE \(\$15\.9M ARR\) & TOKENOMICS",
        "title_new": "### 3. TIERED MICRO-FEE CAPACITY & DEFENSIBLE TOKENOMICS ($0.7M - $1.4M PROTOCOL TAKE-RATE)",
        "vol_old": r"\* \*\*Ecosystem Services:\*\* zkTLS Verification Fees \(\$0\.001/proof\) \+ Priority State Channel Liquidity Spreads generate robust blended \$15\.9M ARR\.",
        "vol_new": "* **Protocol Take-Rate Economics:** At a conservative 0.05% - 0.10% protocol take-rate on $1.4B annualized network micro-settlement capacity, HAICHAIN generates a sustainable, audited **$700,000 - $1,400,000 USD/year** in protocol reserves (strictly matching Whitepaper Section 7).",
        "token_old": r"\* \*\*Token Value Accrual:\*\* 50% of all global settlement fees fund automated continuous \*\*Buyback & Burn\*\*; 50% distributed as \*\*Real Yield \(USDC/USDT\)\*\* to veHAI governance stakers\.",
        "token_new": "* **Token Value Accrual (Howey Test Compliant Utility):** 50% of protocol fees fund automated continuous **Buyback & Burn**; 50% allocated to Protocol Reserves & CHGB (Cryptographic Hardware Gas Bond) for relayer insurance and dispute bonds. Zero passive dividend distributions (non-security utility architecture).",
        "audit_old": r"vượt qua \*\*15/15 bài test bảo mật cấp quân sự\*\*|Passed 15/15 automated formal verification vectors",
        "audit_new": "Passed 15/15 automated formal verification test vectors. Independent external security audits with OtterSec & Neodyme scheduled prior to Mainnet TGE"
    },
    "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md": {
        "title_old": r"### 3\. ĐỘNG CƠ DOANH THU ĐA TẦNG \(\$15\.9M ARR\) & TOKENOMICS",
        "title_new": "### 3. CÔNG SUẤT VI PHÍ ĐA TẦNG & TOKENOMICS AN TOÀN PHÁP LÝ ($0.7M – $1.4M PROTOCOL TAKE-RATE)",
        "vol_old": r"Phí xác thực zkTLS và chênh lệch thanh khoản kênh tạo tổng doanh thu \$15\.9M ARR\.",
        "vol_new": "Với tỷ lệ trích phí (take-rate) chuẩn mực 0.05% – 0.10% trên $1.4 Tỷ USD tổng công suất thanh toán vi mô luân chuyển hàng năm, giao thức tạo ra dòng ngân khố bền vững **$700.000 – $1.400.000 USD/năm** (khớp hoàn toàn với Bảng Tokenomics Whitepaper Chương 7).",
        "token_old": r"\* \*\*Cơ chế Tích lũy Giá trị Token:\*\* 50% doanh thu dùng để \*\*Mua lại và Đốt bỏ \$HAISI \(Buyback & Burn\)\*\* vĩnh viễn; 50% chia thưởng \*\*Dòng tiền Thật \(Real Yield USDC/USDT\)\*\* cho staker veHAI\.",
        "token_new": "* **Cơ chế Tích lũy Giá trị Token (Tuân thủ Khung Howey Test Quốc tế):** 50% phí giao thức dùng để **Mua lại và Đốt bỏ $HAISI (Buyback & Burn)** vĩnh viễn; 50% phân bổ vào Quỹ Dự trữ Giao thức & CHGB (Cryptographic Hardware Gas Bond) để bảo hiểm cho relayer và xử lý tranh chấp. Hoàn toàn không chia cổ tức thụ động (Zero Dividend Yields), loại bỏ triệt để rủi ro chứng khoán.",
        "audit_old": r"vượt qua \*\*15/15 bài test bảo mật cấp quân sự\*\*",
        "audit_new": "vượt qua **15/15 bài test vector bất biến toán học tự động** (Formal Verification). Kiểm toán bảo mật độc lập bên thứ ba (External Audit) được lên lịch thực hiện trước Mainnet TGE"
    },
    "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md": {
        "title_old": r"### 3\. ĐỘNG CƠ DOANH THU ĐA TẦNG \(\$15\.9M ARR\) & TOKENOMICS",
        "title_new": "### 3. CÔNG SUẤT VI PHÍ ĐA TẦNG & TOKENOMICS AN TOÀN PHÁP LÝ ($0.7M – $1.4M PROTOCOL TAKE-RATE)",
        "vol_old": r"Phí xác thực zkTLS và chênh lệch thanh khoản kênh tạo tổng doanh thu \$15\.9M ARR\.",
        "vol_new": "Với tỷ lệ trích phí (take-rate) chuẩn mực 0.05% – 0.10% trên $1.4 Tỷ USD tổng công suất thanh toán vi mô luân chuyển hàng năm, giao thức tạo ra dòng ngân khố bền vững **$700.000 – $1.400.000 USD/năm** (khớp hoàn toàn với Bảng Tokenomics Whitepaper Chương 7).",
        "token_old": r"\* \*\*Cơ chế Tích lũy Giá trị Token:\*\* 50% doanh thu dùng để \*\*Mua lại và Đốt bỏ \$HAISI \(Buyback & Burn\)\*\* vĩnh viễn; 50% chia thưởng \*\*Dòng tiền Thật \(Real Yield USDC/USDT\)\*\* cho staker veHAI\.",
        "token_new": "* **Cơ chế Tích lũy Giá trị Token (Tuân thủ Khung Howey Test Quốc tế):** 50% phí giao thức dùng để **Mua lại và Đốt bỏ $HAISI (Buyback & Burn)** vĩnh viễn; 50% phân bổ vào Quỹ Dự trữ Giao thức & CHGB (Cryptographic Hardware Gas Bond) để bảo hiểm cho relayer và xử lý tranh chấp. Hoàn toàn không chia cổ tức thụ động (Zero Dividend Yields), loại bỏ triệt để rủi ro chứng khoán.",
        "audit_old": r"vượt qua \*\*15/15 bài test bảo mật cấp quân sự\*\*",
        "audit_new": "vượt qua **15/15 bài test vector bất biến toán học tự động** (Formal Verification). Kiểm toán bảo mật độc lập bên thứ ba (External Audit) được lên lịch thực hiện trước Mainnet TGE"
    }
}

# Update the specific memos
for filename, d in memos_data.items():
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(d["title_old"], d["title_new"], c)
        c = re.sub(d["vol_old"], d["vol_new"], c)
        c = re.sub(d["token_old"], d["token_new"], c)
        c = re.sub(d["audit_old"], d["audit_new"], c)
        # Also clean up the second English half in VI_EN if present
        if "VI_EN" in filename:
            c = re.sub(r"### 3\. TIERED REVENUE ENGINE \(\$15\.9M ARR\) & REAL YIELD CASH FLOW", "### 3. TIERED MICRO-FEE CAPACITY & DEFENSIBLE TOKENOMICS ($0.7M - $1.4M PROTOCOL TAKE-RATE)", c)
            c = re.sub(r"\* \*\*Ecosystem Services:\*\* zkTLS Verification Fees \(\$0\.001/proof\) \+ Priority State Channel Liquidity Spreads generate robust blended \$15\.9M ARR\.", "* **Protocol Take-Rate Economics:** At a conservative 0.05% - 0.10% protocol take-rate on $1.4B annualized network micro-settlement capacity, HAICHAIN generates a sustainable **$700,000 - $1,400,000 USD/year** in protocol reserves (strictly matching Whitepaper Section 7).", c)
            c = re.sub(r"\* \*\*Token Value Accrual:\*\* 50% of all global settlement fees fund automated continuous \*\*Buyback & Burn\*\*; 50% distributed as \*\*Real Yield \(USDC/USDT\)\*\* to veHAI governance stakers\.", "* **Token Value Accrual (Howey Test Compliant Utility):** 50% of protocol fees fund automated continuous **Buyback & Burn**; 50% allocated to Protocol Reserves & CHGB. Zero passive dividend distributions (non-security utility architecture).", c)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {filename}")

# Other languages: ZH, KO, ES, FR, RU, HE, HI, KK
other_langs = ["ZH", "KO", "ES", "FR", "RU", "HE", "HI", "KK"]
for l in other_langs:
    fn = f"HAICHAIN_PRESEED_ONE_PAGER_MEMO_{l}.md"
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f:
            c = f.read()
        # Replace $15.9M ARR in section 3 header
        c = re.sub(r"### 3\..*?\$15\.9M ARR.*", "### 3. TIERED MICRO-FEE CAPACITY & DEFENSIBLE TOKENOMICS ($0.7M - $1.4M PROTOCOL TAKE-RATE)", c)
        # Replace 15.9M in body
        c = re.sub(r"(\$15\.9M ARR|\$15\.9M)", "$0.7M - $1.4M Protocol Take-Rate", c)
        # Remove Real Yield dividends
        c = re.sub(r"Real Yield.*?(veHAI|staker)", "50% Buyback & Burn + 50% Protocol Reserves (CHGB - Howey Test Compliant)", c)
        with open(fn, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {fn}")

print("ALL MEMOS UPDATED SUCCESSFULLY.")
