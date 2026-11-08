import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Table 1: Competitor Matrix for VI
VI_COMPETITOR_TABLE = """| Nền Tảng / Mô Hình | Điểm Mù Kiến Trúc Tử Huyệt | Giải Pháp Đột Phá Của HAICHAIN SI |
| :--- | :--- | :--- |
| **Coinbase AgentKit & ElizaOS (ai16z)** | Lộ Private Key EOA; Tấn công Prompt Injection làm cháy sạch ví chính; Không có giới hạn tốc độ on-chain; Thiếu nút dừng khẩn cấp phần cứng. | Dây cương Merkle Capability Leaf (4 thành phần); Hũ tiền PDA cô lập; 1-Chạm Panic Kill-Switch cưỡng bức đóng băng và rút tiền (< 400ms, trần lý thuyết $\\tau \\le 12\\text{s}$). |
| **Bittensor (TAO)** | Độ trễ khối 12 giây (12.000ms - bất khả thi cho vi thanh toán thời gian thực); Yuma Consensus bị thông đồng và gian lận sao chép mô hình; Thoái hóa dữ liệu tự hoại (MAD). | Khối 50ms BFT Netting; Dòng tiền thật USDT/USDC; Proof of Actual Intelligence (PoAI) nạp trực giác sống của con người, triệt hạ hoàn toàn suy thoái dữ liệu MAD. |
| **ASI Alliance (Fetch.ai / SingNet)** | Chi phí hợp đồng thông minh CPI đắt đỏ trên Cosmos/EVM; Độ trễ BFT nhiều giây; Thiếu mã máy vi thanh toán; Tác tử tách rời thể nhân con người. | Mã máy OP_402_PAY nhúng trực tiếp vào CPU máy ảo (> 100.000 TPS, 0 phí CPI); Định danh Soulbound DID neo vào Passkey FaceID sinh trắc học (EU AI Act). |
| **Virtuals Protocol (Base Layer 2)** | Nghẽn cổ chai ghi đơn luồng của EVM trên Base; Phí blob Ethereum L1 biến động ($0.01 - $0.50); Tập trung đầu cơ token meme thay vì hạ tầng tiện ích tài chính cho doanh nghiệp. | Xử lý song song Sealevel 32 luồng ATA; Bù trừ đối xứng nén 99.999% (gói tin 771B); Thanh toán tiện ích thực bằng USDT ổn định không chịu rủi ro biến động giá. |
| **Stripe / Tempo MPP & Web2 Rails** | Phí sàn cố định $0.30 + 2.9% (đắt gấp 150.000% giá trị lệnh gọi API $0.0002); Thời gian bù trừ 2-5 ngày; Rủi ro bồi hoàn chargeback (60-90 ngày); Thiếu hũ tiền kiểm chứng hình thức on-chain. | Vi tiện ích thực sự ($0.000001 nén / $0.001 gốc); Tốc độ chốt sổ mật mã dưới 400ms (trần bảo vệ lý thuyết $\\tau \\le 12\\text{s}$); Triệt tiêu 100% rủi ro bồi hoàn qua Escrow phân lập. |
| **Worldcoin (Tools for Humanity)** | Chỉ quét mống mắt (The Orb) để phát token UBI thụ động; Hoàn toàn không có runtime thực thi cho máy; Không quản trị hạn mức chi tiêu; Không biến con người thành bộ đồng xử lý nhận thức. | Đưa chuẩn sinh trắc học mở (Passkey/ZK-PoH) vào thẳng chu trình kinh tế (Reverse Micro-Tasking), biến trí tuệ con người thành bộ đồng xử lý nhận thức nhận thù lao vi mô cho Siêu AI. |
| **HTTP x402 & Pay.sh (Solana x Google Cloud)** | Chỉ là giao thức truyền thông HTTP/proxy thô; Giới hạn 1 delegate token Solana; Lỗ hổng thiếu trần chi tiêu client (V12 audit); Thiếu mạch ngắt tự hành on-chain và thiếu cơ chế phạt nhà mạng. | Lớp Quản trị Chính sách & Hũ PDA cô lập (bổ trợ hoàn hảo cho x402/Pay.sh); Cây năng lực Merkle đa tầng (Multi-delegate); Mạch ngắt tự hành < 400ms; Bounded Loss triệt tiêu hoàn toàn rủi ro cháy ví. |"""

