# HAICHAIN: CHIẾN LƯỢC MỞ BÁN TOKEN & KẾ HOẠCH ĐỊNH GIÁ HAI GIAI ĐOẠN
### (HAICHAIN TWO-PHASE TOKEN SALE & DUAL-PRICING STRATEGIC DEPLOYMENT PLAN)

* **Hội đồng Thẩm định:** Kỹ sư Cốt lõi Solana (Systems & Liquidity) $\times$ Kỹ sư An toàn & Căn chỉnh AI Anthropic
* **Phiên bản:** v1.0.0 Strategic Masterplan
* **Ngôn ngữ:** Song ngữ Hoàn chỉnh (Tiếng Việt & English Edition)
* **Tổng cung cố định:** 1.000.000.000 $HAI (Một Tỷ Token)
* **Quyết định Chiến lược:** **Vòng Bán Nội Bộ $0.007 (Pre-Seed) $\longrightarrow$ Mở Bán Công Khai $0.010 (Public TGE)**

---

# PHẦN 1: BẢN KẾ HOẠCH TIẾNG VIỆT (VIETNAMESE EDITION)

## 1. TỔNG QUAN CHIẾN LƯỢC ĐỊNH GIÁ HAI GIAI ĐOẠN

Nhằm đảm bảo dự án có đủ dòng tiền phát triển kỹ thuật ngay trong giai đoạn xây dựng (Development Phase), đồng thời tạo ra một bệ phóng thanh khoản công bằng, bùng nổ và miễn nhiễm với nạn xả hàng bot khi bước ra thị trường công khai, HAICHAIN áp dụng chiến lược mở bán phân tầng:

* **GIAI ĐOẠN 1: BÁN NỘI BỘ (EARLY PRE-SEED):**
  * **Mức giá:** **\$0.007 USD / $HAI**
  * **Định giá toàn bộ (FDV):** **\$7.000.000 USD**
  * **Mục tiêu:** Huy động nguồn vốn đầu tiên tài trợ kiểm toán bảo mật, hạ tầng máy chủ GPU và chi phí vận hành cốt lõi.
* **GIAI ĐOẠN 2: MỞ BÁN CÔNG KHAI (PUBLIC COMMUNITY TGE):**
  * **Mức giá:** **\$0.010 USD / $HAI (Tròn 1 Cent)**
  * **Định giá toàn bộ (FDV):** **\$10.000.000 USD**
  * **Mục tiêu:** Thiết lập thanh khoản sâu vĩnh viễn trên Meteora DLMM, thu hút người dùng toàn cầu và các lập trình viên AI.

$$\text{Tỷ lệ chiết khấu ưu đãi nội bộ:} \quad \frac{\$0.010 - \$0.007}{\$0.010} = \mathbf{30\%} \quad (\text{Lợi nhuận tiềm năng: } +42.8\%)$$

---

## 2. BẢNG SO SÁNH ĐỊNH LƯỢNG GIỮA HAI VÒNG

```
+----------------------------------------------------------------------------------------------------+
|                         BẢNG ĐỐI CHIẾU CHIẾN LƯỢC HAI VÒNG MỞ BÁN $HAI                             |
+----------------------------------------------------------------------------------------------------+
| TIÊU CHÍ                     VÒNG BÁN NỘI BỘ (PRE-SEED)            VÒNG MỞ BÁN CÔNG KHAI (TGE)     |
+----------------------------------------------------------------------------------------------------+
| Thời điểm thực hiện          Giai đoạn đang phát triển (Hiện tại)  Khi hoàn tất kiểm toán & Mainnet|
| Mức giá mỗi token            $0.007 USD                            $0.010 USD (1 Cent)             |
| Định giá toàn bộ (FDV)       $7.000.000 USD                        $10.000.000 USD                 |
| Số lượng token phân bổ       20.000.000 - 30.000.000 $HAI (2% - 3%) 100.000.000 $HAI (10%)         |
| Số tiền huy động mục tiêu    $140.000 - $210.000 USD               $1.000.000 USD                  |
| Phương thức triển khai       Hợp đồng SAFT + Khóa on-chain         Meteora Alpha Vault + DLMM Pool |
| Điều kiện mở khóa (Vesting)  Mở 20% tại TGE, Khóa Cliff 2 tháng,   Mở khóa tuyến tính trong 7 ngày |
|                              Trả dần tuyến tính 6 tháng            (Chống bot sniping)             |
| Phân bổ số tiền thu được     100% tài trợ Dev, Audit, Server       50% tạo Pool thanh khoản Locked |
|                                                                    50% Kho bạc dự trữ L1           |
| Đối tượng tham gia           Bạn bè, Kỹ sư cốt lõi, Co-builders    Cộng đồng toàn cầu & Devs AI    |
+----------------------------------------------------------------------------------------------------+
```

