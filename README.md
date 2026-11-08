# HAICHAIN
> **THE FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE ERA**  
> **HỆ ĐIỀU HÀNH TÀI CHÍNH CHO KỶ NGUYÊN MÁY TỰ HÀNH**

## The Economic Bedrock for the Symbiotic Superintelligence Era AI²
### Nền Tảng Kinh Tế Cho Kỷ Nguyên Siêu Trí Tuệ Cộng Sinh AI²

**The Autonomous Financial Firewall for AI Agents. Enforcing deterministic Merkle CapLeaf invariants, bounded-loss spending limits, and prompt-injection immunity to prevent catastrophic wallet drainage.**

*Bức tường lửa tài chính tự hành cho AI Agent. Thiết lập bất biến ngân sách Merkle CapLeaf, giới hạn rủi ro hữu hạn (Bounded Loss) và miễn nhiễm rút ruột ví khi AI bị tấn công Prompt Injection.*

```
[ 🛡️ Zero-Drain Budget Firewall ]   [ ⚡ Sub-Second Panic Kill-Switch ]   [ 🔌 Universal x402 & MCP Adapter ]
[ 🛡️ Chống Rút Ruột Ví ]            [ ⚡ Cầu Chì Khẩn Cấp < 1 Giây ]       [ 🔌 Tương Thích Chuẩn x402 & MCP ]
```

---

> [!WARNING]
> **⚠️ DEVNET TESTING PROTOTYPE (`v0.1.0-prototype`) — UN-AUDITED — DO NOT DEPOSIT REAL FUNDS**
> This repository contains open-source software under active security research, protocol hardening, and developer preview. It has **NOT** completed an independent third-party audit. Do **NOT** deposit real funds on Solana mainnet. All token allocations, smart contracts, and settlement flows currently operate in test mode on **Solana Devnet**.

---

## 1. Tử Huyệt Thị Trường & Lý Do Doanh Nghiệp Cần HAICHAIN

> 🚨 **VẤN ĐỀ SINH TỬ:** *Nếu bạn cấp quyền cho AI Agent tự do tiêu tiền từ ví Coinbase AgentKit hoặc Stripe, làm sao bạn đảm bảo một câu Prompt Injection ác ý ẩn trong dữ liệu web không rút sạch toàn bộ quỹ doanh nghiệp chỉ trong 2 giây?*

* **Stripe & Coinbase AgentKit:** Cung cấp đường ray thanh toán và cổng chuyển tiền, nhưng **hoàn toàn bỏ ngỏ tầng phòng vệ ngân sách**. Khi bot bị chiếm quyền qua prompt, kẻ tấn công có thể ra lệnh rút sạch ví.
* **HAICHAIN:** Đóng vai trò là **Lớp Bảo vệ & Điều phối Đa năng (Security & Governance Adapter)** bọc ngoài các chuẩn đó:
  1. **Khống chế trần rủi ro hữu hạn (Bounded Loss):** Khóa cứng trần chi tiêu tối đa mỗi lượt gọi ($0.001 - $1.00) và trần tốc độ chi tiêu theo cửa sổ trượt (Sliding Velocity) bằng toán học Merkle CapLeaf.
  2. **Miễn nhiễm Prompt Injection:** Kể cả khi AI bị đầu độc bộ nhớ, các bất biến toán học $I_1 - I_9$ trên Solana L1 lập tức từ chối mọi lệnh rút quá hạn mức.
  3. **Cầu chì khẩn cấp dưới 1 giây (< 400ms):** Tự động vô hiệu hóa toàn bộ voucher ngoại chuỗi khi phát hiện vòng lặp bất thường.
  4. **Adapter đa năng:** Cắm trực tiếp vào **Coinbase x402**, **Anthropic MCP (Claude / Cursor)**, **ElizaOS (ai16z)**, **Stripe MPP**, **Solana L1** và **EVM**.

---

## 2. 1-Click Quickstart: Bọc Bức Tường Lửa Cho Agent Trong 30 Giây