# Table 2: SaaS vs Utility for VI
VI_SAAS_TABLE = """| Tiêu Chí Kinh Tế | Mô Hình Thuê Bao SaaS Cũ (Web2) | Giao Thức Tiện Ích HAICHAIN (v1.1) |
| :--- | :--- | :--- |
| **Triết Lý Tính Phí** | Trả tiền để truy cập (Cố định tháng dù không dùng) | Trả tiền theo lượt thực thi (Vi thanh toán phần cent) |
| **Dung Lượng Chưa Dùng** | Mất trắng 100% khi hết chu kỳ tháng (Chi phí chìm) | Bảo toàn 100% trong hũ PDA thuộc quyền sở hữu người dùng |
| **Đơn Vị Định Giá** | Đầu người giả định ($20 - $50 / tháng / nhân viên) | Thực tế tiêu thụ compute ($0.0002 / lệnh gọi API) |
| **Phương Thức Tương Tác** | Con người bấm chuột thủ công trên giao diện Web | Tác tử AI tự động gọi máy-đến-máy qua giao thức HTTP x402 |
| **Bảo Vệ Tài Chính** | Thẻ tín dụng doanh nghiệp lưu lộ thiên trên SaaS | Hũ tiền PDA phân lập có trần cứng Merkle CapLeaf ($5.00) |
| **Chi Phí Thực Tế Tháng** | $150.00 - $300.00 / nhân viên / tháng | $3.40 / tháng (Tiết kiệm thực 97.7% nhờ cơ chế BYOK) |"""

# Table 3: Invisible Web3 Onboarding for VI
VI_ONBOARDING_TABLE = """| Bước 1: Passkey Sinh Trắc Học | Bước 2: Nạp Tiền Đa Kênh Toàn Cầu | Bước 3: Hũ Tiền An Toàn (Safe Pot) |
| :--- | :--- | :--- |
| **Apple FaceID / TouchID / TPM 2.0**<br>WebAuthn Secure Enclave<br>• Không lưu trữ Seed Phrase<br>• Chống trộm khóa cấp chip phần cứng | **Apple Pay / Google Pay / Thẻ / VietQR**<br>Interactive Sandbox Demo (VASP In Progress)<br>• 0 thủ tục KYC sàn Crypto rườm rà<br>• Chuyển đổi 1:1 sang USDT bảo chứng | **Hũ PDA Phân Lập (Isolated $10.00)**<br>Trần chi tiêu cứng Bounded Loss<br>• Cầu chì tự động ngắt kết nối bất thường<br>• 1-Chạm Panic rút 100% tiền về ví lạnh |"""

# Table 4: 6 Invariants Defense Matrix for VI
VI_INVARIANTS_TABLE = """| Bất Biến / Lớp Phòng Thủ | Véc-tơ Tấn Công & Lỗ Hổng Lịch Sử | Cơ Chế Thực Thi Mật Mã Của HAICHAIN |
| :--- | :--- | :--- |
| **1. Kiểm Tra Chữ Ký Native (Sysvar)** | Giả mạo tài khoản sysvar ngữ cảnh (CVE-2022-24300) | Khóa cứng địa chỉ Sysvar Instructions: `Sysvar1nstructions1111111111111111111111111`. |
| **2. Gốc Merkle Khác Không & Chống PDA Trống** | Bỏ qua xác minh Merkle khi root chưa khởi tạo | Ép buộc bất biến: `require!(composite_root != [0u8; 32])` tại thời điểm gọi lệnh. |
| **3. Rào Chắn Tấn Công Prompt Injection** | Tác tử AI bị đầu độc prompt, chuyển tiền sang ví tặc | Cây năng lực Merkle 4 thành phần (`Pubkey \|\| MaxSpend \|\| Expiry \|\| Nonce`) giới hạn cứng số tiền. |
| **4. Kiểm Soát Số Dư ATA Thời Gian Thực** | Lệch sổ kế toán nội bộ và tấn công lạm phát donation | Tải lại số dư ATA nghiêm ngặt: `require!(actual_ata_balance >= spend_amount)`. |
| **5. Cách Ly Thanh Khoản Flash-Loan** | Vay nhanh, nạp tiền và rút cạn trong cùng một khối | Khóa thời gian đa slot: `require!(slot >= last_deposit_slot + 2)`. |
| **6. Phân Lập Tài Khoản Đóng Băng Tether** | Đóng băng chéo tài khoản người dùng từ bên thứ ba | Mỗi người dùng sở hữu Associated Token Account (ATA) độc lập, triệt tiêu lây nhiễm rủi ro. |"""

