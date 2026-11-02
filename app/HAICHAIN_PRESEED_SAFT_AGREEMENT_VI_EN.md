# HAICHAIN PRE-SEED SAFT AGREEMENT
## THỎA THUẬN CHUYỂN NHƯỢNG TOKEN TƯƠNG LAI - VÒNG NỘI BỘ PRE-SEED
### (SIMPLE AGREEMENT FOR FUTURE TOKENS - PRIVATE PRE-SEED ROUND)

* **Mã hiệu hợp đồng:** `HAICHAIN-SAFT-PRESEED-2026`
* **Cơ quan bảo chứng kỹ thuật:** Hội đồng Kiến trúc Hệ thống Phân tán HAICHAIN
* **Phiên bản:** v1.0.0 Institutional Legal Standard (Song ngữ / Bilingual: Tiếng Việt & English)
* **Tài sản cơ sở:** Token Quản trị & Tiện ích Mạng lưới `$HAISI` (Solana SPL Token)
* **Tổng cung cố định:** 1.000.000.000 $HAISI (Một Tỷ Token)
* **Mức giá phát hành vòng này:** **\$0.007 USD / $HAISI** (Định giá FDV: **\$7.000.000 USD**)
* **Mức giá niêm yết công khai dự kiến (TGE):** **\$0.010 USD / $HAISI** (Định giá FDV: **\$10.000.000 USD**)
* **Tỷ lệ chiết khấu ưu đãi:** **30%** (Tỷ suất lợi nhuận ban đầu: **+42.8%**)

---

# PHẦN 1: BẢN HỢP ĐỒNG TIẾNG VIỆT (VIETNAMESE EDITION)

Hợp Đồng Chuyển Nhượng Token Tương Lai này ("**Thỏa Thuận**" hoặc "**SAFT**") được lập và có hiệu lực kể từ ngày ký ("**Ngày Hiệu Lực**"), giữa các bên sau đây:

1. **BÊN PHÁT HÀNH ("Dự án" hoặc "HAICHAIN"):**
   * Dự án: **HAICHAIN Protocol** (Hệ điều hành tài chính và thanh toán vi mô cho Tác tử AI)
   * Hạ tầng: Blockchain Solana L1 (Anchor v6.9.3 Standard)
   * Đại diện bởi: Đội ngũ Sáng lập & Hội đồng Kỹ sư Cốt lõi HAICHAIN.

2. **BÊN MUA ("Nhà Đầu Tư" hoặc "Early Backer"):**
   * Họ và tên / Tổ chức: `________________________________________________`
   * Số CCCD / Hộ chiếu: `________________________________________________`
   * Địa chỉ Email: `________________________________________________`
   * Địa chỉ Ví Solana (Nhận Token): `________________________________________________`

Hai Bên cùng thống nhất ký kết bản thỏa thuận với các điều khoản bất biến sau:

---

### ĐIỀU 1: ĐỐI TƯỢNG VÀ THÔNG SỐ GIAO DỊCH

1. **Số Tiền Đóng Góp (Purchase Amount):**
   * Bên Mua đồng ý thanh toán số tiền: `_____________` **USD** (bằng USDT Tether SPL/ERC-20/TRC-20 hoặc SOL theo tỷ giá quy đổi tại thời điểm chuyển tiền).
2. **Số Lượng Token Phân Bổ (Allocated Tokens):**
   $$\text{Số Lượng Token ($HAISI)} = \frac{\text{Số Tiền Đóng Góp (USD)}}{\$0.007 \text{ USD}}$$
   * Tổng số token Bên Mua được quyền nhận: `_____________` **$HAISI**.
3. **Giới Hạn Hạn Mức Toàn Vòng:**
   * Vòng bán nội bộ Pre-Seed bị khóa trần cứng ở mức **25.000.000 đến 30.000.000 $HAISI (tối đa 3.0% tổng cung)**, tương đương tổng vốn huy động tối đa \$210.000 USD.

---

### ĐIỀU 2: LỊCH MỞ KHÓA ON-CHAIN VESTING (3 BẤT BIẾN KỸ THUẬT)

Để bảo vệ cấu trúc giá thị trường cho ngày mở bán công khai \$0.010, Bên Mua cam kết tuân thủ lịch mở khóa on-chain được mã hóa bằng Smart Contract (Streamflow hoặc Solana SPL Token Vesting):

