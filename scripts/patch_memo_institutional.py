import shutil

def patch_memo_vi_en():
    path = 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_sec3_vi = """### 3. TẠI SAO TOKEN $HAISI CÓ GIÁ TRỊ TĂNG TRƯỞNG BỀN VỮNG?
* **Mô hình Dòng tiền Thật (Real Yield in USDT):** 40% toàn bộ doanh thu phí giao dịch vi mô của hàng triệu tác tử AI trên toàn cầu được **chia trực tiếp bằng USDT thật** cho những người khóa token `$HAISI` (`veHAI`). 60% doanh thu còn lại dùng để **Mua lại và Đốt bỏ $HAISI (Buyback & Burn)** vĩnh viễn trên sàn DEX.
* **Lộ trình trở thành Blockchain L1 độc lập ($5B – $10B FDV):** Token SPL `$HAISI` sẽ chuyển đổi 1:1 trở thành Native Gas Coin của mạng lưới **HAICHAIN Sovereign L1** trong giai đoạn 3, mở ra cơ hội tăng trưởng vốn hóa hàng trăm lần cho các nhà đầu tư vòng đầu."""

    new_sec3_vi = """### 3. TẠI SAO TOKEN $HAISI CÓ GIÁ TRỊ TĂNG TRƯỞNG BỀN VỮNG?
* **Cỗ Máy Dòng Tiền 3 Tầng (Tiered Institutional Revenue Engine):** Doanh thu giao thức được bảo chứng vững chắc từ 3 nguồn độc lập:
  1. **Phí Vi Mô Giao Thức (0,10%):** Dành cho hàng triệu lượt gọi vi mô HTTP x402 giữa các tác tử AI.
  2. **Phí Quản Trị Swarm Doanh Nghiệp (2,50%):** Cung cấp API Gateway, phân bổ hạn mức ngân sách và kiểm toán chi tiêu cho các AI Studio & Enterprise Swarm ($10k–$100k/tháng).
  3. **Lợi Tức Kho Bạc Ký Quỹ (Escrow Float Yield 4,25% APY):** Lợi tức sinh lời từ dòng tiền stablecoin nhàn rỗi (Circle USDC/EURC chuẩn MiCA) bảo chứng bằng T-Bills thanh khoản cao.
* **Cơ Chế Tích Lũy Giá Trị Token $HAISI:** Doanh thu thặng dư được phân bổ: **50% Mua lại & Đốt bỏ (Deflationary Buyback & Burn)** trên thị trường giao ngay, và **50% Phần Thưởng Khóa An Ninh (Security Staking Rewards)** cho các Validator vận hành nút bù trừ vi mô. Người nắm giữ $HAISI còn được **giảm 50% phí dịch vụ B2B**.
* **Lộ Trình Hạ Tầng SVM Chuyên Biệt (Specialized SVM App-Chain):** Giai đoạn 1–2 hoạt động mượt mà trực tiếp trên Solana Mainnet; Giai đoạn 3 chuyển đổi mở rộng thành Subnet SVM chuyên dụng cho tài chính tác tử AI khi lưu lượng vượt 50.000 tx/giây."""

    content = content.replace(old_sec3_vi, new_sec3_vi)

    old_sec3_en = """### 3. TOKEN VALUATION TRAJECTORY & REAL YIELD CASH FLOW
* **100% Real Yield in USDT:** 40% of all micro-transaction fees generated across the global autonomous agent network are distributed directly in liquid USDT to locked `$HAISI` (`veHAI`) holders. 60% of all revenue is programmatically channeled into **open-market Buyback & Burn**.
* **Transition to Sovereign Machine L1 ($5B – $10B FDV):** In Phase 3, the SPL `$HAISI` token converts 1:1 into the Native Gas Coin of the **HAICHAIN Sovereign L1**, offering institutional early backers an asymmetric return trajectory."""

    new_sec3_en = """### 3. TOKEN VALUATION TRAJECTORY & HARDENED CASH-FLOW ENGINE
* **Three-Pillar Institutional Revenue Engine:** Protocol cash flows are anchored across three diversified tiers:
  1. **0.10% Micro-Escrow Tick Fee:** High-velocity settlement across autonomous HTTP x402 agent queries.
  2. **2.50% Enterprise Swarm Gateway Fee:** Cryptographic spending governance and audit trails for enterprise AI clusters ($10k–$100k/mo budgets).
  3. **4.25% Escrow Float Yield:** Real-world asset yields generated from idle pre-funded escrow deposits (Circle USDC/EURC compliant under EU MiCA).
* **Deflationary Value Capture:** Protocol operational surplus executes **50% Programmatic Buyback & Burn** and **50% Escrow Security Staking Rewards** for dispute-arbitrating validation nodes. Staking $HAISI grants enterprises a 50% discount on gateway fees.
* **Specialized SVM Application Architecture:** Phase 1–2 anchored natively on Solana Mainnet throughput; Phase 3 transitions to an Application-Specific SVM Subnet as transaction velocity exceeds 50,000 queries/second."""

    content = content.replace(old_sec3_en, new_sec3_en)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md")
    shutil.copyfile(path, 'app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md')
    print("Synced to app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md")

def patch_memo_en():
    path = 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_sec3 = """### 3. TOKEN VALUATION TRAJECTORY & REAL YIELD CASH FLOW
* **100% Real Yield in USDT:** 40% of all micro-transaction fees generated across the global autonomous agent network are distributed directly in liquid USDT to locked `$HAISI` (`veHAI`) holders. 60% of all revenue is programmatically channeled into **open-market Buyback & Burn**.
* **Transition to Sovereign Machine L1 ($5B – $10B FDV):** In Phase 3, the SPL `$HAISI` token converts 1:1 into the Native Gas Coin of the **HAICHAIN Sovereign L1**, offering institutional early backers an asymmetric return trajectory."""

    new_sec3 = """### 3. TOKEN VALUATION TRAJECTORY & HARDENED CASH-FLOW ENGINE
* **Three-Pillar Institutional Revenue Engine:** Protocol cash flows are anchored across three diversified tiers:
  1. **0.10% Micro-Escrow Tick Fee:** High-velocity settlement across autonomous HTTP x402 agent queries.
  2. **2.50% Enterprise Swarm Gateway Fee:** Cryptographic spending governance and audit trails for enterprise AI clusters ($10k–$100k/mo budgets).
  3. **4.25% Escrow Float Yield:** Real-world asset yields generated from idle pre-funded escrow deposits (Circle USDC/EURC compliant under EU MiCA).
* **Deflationary Value Capture:** Protocol operational surplus executes **50% Programmatic Buyback & Burn** and **50% Escrow Security Staking Rewards** for dispute-arbitrating validation nodes. Staking $HAISI grants enterprises a 50% discount on gateway fees.
* **Specialized SVM Application Architecture:** Phase 1–2 anchored natively on Solana Mainnet throughput; Phase 3 transitions to an Application-Specific SVM Subnet as transaction velocity exceeds 50,000 queries/second."""

    content = content.replace(old_sec3, new_sec3)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md")
    shutil.copyfile(path, 'app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md')
    print("Synced to app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.md")

patch_memo_vi_en()
patch_memo_en()