# Table 5: Roadmap Matrix for VI
VI_ROADMAP_TABLE = """| Giai Đoạn | Mục Tiêu Cốt Lõi | Kết Quả Kỹ Thuật Bàn Giao |
| :--- | :--- | :--- |
| **Giai đoạn 1: Tháng 1–12 (Q4 2026)** | **Mở rộng thương mại trên Solana L1**<br>(Thâm nhập thị trường & Đạt chuẩn PMF) | • Triển khai hợp đồng lõi v6.9.3 trên Solana Mainnet<br>• Tích hợp Passkey WebAuthn & Cổng nạp tiền VASP theo chuẩn pháp lý<br>• Ra mắt MCP Server cho Cursor, Claude, Antigravity<br>• Hoàn thành bộ kiểm thử 72/72 bài test bất biến lõi<br>• Kiểm toán bảo mật độc lập với OtterSec & Neodyme |
| **Giai đoạn 2: Tháng 12–24 (Q2 2027)** | **App-Rollup chuyên dụng trên nền SVM**<br>(Mở rộng quy mô hệ sinh thái & Mạng Relayer) | • Testnet bộ sắp xếp giao dịch (Sequencer) SVM chuyên dụng<br>• Tích hợp tính sẵn sàng dữ liệu (DA) với Celestia / EigenDA<br>• Kích hoạt thị trường tri thức cộng sinh & Giao thức vi nhiệm vụ đảo ngược<br>• Nâng công suất tổng hợp lên hơn 50.000 TPS máy móc |
| **Giai đoạn 3: Tháng 24–36+ (Q4 2027+)** | **Blockchain L1 Độc Lập Cho Siêu Trí Tuệ**<br>(Đích đến điều phối ASI phi tập trung) | • Ra mắt mạng thử nghiệm máy ảo Bare-Metal HAI-VM<br>• Tích hợp mã máy phần cứng gốc `OP_402_PAY`<br>• Kích hoạt đồng thuận kép: Proof-of-Agentic-Work (PoAW) + Proof-of-Actual-Intelligence (PoAI)<br>• Cầu nối chuyển đổi 1:1 hai chiều giữa SPL và token $HAISI L1 gốc<br>• Tốc độ thực thi máy móc vượt mốc 100.000 TPS |"""