1. **Mở khóa tại ngày TGE (Initial TGE Unlock):**
   * Giải ngân chính xác **20%** số lượng token về ví nhận của Bên Mua ngay tại thời điểm niêm yết công khai trên sàn DEX (Meteora DLMM / Raydium).
2. **Khóa Đóng Băng Hoàn Toàn (Cliff Period):**
   * Khóa cứng **0% mở khóa trong vòng 2 tháng** tiếp theo (tương đương 60 ngày kể từ ngày TGE).
3. **Mở Khóa Tuyến Tính On-Chain (Linear Streaming):**
   * **80% số token còn lại** được mở khóa tự động theo từng block/giây trải đều trong **6 tháng** tiếp theo (tương đương 180 ngày). Bên Mua có thể tự kết nối ví và rút token đã mở khóa bất kỳ lúc nào mà không phụ thuộc vào con người.

```
       BIỂU ĐỒ LỊCH MỞ KHÓA TOKEN VÒNG PRE-SEED ($0.007)
       
  100% ┌───────────────────────────────────────────────────► [Tháng 8: Mở khóa 100%]
       │                                            /
       │                                           /  (Mở khóa tuyến tính từng giây
       │                                          /    trong 6 tháng tiếp theo)
   20% ├───┐                                     /
       │   │                                    /
       │   │   [Cliff 2 Tháng: Đóng băng]     /
    0% └───┴─────────────────────────────────┴─────────────► Thời gian
         TGE (Ngày 0)                     Tháng 2          Tháng 8
```

---

### ĐIỀU 3: BẢN CHẤT TÀI SẢN & CAM KẾT PHÁP LÝ

1. **Phân loại Tài sản (Utility Commodity):**
   * Token `$HAISI` được định nghĩa là **Tài nguyên Tiện ích & Quản trị Mạng lưới (Network Utility & Governance Commodity)**.
   * `$HAISI` được dùng để: Giảm 50% phí giao dịch vi mô cho AI, stake quản trị veHAI nhận ưu đãi giảm phí và bảo hiểm rủi ro relayer, vote thông số giao thức (100% không chia cổ tức thụ động), và làm phí Gas cho mạng lưới Sovereign L1 trong tương lai.
2. **Không Cam Kết Lợi Nhuận Tài Chính (No Investment Advice):**
   * Thỏa thuận này không cấu thành một hợp đồng góp vốn cổ phần, trái phiếu hay chứng khoán có bảo đảm lợi nhuận. Bên Mua hiểu rõ rủi ro của thị trường công nghệ cao và tự chịu trách nhiệm về quyết định của mình.
3. **Cam Kết Không Bán Tháo Phá Giá (Anti-Flipping & Non-Circumvention):**
   * Bên Mua cam kết không thực hiện các hành vi bán khống (shorting), thỏa thuận ngầm OTC dưới mức giá niêm yết \$0.010, hoặc cung cấp thanh khoản cho các pool phi chính thức gây ảnh hưởng xấu đến biểu đồ giá của dự án.

---

### ĐIỀU 4: CAM KẾT BẢO MẬT THÔNG TIN (NON-DISCLOSURE AGREEMENT)

* Bên Mua cam kết giữ bí mật tuyệt đối về mức giá ưu đãi nội bộ **\$0.007 USD** và các tài liệu kỹ thuật nội bộ đính kèm cho đến khi dự án chính thức công bố công khai đợt mở bán \$0.010 ra toàn cầu. Mọi hành vi làm lộ thông tin gây tổn hại đến chiến dịch TGE sẽ bị hủy bỏ tư cách nhận token còn lại trong hợp đồng.

---

### CHỮ KÝ VÀ XÁC NHẬN CỦA CÁC BÊN

