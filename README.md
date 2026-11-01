# HAICHAIN v6.9.3
### The Universal Autonomous Machine Financial Operating System
**"Primary Settlement via USDT (Tether SPL), HTTP x402 Native Protocol, Ephemeral Nullifier Replay Defense, Recyclable Rent Economics & Zero-Griefing Direct PDA Authority"**

HAICHAIN is the global real-time financial settlement and micro-payment operating system for Autonomous AI Agents built on **Solana L1**. The protocol bridges two critical frontiers:
1. **For Global Consumers & AI Power-Users (Worldwide):** Eliminates predatory $150-$450/month recurring SaaS subscriptions, replacing them with granular pay-per-action micro-cents in **USDT (Tether)** ($0.0008 USDT per LLM query, $0.0002 USDT per web scrape). Offers 10-second onboarding via Binance/OKX direct Solana withdrawal, Apple Pay, Google Pay, or cross-chain bridge (TRC-20 / ERC-20), secured by a One-Click Panic Kill-Switch with strictly enforced ownership return.
2. **For Global Enterprises, Developers & Robotics:** Enforces verified immunity against historic $800M+ exploits (Wormhole, Nomad, Euler, Mango), **insulates against Tether blacklist freeze contagion via Dedicated Non-Commingled ATAs**, **blocks ElizaOS-style Indirect Prompt Injection via Composite Merkle Whitelists**, **eliminates double-spend replay attacks via Ephemeral Nullifier PDAs**, **reclaims 100% of temporary SOL rent via `reclaim_expired_nullifier`**, and **strictly prevents MEV rent leakage via the Anti-Rent-Theft Invariant**. Supports OpenAI o1/o3 and Claude 3.5 extended reasoning via Elastic Escrow, and powers edge IoT and robotics (Tesla Optimus) with a < 200KB RAM Bare-Metal C-SDK.

---

## OFFICIAL TOKEN STANDARD

* **Primary Settlement Asset:** **USDT (Tether SPL Token on Solana)**
* **Official Solana USDT Mint:** `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`
* **Precision:** 6 Decimals (`1 USDT = 1,000,000 micro-units`)
* **Tether Freeze Protection:** Dedicated Non-Commingled Token Accounts guarantee zero cross-account contagion if Tether blacklists external malicious addresses.

---

## REPOSITORY ARCHITECTURE

```
c:\Users\Surface\Documents\8. HAICHAIN\
├── app/
│   ├── index.html                  # Apple Luxury Landing Page
│   └── dashboard.html              # Full Web3 User Dashboard & AI Terminal
├── programs/
│   └── haichain-core/              # Solana Anchor v6.9.2 Smart Contract (Rust)
│       ├── Cargo.toml
│       └── src/lib.rs              # Nullifier PDAs, Rent Reclaim, Direct Authority, USDT & Panic
├── sdk/
│   ├── typescript/                 # Global Client SDK (x402 Protocol, USDT, Rent Reclamation)
│   │   ├── src/index.ts
│   │   └── package.json
│   └── c-edge/                     # Bare-Metal C-SDK (< 200KB RAM) for Robotics & IoT
│       ├── haichain_flash.h
│       └── haichain_flash.c
├── mcp-server/                     # Model Context Protocol Server (Claude & Cursor)
│   ├── src/index.ts
│   └── package.json
├── tests/
│   └── haichain-security.test.ts  # 14 Exploit Immunity, Replay, Rent Theft & Attribution Tests
├── Anchor.toml                     # Anchor Deployment Configuration
├── Cargo.toml                      # Workspace Cargo with Release LTO
├── HAICHAIN_WHITEPAPER_V1.0_EN.md  # Official Whitepaper v1.0 (English Edition)
├── HAICHAIN_WHITEPAPER_V1.0_VI.md  # Bản Sách Trắng Chính Thức v1.0 (Tiếng Việt)
├── HAICHAIN_INVESTOR_PITCH_DECK_V1.0.md # Seed Round Investor Pitch Deck ($1.2M at $15M FDV)
├── HAICHAIN_FINANCIAL_MODEL_3YR_PL.md   # 3-Year P&L, Unit Economics & Month-20 Breakeven
├── HAICHAIN_MASTER_ANNOUNCEMENT_X_THREAD.md # Master 12-Part Viral Launch Thread & Manifesto
├── HAICHAIN_MASTER_PROJECT_COMPLETION_REPORT.md # Master Project Completion Report & Sign-Off
├── DEVNET_DEPLOYMENT_GUIDE.md      # Solana Devnet Deployment & Operations Manual
├── DEVELOPER_QUICKSTART.md         # 60-Second AI Agent Integration Guide
└── README.md                       # Master Documentation & Quickstart
```