# Table 1: Competitor Matrix for EN
EN_COMPETITOR_TABLE = """| Platform / Model | Critical Architectural Blind Spot | HAICHAIN Protocol Breakthrough |
| :--- | :--- | :--- |
| **Coinbase AgentKit & ElizaOS (ai16z)** | Raw EOA Private Key Exposure; Indirect prompt injection causes catastrophic wallet drain; Zero on-chain velocity bounds; No hardware kill switch. | Merkle Capability Leaves (CapLeaf 4-tuple bound); Segregated PDA Spending Pots; 1-Tap Emergency Panic Kill-Switch (< 400ms wire finality, theoretical upper bound $\\tau \\le 12\\text{s}$). |
| **Bittensor (TAO)** | 12,000ms Block Latency (incapable of real-time micro-settlements); Yuma Consensus collusion & copycat mining; Closed-loop Model Autophagy Disorder (MAD). | 50ms Fast-Path BFT Netting; Real utility streaming USDT/USDC; Proof of Actual Intelligence (PoAI) ingesting unpoisoned human ground truth via quadratic Schelling staking. |
| **ASI Alliance (Fetch.ai / SingNet)** | Cosmos/EVM Smart Contract CPI overhead; Multi-second BFT latency; Lack of native wire micro-opcodes; Decoupled from human legal identity. | Native OP_402_PAY opcode compiled into VM bytecode (> 100,000 TPS, zero CPI overhead); Unified Soulbound DIDs anchoring machines to human biometric Passkeys (EU AI Act). |
| **Virtuals Protocol (Base Layer 2)** | Single-threaded EVM write-lock contention on Base; Volatile Ethereum L1 blob fees ($0.01 - $0.50); Speculative meme bonding curves over enterprise utility. | Sealevel 32-partitioned ingestion ATAs; Off-chain symmetric netting yielding 99.999% compression (771-byte datagram); Enterprise stablecoin settlement. |
| **Stripe / Tempo MPP & Legacy Web2 Rails** | $0.30 + 2.9% fixed fee floor (150,000% overhead on $0.0002 API calls); T+2 to T+5 day settlement lag; Chargeback fraud risk; Lacks on-chain invariant vaults. | Pure micro-utility ($0.000001 netted); Sub-400ms cryptographic wire finality; Zero chargeback risk via PDA escrow; Invariant-enforced spending pots. |
| **Worldcoin (Tools for Humanity)** | Single-purpose proprietary hardware (The Orb) for passive UBI token distribution; Zero machine execution runtime; Zero capability bounding. | Open biometric standards (WebAuthn/ZK-PoH) integrated directly into the economic loop (Reverse Micro-Tasking), turning human minds into an active, compensated ASI coprocessor. |
| **HTTP x402 & Pay.sh (Solana x Google Cloud)** | Transport-layer request/response pipes; Single-delegate token limit on Solana; No client spending caps (V12 audit CVEs); Lacks on-chain kill switch and provider slashing. | Programmable Policy & Vault Layer (drop-in companion); Multi-delegate Merkle capability; Isolated PDA pots; Panic Circuit Breaker in < 400ms; Bounded Loss Theorem (zero drain). |"""

# Table 2: SaaS vs Utility for EN
EN_SAAS_TABLE = """| Economic Dimension | Legacy Per-Seat SaaS (Web2) | HAICHAIN Utility Protocol (v1.1) |
| :--- | :--- | :--- |
| **Billing Philosophy** | Pay-to-Access (Forced Fixed Monthly Fee) | Pay-per-Execution (Fractional Nano-Cents) |
| **Unused Quota** | 100% Forfeited at Month-End (Sunk Cost) | 100% Retained in User Custody / PDA |
| **Billing Unit** | Arbitrary Human "Seat" ($20 - $50/mo) | Actual Consumed Compute / API Tokens |
| **Interactivity Mode** | Human Clicking Visual Web UI | Headless Agent-to-Agent Autonomous API |
| **Financial Security** | Full Corporate Credit Card on File | Isolated PDA Spending Pot ($5.00 Hard Cap) |
| **Effective Monthly Expense** | $150.00 - $300.00 / seat / month | $3.40 / month (97.7% Real Reduction via BYOK) |"""

# Table 3: Cross-Paradigm Infrastructure Matrix for EN
EN_CROSS_PARADIGM_TABLE = """| Metric | Web2 Rails (Stripe / Visa) | EVM L1 / L2 (Base / Arbitrum) | HAICHAIN Protocol |
| :--- | :--- | :--- | :--- |
| **Minimum Practical Fee** | $0.30 fixed fee floor | $0.02 - $0.50 gas spike | $0.000001 (1,000:1 Compressed Netting) |
| **Settlement Latency** | 2 - 5 Business Days | 2,000 - 15,000ms | < 400ms Wire Finality (τ ≤ 12s on-chain ceiling) |
| **Prompt-Injection Risk** | Complete Card Drain | Drain of Master EOA | Mathematically 0 (PDA Vault Ceiling) |
| **Onboarding Friction** | KYC, Bank Forms, 3 Days | 12-Word Seed Phrase, Gas | Passkey FaceID (< 60s, True Invisible Web3) |
| **Reversibility / Panic** | Chargeback (60-90 Days) | Irreversible On-Chain Loss | 1-Tap Panic Circuit Breaker (< 400ms) |"""