| ĐẠI DIỆN DỰ ÁN HAICHAIN | BÊN MUA (NHÀ ĐẦU TƯ PRE-SEED) |
| :--- | :--- |
| **Ký và ghi rõ họ tên:**<br><br><br>____________________________________ | **Ký và ghi rõ họ tên:**<br><br><br>____________________________________ |
| **Ngày ký:** ____ / ____ / 2026 | **Ngày ký:** ____ / ____ / 2026 |
| **Địa chỉ ví Multi-Sig nhận vốn:**<br>`HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **Địa chỉ ví Solana nhận Token:**<br>`________________________________________________` |

---
---

# PART 2: ENGLISH EDITION

## SIMPLE AGREEMENT FOR FUTURE TOKENS (SAFT)
### PRIVATE PRE-SEED ROUND - HAICHAIN PROTOCOL

THIS SIMPLE AGREEMENT FOR FUTURE TOKENS (this "**Agreement**" or "**SAFT**") certifies that in exchange for the payment by the undersigned purchaser (the "**Purchaser**") of the purchase amount set forth below (the "**Purchase Amount**"), **HAICHAIN Decentralized Systems Architecture Taskforce** (the "**Company**" or "**HAICHAIN**") hereby issues to the Purchaser the right to certain allocations of **$HAISI Tokens** (the "**Tokens**"), subject to the terms and conditions herein.

---

### 1. TRANSACTION PARAMETERS & PRICING
1. **Token Standard:** Solana SPL Token (Anchor v6.9.3 Military-Grade Kernel).
2. **Fixed Total Supply:** Exactly **1,000,000,000 $HAISI**.
3. **Offering Price per Token:** **\$0.007 USD / $HAISI** (Implying a **\$7,000,000 USD** Fully Diluted Valuation).
4. **Target Public Listing Price (TGE):** **\$0.010 USD / $HAISI** (Implying a **\$10,000,000 USD** Fully Diluted Valuation).
5. **Purchaser Price Preference:** **30% Discount** relative to Public TGE (+42.8% immediate unvested listing upside).
6. **Aggregate Round Cap:** Hard-capped at **25,000,000 to 30,000,000 $HAISI (Max 3.0% of Total Supply)**, totaling \$210,000 USD.

---

### 2. ON-CHAIN VESTING & DISTRIBUTION MECHANISM
To ensure market integrity and prevent secondary liquidity dilution, 100% of Tokens issued under this SAFT are routed into an autonomous Solana Program Derived Address (PDA) vesting escrow (via **Streamflow** or **SPL Token Vesting**):

1. **Initial TGE Unlock:** Exactly **20.0%** of total purchased Tokens become claimable at the Token Generation Event (TGE).
2. **Cliff Freeze Barrier:** A mandatory **2-Month Cliff** (60 calendar days) strictly freezes all token distributions post-TGE.
3. **Continuous Linear Stream:** The remaining **80.0%** unlocks continuously on a per-slot basis across the subsequent **6 Months** (180 calendar days).
4. **Self-Sovereign Claiming:** Purchaser can independently invoke the on-chain claim instruction directly from their registered non-custodial Solana wallet without intermediary counterparty reliance.

---

### 3. ASSET CLASSIFICATION & REGULATORY REPRESENTATIONS
1. **Network Utility Commodity:** The $HAISI Token is structured as a functional programmatic utility commodity utilized for protocol fee abatements (50% reduction on machine micro-payments), veHAI governance staking, relayer insurance bonding, programmatic Buyback & Burn, and sovereign L1 gas consensus. Zero passive cash dividends are distributed.
2. **No Equity or Security Classification:** This Agreement does not grant Purchaser equity shares, dividends, or voting shares in any corporate entity. Acquisition is based on the utility demand of the protocol.
3. **Anti-Sybil & Anti-Dumping Covenant:** Purchaser covenants not to execute off-market OTC synthetic hedging or dumping operations designed to manipulate open market discovery during the Public Launch phase.

---

### 4. CONFIDENTIALITY & NON-DISCLOSURE
Purchaser agrees to maintain strict confidentiality regarding the preferential \$0.007 valuation terms until the Company officially broadcasts the Public Community Sale terms to worldwide institutional and retail audiences.

---

### EXECUTION BLOCK

* **Purchaser Full Name / Entity:** `________________________________________________`
* **Passport / National ID No:** `________________________________________________`
* **Contact Email:** `________________________________________________`
* **Purchase Amount (USD equivalent):** `$________________________`
* **Allocated $HAISI Tokens:** `________________________ $HAISI`
* **Purchaser Solana Receiving Wallet (Ed25519 Pubkey):**  
  `____________________________________________________________________`

**FOR THE COMPANY (HAICHAIN):**  
Signature: `____________________________________`  
Date: `____ / ____ / 2026`  

**FOR THE PURCHASER:**  
Signature: `____________________________________`  
Date: `____ / ____ / 2026`  