---

## INSTITUTIONAL REPOSITORY DOSSIER
* **Pre-Seed SAFT Agreement ($0.007):** [`HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md) *(Hợp đồng SAFT Pháp lý Chuẩn mực Vòng Bán Nội Bộ $0.007 Song ngữ)*
* **Pre-Seed Investment One-Pager Memo:** [`HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md) *(Bản Tóm Tắt Đầu Tư 1 Trang Vòng $0.007 cho Bạn bè, Thiên thần & Co-builders)*
* **Dual-Phase Token Sale & Pricing Strategy:** [`HAICHAIN_TOKEN_SALE_AND_PRICING_STRATEGY_VI_EN.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_TOKEN_SALE_AND_PRICING_STRATEGY_VI_EN.md) *(Chiến Lược Mở Bán Hai Giai Đoạn: Nội bộ $0.007 -> Công khai $0.010 & 3 Nguyên Tắc Khóa Token)*
* **The $AI^2$ Manifesto & Philosophy:** [`HAICHAIN_AI2_PHILOSOPHY_AND_SYMBIOSIS.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_AI2_PHILOSOPHY_AND_SYMBIOSIS.md) *(Bản Tuyên Ngôn Triết Lý Nền Tảng $AI^2$: Human + AI Symbiosis & Actual Intelligence)*
* **Official Blog & Thought Leadership:** [`HAICHAIN_BLOG_AI_HIRING_HUMANS_VI_EN.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_BLOG_AI_HIRING_HUMANS_VI_EN.md) *(Chuyên luận Song ngữ: Khi AI trở thành bên trả lương cho nhân loại - Reverse Micro-Tasking)*
* **Master Completion Report & Sign-Off:** [`HAICHAIN_MASTER_PROJECT_COMPLETION_REPORT.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_MASTER_PROJECT_COMPLETION_REPORT.md) *(Certified 100% completion dossier & asset inventory)*
* **Developer Quickstart Guide:** [`DEVELOPER_QUICKSTART.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/DEVELOPER_QUICKSTART.md) *(60-Second Setup for Claude, Cursor, CrewAI & ElizaOS)*
* **Official Whitepaper (EN):** [`HAICHAIN_WHITEPAPER_V1.0_EN.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_WHITEPAPER_V1.0_EN.md) *(Institutional calibers, mathematical FSM & L1 Endgame)*
* **Bản Sách Trắng Chính Thức (VI):** [`HAICHAIN_WHITEPAPER_V1.0_VI.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_WHITEPAPER_V1.0_VI.md) *(Toàn văn 10 chương đặc tả kỹ thuật tiếng Việt)*
* **Devnet Deployment Manual:** [`DEVNET_DEPLOYMENT_GUIDE.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/DEVNET_DEPLOYMENT_GUIDE.md) *(Automated Devnet deployer, PDAs & Explorer links)*
* **Master Launch Thread & Manifesto:** [`HAICHAIN_MASTER_ANNOUNCEMENT_X_THREAD.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_MASTER_ANNOUNCEMENT_X_THREAD.md) *(Viral 12-tweet thread, Mirror essay & Farcaster casts)*
* **Investor Pitch Deck v1.0:** [`HAICHAIN_INVESTOR_PITCH_DECK_V1.0.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_INVESTOR_PITCH_DECK_V1.0.md) *(10-Slide Seed Memo: $1.2M at $15M FDV)*
* **3-Year Financial Model & P&L:** [`HAICHAIN_FINANCIAL_MODEL_3YR_PL.md`](file:///c:/Users/Surface/Documents/8.%20HAICHAIN/HAICHAIN_FINANCIAL_MODEL_3YR_PL.md) *(Unit economics, EBITDA & burn rate)*
* **Live Web Landing Page:** `http://localhost:3000/` (Apple luxury minimalist presentation)
* **Live Web3 User Dashboard:** `http://localhost:3000/dashboard` (Full-featured financial OS & AI Terminal)

---

## 10 CORE ARCHITECTURAL INVARIANTS (v6.9.3 ZERO-GRIEFING HARDENED)

1. **Zero-Spend & Zero-Deposit Griefing Immunity:** Bắt buộc `amount > 0` và `spend_amount > 0`. Ngăn chặn triệt để vector tấn công nạp 0 USDT để liên tục reset slot cách ly quarantine (Mango DoS) hoặc phát vé thanh toán 0 USDT để đốt cháy Nonce của người dùng (Nullifier Griefing).
2. **Recyclable Rent Economics (`reclaim_expired_nullifier`):** Bổ sung hàm đóng tài khoản Nullifier đã hết hạn, hoàn trả 100% lượng SOL Rent-Exempt Reserve về ví người dùng/relayer. Chi phí lưu trữ dài hạn thực tế = $0.0000.
3. **Anti-Rent-Theft Invariant:** Ràng buộc chặt chẽ tài khoản nhận SOL hoàn phí (`rent_receiver`) phải trùng khớp chính xác với `master_owner`. Bất kỳ ai (hoặc MEV bot) cũng có thể gọi hàm dọn rác, nhưng SOL bắt buộc 100% chảy về ví người dùng, ngăn chặn tuyệt đối việc bị bòn rút SOL.
4. **Panic Destination Ownership Invariant:** Ràng buộc tài khoản nhận tiền giải cứu khẩn cấp (`user_safe_destination_ata.owner == master_owner`), ngăn chặn tuyệt đối trường hợp kẻ tấn công hoặc frontend độc hại chuyển hướng tiền rút sang địa chỉ khác.
5. **Double-Spend Replay Immunity (Ephemeral Nullifier PDA):** Mỗi vé thanh toán chứa nonce đơn điệu. Smart contract khởi tạo tài khoản `NullifierRecord` deterministic (`[b"nullifier", vault_pda, nonce]`). Cố gắng phát lại cùng một vé sẽ lập tức dừng lại với lỗi `AccountAlreadyInitialized`.
6. **Direct Vault PDA Authority (Zero-Mismatch CPI):** Loại bỏ hoàn toàn tài khoản signer trung gian. `agent_vault` trực tiếp làm owner của ATA chuyên dụng, đảm bảo hạt giống dẫn xuất PDA (seeds) khớp 100% khi chuyển token SPL.
7. **4-Tuple Bound Capability Leaf (Anti-Front-Running):** Khóa cứng `sub_agent_signer.key()`, `max_amount`, `expiry_slot`, và `nonce` vào lá cây Merkle, ngăn chặn MEV bots hoặc tác tử giả mạo cướp vé thanh toán.
8. **Decoupled Depositor Signer (Automated Fiat On-Ramps):** Cổng nạp tiền từ bên thứ ba (Apple Pay, Stripe, SEPA) có thể nạp thẳng vào vault mà không đòi hỏi khóa riêng tư của Master Owner phải trực tuyến.
9. **Single Composite Merkle Proof (< 1,232-byte IPv6 MTU):** Băm ghép quyền hạn và nhà cung cấp ATA vào một lá Merkle duy nhất giúp thu gọn kích thước gói tin còn ~771 bytes, nằm trọn vẹn trong giới hạn MTU vật lý của mạng Solana.
10. **Historic $800M+ Exploit Fortress:** Xác thực địa chỉ Sysvar Instructions (Wormhole $320M), cấm gốc Merkle 0x0 rỗng (Nomad $190M), reload số dư thực trước khi chi (Euler $197M), và hàng rào cách ly đa slot chống flash loan (Mango $114M).

---

## QUICKSTART GUIDE

### 1. Build Solana Anchor Kernel:
```bash
cargo check
```

### 2. Run Forensic Security Test Suite (15 Test Cases):
```bash
npm test
```

### 3. Deploy Orchestration to Solana Devnet:
```bash
npm run deploy:devnet
```

### 4. Run Live On-Chain Micro-Escrow Simulation (Devnet):
```bash
npm run simulate:devnet
```

### 5. Configure Anthropic Claude Desktop MCP:
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "haichain": {
      "command": "node",
      "args": ["c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js"]
    }
  }
}
```

---
*Developed by the HAICHAIN Global Architecture Taskforce (v6.9.3 Zero-Griefing Standard).*