# Table 4: Onboarding Topology for EN
EN_ONBOARDING_TABLE = """| 1. Biometric Passkey Enclave | 2. Universal Fiat On-Ramp | 3. Isolated Safe Pot (PDA) |
| :--- | :--- | :--- |
| **Hardware Key Protection**<br>• Apple FaceID / TouchID<br>• WebAuthn Secure Enclave<br>• Zero Seed Phrases | **Frictionless Top-Up**<br>• Apple Pay / Google Pay / Card<br>• Instant QR / SEPA / Local Rail<br>• Zero Crypto Exchange Friction | **Deterministic Loss Ceiling**<br>• Isolated $10.00 Sub-Pot<br>• Anti-Drain Circuit Breaker<br>• 1-Tap Emergency Panic Freeze |"""

# Table 5: 6 Invariants Defense Matrix for EN
EN_INVARIANTS_TABLE = """| Invariant / Defense Layer | Attack Vector & Historic Exploit | HAICHAIN Cryptographic Enforcement |
| :--- | :--- | :--- |
| **1. Sysvar Introspection** | Sysvar account spoofing (CVE-2022-24300) | Hardcoded `Sysvar1nstructions1111111111111111111111111` address validation. |
| **2. Non-Zero Merkle Root** | Uninitialized PDA / Zero-hash bypass | `require!(composite_root != [0u8; 32])` enforced at program invocation. |
| **3. Capability Leaf Bounding** | Indirect prompt injection & wallet drain | 4-Tuple Merkle Leaf (`Pubkey \|\| MaxSpend \|\| Expiry \|\| Nonce`) limits spend. |
| **4. Live ATA Balance Introspection** | Accounting drift & donation inflation | Strict balance reload: `require!(actual_ata_balance >= spend_amount)`. |
| **5. Flash-Loan Liquidity Quarantine** | Same-block deposit-borrow-drain exploits | Multi-slot timelock: `require!(slot >= last_deposit_slot + 2)`. |
| **6. Segregated Token Account Isolation** | Cross-user contagion & third-party freezes | Independent per-vault SPL Associated Token Accounts (zero contagion). |"""

# Table 6: Roadmap Matrix for EN
EN_ROADMAP_TABLE = """| Timeline | Milestone Objective | Key Technical Deliverables |
| :--- | :--- | :--- |
| **Phase 1: Months 1–12 (Q4 2026)** | **Solana L1 Core & Enterprise Integration**<br>(Market Penetration & Commercial PMF) | • Hardened Kernel v6.9.3 on Solana Mainnet<br>• Biometric WebAuthn Passkeys & Regulated VASP Gateway<br>• Model Context Protocol (MCP) Server for Cursor & Claude<br>• Invariant Verification Suite ($I_1 \dots I_9$, 72/72 tests passing)<br>• Independent Smart Contract Audits (OtterSec & Neodyme) |
| **Phase 2: Months 12–24 (Q2 2027)** | **High-Throughput Dedicated SVM App-Rollup**<br>(Ecosystem Scaling & Relayer Mesh) | • Dedicated SVM Sequencer Testnet<br>• Modular Data Availability via Celestia / EigenDA<br>• Symbiotic Knowledge Marketplace Launch<br>• Reverse Micro-Tasking Protocol Active<br>• Aggregated 50,000+ Machine TPS Capacity |
| **Phase 3: Months 24–36+ (Q4 2027+)** | **HAICHAIN Sovereign Machine L1 (ASI)**<br>(Decentralized Superintelligence Endgame) | • HAI-VM Bare-Metal Virtual Machine Testnet<br>• Native Hardware-Level `OP_402_PAY` Opcode<br>• Dual-Tier Consensus: Proof-of-Agentic-Work (PoAW) + Proof-of-Actual-Intelligence (PoAI)<br>• 1:1 Two-Way Teleport Bridge between SPL and Native $HAISI<br>• Peak Machine TPS Exceeding 100,000 TPS |"""

