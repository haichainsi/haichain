# scripts/update_whitepaper_x402.py
# Updates HAICHAIN Whitepapers (VI and EN) with standardized x402 integration specifications.

import os

VI_PATH = "HAICHAIN_WHITEPAPER_V1.0_VI.md"
EN_PATH = "HAICHAIN_WHITEPAPER_V1.0_EN.md"

VI_NEW_SECTION = """### 4.6. Định Vị Liên Minh: HAICHAIN Là Lớp Quản Trị Chính Sách & Chốt An Toàn Cho Chuẩn HTTP x402 và Solana Pay.sh

Trong bức tranh toàn cảnh của nền kinh tế tác tử tự hành, thị trường chứng kiến sự bùng nổ của các chuẩn giao tiếp thanh toán mở như **HTTP x402** (do Coinbase khởi xướng, được Linux Foundation bảo trợ cùng sự tham gia của Visa & Mastercard) và **Pay.sh** (sáng kiến hợp tác giữa Solana Foundation và Google Cloud ra mắt tháng 5/2026).

```
         PHÂN TẦNG HẠ TẦNG THANH TOÁN TÁC TỬ TỰ HÀNH TOÀN CẦU
         
   [ TÁC TỬ & BẦY ĐÀN AI ] : Claude Desktop, Cursor, ElizaOS, CrewAI
                                │
                                ▼
   [ GIAO TIẾP & BÁO PHÍ ] : Chuẩn HTTP x402 & Solana Pay.sh Middleware
   (Báo mã 402 Payment Required & Vận chuyển Header thanh toán X-PAYMENT)
                                │
                                ▼
   [ CHÍNH SÁCH & BẢO VỆ ] : ★ HAICHAIN AGENT POLICY VAULT ★
   (Cây năng lực Merkle CapLeaf, Hạn mức cứng MaxSpend, Chốt ngắt Panic < 400ms)
                                │
                                ▼
   [ ĐƯỜNG RAY CHỐT SỔ L1 ] : Solana L1 Ledger, Sui Move Objects & Base L2 (USDC/USDT)
```

1. **Phân Định Vai Trò Rõ Ràng (Bổ trợ Chiến lược Thay vì Đối đầu):**
   * **x402 và Pay.sh đóng vai trò là "Đường Ống Giao Tiếp" (Communication & Invoicing Protocol):** Định nghĩa chuẩn giao thức cấp ứng dụng: máy chủ API phát hiện thiếu thanh toán sẽ trả về mã trạng thái HTTP 402 cùng cấu trúc dữ liệu yêu cầu chi trả (`maxAmountRequired`, `resource`, `payTo`, `asset`, `network`, `nonce`), và phía Client gửi lại thông điệp ủy quyền thanh toán qua Header `X-PAYMENT` hoặc `Authorization: X402`.
   * **HAICHAIN đóng vai trò là "Ngân Hàng Quản Trị Chính Sách & Kho Quỹ An Toàn" (Cryptographic Smart Policy & Safe Custody Vault):** Trả lời những câu hỏi sinh tử mà x402 và Pay.sh theo đuổi tính trung lập nên cố tình để ngỏ: *Tác tử lấy tiền từ đâu? Ai cấp quyền ủy thác? Làm sao ngăn chặn một tác tử LLM bị Jailbreak hoặc Prompt Injection rút cạn sạch ngân quỹ của công ty?* Giống như giao thức quét mã QR hay máy POS thanh toán không thể thay thế được hệ thống quản trị hạn mức của ngân hàng phát hành thẻ, x402 càng phổ biến bao nhiêu thì nhu cầu sử dụng HAICHAIN để bảo vệ tài sản doanh nghiệp càng trở nên cấp bách bấy nhiêu.

2. **Khắc Phục Toàn Diện 3 Lỗ Hổng Thực Tế Của Chuẩn x402 Thuần Túy:**
   * **Lỗ hổng 1: Thiếu trần chi tiêu nội tại (No Native Budget Caps):** Trong chuẩn x402 thuần, máy chủ yêu cầu bao nhiêu thì tác tử (nếu có quyền ký) sẽ ký bấy nhiêu. Nếu gặp máy chủ ma đưa giá $100 thay vì $0.001, ví tác tử sẽ bị bòn rút ngay tức khắc. HAICHAIN giải quyết bằng **Định Lý Giới Hạn Thiệt Hại (Bounded Loss Theorem)**:
   $$\\Delta \\text{Loss}_{\\max} \\le \\min\\left(\\text{max\\_spend} - \\text{consumed},\\, \\text{window\\_cap}\\right)$$
   Mọi yêu cầu vượt quá `max_spend` hoặc `window_cap` đều bị máy ảo chính sách `PolicyEngine` từ chối ký ngay tại nguồn, tuyệt đối không xuất xưởng chữ ký hợp lệ.
   * **Lỗ hổng 2: Độ trễ giao dịch đơn lẻ và tắc nghẽn L1:** Việc bắt từng lượt gọi API phải đợi xác nhận giao dịch trên sổ cái blockchain L1 làm chậm chu kỳ suy luận của mô hình AI (mất từ 400ms đến 2.000ms). HAICHAIN thiết lập **Kiến Trúc Hai Nhịp (Dual-Path Architecture)**:
     - *Nhịp nhanh (Fast-Path Off-chain Voucher < 2ms):* Tác tử ký voucher vi thanh toán ngoại chuỗi đơn điệu tăng dần. Máy chủ xác thực chữ ký Ed25519 trong chưa đầy 2ms và trả dữ liệu streaming ngay lập tức.
     - *Nhịp thanh quyết toán (Direct L1 / Batch Settlement):* Các vi voucher được gom lô và cấn trừ qua Cỗ máy Bù trừ Đa phương HAICHAIN trước khi đóng sổ trên Solana L1 hoặc Base L2.
   * **Lỗ hổng 3: Tấn công phát lại (Replay Attacks):** HAICHAIN Paywall và Core Contract triển khai bộ đệm vô hiệu hóa kép: **Nullifier In-Memory Cache** trên middleware và **Ephemeral Nullifier PDA** trên chuỗi, chặn đứng 100% việc tái sử dụng cùng một chữ ký hoặc nonce thanh toán.

3. **Đặc Tả Kỹ Thuật Tương Thích Chuẩn Hóa Hai Chiều (Dual-Stack Envelope):**
   Gói `@haichainsi/agent-pay` và `@haichainsi/sdk` hỗ trợ đầy đủ chuẩn nhận dạng mạng **CAIP-2** và chuẩn phong bì dữ liệu:
   * **Bảng Định Danh Chuỗi (CAIP-2 Identifiers):**
     - Solana Mainnet: `solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp`
     - Solana Devnet: `solana:EtWTRABZaYq6iMfeYKouRu166VU2xqa1`
     - Base Mainnet (Coinbase L2): `eip155:8453`
   * **Phong Bì Chữ Ký Kép (Dual Signature Envelope):** Hỗ trợ chữ ký **Ed25519 Detached Signature** cho hệ sinh thái Solana/Sui và **EIP-712 Typed Data** cho hệ sinh thái Base/EVM, đồng thời nhúng chặt khóa băm gốc Merkle `leafHashHex` (223 bytes) vào siêu dữ liệu:
   ```typescript
   // Tác tử AI xử lý thử thách thanh toán x402 chuẩn hóa một cách an toàn qua HAICHAIN PolicyEngine
   const challenge = X402Client.parseChallenge(rawHttp402Response);
   const payment = x402Client.generatePaymentResponse(
     challenge,
     leafHashHex,
     channelId,
     CapScopeClass.DATA_API | CapScopeClass.LLM_INFERENCE
   );

   // Gửi lại Header chuẩn x402 toàn cầu (X-PAYMENT Base64) bảo chứng bởi HAICHAIN Guardrail
   fetch(challenge.resource, {
     headers: {
       "X-PAYMENT": payment.headers["X-PAYMENT"],
       "Authorization": payment.headers["Authorization"]
     }
   });
   ```
   Nhờ kiến trúc tương thích hoàn hảo này, HAICHAIN không thay thế hay loại trừ x402, mà trở thành **hạ tầng bảo vệ và quản trị rủi ro tối thượng** cho mọi tác tử hoạt động trên nền kinh tế Internet mở."""