---

## 3. BA NGUYÊN TẮC BẢO VỆ SỐNG CÒN (BẮT BUỘC THỰC THI)

Để mức giá \$0.007 nội bộ không trở thành mối nguy hại bán tháo đè bẹp mức giá \$0.010 công khai, dự án thiết lập **3 bất biến kỹ thuật và pháp lý**:

### NGUYÊN TẮC 1: KHÓA TOKEN ON-CHAIN BẮT BUỘC (ON-CHAIN VESTING CONTRACT)
* **Rủi ro:** Nếu người mua nội bộ nhận 100% token lỏng tại TGE, họ có thể xả ngay để chốt lời 43%, gây sụp đổ biểu đồ giá công khai.
* **Quy chuẩn thực thi:**
  * Toàn bộ token nội bộ được khóa trên Solana thông qua hợp đồng thông minh **Streamflow** hoặc **SPL Token Vesting**.
  * **Tại ngày TGE (\$0.010):** Chỉ mở khóa tối đa **20%** số token.
  * **Khóa Cliff (Đóng băng tuyệt đối):** Khóa cứng trong **2 tháng** tiếp theo (Slot $N$ đến Slot $N + 12.960.000$).
  * **Trả dần (Linear Streaming):** Mở khóa đều đặn từng block trong **6 tháng** tiếp theo.
  * *Ý nghĩa:* Người mua nội bộ được hưởng giá rẻ hơn 30% để đổi lại cam kết đồng hành dài hạn, bảo vệ an toàn 100% cho người mua công khai.

### NGUYÊN TẮC 2: GIỚI HẠN TRẦN HẠN MỨC NỘI BỘ (HARD ALLOCATION CAP)
* **Quy chuẩn thực thi:**
  * Hạn mức tối đa cho toàn bộ vòng bán nội bộ bị khóa cứng ở mức: **30.000.000 $HAI (Tối đa 3.0% tổng cung)**.
  * Hạn mức mua tối đa cho mỗi cá nhân: **\$5.000 &ndash; \$15.000 USD** (trừ trường hợp nhà đầu tư thiên thần chiến lược ký cam kết đồng hành đặc biệt).
  * *Ý nghĩa:* Tuyệt đối không để bất kỳ cá nhân nội bộ nào nắm giữ lượng token đủ lớn để có thể thao túng thị trường.

### NGUYÊN TẮC 3: PHÁP LÝ CHUẨN MỰC BẰNG HỢP ĐỒNG SAFT & CAM KẾT BẢO MẬT (SAFT & NDA)
* **Quy chuẩn thực thi:**
  * Toàn bộ các giao dịch mua nội bộ trước TGE đều được văn bản hóa thông qua hợp đồng **SAFT (Simple Agreement for Future Tokens)** chuẩn quốc tế.
  * Ràng buộc điều khoản không tiết lộ giá (**Non-Disclosure Agreement - NDA**) nhằm bảo vệ tâm lý thị trường cho đợt mở bán công khai \$0.010.
  * Ghi rõ điều khoản: Token giao dịch là Utility Token phục vụ chiết khấu và vận hành trong hệ sinh thái HaiChain, không phải cổ phần đầu tư tài chính sinh lời cam kết.

---

# PART 2: ENGLISH EDITION

## 1. TWO-PHASE DUAL-PRICING TOKEN SALE OVERVIEW

To ensure adequate capital runway during the core engineering development phase while establishing a liquid, fair, and anti-dumping launchpad for the public markets, HAICHAIN formalizes a two-tiered token distribution strategy:

* **PHASE 1: PRIVATE PRE-SEED (INTERNAL DEVELOPMENT ROUND):**
  * **Token Price:** **\$0.007 USD / $HAI**
  * **Fully Diluted Valuation (FDV):** **\$7,000,000 USD**
  * **Core Mandate:** Bootstrap initial smart contract security audits, GPU infrastructure staking, and foundational operations.