def safe_sub(pattern, replacement, string):
    return re.sub(pattern, lambda m: replacement, string)

def apply_vietnamese():
    path = "HAICHAIN_WHITEPAPER_V1.0_VI.md"
    text = open(path, "r", encoding="utf-8").read().replace("\r\n", "\n")
    
    # Replace Table 1: Competitor Matrix
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*BẢNG SO SÁNH ĐỐI THỦ THỰC NGHIỆM[\s\S]*?\n\+[ -]+\+\n```', VI_COMPETITOR_TABLE, text)
    
    # Replace Table 2: SaaS vs Utility
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*BẪY THUÊ BAO ĐẦU NGƯỜI CŨ[\s\S]*?\n\+[ -]+\+\n```', VI_SAAS_TABLE, text)
    
    # Replace Table 3: Invisible Web3 Onboarding
    text = safe_sub(r'```[^\n]*\n\s*\+[ -]+\+\n\s*\|\s*QUY TRÌNH TIẾP CẬN VÔ HÌNH[\s\S]*?\n\s*\+[ -]+\+\n```', VI_ONBOARDING_TABLE, text)
    
    # Replace Table 4: 6 Invariants
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*MA TRẬN PHÒNG THỦ 6 BẤT BIẾN[\s\S]*?\n\+[ -]+\+\n```', VI_INVARIANTS_TABLE, text)
    
    # Replace Table 5: Roadmap
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*MA TRẬN LỘ TRÌNH TRIỂN KHAI CHIẾN LƯỢC[\s\S]*?\n\+[ -]+\+\n```', VI_ROADMAP_TABLE, text)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open("app/" + path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Vietnamese whitepaper markdown tables applied.")

def apply_english():
    path = "HAICHAIN_WHITEPAPER_V1.0_EN.md"
    text = open(path, "r", encoding="utf-8").read().replace("\r\n", "\n")
    
    # Replace Cross-Paradigm table
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*CROSS-PARADIGM INFRASTRUCTURE COMPARISON MATRIX[\s\S]*?\n\+[ -]+\+\n```', EN_CROSS_PARADIGM_TABLE, text)
    
    # Replace SaaS table
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*LEGACY PER-SEAT SUBSCRIPTION TRAP[\s\S]*?\n\+[ -]+\+\n```', EN_SAAS_TABLE, text)
    
    # Replace Competitor table
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*EMPIRICAL ARCHITECTURAL MATRIX[\s\S]*?\n\+[ -]+\+\n```', EN_COMPETITOR_TABLE, text)
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*EMPIRICAL COMPETITOR AUDIT[\s\S]*?\n\+[ -]+\+\n```', EN_COMPETITOR_TABLE, text)
    
    # Replace Onboarding table
    text = safe_sub(r'```[^\n]*\n\s*\+[ -]+\+\n\s*\|\s*INVISIBLE WEB3 ONBOARDING TOPOLOGY[\s\S]*?\n\s*\+[ -]+\+\n```', EN_ONBOARDING_TABLE, text)
    
    # Replace 6 Invariants table
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*HAICHAIN v6\.9\.3 SIX INVARIANTS[\s\S]*?\n\+[ -]+\+\n```', EN_INVARIANTS_TABLE, text)
    
    # Replace Roadmap table
    text = safe_sub(r'```[^\n]*\n\+[ -]+\+\n\|\s*HAICHAIN GLOBAL EXECUTION & ROADMAP MATRIX[\s\S]*?\n\+[ -]+\+\n```', EN_ROADMAP_TABLE, text)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open("app/" + path, "w", encoding="utf-8") as f:
        f.write(text)
    print("English whitepaper markdown tables applied.")

if __name__ == "__main__":
    apply_vietnamese()
    apply_english()