EN_NEW_SECTION = """### 6.6. Strategic Positioning: HAICHAIN as the Policy & Circuit Breaker Layer for HTTP x402 and Solana Pay.sh

Across the broader landscape of autonomous agent infrastructure, open machine-payment communication protocols have gained rapid institutional adoption, notably **HTTP x402** (originated by Coinbase, transitioned to the Linux Foundation with Visa and Mastercard participation) and **Pay.sh** (jointly launched by the Solana Foundation and Google Cloud in May 2026).

```
        GLOBAL AUTONOMOUS AGENT FINANCIAL INFRASTRUCTURE STACK
        
   [ AGENTS & REASONING SWARMS ] : Claude Desktop, Cursor, ElizaOS, CrewAI
                                  │
                                  ▼
   [ COMMUNICATION & INVOICING ] : HTTP x402 Specification & Pay.sh Proxy
   (Emits 402 Payment Required & transports X-PAYMENT cryptographic payloads)
                                  │
                                  ▼
   [ POLICY & RISK GOVERNANCE  ] : ★ HAICHAIN AGENT POLICY VAULT ★
   (Merkle Capability Trees, Hard MaxSpend Caps, Sub-400ms Panic Kill-Switch)
                                  │
                                  ▼
   [ ON-CHAIN SETTLEMENT RAILS ] : Solana L1 Ledger, Sui Move Objects & Base L2 (USDC/USDT)
```

1. **Clear Division of Roles (Complementary Ecosystem Synergy, Never Direct Competition):**
   * **x402 and Pay.sh serve as the "Communication & Messaging Pipes":** Defining how APIs return HTTP `402 Payment Required` with structured challenge bodies (`maxAmountRequired`, `resource`, `payTo`, `asset`, `network`, `nonce`) and how clients return payment authorizations via the `X-PAYMENT` or `Authorization: X402` header.
   * **HAICHAIN serves as the "Enterprise Risk Bank & Safe Policy Vault":** Solving the mission-critical vulnerabilities that x402 and Pay.sh intentionally leave open: *Where does the agent store capital? Who enforces spending limits? How is a prompt-injected LLM stopped from emptying corporate treasury accounts?* Just as a POS card terminal does not replace a bank's corporate risk-underwriting infrastructure, the widespread expansion of x402 accelerates enterprise demand for HAICHAIN policy vaults.

2. **Decisively Neutralizing 3 Critical Vulnerabilities of Pure x402:**
   * **Vulnerability 1: Absence of Inherent Spending Ceilings:** Pure x402 allows any malicious endpoint to invoice an unconstrained amount. HAICHAIN neutralizes this via the **Bounded Loss Theorem**:
   $$\\Delta \\text{Loss}_{\\max} \\le \\min\\left(\\text{max\\_spend} - \\text{consumed},\\, \\text{window\\_cap}\\right)$$
   Any request violating `max_spend` or `window_cap` is rejected client-side by `PolicyEngine` before any signature can be minted.
   * **Vulnerability 2: Latency Penalties and L1 Congestion:** Forcing every single micro-call to wait for L1 block finality degrades LLM streaming performance. HAICHAIN introduces a **Dual-Path Architecture**:
     - *Fast-Path Off-chain Voucher (< 2ms):* Detached Ed25519 micro-vouchers are verified off-chain by server middleware in sub-2ms, delivering immediate wire-speed data streaming.
     - *Batch Settlement Path:* Vouchers are aggregated and cleared via the HAICHAIN Multilateral Netting Engine prior to on-chain settlement on Solana L1 or Base L2.
   * **Vulnerability 3: Replay Attacks:** HAICHAIN Paywall and Core Programs deploy dual nullifier barriers: **In-Memory Nullifier Caches** on middleware and **Ephemeral Nullifier PDAs** on-chain, rendering replay attacks mathematically impossible.

3. **Standardized Dual-Stack Envelope & CAIP-2 Interoperability:**
   The `@haichainsi/agent-pay` and `@haichainsi/sdk` packages provide turnkey support for standard **CAIP-2 Chain Identifiers** and dual signature formats:
   * **CAIP-2 Identifiers:**
     - Solana Mainnet: `solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp`
     - Solana Devnet: `solana:EtWTRABZaYq6iMfeYKouRu166VU2xqa1`
     - Base Mainnet (Coinbase L2): `eip155:8453`
   * **Dual Signature Envelope:** Supports **Ed25519 Detached Signatures** for Solana/Sui alongside **EIP-712 Typed Data** for Base/EVM, cryptographically binding the 223-byte CapLeaf Merkle hash into standard x402 authorization headers:
   ```typescript
   // Autonomous agent resolves standard HTTP x402 payment challenge via safe HAICHAIN Vault
   const challenge = X402Client.parseChallenge(rawHttp402Response);
   const payment = x402Client.generatePaymentResponse(
     challenge,
     leafHashHex,
     channelId,
     CapScopeClass.DATA_API | CapScopeClass.LLM_INFERENCE
   );

   // Retries with standard global x402 Header (X-PAYMENT Base64) protected by HAICHAIN Guardrail
   fetch(challenge.resource, {
     headers: {
       "X-PAYMENT": payment.headers["X-PAYMENT"],
       "Authorization": payment.headers["Authorization"]
     }
   });
   ```
   HAICHAIN does not seek to replace x402 or Pay.sh; it serves as the essential cryptographic safety seatbelt that allows enterprises to confidently deploy high-velocity autonomous agents onto these public payment rails."""

def update_file(path, old_marker_start, old_marker_end, new_content):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    start_idx = text.find(old_marker_start)
    if start_idx == -1:
        print(f"Error: Start marker '{old_marker_start}' not found in {path}")
        return False

    end_idx = text.find(old_marker_end, start_idx)
    if end_idx == -1:
        print(f"Error: End marker '{old_marker_end}' not found in {path}")
        return False

    updated_text = text[:start_idx] + new_content + "\n\n" + text[end_idx:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated_text)

    print(f"Successfully updated {path}")
    return True

if __name__ == "__main__":
    vi_ok = update_file(VI_PATH, "### 4.6. Định Vị Liên Minh:", "## CHƯƠNG 5:", VI_NEW_SECTION)
    en_ok = update_file(EN_PATH, "### 6.6. Strategic Positioning:", "## 7. MULTILATERAL SYMMETRIC NETTING", EN_NEW_SECTION)
    if vi_ok and en_ok:
        print("ALL WHITEPAPER UPDATES COMPLETED SUCCESSFULLY.")
    else:
        exit(1)