### Python (`haichain-agent-pay`):
```python
from haichain_pay import firewall

# Doanh nghiệp chỉ cần gắn 1 dòng decorator để bảo vệ Agent
@firewall.protect(daily_cap=50.0, per_call_cap=1.0)
async def run_enterprise_agent(prompt: str):
    # Tích hợp trực tiếp với Coinbase AgentKit, LangChain, Claude, ElizaOS
    # Tự động ngắt khi phát hiện Prompt Injection hoặc vượt trần ngân sách
    return await my_agent.execute(prompt)
```

### Node.js / TypeScript (`@haichainsi/agent-pay`):
```typescript
import { firewall } from "@haichainsi/agent-pay";

// Bọc bất kỳ hàm gọi Agent nào với hạn mức ngân sách cứng
const safeAgentTask = firewall.protect(
  { maxDailyBudget: 50.0, maxPerCall: 1.0, anomalyKill: true },
  async (prompt: string) => {
    return await agent.run(prompt);
  }
);
```

---

## 3. Lộ Trình Triển Khai Chiến Lược (2 Giai Đoạn)

* **Giai đoạn 1 (Wedge hiện tại): Phủ sóng SDK Tường lửa (Agent Financial Firewall) cho 1,000+ AI Agent.**
  * Triển khai Financial Firewall & Micro-Escrows chạy thực chiến trên Solana L1 (tận dụng tốc độ 400ms và chi phí nano-cent cực rẻ để phục vụ thị trường ngay lập tức).
* **Giai đoạn 2 (Endgame dài hạn): Tự động kích hoạt Kênh trạng thái vi mô và hoàn thiện Hệ điều hành tài chính.**
  * Khi quy mô giao dịch agentic vượt ngưỡng hàng tỷ lệnh/ngày, mở rộng thành Sovereign App-chain / L1 độc lập với cơ chế đồng thuận Proof of Actual Intelligence (PoAI).

---

## 4. Chuẩn Token Devnet & Hợp Đồng Thông Minh

* **Tài sản thanh toán:** **USDT (Tether SPL Token trên Solana)**
* **Solana USDT Mint (Tham chiếu Mainnet):** `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`
* **Độ chính xác:** 6 Decimals (`1 USDT = 1,000,000 micro-units`)
* **Chương trình Solana Devnet ID:** `DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk`

---

## 5. Kiến Trúc Kho Lưu Trữ

```
c:\Users\Surface\Documents\8. HAICHAIN\
├── app/
│   ├── index.html                  # Landing Page (Định vị Bức tường lửa & Hệ điều hành)
│   └── dashboard.html              # Web3 Agent & Channel Dashboard
├── programs/
│   └── haichain-core/              # Solana Anchor Smart Contract (Rust)
│       ├── Cargo.toml
│       └── src/lib.rs              # Pot, CapLeaf, Channel Escrow, Panic & Dispute Invariants
├── packages/
│   ├── agent-pay/                  # Node.js x402 Paywall & 1-Click Firewall Middleware
│   │   ├── src/firewall.ts
│   │   └── src/index.ts
│   └── agent-pay-python/           # Python SDK (FastAPI, ASGI & @firewall.protect decorator)
│       ├── haichain_pay/firewall.py
│       └── haichain_pay/paywall.py
├── sdk/
│   ├── typescript/                 # Global Client SDK (x402 Protocol, PolicyEngine, CapLeaf)
│   └── c-edge/                     # Bare-Metal C-SDK (< 200KB RAM) cho Robotics & IoT
├── mcp-server/                     # Model Context Protocol Server (Claude & Cursor)
├── server/
│   └── production-agent-relayer.js # Relayer với Anti-SSRF Guard & Rate Limiting
└── tests/
    ├── haichain-negative-invariants.test.ts # Negative Test Suite (Test Âm)
    └── haichain-x402-interoperability.test.ts # RFC-compliant x402 interop suite
```

---

## 6. Hướng Dẫn Kiểm Thử & Xác Minh (Test Verification)

### Kiểm tra Hợp đồng Thông minh Solana Anchor:
```bash
cd programs/haichain-core
cargo check
cargo test
```

### Chạy Toàn Bộ Test Suite TypeScript & i18n (92 Tests):
```bash
npm test
```

### Chạy Bộ Test Python (12 Tests bao gồm 1-Click Firewall):
```bash
python -m unittest discover -s packages/agent-pay-python/tests
```

---
*Giấy phép: MIT License (`LICENSE`). Bản quyền thuộc về Dự án HAICHAIN.*