* **PHASE 2: PUBLIC COMMUNITY SALE (TGE LAUNCHPAD):**
  * **Token Price:** **\$0.010 USD / $HAI (Flat 1 Cent)**
  * **Fully Diluted Valuation (FDV):** **\$10,000,000 USD**
  * **Core Mandate:** Establish permanent protocol-owned liquidity on Meteora DLMM and onboard global AI builders.

$$\text{Internal Preference Discount:} \quad \frac{\$0.010 - \$0.007}{\$0.010} = \mathbf{30\%} \quad (\text{Target Listing Yield: } +42.8\%)$$

---

## 2. QUANTITATIVE ALLOCATION COMPARISON MATRIX

```
+----------------------------------------------------------------------------------------------------+
|                         HAICHAIN DUAL-PHASE TOKEN SALE COMPARISON                                  |
+----------------------------------------------------------------------------------------------------+
| METRIC                       PHASE 1: PRIVATE PRE-SEED             PHASE 2: PUBLIC COMMUNITY (TGE)  |
+----------------------------------------------------------------------------------------------------+
| Execution Horizon            Active Development Phase (Current)    Post-Audit Mainnet Ignition      |
| Offering Price per Token     $0.007 USD                            $0.010 USD (1 Cent)              |
| Fully Diluted Valuation (FDV) $7,000,000 USD                       $10,000,000 USD                  |
| Token Allocation             20,000,000 - 30,000,000 $HAI (2% - 3%)100,000,000 $HAI (10%)          |
| Target Capital Raised        $140,000 - $210,000 USD               $1,000,000 USD                   |
| Distribution Mechanism       Legal SAFT + On-Chain Vesting Escrow  Meteora Alpha Vault + DLMM Pool  |
| Vesting Schedule             20% TGE Unlock, 2-Month Cliff,        7-Day Smooth Linear Vesting      |
|                              6-Month Continuous Linear Stream      (Anti-Bot Sniping Barrier)       |
| Capital Allocation           100% Dev, Security Audit, Cloud GPUs  50% Permanent Burned DEX LP      |
|                                                                    50% Sovereign L1 Treasury        |
| Target Participants          Core Engineers, Angel Builders        Global Community & AI Devs       |
+----------------------------------------------------------------------------------------------------+
```

---

## 3. THE THREE INDISPENSABLE SAFEGUARD INVARIANTS

To mathematically insulate the \$0.010 public launch against predatory arbitrage from early \$0.007 allocations, the protocol enforces three engineering and game-theoretic invariants:

### INVARIANT 1: ENFORCED ON-CHAIN VESTING CONTRACTS (ANTI-DUMP DEFENSE)
* **Vulnerability:** Unlocked internal allocations at \$0.007 incentivize instant 43% profit realization upon public DEX quotation, crashing the chart.
* **Enforcement:**
  * 100% of internal tokens are deposited into autonomous Solana vesting vaults via **Streamflow** or **SPL Token Vesting**.
  * **At TGE (\$0.010):** Exactly **20%** of tokens are claimable.
  * **Cliff Barrier:** An unyielding **2-month lockup window** freezes all claims.
  * **Linear Streaming:** Remaining tokens unlock on a per-second basis over the subsequent **6 months**.
  * *Verdict:* Early participants trade immediate liquidity for a 30% price discount, perfectly aligning incentives with the protocol's 3-year roadmap.

### INVARIANT 2: STRICT AGGREGATE ALLOCATION HARD-CAP
* **Enforcement:**
  * The internal round is strictly bounded to an absolute ceiling of **30,000,000 $HAI (3.0% of Total Supply)**.
  * Individual wallet caps are set between **\$5,000 and \$15,000 USD**, preventing the creation of malicious private syndicates capable of moving secondary market prices.

### INVARIANT 3: JURISDICTIONAL SAFT INSTRUMENTS & BINDING CONFIDENTIALITY
* **Enforcement:**
  * All internal pre-TGE subscriptions are executed under institutional **Simple Agreements for Future Tokens (SAFT)**.
  * Mandatory Non-Disclosure Agreements (NDA) legally prevent premature price signaling that could destabilize public market expectations.
  * Explicit legal classification of `$HAI` as a functional Network Utility Commodity utilized for protocol fee abatements and sovereign consensus, neutralizing US SEC Howey Test liability.

---
*Ratified by the HAICHAIN Systems Architecture Taskforce &bull; Strategic Capital Operations v1.0 &bull; 2026*
