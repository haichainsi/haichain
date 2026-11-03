# -*- coding: utf-8 -*-
"""
HAICHAIN Institutional Risk Due Diligence Report - Complete 10-Language Generator & PDF Compiler
Upgraded Layout:
  - Official Haichain White Logo at top
  - Document Title / Tagline positioned harmoniously and balanced DIRECTLY UNDER the Haichain Logo
  - Localized 3-Column Meta Footer for each of the 10 languages
  - Full institutional rigor, mathematical formulas, threat matrix, and 9 invariants across all 10 languages
"""

import os
import sys
import shutil
import re
import base64
import subprocess
import markdown

sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "haichain-official-logo-white.png")

def get_logo_base64():
    if os.path.exists(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

def format_math(text):
    math_blocks = []
    def save_block(m):
        math_blocks.append(m.group(1))
        return f"__MATH_BLOCK_PLACEHOLDER_{len(math_blocks)-1}__"
    text = re.sub(r'\$\$(.*?)\$\$', save_block, text, flags=re.DOTALL)
    
    math_inlines = []
    def save_inline(m):
        math_inlines.append(m.group(1))
        return f"__MATH_INLINE_PLACEHOLDER_{len(math_inlines)-1}__"
    text = re.sub(r'\$([^\$\n]+?)\$', save_inline, text)
    
    for idx, block in enumerate(math_blocks):
        clean_html = latex_to_html(block.strip())
        text = text.replace(f"__MATH_BLOCK_PLACEHOLDER_{idx}__", f'<div class="math-display">{clean_html}</div>')
        
    for idx, inline in enumerate(math_inlines):
        clean_html = latex_to_html(inline.strip())
        text = text.replace(f"__MATH_INLINE_PLACEHOLDER_{idx}__", f'<span class="math-inline">{clean_html}</span>')
        
    return text

def latex_to_html(tex):
    s = tex
    s = re.sub(r'\\mathbf\{([^}]+)\}', r'<b>\1</b>', s)
    s = re.sub(r'\\textbf\{([^}]+)\}', r'<b>\1</b>', s)
    s = re.sub(r'\\text\{([^}]+)\}', r'<span class="math-text">\1</span>', s)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 &frasl; \2)', s)
    s = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'_([a-zA-Z0-9])', r'<sub>\1</sub>', s)
    s = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', s)
    s = re.sub(r'\^([a-zA-Z0-9])', r'<sup>\1</sup>', s)
    s = re.sub(r'\\lceil', r'&lceil;', s)
    s = re.sub(r'\\rceil', r'&rceil;', s)
    s = re.sub(r'\\min', r'min', s)
    s = re.sub(r'\\left\(', r'(', s)
    s = re.sub(r'\\right\)', r')', s)
    s = re.sub(r'\\land', r'&and;', s)
    s = re.sub(r'\\neg', r'&not;', s)
    s = re.sub(r'\\subseteq', r'&sube;', s)
    s = re.sub(r'\\mathcal\{A\}', r'A', s)
    
    symbols = {
        r'\times': '&times;', r'\iff': '&hArr;', r'\implies': '&rArr;', r'\to': '&rarr;',
        r'\leftarrow': '&larr;', r'\forall': '&forall;', r'\exists': '&exist;', r'\ge': '&ge;',
        r'\le': '&le;', r'\ne': '&ne;', r'\approx': '&asymp;', r'\equiv': '&equiv;',
        r'\pm': '&plusmn;', r'\in': '&isin;', r'\cdot': '&middot;', r'\sum': '&sum;',
        r'\prod': '&prod;', r'\Delta': '&Delta;', r'\alpha': '&alpha;', r'\beta': '&beta;',
        r'\gamma': '&gamma;', r'\tau': '&tau;', r'\pi': '&pi;', r'\mu': '&mu;',
        r'\sigma': '&sigma;', r'\epsilon': '&epsilon;', r'\theta': '&theta;', r'\lambda': '&lambda;',
        r'\omega': '&omega;', r'\Omega': '&Omega;', r'\,': ' ', r'\quad': ' &nbsp; ', r'\qquad': ' &nbsp; &nbsp; ', r'\dots': '&hellip;'
    }
    for macro, rep in symbols.items():
        s = s.replace(macro, rep)
    return s

DOCS = {}

# 1. EN - English
DOCS['en'] = {
    'title': 'HAICHAIN: Institutional Risk Due Diligence Report',
    'subtitle': 'Mathematical Proofs, Threat Modeling & Red-Team Verification Matrix for Tier-1 Allocators and Audit Firms',
    'edition': 'Institutional Risk Due Diligence Report v1.1 • Cryptographic Defense Standard',
    'tag': 'HAICHAIN CRYPTOGRAPHIC DEFENSE & PROTOCOL RISK ASSESSMENT',
    'footer': 'CONFIDENTIAL & INSTITUTIONAL • HAICHAIN GLOBAL RISK TASKFORCE',
    'meta_audience_lbl': 'Target Audience',
    'meta_audience_val': 'Tier-1 Venture Allocators & Audit Firms',
    'meta_sec_lbl': 'Cryptographic Security',
    'meta_sec_val': 'Hardware Passkey • 9 Invariants Bound',
    'meta_kern_lbl': 'Protocol Kernel',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 Bytes',
    'md': """# HAICHAIN INSTITUTIONAL RISK DUE DILIGENCE REPORT
## Mathematical Proofs, Threat Modeling & Red-Team Verification Matrix
**Target Audience:** Tier-1 Venture Capitalists (a16z crypto, Paradigm, Sequoia), Institutional Custodians, and Top-Tier Audit Firms (OtterSec, Neodyme, Kudelski Security)  
**Protocol Version:** HAICHAIN Kernel v1.1 / CapLeaf v1 (223 Bytes Wire Schema)  
**Standard:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. EXECUTIVE SUMMARY & SECURITY PARADIGM

Autonomous AI agents executing financial micro-transactions introduce fundamentally distinct attack surfaces from human-operated DeFi:
1. **Zero Human-in-the-Loop Latency:** An AI agent executing tool calls can be coerced via Indirect Prompt Injection into issuing thousands of unauthorized payment vouchers in seconds.
2. **Key Exfiltration Vulnerability:** Running agent instances on distributed worker nodes (Cloudflare Workers, local desktop MCPs, serverless functions) increases the risk of private key exfiltration.
3. **Sybil Counterparty Proliferation:** In an open M2M network, malicious merchants can register unlimited burner domains to bypass domain-based rate limits.

To solve this without sacrificing sub-millisecond execution, **HAICHAIN decouples execution from custody**:
- **Master Authority:** WebAuthn FIDO2 Biometric Hardware Passkey (P-256) retaining 100% sovereign ownership over the spending pot.
- **Sub-Agent Authority:** Ephemeral Ed25519 keypairs strictly sandboxed inside out-of-process Policy Engines with zero access to underlying wallet seeds.
- **On-Chain Merkle Anchor:** 223-byte leaf wire schema enforcing 9 non-malleable mathematical invariants ($I_1 \\dots I_9$).

---

## 2. FORMAL THREAT MODEL & LOSS BOUND FORMULAS

### 2.1. Attack Surface Taxonomy

| Threat Class | Scenario | Conventional Web3 Exposure | HAICHAIN Worst-Case Ceiling |
| :--- | :--- | :--- | :--- |
| **$T_1$ (Indirect Prompt Injection)** | LLM coerced to pay unapproved merchant | Entire wallet drained ($100,000+) | **$E_{\\text{theft}} = 0$** (Blocked by Merkle root whitelist) |
| **$T_2$ (Merchant Collusion)** | Legitimate merchant attempts double-claiming | Double-charge on user account | **$E_{\\text{theft}} = 0$** (Anchor monotonically enforces $P_i \\le \\min(C_i, R_i)$) |
| **$T_3$ (Probation Domain Flood)** | Sub-agent attempts loop drainage on new API | Cumulative exhaustion of pot | **$E_{\\text{theft}} \\le M_{\\text{tpl}}$** (Burned from parent template ceiling) |
| **$T_4$ (Complete Agent Compromise)** | Private key exfiltrated + colluding merchant | Total pot drained immediately | **$E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$** |

---

### 2.2. Theorem 6.1: Upper Bound on Worst-Case Theft ($T_4$)

Let $\\tau$ be the total protocol response latency from the instant an unauthorized transaction is initiated to the instant the on-chain panic freeze transaction lands:
$$\\tau = t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$$
where:
- $t_{\\text{detect}} \\le 5.0\\text{s}$ (telemetry anomaly detection threshold)
- $t_{\\text{owner}} \\le 2.0\\text{s}$ (Passkey one-touch biometric authorization)
- $t_{\\text{land}} \\le 5.0\\text{s}$ (Solana high-priority transaction inclusion)

Under full compromise of the agent's Ed25519 signing key and active collusion with an authenticated merchant in the active Merkle tree, the maximum cumulative theft $E_{\\text{theft}}(\\tau)$ is bounded by:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

Where:
- $B$: Total available pot balance (`pot.balance`).
- $K$: Active leaf cumulative spend ceiling (`leaf.max_spend`).
- $W_p$: Velocity limit per sliding window (`leaf.window_cap`).
- $\\omega_p$: Window duration (typically $3,600\\text{s}$).
- $n(\\tau, \\omega_p) = \\lceil \\tau / \\omega_p \\rceil$: Number of sliding windows spanned during response window $\\tau$. For $\\tau = 12\\text{s} \\ll 3600\\text{s}$, $n(\\tau, \\omega_p) = 1$.
- $\\sum E_i$: Sum of escrow capacities locked across active channels for colluding merchants.

**Corollary:** For an institutional pot with $10,000\\text{ USDT}$ balance, a leaf budget cap of $50\\text{ USDT}$, and a velocity cap of $10\\text{ USDT / hour}$, an attacker compromising the agent's key cannot drain more than **$10\\text{ USDT}$** before the freeze takes effect, preserving **$9,990\\text{ USDT}$ (99.9%)** of capital.

---

## 3. RED-TEAM PENETRATION & HARDENING MATRIX

During the internal red-team forensic audit, 5 critical attack vectors were evaluated and hardened into the protocol kernel:

| # | Attack Vector | Vulnerability Mechanism | Hardened On-Chain Invariant |
|:---:|:---|:---|:---|
| **1** | **Jito MEV Panic Front-Run** | Malicious voucher bundles placed ahead of owner Panic Freeze | **Panic Epoch Tag ($I_6$)**<br>Channel tagged with epoch; instantly invalidated |
| **2** | **Window Straddle Double-Dip** | Splitting reserve across window boundary to draw 2x velocity | **Atomic Epoch Consumption**<br>Reserve strictly burns window capacity in anchor |
| **3** | **Merchant Liquidity Hostage** | Uncooperative merchant leaves unspent channel un-settled | **OwnerForceReclaim ($I_1$)**<br>Zero-claim channels unlocked immediately by master owner |
| **4** | **Rent Lamport Vampire Drain** | Third-party rent-recipient draining rent on channel close | **Canonical Rent Recipient**<br>Rent strictly refunded to original funder (`grant_pot`) |
| **5** | **Indirect Micro-Loop Sybil** | 1,000 child probation leaves draining small micro-reserves | **Template Budget Burn**<br>`activate_child` burns parent `max_reserve` ceiling |

---

## 4. MATHEMATICAL INVARIANTS AUDIT REPORT ($I_1 \\dots I_9$)

Every on-chain instruction in `programs/haichain-core/src/lib.rs` preserves all 9 state invariants without exception:

1. **$I_1$ (Conservation of Capital):**
   $$\\text{Vault}_{\\text{ATA}} + \\sum_{\\text{channels}} \\text{Escrow}_j + \\sum \\text{Paid}_j + \\text{Refunds} = \\text{Net Deposits}$$
   Verified by `test_invariant_i1_conservation` in test suite.

2. **$I_2$ (Canonical Payee Safety):**
   $$\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$$
   Enforced on-chain via Anchor constraint; prevents third-party token account redirection.

3. **$I_3$ (Budget Ceiling):**
   $$\\text{consumed} \\le \\text{max\\_spend} \\quad \\land \\quad \\text{budget\\_used} \\le \\text{budget\\_total}$$
   Checked before every reserve or settlement execution.

4. **$I_4$ (Autonomous Velocity Rate Limiter):**
   $$\\text{window\\_used} \\le \\text{window\\_cap} \\quad \\forall t \\in [T_0, T_0 + \\omega]$$
   Prevents rapid automated capital drainage.

5. **$I_5$ (Monotonic PDA Narrowing):**
   $$\\text{Channel PDA} \\subseteq \\text{Grant PDA} \\subseteq \\text{Pot PDA}$$
   Child instances cannot broaden permissions granted by parent.

6. **$I_6$ (Panic Epoch & Freeze Isolation):**
   $$\\text{pot.panic\\_epoch} == \\text{channel.created\\_at\\_epoch} \\quad \\land \\quad \\neg\\text{pot.frozen}$$
   Instant protocol shutdown completely halts all voucher processing.

7. **$I_7$ (Heartbeat Expiration):**
   $$\\text{current\\_time} \\le \\text{valid\\_until}$$
   Stale or abandoned sessions cannot execute new reserves.

8. **$I_8$ (Monotonic Settlement & Settle-Once):**
   $$\\text{paid}_{\\text{new}} \\le \\min(\\text{cumulative\\_amount}, \\text{reserved\\_amount}) \\quad \\land \\quad \\text{paid}_{\\text{new}} \\ge \\text{paid}_{\\text{old}}$$
   Guarantees zero double-spending across channel vouchers.

9. **$I_9$ (Sybil Account Isolation):**
   $$\\text{PDA}(\\text{"chan"}, \\text{grant}, \\text{channel\\_id}) \\text{ is unique}$$
   One capability leaf maps to exactly one on-chain account.

---

## 5. TOKENOMICS & REGULATORY COMPLIANCE

### 5.1. Zero-Dividend Pure Utility Standard (Howey & MiCA Immune)
- **Zero Passive Staking / Yield:** HAICHAIN has eliminated all forms of passive staking yield or dividends. The protocol offers no profit expectations derived from the entrepreneurial efforts of others.
- **50% Buyback & Burn:** 50% of protocol fees generated from network volume are used to purchase $HAISI on open DEX markets and burn it permanently, creating programmatic deflation directly tied to network utility.
- **50% Protocol Reserve Fund (CHGB):** 50% of protocol fees are directed into the autonomous slashable reserve fund to backstop provider SLAs and guarantee cross-chain liquidity.

### 5.2. Multi-Chain Settlement Capabilities
- **Solana L1 Anchor Kernel:** Native micro-voucher state machine with 223-byte leaf schema, running at 400ms finality.
- **Sui Move Linear Object Model (`AgentCap`):** Linear capability structs with zero `copy` or `drop` primitives, preventing duplicate delegation.
- **Tron TRC20 Rail Solver:** Off-chain intent verification with on-chain Merkle audit trail for low-cost USDT settlements in global emerging markets.

---

## 6. EXTERNAL AUDIT RECOMMENDATIONS & DATA ROOM ACCESS

The external audit package is organized into:
- `/programs/haichain-core/src/lib.rs` (Anchor Rust Kernel v1.1)
- `/programs/haichain-sui/sources/capleaf.move` (Sui Move Package)
- `/sdk/typescript/src/capleaf.ts` (223-Byte LE Wire Schema & Merkle Tree)
- `/sdk/typescript/src/policy-engine.ts` (Zero-Knowledge Key Isolation Sandbox)
- `/tests/` (72 Passing Automated Fuzzing & Invariant Verification Tests)

**Conclusion:** HAICHAIN v1.1 provides the first mathematically proven, hardware-isolated payment layer for autonomous AI agents, setting the benchmark for institutional safety in the agentic economy.
"""
}

# 2. VI - Vietnamese
DOCS['vi'] = {
    'title': 'HAICHAIN: Báo Cáo Thẩm Định Rủi Ro & Phòng Thủ Mật Mã',
    'subtitle': 'Chứng minh Toán học, Mô hình Đe dọa & Ma trận Kiểm thử Xâm nhập Red-Team cho Nhà Đầu tư Thể chế',
    'edition': 'Báo Cáo Thẩm Định Rủi Ro Thể Chế v1.1 • Tiêu Chuẩn Phòng Thủ Mật Mã',
    'tag': 'HAICHAIN BÁO CÁO ĐÁNH GIÁ RỦI RO & PHÒNG THỦ MẬT MÃ TOÀN DIỆN',
    'footer': 'TÀI LIỆU BẢO MẬT & THỂ CHẾ • HAICHAIN GLOBAL RISK TASKFORCE',
    'meta_audience_lbl': 'Đối Tượng Báo Cáo',
    'meta_audience_val': 'Quỹ Mạo Hiểm Hạng 1 & Đơn Vị Kiểm Toán',
    'meta_sec_lbl': 'An Toàn Mật Mã',
    'meta_sec_val': 'Phần Cứng Passkey • Khóa 9 Bất Biến',
    'meta_kern_lbl': 'Nhân Giao Thức',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 Bytes',
    'md': """# BÁO CÁO THẨM ĐỊNH RỦI RO & PHÒNG THỦ MẬT MÃ HAICHAIN
## Chứng minh Toán học, Mô hình Đe dọa & Ma trận Kiểm thử Xâm nhập Red-Team
**Đối tượng mục tiêu:** Các Quỹ đầu tư mạo hiểm Hạng 1 (a16z crypto, Paradigm, Sequoia), Đơn vị Lưu ký Thể chế và Các Công ty Kiểm toán Bảo mật Hàng đầu (OtterSec, Neodyme, Kudelski Security)  
**Phiên bản Giao thức:** HAICHAIN Kernel v1.1 / CapLeaf v1 (Cấu trúc 223 Bytes Wire Schema)  
**Tiêu chuẩn:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. TỔNG QUAN ĐIỀU HÀNH & MÔ HÌNH BẢO MẬT

Các AI Agent tự hành thực hiện thanh toán vi mô tạo ra các bề mặt tấn công hoàn toàn khác biệt so với DeFi do con người thao tác:
1. **Độ trễ Không-có-Con-người-can-thiệp:** Một AI Agent khi thực thi các lệnh gọi công cụ có thể bị cưỡng ép thông qua Tấn công Chèn Lệnh Gián tiếp (Indirect Prompt Injection) để phát hành hàng nghìn chứng từ thanh toán trái phép chỉ trong vài giây.
2. **Lỗ hổng Rò rỉ Khóa Bí mật:** Việc chạy các phiên bản agent trên các nút máy chủ phân tán (Cloudflare Workers, máy tính cục bộ MCP, serverless) làm tăng nguy cơ rò rỉ khóa riêng tư.
3. **Sự bùng nổ Tấn công Mạo danh Sybil:** Trong mạng lưới M2M mở, các bên bán độc hại có thể đăng ký vô hạn tên miền rác để vượt qua các hạn chế tỷ lệ giao dịch theo tên miền.

Để giải quyết triệt để bài toán này mà không hy sinh tốc độ mili-giây, **HAICHAIN tách rời hoàn toàn quyền thực thi khỏi quyền lưu ký vốn**:
- **Quyền Chủ quyền Tối cao:** Khóa sinh trắc học phần cứng FIDO2 WebAuthn Passkey (P-256) giữ 100% quyền sở hữu bất biến đối với kho quỹ chi tiêu.
- **Quyền Hạn của Agent Con:** Các cặp khóa Ed25519 tạm thời (ephemeral) bị cô lập tuyệt đối bên trong Công cụ Chính sách (Policy Engine) ngoài tiến trình, hoàn toàn không có quyền truy cập vào chuỗi hạt giống (seed phrase) của ví gốc.
- **Mỏ neo Merkle Trên Chuỗi:** Cấu trúc CapLeaf 223 byte thực thi 9 bất biến toán học bất khả xâm phạm ($I_1 \\dots I_9$).

---

## 2. MÔ HÌNH ĐE DỌA CHÍNH THỨC & CÔNG THỨC GIỚI HẠN THIỆT HẠI

### 2.1. Phân loại Bề mặt Tấn công

| Phân loại Đe dọa | Kịch bản Tấn công | Mức độ Rủi ro Web3 Truyền thống | Giới hạn Thiệt hại Tối đa của HAICHAIN |
| :--- | :--- | :--- | :--- |
| **$T_1$ (Chèn Lệnh Gián tiếp)** | LLM bị lừa trả tiền cho bên bán chưa cấp phép | Cạn kiệt toàn bộ ví ($100.000+) | **$E_{\\text{theft}} = 0$** (Bị chặn bởi Whitelist gốc Merkle) |
| **$T_2$ (Thông đồng Bên bán)** | Bên bán hợp lệ cố gắng rút tiền 2 lần (double-claim) | Bị trừ tiền kép trên tài khoản | **$E_{\\text{theft}} = 0$** (Anchor bắt buộc $P_i \\le \\min(C_i, R_i)$) |
| **$T_3$ (Tấn công Miền Thử việc)** | Agent con cố xả tiền liên tục vào API mới | Vét cạn dần số dư kho quỹ | **$E_{\\text{theft}} \\le M_{\\text{tpl}}$** (Khóa theo ngân sách trần mẫu cha) |
| **$T_4$ (Agent Bị Chiếm Quyền Hoàn Toàn)** | Khóa riêng bị lộ + thông đồng với bên bán | Toàn bộ quỹ bị rút sạch ngay lập tức | **$E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$** |

---

### 2.2. Định lý 6.1: Giới hạn Trần Thiệt hại Trường hợp Xấu nhất ($T_4$)

Gọi $\\tau$ là tổng thời gian trễ phản hồi của giao thức từ thời điểm một giao dịch trái phép được khởi tạo cho đến khi lệnh ngắt khẩn cấp (Panic Freeze) được ghi nhận thành công trên chuỗi:
$$\\tau = t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$$
Trong đó:
- $t_{\\text{detect}} \\le 5.0\\text{s}$ (ngưỡng phát hiện dị thường đo lường từ xa)
- $t_{\\text{owner}} \\le 2.0\\text{s}$ (thao tác 1 chạm xác thực sinh trắc học Passkey)
- $t_{\\text{land}} \\le 5.0\\text{s}$ (thời gian đưa giao dịch ưu tiên cao vào khối Solana)

Trong kịch bản xấu nhất khi khóa ký Ed25519 của agent bị lộ hoàn toàn và có sự thông đồng với bên bán đã được xác thực trong cây Merkle, tổng thiệt hại tối đa $E_{\\text{theft}}(\\tau)$ bị chặn cứng bởi công thức:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

Trong đó:
- $B$: Tổng số dư khả dụng trong kho quỹ (`pot.balance`).
- $K$: Hạn mức chi tiêu tối đa tích lũy của lá phân quyền (`leaf.max_spend`).
- $W_p$: Giới hạn vận tốc tiêu tiền trên mỗi cửa sổ trượt (`leaf.window_cap`).
- $\\omega_p$: Thời lượng của cửa sổ trượt (mặc định $3.600\\text{s}$).
- $n(\\tau, \\omega_p) = \\lceil \\tau / \\omega_p \\rceil$: Số cửa sổ trượt trải qua trong thời gian phản hồi $\\tau$. Với $\\tau = 12\\text{s} \\ll 3600\\text{s}$, $n(\\tau, \\omega_p) = 1$.
- $\\sum E_i$: Tổng hạn mức ký quỹ đang khóa tại các kênh với các bên bán thông đồng.

**Hệ quả thực tế:** Đối với một kho quỹ thể chế có số dư $10.000\\text{ USDT}$, hạn mức ngân sách lá là $50\\text{ USDT}$, và hạn mức vận tốc là $10\\text{ USDT / giờ}$, kẻ tấn công dù chiếm được khóa của agent cũng **không thể bòn rút quá $10\\text{ USDT}$** trước khi lệnh ngắt khẩn cấp đóng băng toàn bộ quỹ, bảo toàn nguyên vẹn **$9.990\\text{ USDT}$ (99,9%)** tài sản.

---

## 3. MA TRẬN PHÒNG THỦ & KIỂM THỬ XÂM NHẬP RED-TEAM

Trong cuộc kiểm toán điều tra kỹ thuật nội bộ, 5 vector tấn công nghiêm trọng đã được kiểm thử và đóng cứng vào nhân giao thức:

| STT | Vector Tấn công | Cơ chế Khai thác Tiềm ẩn | Biện pháp Khắc phục Cốt lõi |
|:---:|:---|:---|:---|
| **1** | **Rút Tiền Kép Kênh Ký Quỹ**<br>(Channel Escrow Double-Dip) | Bên bán gửi nhiều chứng từ tích lũy để rút vượt hạn mức | **Thanh toán Đơn điệu Không thể Đảo ngược**<br>$P_i \le \min(C, R)$: Khóa cứng mức chi trả tối đa |
| **2** | **Chiếm Đoạt Tài Khoản ATA** | Chuyển hướng thanh toán sang tài khoản Token bên thứ 3 | **Ràng buộc Khắt khe Địa chỉ ATA**<br>Xác thực bất biến PDA trực tiếp trên Solana L1 |
| **3** | **Tấn công Bỏ qua Cầu Dao Khẩn Cấp**<br>(Panic-Bypass) | Kênh cũ tiếp tục rút tiền sau khi chủ sở hữu đã kích hoạt nút Panic | **Cách ly Kỷ nguyên Panic ($I_6$)**<br>Hủy bỏ hiệu lực tức thì toàn bộ chứng từ cũ trong 380ms |
| **4** | **Bòn Rút Lamport Tiền Thuê**<br>(Rent Lamport Vampire) | Bên thứ ba chiếm đoạt lamports tiền thuê khi đóng kênh thanh toán | **Hoàn Trả Tuyệt Đối Tiền Thuê**<br>Tự động hoàn 100% về ví kho quỹ gốc (`grant_pot`) |
| **5** | **Tấn công Sybil Vòng lặp Nhỏ** | Tạo 1.000 nhánh con thử việc để bòn rút các khoản dự trữ vi mô | **Tiêu Hao Ngân Sách Mẫu Cha**<br>`activate_child` đốt trực tiếp trần ngân sách gốc của cha |

---

## 4. BÁO CÁO KIỂM TOÁN 9 BẤT BIẾN TOÁN HỌC ($I_1 \\dots I_9$)

Mọi chỉ thị trên chuỗi trong `programs/haichain-core/src/lib.rs` đều bảo toàn 9 bất biến trạng thái không có ngoại lệ:

1. **$I_1$ (Bảo toàn Vốn Tối cao):**
   $$\\text{Vault}_{\\text{ATA}} + \\sum_{\\text{channels}} \\text{Escrow}_j + \\sum \\text{Paid}_j + \\text{Refunds} = \\text{Tổng Tiền Nạp Ròng}$$
   Được xác thực bởi kiểm thử `test_invariant_i1_conservation`.

2. **$I_2$ (An toàn Người Thụ hưởng Đích thực):**
   $$\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$$
   Thực thi trên chuỗi qua ràng buộc Anchor; triệt tiêu hoàn toàn chuyển hướng tài khoản.

3. **$I_3$ (Hạn mức Ngân sách Bất biến):**
   $$\\text{consumed} \\le \\text{max\\_spend} \\quad \\land \\quad \\text{budget\\_used} \\le \\text{budget\\_total}$$
   Kiểm tra bắt buộc trước mọi thao tác dự trữ hoặc thanh toán.

4. **$I_4$ (Giới hạn Tốc độ Tiêu tiền Tự hành):**
   $$\\text{window\\_used} \\le \\text{window\\_cap} \\quad \\forall t \\in [T_0, T_0 + \\omega]$$
   Ngăn chặn hành vi rút cạn vốn thần tốc tự động.

5. **$I_5$ (Thu hẹp Quyền Hạn Đơn điệu PDA):**
   $$\\text{Channel PDA} \\subseteq \\text{Grant PDA} \\subseteq \\text{Pot PDA}$$
   Các thực thể con không bao giờ có thể mở rộng quyền vượt quá thực thể cha.

6. **$I_6$ (Cách ly Kỷ nguyên Khẩn cấp & Đóng băng Tức thì):**
   $$\\text{pot.panic\\_epoch} == \\text{channel.created\\_at\\_epoch} \\quad \\land \\quad \\neg\\text{pot.frozen}$$
   Đóng băng hệ thống lập tức vô hiệu hóa 100% chứng từ thanh toán đang lưu hành.

7. **$I_7$ (Hạn Khóa Phiên Làm việc Sinh trắc học):**
   $$\\text{current\\_time} \\le \\text{valid\\_until}$$
   Các phiên làm việc hết hạn hoặc bị bỏ rơi không thể thực hiện thêm giao dịch.

8. **$I_8$ (Thanh toán Đơn điệu & Quyết toán Một lần):**
   $$\\text{paid}_{\\text{new}} \\le \\min(\\text{cumulative\\_amount}, \\text{reserved\\_amount}) \\quad \\land \\quad \\text{paid}_{\\text{new}} \\ge \\text{paid}_{\\text{old}}$$
   Đảm bảo tuyệt đối không có gian lận chi tiêu kép giữa các chứng từ.

9. **$I_9$ (Cách ly Tài khoản Chống Tấn công Sybil):**
   $$\\text{PDA}(\\text{"chan"}, \\text{grant}, \\text{channel\\_id}) \\text{ là duy nhất}$$
   Một lá phân quyền tương ứng chính xác với một tài khoản trên chuỗi duy nhất.

---

## 5. MÔ HÌNH TOKENOMICS & TUÂN THỦ PHÁP LÝ

### 5.1. Tiêu chuẩn Tiện ích Thuần túy Không Cổ tức (Miễn nhiễm Howey & MiCA)
- **Không Chia Cổ Tức / Không Staking Thụ Động:** HAICHAIN loại bỏ hoàn toàn mọi hình thức trả lãi thụ động hoặc cam kết lợi nhuận từ công sức của bên thứ ba, đảm bảo tính chất tiện ích thuần túy.
- **50% Phí Mua Lại & Đốt (Buyback & Burn):** 50% doanh thu phí giao thức từ lưu lượng mạng lưới được dùng để mua lại $HAISI trên DEX và đốt vĩnh viễn, tạo áp lực giảm phát gắn liền với mức độ sử dụng thực tế.
- **50% Quỹ Dự trữ Giao thức (CHGB):** 50% phí giao thức được chuyển vào Quỹ dự trữ tự hành có thể bị cắt giảm (slashable reserve) để bảo chứng cam kết chất lượng dịch vụ (SLA) và thanh khoản đa chuỗi.

### 5.2. Khả năng Quyết toán Đa Chuỗi
- **Solana L1 Anchor Kernel:** Máy trạng thái vi chứng từ gốc với cấu trúc 223 byte, đạt tốc độ chốt giao dịch 400ms.
- **Sui Move Linear Object Model (`AgentCap`):** Cấu trúc phân quyền tuyến tính không có hàm `copy` hay `drop`, ngăn chặn sao chép quyền hạn.
- **Tron TRC20 Rail Solver:** Bộ giải ý định ngoài chuỗi kết hợp bằng chứng kiểm toán Merkle trên chuỗi cho các khoản quyết toán USDT chi phí cực thấp tại các thị trường mới nổi.

---

## 6. KHUYẾN NGHỊ KIỂM TOÁN NGOÀI & TRUY CẬP PHÒNG DỮ LIỆU DATA ROOM

Gói tài liệu kiểm toán thể chế bao gồm:
- `/programs/haichain-core/src/lib.rs` (Anchor Rust Kernel v1.1)
- `/programs/haichain-sui/sources/capleaf.move` (Gói Sui Move)
- `/sdk/typescript/src/capleaf.ts` (Cấu trúc 223 Byte & Cây Merkle)
- `/sdk/typescript/src/policy-engine.ts` (Môi trường Cô lập Khóa Zero-Knowledge)
- `/tests/` (72 Kiểm thử Tự động Fuzzing & Xác minh Bất biến đã Passed)

**Kết luận:** HAICHAIN v1.1 cung cấp lớp thanh toán đầu tiên trên thế giới được chứng minh toán học và cô lập bằng phần cứng cho các AI Agent tự hành, thiết lập tiêu chuẩn vàng về an toàn thể chế trong nền kinh tế AI.
"""
}

# 3. ZH - Chinese
DOCS['zh'] = {
    'title': 'HAICHAIN: 机构级风险尽职调查与安全防御报告',
    'subtitle': '面向一线投资机构与顶级审计团队的数学证明、威胁建模与红队安全验证矩阵',
    'edition': '机构级风险尽职调查报告 v1.1 • 密码学安全防御标准',
    'tag': 'HAICHAIN 机构级密码学安全防御与协议风险评估报告',
    'footer': '机密与机构级专用 • HAICHAIN 全球系统风险特别工作组',
    'meta_audience_lbl': '目标受众',
    'meta_audience_val': '一线风险投资机构与顶级审计机构',
    'meta_sec_lbl': '密码学安全标准',
    'meta_sec_val': '硬件 Passkey • 9 大不变性约束',
    'meta_kern_lbl': '协议内核版本',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 字节',
    'md': """# HAICHAIN 机构级风险尽职调查与安全防御报告
## 数学证明、威胁建模与红队安全验证矩阵
**目标受众：** 一线风险投资机构 (a16z crypto, Paradigm, Sequoia)、机构级数字资产托管商及顶级安全审计公司 (OtterSec, Neodyme, Kudelski Security)  
**协议版本：** HAICHAIN Kernel v1.1 / CapLeaf v1 (223 字节线缆协议架构)  
**技术标准：** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. 执行摘要与安全范式

执行微支付的自主 AI Agent 带来了与人类操作 DeFi 本质不同的攻击面：
1. **零人工干预延迟：** 执行工具调用的 AI Agent 可能被间接提示词注入 (Indirect Prompt Injection) 挟持，在数秒内签发成千上万笔未授权支付凭证。
2. **私钥泄露脆弱性：** 在分布式计算节点 (Cloudflare Workers, 本地 MCP, 无服务器函数) 上运行 Agent 会极大地增加私钥泄露风险。
3. **女巫商户无限泛滥：** 在开放的机器对机器 (M2M) 网络中，恶意商户可无限注册一次性域名以规避基于域名的频率限制。

为彻底解决此问题且不牺牲亚毫秒级执行速度，**HAICHAIN 将资金执行权与托管权彻底解耦**：
- **主权最高控制权：** WebAuthn FIDO2 生物识别硬件通行密钥 (Passkey P-256) 对金库保留 100% 绝对所有权。
- **子 Agent 权限隔离：** 临时 Ed25519 密钥对被严格沙箱隔离在跨进程策略引擎 (Policy Engine) 中，完全无法触碰底层钱包助记词。
- **链上 Merkle 锚定：** 223 字节的权限叶节点协议在 Solana L1 上硬性执行 9 大数学不变性 ($I_1 \\dots I_9$)。

---

## 2. 形式化威胁模型与损失上限公理

### 2.1. 攻击面分类矩阵

| 威胁等级 | 攻击场景 | 传统 Web3 暴露风险 | HAICHAIN 最坏情况损失上限 |
| :--- | :--- | :--- | :--- |
| **$T_1$ (间接提示词注入)** | 大模型被诱导向未授权商户付款 | 整个钱包被彻底搬空 ($100,000+) | **$E_{\\text{theft}} = 0$** (受 Merkle 根白名单物理拦截) |
| **$T_2$ (恶意商户共谋)** | 合法商户企图重复结算凭证 | 用户账户发生双重扣款 | **$E_{\\text{theft}} = 0$** (Anchor 单调递增约束 $P_i \\le \\min(C_i, R_i)$) |
| **$T_3$ (试用期域名洪水攻击)** | 子 Agent 试图在不受信新 API 上耗尽资金 | 金库资金逐渐枯竭 | **$E_{\\text{theft}} \\le M_{\\text{tpl}}$** (硬顶受父模板总预算完全锁定) |
| **$T_4$ (Agent 遭遇完全攻陷)** | 私钥泄露 + 与合谋商户联合攻击 | 金库全部资金瞬间被卷走 | **$E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$** |

---

### 2.2. 定理 6.1：最坏情况下资金被盗上限公理 ($T_4$)

设 $\\tau$ 为从发生第一笔未授权交易到链上紧急熔断交易 (Panic Freeze) 成功上链的协议总响应延迟：
$$\\tau = t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$$
其中：
- $t_{\\text{detect}} \\le 5.0\\text{s}$ (遥测指标异常检测阈值)
- $t_{\\text{owner}} \\le 2.0\\text{s}$ (Passkey 一键生物识别确认)
- $t_{\\text{land}} \\le 5.0\\text{s}$ (Solana 高优先级交易确认上链时间)

在 Agent 的 Ed25519 签名私钥被完全攻破且攻击者与 Merkle 树内的有效商户合谋的最极端情况下，最大累积被盗金额 $E_{\\text{theft}}(\\tau)$ 严格受限于：

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

其中：
- $B$: 金库总可用余额 (`pot.balance`)。
- $K$: 当前权限叶节点的累积支出上限 (`leaf.max_spend`)。
- $W_p$: 滑动窗口内的速率上限 (`leaf.window_cap`)。
- $\\omega_p$: 滑动窗口时长 (默认 $3,600\\text{s}$ 即 1 小时)。
- $n(\\tau, \\omega_p) = \\lceil \\tau / \\omega_p \\rceil$: 在响应时间 $\\tau$ 内跨越的滑动窗口数量。由于 $\\tau = 12\\text{s} \\ll 3600\\text{s}$，故 $n(\\tau, \\omega_p) = 1$。
- $\\sum E_i$: 锁定在所有合谋商户通道中的托管额度总和。

**结论推导：** 对于一个拥有 $10,000\\text{ USDT}$ 余额的机构金库，若单叶节点预算设为 $50\\text{ USDT}$，速率上限设为 $10\\text{ USDT / 小时}$，即使黑客完全拿到 Agent 密钥，在熔断生效前**最多只能盗取 $10\\text{ USDT}$**，为机构保全了 **$9,990\\text{ USDT}$ (99.9%)** 的本金安全。

---

## 3. 红队渗透测试与内核加固矩阵

在内部取证审计中，5 大关键攻击向量均已通过渗透测试并在协议内核中获得根本性防御：

| 序号 | 攻击向量 | 传统漏洞机理 | HAICHAIN 核心防御对策 |
|:---:|:---|:---|:---|
| **1** | **通道双重认领攻击** | 商户提交多张历史凭证重复提现 | **单调不可逆结算**<br>$P_i \le \min(C, R)$：硬性锁定最大可支取上限 |
| **2** | **ATA 账户恶意劫持** | 攻击者重定向收款账户至第三方地址 | **严格规范绑定商户 Associated Token**<br>在 Solana L1 强制执行 PDA 不变性验证 |
| **3** | **紧急熔断绕过攻击** | 触发熔断后旧通道仍试图结算凭证 | **纪元隔离与全局时间锁 ($I_6$)**<br>380毫秒内立即使全网历史凭证彻底失效 |
| **4** | **租金 Lamports 吸血鬼攻击** | 第三方关闭通道时盗取账户租金 | **租金严格原路返还**<br>关闭通道时自动全额返还至主出资金库 (`grant_pot`) |
| **5** | **微型循环女巫攻击** | 派生 1,000 个子叶节点蚕食小额资金 | **动态消耗父模板总预算池**<br>`activate_child` 实时扣减父级 `max_reserve` 上限 |

---

## 4. 9 大数学不变性链上审计报告 ($I_1 \\dots I_9$)

`programs/haichain-core/src/lib.rs` 中的所有指令均在链上不可改变地遵循以下 9 大不变性：
1. **$I_1$ (资本守恒定律):** 金库 ATA 余额 + 各通道托管额 + 已付凭证额 + 退款 $\\equiv$ 净充值总额。
2. **$I_2$ (规范收款人安全):** 收款 ATA 账户必须严格等于商户地址由 SPL 规范派生的关联代币账户。
3. **$I_3$ (预算绝不超支):** 实际消耗金额 $\\le$ 最大支出额，且已用预算 $\\le$ 总预算。
4. **$I_4$ (自主速率限流):** 任意滑动窗口内的支出绝对不得超过窗口上限。
5. **$I_5$ (PDA 单调权限收窄):** 派生权限只能逐级缩减，绝无法突破上层限制。
6. **$I_6$ (纪元隔离与即时冻结):** 熔断指令触发后，当前金库下所有存量未结算凭证全部作废。
7. **$I_7$ (心跳会话过期机制):** 会话过期后立即禁止任何新增预留资金。
8. **$I_8$ (单调单次清算):** 新清算金额在预留上限内单调递增，杜绝双花。
9. **$I_9$ (账户防重叠隔离):** 每个能力叶节点严格一对一绑定链上独立 PDA 账户。

---

## 5. 代币经济与全球监管合规

### 5.1. 零分红纯实用型代币标准 (彻底免疫 Howey 测试与欧盟 MiCA)
- **零被动分红与零质押收益：** HAICHAIN 坚决不设任何被动利息或承诺收益，杜绝产生依赖他人经营而获利的证券化预期。
- **50% 协议收入回购与销毁：** 来自网络微支付交易手续费的 50% 直接在公开 DEX 市场回购 $HAISI 并打入黑洞地址永久销毁，形成与真实使用量绑定的程序化通缩。
- **50% 协议安全储备金 (CHGB)：** 50% 手续费注入去中心化惩罚准备金，为网络节点 SLA 与跨链清算提供流动性托底。

### 5.2. 多链清算支持能力
- **Solana L1 Anchor Kernel:** 原生状态机执行，223 字节线缆协议，400ms 极速确认。
- **Sui Move 线性对象模型 (`AgentCap`):** 线性能力结构体，杜绝复制或静默丢弃。
- **Tron TRC20 跨链清算求解器:** 链下意图撮合与链上 Merkle 审计结合，满足新兴市场极低成本结算需求。

---

## 6. 外部审计结论与数据室准入

机构审计材料已在代码库中完备归档：
- `/programs/haichain-core/src/lib.rs` (Anchor Rust Kernel v1.1)
- `/programs/haichain-sui/sources/capleaf.move` (Sui Move 模块)
- `/sdk/typescript/src/capleaf.ts` (223 字节 LE 架构及 Merkle 证明树)
- `/sdk/typescript/src/policy-engine.ts` (零知识密钥隔离沙箱)
- `/tests/` (72 项全绿自动化模糊测试与不变性检验套件)

**结论：** HAICHAIN v1.1 建立了全球首个经过严格数学证明与硬件隔离验证的自主 AI 支付协议层，确立了 AI Agent 经济时代的机构级安全最高标准。
"""
}

# 4. KO - Korean
DOCS['ko'] = {
    'title': 'HAICHAIN: 기관용 위험 실사 및 암호학적 보안 감사 보고서',
    'subtitle': '티어-1 벤처 캐피털과 감사 기관을 위한 수학적 증명, 위협 모델링 및 레드팀 검증 매트릭스',
    'edition': '기관용 위험 실사 보고서 v1.1 • 암호학적 방어 표준',
    'tag': 'HAICHAIN 기관급 암호학 방어 및 프로토콜 리스크 평가 보고서',
    'footer': '기밀 및 기관 전용 • HAICHAIN 글로벌 리스크 태스크포스',
    'meta_audience_lbl': '대상 독자',
    'meta_audience_val': '티어 1 VC 및 기관 감사 기업',
    'meta_sec_lbl': '암호학적 보안 표준',
    'meta_sec_val': '하드웨어 패스키 • 9대 불변성 구속',
    'meta_kern_lbl': '프로토콜 커널',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 바이트',
    'md': """# HAICHAIN 기관용 위험 실사 및 암호학적 보안 감사 보고서
## 수학적 증명, 위협 모델링 및 레드팀 침투 검증 매트릭스
**대상 독자:** 글로벌 티어 1 VC (a16z crypto, Paradigm, Sequoia), 기관 수탁 기관 및 최고 수준 보안 감사 기업 (OtterSec, Neodyme, Kudelski Security)  
**프로토콜 버전:** HAICHAIN Kernel v1.1 / CapLeaf v1 (223 바이트 와이어 스키마)  
**표준:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. 경영진 요약 및 보안 패러다임

금융 소액 결제를 자율적으로 수행하는 AI 에이전트는 인간이 제어하는 DeFi와 본질적으로 다른 공격 표면을 제공합니다:
1. **인간 개입 지연 시간 제로:** 도구 호출을 실행하는 AI 에이전트는 간접 프롬프트 주입(Indirect Prompt Injection)을 통해 수초 내에 수천 개의 무단 지불 바우처를 발행하도록 강제될 수 있습니다.
2. **개인키 유출 취약성:** 분산 워커 노드(Cloudflare Workers, 로컬 데스크톱 MCP, 서버리스)에서 에이전트 인스턴스를 실행하면 개인키 유출 위험이 커집니다.
3. **시빌 카운터파티 범람:** 개방형 M2M 네트워크에서 악의적인 가맹점은 무제한 일회용 도메인을 등록하여 도메인 기반 속도 제한을 우회할 수 있습니다.

밀리초 단위의 초고속 실행을 유지하면서 이 문제를 근본적으로 해결하기 위해 **HAICHAIN은 자금 집행권과 자금 보관권을 완전히 분리**합니다:
- **주권 최고 통제권:** WebAuthn FIDO2 생체 인식 하드웨어 패스키(Passkey P-256)가 금고 자산에 대한 100% 절대적 주권 소유권을 유지합니다.
- **하위 에이전트 권한 격리:** 임시 Ed25519 키 쌍은 프로세스 외부 정책 엔진(Policy Engine) 내에 샌드박스로 완벽하게 격리되며 기본 지갑 시드 문구에 절대 접근할 수 없습니다.
- **온체인 머클 앵커:** 223바이트 리프 스키마는 솔라나 L1 상에서 9가지 수학적 불변성($I_1 \\dots I_9$)을 엄격히 강제합니다.

---

## 2. 형식적 위협 모델 및 손실 한계 공식

### 2.1. 공격 표면 분류 체계

| 위협 등급 | 공격 시나리오 | 기존 Web3 노출 위험 | HAICHAIN 최악의 경우 손실 상한 |
| :--- | :--- | :--- | :--- |
| **$T_1$ (간접 프롬프트 주입)** | LLM이 미승인 가맹점에 자금을 지불하도록 유도됨 | 지갑 전체 자금 탈취 ($100,000+) | **$E_{\\text{theft}} = 0$** (머클 루트 화이트리스트에 의해 원천 차단) |
| **$T_2$ (가맹점 공모 이중 청구)** | 합법 가맹점이 바우처를 중복 정산 시도 | 사용자 계정에서 이중 차감 발생 | **$E_{\\text{theft}} = 0$** (Anchor 단조 증가 강제 $P_i \\le \\min(C_i, R_i)$) |
| **$T_3$ (수습 도메인 루프 공격)** | 하위 에이전트가 신규 API에 자금을 지속 소진 시도 | 금고 잔액이 점진적으로 고갈됨 | **$E_{\\text{theft}} \\le M_{\\text{tpl}}$** (상위 템플릿 총 예산 한도에 의해 잠김) |
| **$T_4$ (에이전트 완전 장악)** | 개인키 유출 + 공모 가맹점과 결탁 공격 | 금고 전체 자금이 즉시 탈취됨 | **$E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$** |

---

### 2.2. 정리 6.1: 최악의 경우 자금 도난 상한 공리 ($T_4$)

$\\tau$를 첫 무단 거래가 개시된 시점부터 온체인 긴급 동결 트랜잭션(Panic Freeze)이 블록체인에 안착할 때까지의 프로토콜 총 응답 지연 시간이라고 정의합니다:
$$\\tau = t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$$
여기서:
- $t_{\\text{detect}} \\le 5.0\\text{s}$ (원격 측정 이상 징후 감지 임계값)
- $t_{\\text{owner}} \\le 2.0\\text{s}$ (패스키 생체 인증 원터치 승인)
- $t_{\\text{land}} \\le 5.0\\text{s}$ (솔라나 고우선순위 트랜잭션 블록 포함 시간)

에이전트의 Ed25519 서명 키가 완전히 유출되고 머클 트리 내 검증된 가맹점과 공모하는 최악의 극단적 상황에서도 최대 누적 도난 금액 $E_{\\text{theft}}(\\tau)$는 수학적으로 완벽히 제한됩니다:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

여기서:
- $B$: 금고 총 가용 잔액 (`pot.balance`).
- $K$: 활성 권한 리프의 누적 지출 한도 (`leaf.max_spend`).
- $W_p$: 슬라이딩 윈도우당 지출 속도 제한 (`leaf.window_cap`).
- $\\omega_p$: 슬라이딩 윈도우 지속 시간 (기본값 $3,600\\text{s}$ = 1시간).
- $n(\\tau, \\omega_p) = \\lceil \\tau / \\omega_p \\rceil$: 응답 시간 $\\tau$ 동안 걸치는 슬라이딩 윈도우 수. $\\tau = 12\\text{s} \\ll 3600\\text{s}$이므로 $n(\\tau, \\omega_p) = 1$.
- $\\sum E_i$: 공모 가맹점 채널에 묶인 에스크로 한도 총합.

**결론 도출:** 잔액 $10,000\\text{ USDT}$의 기관 금고에서 단일 리프 예산이 $50\\text{ USDT}$, 속도 한도가 $10\\text{ USDT / 시간}$으로 설정된 경우, 해커가 에이전트 키를 완벽히 탈취하더라도 동결 발효 전까지 **최대 $10\\text{ USDT}$ 이상 탈취할 수 없으며**, 원금의 **$9,990\\text{ USDT}$ (99.9%)**가 완벽히 보존됩니다.

---

## 3. 레드팀 침투 테스트 및 커널 강화 매트릭스

내부 포렌식 감사에서 5대 주요 공격 벡터가 검증되었으며 프로토콜 커널에서 하드웨어적으로 방어됩니다:

| # | 공격 벡터 | 취약점 메커니즘 | 온체인 핵심 방어 대책 |
|:---:|:---|:---|:---|
| **1** | **채널 에스크로 이중 청구** | 가맹점이 여러 누적 바우처 제출하여 한도 초과 인출 | **단조 비가역 정산**<br>$P_i \le \min(C, R)$: 최대 지출 한도 엄격 잠금 |
| **2** | **ATA 토큰 계정 하이재킹** | 공격자가 수취 계정을 제3자 주소로 임의 변경 | **가맹점 SPL Associated Token 결합**<br>Solana L1에서 PDA 불변성 하드웨어적 강제 |
| **3** | **패닉 동결 우회 공격** | 동결 명령 이후 기존 채널에서 잔여 바우처 정산 시도 | **에포크 격리 및 전역 시간 무효화 ($I_6$)**<br>380ms 내 구형 바우처 즉시 효력 상실 |
| **4** | **임대 Lamport 흡혈 공격** | 채널 종료 시 계정 보관용 임대료 탈취 | **임대료 출자 주 금고로 전액 환불**<br>종료 시 원본 펀딩 풀(`grant_pot`)로 자동 귀속 |
| **5** | **미세 루프 시빌 공격** | 1,000개 수습 리프 생성 후 소액 분할 인출 | **상위 템플릿 총 예산 한도 잠금**<br>`activate_child` 호출 시 상위 `max_reserve` 직접 차감 |

---

## 4. 9대 수학적 불변성 온체인 감사 보고서 ($I_1 \\dots I_9$)

`programs/haichain-core/src/lib.rs`의 모든 온체인 명령어는 다음 9가지 불변성을 영구히 준수합니다:
1. **$I_1$ (자본 보존의 법칙):** 금고 ATA 잔액 + 채널 에스크로 + 정산 완료액 + 환불액 $\\equiv$ 순 예치 총액.
2. **$I_2$ (정규 수취인 안전성):** 수취 ATA는 반드시 가맹점 주소로부터 표준 파생된 계정이어야 함.
3. **$I_3$ (예산 한도 불변성):** 실소진액 $\\le$ 최대 지출 한도 및 기사용 예산 $\\le$ 총 예산.
4. **$I_4$ (자율 속도 제한):** 임의의 슬라이딩 윈도우 내 지출은 윈도우 한도를 절대 초과 불가.
5. **$I_5$ (PDA 권한 단조 축소):** 파생 권한은 상위 권한 범위를 절대 확장할 수 없음.
6. **$I_6$ (패닉 에포크 및 즉시 동결):** 동결 발동 즉시 기존 미정산 바우처 전부 무효화.
7. **$I_7$ (하트비트 세션 만료):** 세션 만료 즉시 신규 자금 예약 차단.
8. **$I_8$ (단조 1회 정산성):** 신규 정산액은 예약 한도 내에서 단조 증가, 이중 지불 방지.
9. **$I_9$ (시빌 계정 격리성):** 각 권한 리프는 온체인 고유 PDA 계정과 1:1 결합.

---

## 5. 토크노믹스 및 글로벌 규제 준수

### 5.1. 무배당 순수 유틸리티 표준 (Howey 및 MiCA 면제)
- **수동 스테이킹 이자 및 배당금 제로:** 타인의 경영 노력에 의존하는 수익 기대를 완전히 배제하여 증권성 규제를 원천 차단합니다.
- **50% 프로토콜 수수료 바이백 및 영구 소각:** 네트워크 소액 결제 수수료의 50%를 공개 시장에서 $HAISI로 바이백하여 영구 소각함으로써 실사용 기반 디플레이션을 구현합니다.
- **50% 프로토콜 준비금 (CHGB):** 50%의 수수료는 노드 SLA 보증 및 크로스체인 정산 유동성을 위해 슬래싱 가능한 자율 준비금으로 유치됩니다.

### 5.2. 멀티체인 정산 지원 능력
- **Solana L1 Anchor Kernel:** 223바이트 리프 스키마, 400ms 초고속 확정성.
- **Sui Move 선형 객체 모델 (`AgentCap`):** 권한 복제 및 폐기를 금지하여 다중 위임 원천 차단.
- **Tron TRC20 레일 솔버:** 신흥 시장을 위한 극저비용 온체인 머클 감사 결합 오프체인 정산.

---

## 6. 외부 감사 권고사항 및 데이터 룸 접근

기관 검토용 감사 패키지는 코드베이스에 완벽히 구축되어 있습니다:
- `/programs/haichain-core/src/lib.rs` (Anchor Rust Kernel v1.1)
- `/programs/haichain-sui/sources/capleaf.move` (Sui Move 패키지)
- `/sdk/typescript/src/capleaf.ts` (223 바이트 스키마 및 머클 트리)
- `/sdk/typescript/src/policy-engine.ts` (영지식 키 격리 샌드박스)
- `/tests/` (72개 자동화 퍼징 및 불변성 검증 통과 테스트)

**결론:** HAICHAIN v1.1은 자율 AI 에이전트를 위해 수학적으로 증명되고 하드웨어로 격리된 세계 최초의 결제 레이어로서 에이전트 경제 시대의 기관급 안전 기준을 수립합니다.
"""
}

# 5. FR - French
DOCS['fr'] = {
    'title': 'HAICHAIN: Rapport de Diligence Raisonnable des Risques Institutionnels',
    'subtitle': 'Preuves Mathématiques, Modélisation des Menaces et Matrice de Vérification Red-Team pour Allocateurs Tier-1',
    'edition': 'Rapport Institutionnel de Risque v1.1 • Norme de Défense Cryptographique',
    'tag': 'HAICHAIN RAPPORT INSTITUTIONNEL D’ÉVALUATION DES RISQUES & DÉFENSE CRYPTOGRAPHIQUE',
    'footer': 'CONFIDENTIEL & INSTITUTIONNEL • TASKFORCE GLOBALE DE RISQUE HAICHAIN',
    'meta_audience_lbl': 'Destinataires',
    'meta_audience_val': 'Fonds Tier-1 & Cabinets d\'Audit',
    'meta_sec_lbl': 'Sécurité Cryptographique',
    'meta_sec_val': 'Passkey Matérielle • 9 Invariants',
    'meta_kern_lbl': 'Noyau Protocole',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 Octets',
    'md': """# RAPPORT DE DILIGENCE RAISONNABLE DES RISQUES INSTITUTIONNELS HAICHAIN
## Preuves Mathématiques, Modélisation des Menaces et Matrice de Vérification Red-Team
**Destinataires :** Fonds de Capital-Risque Tier-1 (a16z crypto, Paradigm, Sequoia), Dépositaires Institutionnels et Cabinets d'Audit de Premier Rang (OtterSec, Neodyme, Kudelski Security)  
**Version du Protocole :** HAICHAIN Kernel v1.1 / CapLeaf v1 (Schéma Wire 223 Octets)  
**Norme Technique :** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Solveur d'Intention Tron Rail

---

## 1. RÉSUMÉ EXÉCUTIF ET PARADIGME DE SÉCURITÉ

Les agents d'IA autonomes exécutant des micro-transactions financières introduisent des surfaces d'attaque fondamentalement différentes de la DeFi humaine :
1. **Zéro Latence Humaine :** Un agent IA exécutant des appels d'outils peut être manipulé par Injection Indirecte de Prompt pour émettre des milliers de bons de paiement illégitimes en quelques secondes.
2. **Vulnérabilité d'Exfiltration de Clés :** L'exécution d'instances d'agents sur des nœuds distribués (Cloudflare Workers, MCP locaux, serverless) accroît considérablement le risque d'exfiltration des clés privées.
3. **Prolifération de Commerçants Sybil :** Dans un réseau M2M ouvert, des commerçants malveillants peuvent enregistrer une infinité de domaines jetables pour contourner les limitations de débit.

Pour résoudre ce défi sans compromettre la rapidité à la milliseconde, **HAICHAIN dissocie entièrement l'exécution financière de la garde des fonds** :
- **Autorité Souveraine Suprême :** La Passkey biométrique matérielle WebAuthn FIDO2 (P-256) conserve 100 % de la propriété inaliénable du coffre.
- **Autorité Isolée des Sous-Agents :** Les paires de clés Ed25519 éphémères sont strictement confinées dans un Moteur de Règles (Policy Engine) hors-processus sans accès à la phrase secrète du portefeuille maître.
- **Ancrage Merkle On-Chain :** Le schéma de feuille de 223 octets applique 9 invariants mathématiques inaltérables ($I_1 \\dots I_9$).

---

## 2. MODÈLE FORMEL DE MENACES ET FORMULES DE LIMITE DE PERTE

### 2.1. Taxonomie de la Surface d'Attaque

| Classe de Menace | Scénario d'Attaque | Risque Web3 Conventionnel | Plafond Pire Cas HAICHAIN |
| :--- | :--- | :--- | :--- |
| **$T_1$ (Injection Indirecte)** | LLM forcé à payer un marchand non approuvé | Portefeuille vidé ($100 000+) | **$E_{\\text{theft}} = 0$** (Bloqué par la whitelist Merkle) |
| **$T_2$ (Collusion Marchande)** | Marchand légitime tentant une double réclamation | Double prélèvement de compte | **$E_{\\text{theft}} = 0$** (Contrainte Anchor $P_i \\le \\min(C_i, R_i)$) |
| **$T_3$ (Attaque Domaine Probation)** | Sous-agent tentant de vider les fonds sur une nouvelle API | Épuisement cumulatif du coffre | **$E_{\\text{theft}} \\le M_{\\text{tpl}}$** (Plafonné au budget du modèle parent) |
| **$T_4$ (Compromission Totale)** | Clé privée compromise + marchand complice | Coffre entièrement vidé sur-le-champ | **$E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$** |

---

### 2.2. Théorème 6.1 : Borne Supérieure du Vol dans le Pire des Cas ($T_4$)

Soit $\\tau$ le temps de réponse total du protocole entre l'émission d'une transaction illicite et l'inscription sur la blockchain du gel d'urgence (Panic Freeze) :
$$\\tau = t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$$
où :
- $t_{\\text{detect}} \\le 5,0\\text{s}$ (seuil de détection des anomalies télémétriques)
- $t_{\\text{owner}} \\le 2,0\\text{s}$ (confirmation biométrique Passkey en 1 clic)
- $t_{\\text{land}} \\le 5,0\\text{s}$ (confirmation haute priorité sur Solana L1)

Même dans l'éventualité la plus grave de compromission intégrale de la clé Ed25519 de l'agent et de collusion active avec un marchand validé dans l'arbre de Merkle, le vol cumulé maximal $E_{\\text{theft}}(\\tau)$ est strictement borné par :

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

Où :
- $B$ : Solde total du coffre (`pot.balance`).
- $K$ : Plafond cumulé de la feuille active (`leaf.max_spend`).
- $W_p$ : Vélocité maximale par fenêtre glissante (`leaf.window_cap`).
- $\\omega_p$ : Durée de la fenêtre (typiquement $3\\,600\\text{s}$ = 1 heure).
- $n(\\tau, \\omega_p) = \\lceil \\tau / \\omega_p \\rceil$ : Nombre de fenêtres traversées pendant $\\tau$. Pour $\\tau = 12\\text{s} \\ll 3600\\text{s}$, $n = 1$.
- $\\sum E_i$ : Somme des montants mis sous séquestre pour les marchands complices.

**Corollaire :** Pour un coffre institutionnel doté de $10\\,000\\text{ USDT}$, avec un budget par feuille de $50\\text{ USDT}$ et une limite de vélocité de $10\\text{ USDT / heure}$, un pirate s'emparant de la clé de l'agent **ne pourra en aucun cas dérober plus de $10\\text{ USDT}$** avant le gel complet, préservant ainsi **$9\\,990\\text{ USDT}$ (99,9 %)** des capitaux.

---

## 3. PÉNÉTRATION RED-TEAM ET MATRICE DE RENFORCEMENT

Cinq vecteurs d'attaque critiques ont été rigoureusement testés et verrouillés dans le noyau :

| # | Vecteur d'Attaque | Mécanisme de Vulnérabilité | Invariant On-Chain Renforcé |
|:---:|:---|:---|:---|
| **1** | **Double Réclamation Escrow** | Soumission de multiples reçus cumulatifs pour dépasser la réserve | **Règlement Monotone Non-Réversible**<br>$P_i \le \min(C_i, R_i)$ : Verrouillage strict du plafond |
| **2** | **Détournement Compte ATA** | Redirection du compte receveur vers un tiers non approuvé | **Liaison Stricte ATA Canonique**<br>Validation cryptographique immuable sur Solana L1 |
| **3** | **Contournement Gel Panic** | Les anciens canaux réclament après activation du Panic Freeze | **Isolation d'Époque Instantanée ($I_6$)**<br>Invalidation immédiate de tous les bons en 380ms |
| **4** | **Drainage Lamport Loyer** | Vol des lamports de loyer lors de la fermeture d'un canal | **Restitution Canonique du Loyer**<br>Remboursement automatique à 100% au trésor (`grant_pot`) |
| **5** | **Attaque Sybil Micro-Boucle** | Création de 1 000 sous-feuilles pour drainer des micro-réserves | **Brûlage du Budget Modèle**<br>`activate_child` déduit directement du plafond père |

---

## 4. RAPPORT D'AUDIT DES 9 INVARIANTS MATHÉMATIQUES ($I_1 \\dots I_9$)

Toutes les instructions de `programs/haichain-core/src/lib.rs` respectent scrupuleusement les 9 invariants mathématiques :
1. **$I_1$ (Conservation du Capital) :** Solde ATA + Escrows + Paiements + Remboursements $\\equiv$ Dépôts Nets.
2. **$I_2$ (Sécurité du Bénéficiaire Canonique) :** Adresse ATA rigoureusement vérifiée sur Solana L1.
3. **$I_3$ (Plafond Budgétaire Inviolable) :** Consommation toujours inférieure ou égale au budget alloué.
4. **$I_4$ (Limitation de Vélocité Autonome) :** Dépenses strictement plafonnées par fenêtre glissante.
5. **$I_5$ (Rétrécissement Monotone PDA) :** Les sous-instances ne peuvent jamais élargir leurs droits.
6. **$I_6$ (Isolation d'Époque et Gel Immédiat) :** Désactivation instantanée de tous les bons en circulation.
7. **$I_7$ (Expiration de Session Heartbeat) :** Arrêt des réservations dès expiration du délai.
8. **$I_8$ (Règlement Unique et Monotone) :** Aucune possibilité de double dépense.
9. **$I_9$ (Isolation de Compte Anti-Sybil) :** Relation 1:1 stricte entre feuille et compte PDA.

---

## 5. MODÈLE ÉCONOMIQUE ET CONFORMITÉ RÉGLEMENTAIRE

### 5.1. Standard d'Utilité Pure Sans Dividende (Immunité Howey & MiCA)
- **Zéro Rendement Passif ni Staking :** Élimination totale de toute promesse de profit dépendant d'efforts tiers.
- **50 % Rachat & Destruction (Buyback & Burn) :** 50 % des frais de protocole sont utilisés pour racheter des $HAISI sur le marché libre et les brûler définitivement.
- **50 % Fonds de Réserve (CHGB) :** 50 % des frais alimentent une réserve de sécurité décentralisée.

### 5.2. Règlement Multi-Chaînes
- **Solana L1 Anchor Kernel :** Finalité en 400 ms avec schéma 223 octets.
- **Sui Move Linear Object Model (`AgentCap`) :** Capacités linéaires sans primitives `copy` ou `drop`.
- **Tron TRC20 Rail Solver :** Règlements à coût quasi-nul pour les marchés émergents.

---

## 6. RECOMMANDATIONS D'AUDIT EXTERNE ET DATA ROOM

Documents d'audit disponibles :
- `/programs/haichain-core/src/lib.rs` (Anchor Rust Kernel v1.1)
- `/programs/haichain-sui/sources/capleaf.move` (Module Sui Move)
- `/sdk/typescript/src/capleaf.ts` (Schéma 223 Octets et Arbre de Merkle)
- `/sdk/typescript/src/policy-engine.ts` (Bac à sable d'isolation à divulgation nulle)
- `/tests/` (72 tests automatisés de fuzzing et d'invariants réussis)

**Conclusion :** HAICHAIN v1.1 fournit la première couche de paiement mathématiquement prouvée et isolée matériellement pour agents IA, établissant la référence de sécurité institutionnelle.
"""
}

# 6. ES - Spanish
DOCS['es'] = {
    'title': 'HAICHAIN: Informe de Diligencia Debida de Riesgos Institucionales',
    'subtitle': 'Demostraciones Matemáticas, Modelado de Amenazas y Matriz de Verificación Red-Team para Asignadores Tier-1',
    'edition': 'Informe de Diligencia Debida de Riesgos v1.1 • Estándar de Defensa Criptográfica',
    'tag': 'HAICHAIN EVALUACIÓN DE RIESGOS INSTITUCIONALES Y DEFENSA CRIPTOGRÁFICA',
    'footer': 'CONFIDENCIAL E INSTITUCIONAL • GRUPO DE TRABAJO GLOBAL DE RIESGO HAICHAIN',
    'meta_audience_lbl': 'Audiencia Objetivo',
    'meta_audience_val': 'Fondos Tier-1 y Firmas Auditoras',
    'meta_sec_lbl': 'Seguridad Criptográfica',
    'meta_sec_val': 'Passkey de Hardware • 9 Invariantes',
    'meta_kern_lbl': 'Núcleo del Protocolo',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 Bytes',
    'md': """# INFORME DE DILIGENCIA DEBIDA DE RIESGOS INSTITUCIONALES DE HAICHAIN
## Demostraciones Matemáticas, Modelado de Amenazas y Matriz de Verificación Red-Team
**Audiencia Objetivo:** Firmas de Capital de Riesgo Tier-1 (a16z crypto, Paradigm, Sequoia), Custodios Institucionales y Firmas Auditoras de Primer Nivel (OtterSec, Neodyme, Kudelski Security)  
**Versión del Protocolo:** HAICHAIN Kernel v1.1 / CapLeaf v1 (Esquema Wire de 223 Bytes)  
**Estándares:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Solver de Intenciones Tron Rail

---

## 1. RESUMEN EJECUTIVO Y PARADIGMA DE SEGURIDAD

Los agentes autónomos de IA que ejecutan microtransacciones financieras presentan vectores de ataque radicalmente distintos a las finanzas descentralizadas tradicionales:
1. **Latencia Cero Sin Intervención Humana:** Un agente de IA que realiza llamadas a herramientas puede verse coaccionado mediante Inyección Indirecta de Prompt para emitir miles de vales de pago no autorizados en segundos.
2. **Vulnerabilidad de Filtración de Claves:** Ejecutar instancias de agentes en nodos distribuidos (Cloudflare Workers, MCPs locales, serverless) multiplica el riesgo de exfiltración de claves privadas.
3. **Proliferación de Comercios Sybil:** En una red M2M abierta, comerciantes maliciosos pueden registrar infinitos dominios desechables para eludir las limitaciones de tasa.

Para neutralizar esta amenaza sin sacrificar la ejecución en milisegundos, **HAICHAIN desvincula por completo la custodia de la ejecución financiera**:
- **Autoridad Soberana Principal:** La llave biométrica de hardware Passkey FIDO2 WebAuthn (P-256) conserva el 100 % de la propiedad inmutable del fondo.
- **Autoridad Aislada de Subagentes:** Los pares de claves Ed25519 efímeros se encuentran estrictamente aislados en un Motor de Políticas fuera de proceso, sin acceso a la frase semilla.
- **Anclaje Merkle en Cadena:** El esquema de hoja de 223 bytes garantiza 9 invariantes matemáticos inmutables ($I_1 \\dots I_9$).

---

## 2. MODELO FORMAL DE AMENAZAS Y FÓRMULAS DE LÍMITE DE PÉRDIDAS

### 2.1. Taxonomía de Superficie de Ataque

| Clase de Amenaza | Escenario | Exposición Web3 Convencional | Límite Peor Caso HAICHAIN |
| :--- | :--- | :--- | :--- |
| **$T_1$ (Inyección Indirecta)** | LLM engañado para pagar a comercio no autorizado | Vaciado total de la billetera ($100,000+) | **$E_{\\text{theft}} = 0$** (Bloqueado por lista blanca Merkle) |
| **$T_2$ (Colusión de Comercio)** | Comercio legítimo intenta liquidar dos veces | Doble cargo en la cuenta de usuario | **$E_{\\text{theft}} = 0$** (Restricción Anchor $P_i \\le \\min(C_i, R_i)$) |
| **$T_3$ (Ataque en Dominio de Prueba)** | Subagente intenta agotar fondos en nueva API | Agotamiento progresivo del fondo | **$E_{\\text{theft}} \\le M_{\\text{tpl}}$** (Bloqueado por presupuesto padre) |
| **$T_4$ (Compromiso Total del Agente)** | Clave privada expuesta + comercio cómplice | Vaciado instantáneo de la totalidad del fondo | **$E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$** |

---

### 2.2. Teorema 6.1: Límite Superior de Robo en el Peor de los Casos ($T_4$)

Sea $\\tau$ la latencia de respuesta total del protocolo desde que se inicia una transacción no autorizada hasta que la orden de congelamiento de emergencia (Panic Freeze) se confirma en cadena:
$$\\tau = t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$$
donde $t_{\\text{detect}} \\le 5.0\\text{s}$, $t_{\\text{owner}} \\le 2.0\\text{s}$, $t_{\\text{land}} \\le 5.0\\text{s}$.

En el escenario extremo de compromiso total de la clave Ed25519 del agente y colusión con un comercio validado en el árbol Merkle, el robo máximo acumulado $E_{\\text{theft}}(\\tau)$ está acotado por:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

**Corolario:** Para un fondo institucional con $10,000\\text{ USDT}$, un tope por hoja de $50\\text{ USDT}$ y un límite de velocidad de $10\\text{ USDT / hora}$, un atacante que comprometa la clave del agente **no podrá sustraer más de $10\\text{ USDT}$** antes de la congelación, preservando el **99.9% ($9,990\\text{ USDT}$)** de los activos.

---

## 3. MATRIZ DE AUDITORÍA Y ENDURECIMIENTO RED-TEAM

Cinco vectores de ataque críticos han sido probados y mitigados en el núcleo:

| # | Vector de Ataque | Mecanismo de Vulnerabilidad | Invariante Endurecido On-Chain |
|:---:|:---|:---|:---|
| **1** | **Doble Reclamación Escrow** | Presentación de múltiples vales acumulativos para exceder reserva | **Liquidación Monótona Inreversible**<br>$P_i \le \min(C_i, R_i)$: Límite de desembolso sellado |
| **2** | **Secuestro de Cuenta ATA** | Redirección de cuenta destino a un tercero malicioso | **Derivación Canónica Estricta**<br>Validación invariable de PDA en Solana L1 |
| **3** | **Evasión de Panic Freeze** | Canales antiguos intentan liquidar tras la activación de emergencia | **Aislamiento de Época Instantáneo ($I_6$)**<br>Invalidación total e inmediata de vales en 380ms |
| **4** | **Drenaje Lamport Alquiler** | Robo de lamports de alquiler al cerrar un canal | **Reembolso Canónico de Alquiler**<br>Retorno forzoso al 100% al fondo original (`grant_pot`) |
| **5** | **Ataque Sybil Micro-Bucles** | Creación de 1.000 sub-hojas para extraer micro-reservas | **Consumo de Presupuesto Padre**<br>`activate_child` descuenta del techo de reserva matriz |

---

## 4. INFORME DE AUDITORÍA DE LOS 9 INVARIANTES MATEMÁTICOS ($I_1 \\dots I_9$)

Todas las instrucciones en `programs/haichain-core/src/lib.rs` satisfacen los 9 invariantes matemáticos:
1. **$I_1$ (Conservación de Capital):** Billetera ATA + Escrow + Liquidado + Reembolsos $\\equiv$ Depósitos Netos.
2. **$I_2$ (Seguridad de Destinatario Canónico):** Cuenta ATA derivada estrictamente del SPL Token.
3. **$I_3$ (Tope Presupuestario Inviolable):** Gasto real siempre inferior o igual al presupuesto total.
4. **$I_4$ (Límite de Velocidad Autónomo):** Tasa de gasto acotada por ventana temporal deslizante.
5. **$I_5$ (Estrechamiento Monótono PDA):** Las sub-instancias no pueden expandir privilegios.
6. **$I_6$ (Aislamiento de Época Panic):** Invalidación inmediata de todos los vales en circulación.
7. **$I_7$ (Expiración de Sesión Heartbeat):** Cese automático de reservas al caducar la sesión.
8. **$I_8$ (Liquidación Monótona Única):** Imposibilidad matemática de doble gasto en canales.
9. **$I_9$ (Aislamiento de Cuenta Anti-Sybil):** Relación 1:1 estricta entre hoja y cuenta PDA on-chain.

---

## 5. TOKENÓMICA Y CUMPLIMIENTO NORMATIVO

- **Cero Dividendos y Cero Rendimiento Pasivo:** Inmunidad absoluta frente a las pruebas de Howey y la normativa europea MiCA.
- **50% Recompra y Quema (Buyback & Burn):** Quema programática de $HAISI financiada por las tarifas de la red.
- **50% Fondo de Reserva del Protocolo (CHGB):** Respaldo para SLAs de proveedores y liquidación multired.

---

## 6. CONCLUSIÓN Y ACCESO A LA SALA DE DATOS (DATA ROOM)

HAICHAIN v1.1 establece la primera infraestructura de pago formalmente demostrada y protegida por hardware para la economía de agentes de IA.
"""
}

# 7. RU - Russian
DOCS['ru'] = {
    'title': 'HAICHAIN: Отчет об Институциональном Дью-Дилидженсе Рисков',
    'subtitle': 'Математические Доказательства, Моделирование Угроз и Матрица Верификации Red-Team для Инвесторов Tier-1',
    'edition': 'Отчет о Рисках Институционального Уровня v1.1 • Стандарт Криптографической Защиты',
    'tag': 'HAICHAIN ИНСТИТУЦИОНАЛЬНЫЙ АУДИТ БЕЗОПАСНОСТИ И ОЦЕНКА РИСКОВ',
    'footer': 'КОНФИДЕНЦИАЛЬНО И ДЛЯ ИНСТИТУЦИОНАЛОВ • ГЛОБАЛЬНАЯ ГРУППА ПО РИСКАМ HAICHAIN',
    'meta_audience_lbl': 'Целевая Аудитория',
    'meta_audience_val': 'Фонды Tier-1 и Аудиторские Компании',
    'meta_sec_lbl': 'Криптографическая Защита',
    'meta_sec_val': 'Аппаратный Passkey • 9 Инвариантов',
    'meta_kern_lbl': 'Ядро Протокола',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 Байта',
    'md': """# ОТЧЕТ ОБ ИНСТИТУЦИОНАЛЬНОМ ДЬЮ-ДИЛИДЖЕНСЕ РИСКОВ HAICHAIN
## Математические Доказательства, Моделирование Угроз и Матрица Верификации Red-Team
**Целевая аудитория:** Венчурные фонды Tier-1 (a16z crypto, Paradigm, Sequoia), институциональные кастодианы и ведущие аудиторские компании (OtterSec, Neodyme, Kudelski Security)  
**Версия протокола:** HAICHAIN Kernel v1.1 / CapLeaf v1 (Сетевая схема 223 байта)  
**Технические стандарты:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. ИСПОЛНИТЕЛЬНОЕ РЕЗЮМЕ И ПАРАДИГМА БЕЗОПАСНОСТИ

Автономные ИИ-агенты, осуществляющие микроплатежи, создают принципиально иные векторы атак по сравнению с традиционными DeFi:
1. **Нулевая задержка без участия человека:** ИИ-агент при выполнении вызовов инструментов может быть скомпрометирован посредством непрямой инъекции промпта (Indirect Prompt Injection) и выпустить тысячи несанкционированных платежных ваучеров за считанные секунды.
2. **Уязвимость утечки закрытых ключей:** Работа экземпляров агентов на распределенных узлах (Cloudflare Workers, локальные MCP, бессерверные функции) увеличивает риск компрометации закрытых ключей.
3. **Размножение мошеннических мерчантов (Sybil):** В открытой сети M2M злоумышленники могут регистрировать неограниченное количество временных доменов для обхода ограничений частоты запросов.

Для полного решения этой задачи без ущерба для субмиллисекундной скорости **HAICHAIN полностью разделяет исполнение платежей и хранение капитала**:
- **Высший суверенный контроль:** Аппаратный биометрический ключ WebAuthn FIDO2 Passkey (P-256) сохраняет 100% суверенное владение пулом средств.
- **Изоляция прав субагентов:** Временные пары ключей Ed25519 строго изолированы в межпроцессном механизме политик (Policy Engine) без доступа к мнемонической фразе кошелька.
- **Ончейн Merkle-якорь:** Схема дескриптора полномочий (223 байта) жестко обеспечивает выполнение 9 математических инвариантов ($I_1 \\dots I_9$).

---

## 2. ФОРМАЛЬНАЯ МОДЕЛЬ УГРОЗ И ОГРАНИЧЕНИЕ УБЫТКОВ

### 2.1. Классификация поверхности атак

| Класс угрозы | Сценарий | Традиционный риск Web3 | Предельные потери в HAICHAIN |
| :--- | :--- | :--- | :--- |
| **$T_1$ (Инъекция промпта)** | LLM принуждают заплатить неавторизованному мерчанту | Полное опустошение кошелька ($100,000+) | **$E_{\\text{theft}} = 0$** (Блокируется белым списком корня Merkle) |
| **$T_2$ (Сговор мерчанта)** | Легитимный мерчант пытается дважды заявить ваучер | Двойное списание с баланса | **$E_{\\text{theft}} = 0$** (Anchor гарантирует $P_i \\le \\min(C_i, R_i)$) |
| **$T_3$ (Атака через новый API)** | Субагент пытается истощить лимит на непроверенном API | Постепенное истощение пула | **$E_{\\text{theft}} \\le M_{\\text{tpl}}$** (Ограничено общим бюджетом шаблона) |
| **$T_4$ (Полный захват агента)** | Утечка ключа + сговор с мерчантом из белого списка | Мгновенный вывод всех средств | **$E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$** |

---

### 2.2. Теорема 6.1: Верхняя граница потерь в худшем сценарии ($T_4$)

Пусть $\\tau$ - общее время отклика протокола от момента первой неавторизованной транзакции до подтверждения транзакции экстренной заморозки (Panic Freeze) в блокчейне:
$$\\tau = t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$$
где $t_{\\text{detect}} \\le 5.0\\text{с}$, $t_{\\text{owner}} \\le 2.0\\text{с}$, $t_{\\text{land}} \\le 5.0\\text{с}$.

Максимальный совокупный ущерб $E_{\\text{theft}}(\\tau)$ математически строго ограничен:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

**Вывод:** Для институционального пула с балансом $10,000\\text{ USDT}$, лимитом на лист $50\\text{ USDT}$ и ограничением скорости $10\\text{ USDT / час}$, злоумышленник, получивший ключ агента, **не сможет похитить более $10\\text{ USDT}$** до срабатывания заморозки, сохраняя **$9,990\\text{ USDT}$ (99.9%)** средств фонда.

---

## 3. МАТРИЦА АППАРАТНОГО УКРЕПЛЕНИЯ RED-TEAM

| № | Вектор Атаки | Механизм Уязвимости | Аппаратный Ончейн Инвариант |
|:---:|:---|:---|:---|
| **1** | **Двойное Списание Эскроу** | Отправка нескольких накопительных ваучеров на сумму выше лимита | **Монотонный Необратимый Расчет**<br>$P_i \le \min(C_i, R_i)$: Аппаратная блокировка перерасхода |
| **2** | **Перехват Аккаунта ATA** | Подмена адреса получателя токенов на посторонний адрес | **Жесткая Каноническая Привязка**<br>Валидация ассоциированного ATA на Solana L1 |
| **3** | **Обход Panic Freeze** | Попытка закрыть канал после активации экстренной заморозки | **Мгновенная Изоляция Эпохи ($I_6$)**<br>Все старые ваучеры аннулируются за 380 мс |
| **4** | **Вампирский Слив Аренды** | Хищение Lamports аренды при закрытии канала | **Возврат Аренды Создателю**<br>Автоматический возврат 100% средств в `grant_pot` |
| **5** | **Sybil-Атака Микро-Циклов** | Создание 1 000 дочерних листьев для распыления баланса | **Сжигание Лимита Шаблона**<br>`activate_child` списывает лимит из родительского пула |

---

## 4. ОТЧЕТ ОБ АУДИТЕ 9 МАТЕМАТИЧЕСКИХ ИНВАРИАНТОВ ($I_1 \\dots I_9$)

Все инструкции в `programs/haichain-core/src/lib.rs` строго соблюдают инварианты:
1. **$I_1$ (Сохранение Капитала):** Баланс ATA + Эскроу + Выплачено + Возвраты $\\equiv$ Чистые Депозиты.
2. **$I_2$ (Безопасность Получателя):** Аккаунт ATA строго равен ассоциированному токен-аккаунту мерчанта.
3. **$I_3$ (Потолок Бюджета):** Фактические расходы строго меньше или равны выделенному бюджету.
4. **$I_4$ (Автономный Скоростной Лимит):** Расход в рамках скользящего окна строго ограничен.
5. **$I_5$ (Монотонное Сужение Прав PDA):** Дочерние инстансы не могут расширять права родителя.
6. **$I_6$ (Изоляция Эпохи Panic Freeze):** Немедленная аннуляция всех обращающихся ваучеров.
7. **$I_7$ (Истечение Сессии Heartbeat):** Запрет новых резервов после окончания таймаута.
8. **$I_8$ (Однократный Расчет):** Исключение любых повторных списаний.
9. **$I_9$ (Изоляция Аккаунтов Sybil):** Каждая способность привязана ровно к одному ончейн PDA.

---

## 5. ТОКЕНОМИКА И РЕГУЛЯТОРНОЕ СООТВЕТСТВИЕ

- **100% Утилитарный стандарт (Иммунитет к Howey и MiCA):** Отсутствие пассивного стейкинга и дивидендов.
- **50% Buyback & Burn:** 50% сетевых сборов направляются на открытый выкуп $HAISI и постоянное сжигание.
- **50% Резервный фонд (CHGB):** Гарантия ликвидности и соблюдения SLA поставщиков.

---

## 6. ЗАКЛЮЧЕНИЕ И ДОСТУП К DATA ROOM

HAICHAIN v1.1 представляет собой первый в мире математически доказанный и аппаратно изолированный платежный уровень для автономных ИИ-агентов.
"""
}

# 8. KK - Kazakh
DOCS['kk'] = {
    'title': 'HAICHAIN: Институционалдық Тәуекелдерді Бағалау Есебі',
    'subtitle': 'Tier-1 Қорлары мен Аудиторлық Компанияларға Арналған Математикалық Дәлелдеулер мен Red-Team Тексеру Матрицасы',
    'edition': 'Институционалдық Тәуекелдерді Бағалау Есебі v1.1 • Криптографиялық Қорғаныс Стандарты',
    'tag': 'HAICHAIN ИНСТИТУЦИОНАЛДЫҚ ТӘУЕКЕЛДЕР МЕН ҚАУІПСІЗДІКТІ БАҒАЛАУ ЕСЕБІ',
    'footer': 'ҚҰПИЯ ЖӘНЕ ИНСТИТУЦИОНАЛДЫҚ • HAICHAIN ЖАҺАНДЫҚ ТӘУЕКЕЛДЕР БОЙЫНША ТОБЫ',
    'meta_audience_lbl': 'Мақсатты Аудитория',
    'meta_audience_val': 'Tier-1 Қорлары мен Аудит Фирмалары',
    'meta_sec_lbl': 'Криптографиялық Қауіпсіздік',
    'meta_sec_val': 'Аппараттық Passkey • 9 Инвариант',
    'meta_kern_lbl': 'Хаттама Ядросы',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 Байт',
    'md': """# HAICHAIN ИНСТИТУЦИОНАЛДЫҚ ТӘУЕКЕЛДЕРДІ БАҒАЛАУ ЖӘНЕ СЕНІМДІЛІК ЕСЕБІ
## Математикалық Дәлелдеулер, Қауіптерді Модельдеу және Red-Team Тексеру Матрицасы
**Мақсатты аудитория:** Tier-1 Венчурлық қорлары (a16z crypto, Paradigm, Sequoia), Институционалдық кастодиандар және жетекші аудит фирмалары (OtterSec, Neodyme, Kudelski Security)  
**Хаттама нұсқасы:** HAICHAIN Kernel v1.1 / CapLeaf v1 (223 Байттық Схема)  
**Стандарт:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. БАСҚАРУШЫЛЫҚ ТҮЙІНДЕМЕ ЖӘНЕ ҚАУІПСІЗДІК ПАРАДИГМАСЫ

Қаржылық микротөлемдерді дербес орындайтын AI Агенттері кәдімгі адам басқаратын DeFi-ден түбегейлі өзгеше қауіп беттерін тудырады:
1. **Адам араласуынсыз нөлдік кідіріс:** Құралдарды шақыратын AI агенті бірнеше секунд ішінде мыңдаған рұқсат етілмеген төлем ваучерлерін шығаруға мәжбүрленуі мүмкін.
2. **Құпия кілттердің сыртқа кету қаупі:** Агент даналарын таратылған түйіндерде іске қосу жеке кілттердің жария болу қаупін күшейтеді.
3. **Sybil жалған сатушыларының көбеюі:** Ашық M2M желісінде қаскүнемдер шектеулерді айналып өту үшін шексіз бір реттік домендерді тіркей алады.

Бұл мәселені миллисекундтық жылдамдықты сақтай отырып толық шешу үшін **HAICHAIN қаржылық орындауды қаражатты сақтау құқығынан түбегейлі ажыратады**:
- **Жоғарғы Егемендік Бақылауы:** WebAuthn FIDO2 биометриялық аппараттық Passkey (P-256) кілті қазынаға 100% мызғымас меншік құқығын сақтайды.
- **Қосалқы агенттердің оқшаулануы:** Ed25519 кілттері негізгі әмиянның сөз тіркесіне қол жеткізе алмайтын Саясат Қозғалтқышында (Policy Engine) оқшауланады.
- **Он-чейн Merkle якоры:** 223 байттық құрылым 9 математикалық инварианттың ($I_1 \\dots I_9$) мызғымас орындалуын талап етеді.

---

## 2. ФОРМАЛЬДЫ ҚАУІП МОДЕЛІ ЖӘНЕ ШЫҒЫНДАРДЫ ШЕКТЕУ

Агенттің Ed25519 кілті толық қолды болған және ақ тізімдегі сатушымен сөз байласқан ең нашар сценарийде де ең жоғарғы ықтимал шығын $E_{\\text{theft}}(\\tau)$ қатаң шектелген:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

**Қорытынды:** $10,000\\text{ USDT}$ қор балансы бар институционалдық қазынада, егер бір жапырақ лимиті $50\\text{ USDT}$, ал жылдамдық шегі $10\\text{ USDT / сағат}$ болса, шабуылдаушы шұғыл бұғаттауға дейін **$10\\text{ USDT}$-дан артық ұрлай алмайды**, бұл қаражаттың **$9,990\\text{ USDT}$ (99.9%)** аман сақталуына кепілдік береді.

---

## 3. ЯДРОНЫ КҮШЕЙТУ ЖӘНЕ 5 ҚАУІПСІЗДІК ТЕТІГІ

1. **Эскроуды Қос Қайтара Алудан Қорғау:** $P_i \\le \\min(C_i, R_i)$ шарты бойынша қайтарымсыз төлем.
2. **ATA Шоттарын Басып Алуға Жол Бермеу:** SPL Associated Token Address-ті қатаң канондық байлау.
3. **Panic Freeze-ді Айналып Өтуді Болдырмау:** Эпоханы жедел оқшаулау ($I_6$).
4. **Жалдау Lamports-тарын Қайтару:** Қаражат автоматты түрде бастапқы қазынаға қайтарылады.
5. **Sybil Микро-Циклдерін Шектеу:** Ата-аналық үлгі шегінен артық шығындалуға жол берілмейді.

---

## 4. 9 МАТЕМАТИКАЛЫҚ ИНВАРИАНТ ($I_1 \\dots I_9$)

Барлық он-чейн нұсқаулықтар 9 математикалық инвариантты ($I_1$ капитал сақталуы, $I_2$ қабылдаушы қауіпсіздігі, $I_3$ бюджет төбесі, $I_4$ автономды жылдамдық, $I_5$ PDA құқықтарының тарылуы, $I_6$ шұғыл эпоха оқшаулануы, $I_7$ сессия мерзімі, $I_8$ қайталанбайтын есеп айырысу, $I_9$ Sybil оқшаулануы) толық сақтайды.

---

## 5. ТОКЕНОМИКА ЖӘНЕ ЗАҢДЫ СӘЙКЕСТІК

- **Таза Утилитарлық Стандарт:** Пассивті табыс пен дивидендтерден ада (Howey және MiCA сынақтарынан толық қорғалған).
- **50% Buyback & Burn:** Желілік комиссиялардың 50%-ы $HAISI токендерін нарықтан сатып алып, мәңгілікке жоюға жұмсалады.
- **50% Сақтық Қоры (CHGB):** Желілік кепілдіктер мен ликвидтілікті қамтамасыз етеді.
"""
}

# 9. HI - Hindi
DOCS['hi'] = {
    'title': 'HAICHAIN: संस्थागत जोखिम देय परिश्रम और सुरक्षा ऑडिट रिपोर्ट',
    'subtitle': 'टियर-1 उद्यम पूंजीपतियों और शीर्ष ऑडिट फर्मों के लिए गणितीय प्रमाण और रेड-टीम सत्यापन मैट्रिक्स',
    'edition': 'संस्थागत जोखिम देय परिश्रम रिपोर्ट v1.1 • क्रिप्टोग्राफिक रक्षा मानक',
    'tag': 'HAICHAIN संस्थागत जोखिम मूल्यांकन और क्रिप्टोग्राफिक रक्षा रिपोर्ट',
    'footer': 'गोपनीय और संस्थागत • HAICHAIN वैश्विक जोखिम कार्यबल',
    'meta_audience_lbl': 'लक्षित दर्शक',
    'meta_audience_val': 'टियर-1 उद्यम पूंजी और ऑडिट फर्म',
    'meta_sec_lbl': 'क्रिप्टोग्राफिक सुरक्षा',
    'meta_sec_val': 'हार्डवेयर पासकी • 9 अपरिवर्तनीय नियम',
    'meta_kern_lbl': 'प्रोटोकॉल कर्नेल',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 बाइट्स',
    'md': """# HAICHAIN संस्थागत जोखिम देय परिश्रम और सुरक्षा ऑडिट रिपोर्ट
## गणितीय प्रमाण, खतरा मॉडलिंग और रेड-टीम सुरक्षा सत्यापन मैट्रिक्स
**लक्ष्य दर्शक:** टियर-1 वेंचर कैपिटलिस्ट (a16z crypto, Paradigm, Sequoia), संस्थागत कस्टोडियन और शीर्ष ऑडिट फर्म (OtterSec, Neodyme, Kudelski Security)  
**प्रोटोकॉल संस्करण:** HAICHAIN Kernel v1.1 / CapLeaf v1 (223 बाइट्स वायर स्कीमा)  
**मानक:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. कार्यकारी सारांश और सुरक्षा प्रतिमान

वित्तीय माइक्रो-भुगतान निष्पादित करने वाले स्वायत्त एआई एजेंट मानव-संचालित डेफी से मौलिक रूप से भिन्न हमले की सतह पेश करते हैं:
1. **शून्य मानवीय हस्तक्षेप विलंबता:** उपकरण कॉल निष्पादित करने वाले एआई एजेंट को अप्रत्यक्ष प्रॉम्प्ट इंजेक्शन (Indirect Prompt Injection) के माध्यम से सेकंडों में हजारों अनधिकृत भुगतान वाउचर जारी करने के लिए मजबूर किया जा सकता है।
2. **निजी कुंजी रिसाव भेद्यता:** वितरित नोड्स पर एजेंट चलाने से निजी कुंजी रिसाव का जोखिम बढ़ जाता है।
3. **सिबिल फर्जी व्यापारियों का प्रसार:** खुले नेटवर्क में, दुर्भावनापूर्ण व्यापारी दर सीमाओं को दरकिनार करने के लिए असीमित अस्थायी डोमेन पंजीकृत कर सकते हैं।

मिलीसेकंड गति का त्याग किए बिना इस समस्या को हल करने के लिए, **HAICHAIN निष्पादन को फंड कस्टडी से पूरी तरह अलग करता है**:
- **सर्वोच्च संप्रभु नियंत्रण:** WebAuthn FIDO2 हार्डवेयर बायोमेट्रिक पासकी (P-256) ट्रेजरी पर 100% पूर्ण स्वामित्व बरकरार रखती है।
- **सब-एजेंट अनुमतियों का अलगाव:** क्षणिक Ed25519 कुंजियाँ नीति इंजन (Policy Engine) में सैंडबॉक्स की गई हैं, जिनकी वॉलेट सीड वाक्यांश तक कोई पहुंच नहीं है।
- **ऑन-चेन मर्कल एंकर:** 223-बाइट स्कीमा सोलाना L1 पर 9 गणितीय अपरिवर्तनीय नियमों ($I_1 \\dots I_9$) को सख्ती से लागू करती है।

---

## 2. औपचारिक खतरा मॉडल और हानि सीमा ($T_4$)

एजेंट की निजी कुंजी से समझौता होने और मर्कल ट्री में व्यापारी के साथ मिलीभगत के सबसे खराब परिदृश्य में भी, अधिकतम चोरी $E_{\\text{theft}}(\\tau)$ गणितीय रूप से सख्ती से सीमित है:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

**व्यावहारिक परिणाम:** $10,000\\text{ USDT}$ बैलेंस वाले संस्थागत फंड के लिए, $50\\text{ USDT}$ लीफ बजट और $10\\text{ USDT / घंटा}$ वेग सीमा के साथ, हमलावर फ्रीज लागू होने से पहले **$10\\text{ USDT}$ से अधिक नहीं चुरा सकता**, जिससे फंड की **$9,990\\text{ USDT}$ (99.9%)** संपत्ति सुरक्षित रहती है।

---

## 3. 5-सूत्रीय रेड-टीम सुदृढ़ीकरण और 9 अपरिवर्तनीय नियम

1. **एस्क्रो दोहरा दावा रोकथाम:** $P_i \\le \\min(C_i, R_i)$ के तहत अपरिवर्तनीय निपटान।
2. **कैनोनिकल ATA खाता सुरक्षा:** तीसरे पक्ष के खातों में रीडायरेक्शन पर पूर्ण रोक।
3. **पैनिक फ्रीज अलगाव ($I_6$):** आपातकालीन फ्रीज के बाद पुराने वाउचर तुरंत अमान्य।
4. **किराया लैम्पॉर्ट्स वापसी:** सभी अप्रयुक्त लैम्पॉर्ट्स मूल फंड में वापस।
5. **सिबिल बजट सीमा:** पैरेंट टेम्पलेट सीमा से अधिक निकासी संभव नहीं।

9 गणितीय नियम ($I_1 \\dots I_9$) पूंजी संरक्षण और सुरक्षा की गारंटी देते हैं।

---

## 4. टोकनॉमिक्स और नियामक अनुपालन

- **शुद्ध उपयोगिता मानक:** कोई निष्क्रिय लाभांश या स्टेकिंग प्रतिफल नहीं (हाउवे और MiCA प्रतिरक्षा)।
- **50% बायबैक और बर्न:** प्रोटोकॉल शुल्क का 50% खुले बाजार से $HAISI खरीदने और नष्ट करने के लिए उपयोग किया जाता है।
- **50% प्रोटोकॉल रिजर्व फंड (CHGB):** नेटवर्क स्थिरता और सुरक्षा के लिए।
"""
}

# 10. HE - Hebrew
DOCS['he'] = {
    'title': 'HAICHAIN: דוח בדיקת נאותות סיכונים מוסדיים',
    'subtitle': 'הוכחות מתמטיות, מידול איומים ומטריצת אימות רד-טים עבור קרנות Tier-1 וחברות ביקורת',
    'edition': 'דוח בדיקת נאותות סיכונים מוסדיים v1.1 • תקן הגנה קריפטוגרפי',
    'tag': 'HAICHAIN דוח הערכת סיכונים מוסדיים והגנה קריפטוגרפית',
    'footer': 'סודי ומוסדי • צוות המשימה הגלובלי לסיכונים של HAICHAIN',
    'meta_audience_lbl': 'קהל יעד',
    'meta_audience_val': 'קרנות מובילות וחברות ביקורת',
    'meta_sec_lbl': 'אבטחה קריפטוגרפית',
    'meta_sec_val': 'מפתח חומרה Passkey • 9 אינווריאנטים',
    'meta_kern_lbl': 'ליבת הפרוטוקול',
    'meta_kern_val': 'HAICHAIN v1.1 • CapLeaf 223 בייטים',
    'md': """# דוח בדיקת נאותות סיכונים מוסדיים ואבטחת קריפטוגרפיה של HAICHAIN
## הוכחות מתמטיות, מידול איומים ומטריצת אימות רד-טים
**קהל יעד:** קרנות הון סיכון מובילות (a16z crypto, Paradigm, Sequoia), גופי משמורת מוסדיים וחברות ביקורת מובילות (OtterSec, Neodyme, Kudelski Security)  
**גרסת פרוטוקול:** HAICHAIN Kernel v1.1 / CapLeaf v1 (סכמת Wire של 223 בייטים)  
**תקנים:** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Tron Rail Intent Solver

---

## 1. תקציר מנהלים ופרדיגמת אבטחה

סוכני בינה מלאכותית אוטונומיים המבצעים מיקרו-תשלומים פיננסיים מציגים משטחי תקיפה שונים מהותית מ-DeFi המופעל על ידי בני אדם:
1. **אפס השהיית מעורבות אנושית:** סוכן AI המבצע קריאות כלים עלול להיחטף באמצעות הזרקת פרומפט עקיפה (Indirect Prompt Injection) ולהנפיק אלפי שוברי תשלום בלתי מורשים בתוך שניות.
2. **פגיעות דליפת מפתחות פרטיים:** הפעלת מופעי סוכנים על גבי צמתים מבוזרים מגבירה את הסיכון לחשיפת מפתחות.
3. **התרבות סוחרים זדוניים (Sybil):** ברשת M2M פתוחה, תוקפים יכולים לרשום דומיינים חד-פעמיים כדי לעקוף מגבלות קצב.

כדי לפתור זאת ללא פגיעה במהירות תת-מילישנייה, **HAICHAIN מפרידה לחלוטין בין ביצוע תשלומים למשמורת הון**:
- **סמכות ריבונית עליונה:** מפתח חומרה ביומטרי WebAuthn FIDO2 Passkey (P-256) שומר על 100% בעלות ריבונית מוחלטת על הקופה.
- **בידוד הרשאות תת-סוכנים:** מפתחות Ed25519 זמניים מבודדים בארגז חול בתוך מנוע המדיניות (Policy Engine) ללא גישה למילות השחזור של הארנק.
- **עוגן מרקל על הבלוקצ'יין:** סכמת עלה של 223 בייטים אוכפת 9 אינווריאנטים מתמטיים ($I_1 \\dots I_9$).

---

## 2. מודל איומים פורמלי ותקרת הפסד ($T_4$)

בתרחיש הקיצון שבו מפתח ה-Ed25519 של הסוכן נחשף במלואו וקיים שיתוף פעולה עם סוחר מאומת בעץ המרקל, סך הגניבה המרבי $E_{\\text{theft}}(\\tau)$ מוגבל באופן מתמטי קשיח:

$$E_{\\text{theft}}(\\tau) \\le \\min\\left(B,\\; K,\\; W_p \\cdot n(\\tau, \\omega_p),\\; \\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)$$

**מסקנה מעשית:** עבור קופה מוסדית עם יתרה של $10,000\\text{ USDT}$, תקרת עלה של $50\\text{ USDT}$ ומגבלת קצב של $10\\text{ USDT / שעה}$, תוקף **לא יוכל לגנוב יותר מ-$10\\text{ USDT}$** לפני כניסת ההקפאה לתוקף, מה שמבטיח הגנה על **$9,990\\text{ USDT}$ (99.9%)** מהקרן.

---

## 3. מטריצת הקשחה ו-9 אינווריאנטים

1. **מניעת תביעה כפולה באסקרו:** פדיון חד-כיווני בלתי הפיך $P_i \\le \\min(C_i, R_i)$.
2. **הגנת חשבון ATA קנוני:** מניעת ניתוב כספים לחשבונות זרים.
3. **בידוד הקפאת פאניקה ($I_6$):** ביטול מיידי של כל השוברים בתפוצה.
4. **השבת דמי שכירות (Lamports):** החזרה מלאה לקופה המקורית.
5. **בלימת מתקפות Sybil:** צריכה קשיחה של תקרת תקציב האב.

כל ההוראות ב-`programs/haichain-core/src/lib.rs` מצייתות ל-9 אינווריאנטים מתמטיים ($I_1 \\dots I_9$).

---

## 4. טוקנומיקה ותאימות רגולטורית

- **תקן שירות טהור ללא דיבידנדים:** חסינות מלאה מפני מבחן Howey ורגולציית MiCA האירופית.
- **50% רכישה חוזרת ושריפה (Buyback & Burn):** 50% מדמי הרשת מופנים לרכישת $HAISI ושריפתו לצמיתות.
- **50% קרן רזרבה אוטונומית (CHGB):** תמיכה ביציבות ורשתות חיסול מרובות.
"""
}

def generate_pdf_for_lang(lang_code):
    import upgrade_risk_reports
    return upgrade_risk_reports.compile_risk_report(lang_code, DOCS[lang_code])

def _legacy_generate_pdf_for_lang(lang_code):
    info = DOCS[lang_code]
    md_filename = f"HAICHAIN_RISK_REPORT_{lang_code.upper()}.md"
    pdf_filename = f"HAICHAIN_RISK_REPORT_{lang_code.upper()}.pdf"
    html_temp = f"HAICHAIN_RISK_REPORT_{lang_code.upper()}_temp.html"
    
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, html_temp)
    
    # Save markdown file
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(info['md'])
    print(f"[+] Wrote markdown: {md_filename}")
    
    # Process text & math
    text_with_math = format_math(info['md'])
    md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    body_html = md_converter.convert(text_with_math)
    
    # Tag Section 3 hardening table with class
    pattern_hardening = re.compile(r"(<table>\s*<thead>\s*<tr>\s*<th[^>]*>\s*(?:#|STT|序号|№|क्र|מס))")
    body_html = pattern_hardening.sub(r'<table class="hardening-matrix-table">\n<thead>\n<tr>\n<th style="text-align: center;">', body_html, count=1)
    
    logo_uri = get_logo_base64()
    is_rtl = (lang_code == 'he')
    direction = "rtl" if is_rtl else "ltr"
    
    full_html = f"""<!DOCTYPE html>
<html lang="{lang_code}" dir="{direction}">
<head>
<meta charset="utf-8">
<title>{info['title']}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

@page {{
  size: A4;
  margin: 22mm 18mm 22mm 18mm;
  @top-left {{
    content: "{info['title']}";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 7pt;
    font-weight: 600;
    letter-spacing: 0.8px;
    color: #71717a;
    text-transform: uppercase;
  }}
  @top-right {{
    content: "haichain.si";
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 500;
    color: #71717a;
  }}
  @bottom-left {{
    content: "{info['footer']}";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 6.5pt;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #a1a1aa;
    text-transform: uppercase;
  }}
  @bottom-right {{
    content: "Page " counter(page);
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 600;
    color: #18181b;
  }}
}}

@page :first {{
  margin: 0;
  @top-left {{ content: none; }}
  @top-right {{ content: none; }}
  @bottom-left {{ content: none; }}
  @bottom-right {{ content: none; }}
}}

body {{
  margin: 0;
  padding: 0;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  color: #18181b;
  background: #ffffff;
  font-size: 9pt;
  line-height: 1.6;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}}

/* Premium Cover Page */
.cover-page {{
  page-break-after: always;
  height: 100vh;
  box-sizing: border-box;
  background: #09090b;
  color: #ffffff;
  padding: 38mm 24mm 28mm 24mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

/* Redesigned Cover Header: Logo on top, Title/Tagline positioned harmoniously and balanced DIRECTLY UNDER the logo */
.cover-header {{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 20mm;
}}

.cover-brand-block {{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}}

.cover-logo {{
  height: 36px;
  width: auto;
  display: block;
}}

.cover-tag {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  font-weight: 600;
  letter-spacing: 1.2px;
  color: #a1a1aa;
  text-transform: uppercase;
  line-height: 1.6;
  max-width: 580px;
}}

.cover-hero {{
  margin-top: auto;
  margin-bottom: auto;
  padding: 16mm 0;
}}

.cover-badge {{
  display: inline-block;
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: 4px;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 22px;
}}

.cover-title {{
  font-size: 26pt;
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.8px;
  color: #ffffff;
  margin: 0 0 16px 0;
}}

.cover-subtitle {{
  font-size: 11pt;
  font-weight: 400;
  line-height: 1.55;
  color: #d4d4d8;
  margin: 0;
  max-width: 90%;
}}

.cover-footer {{
  padding-top: 14mm;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}}

.cover-meta-col {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}

.cover-meta-lbl {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 6.5pt;
  font-weight: 600;
  letter-spacing: 1px;
  color: #71717a;
  text-transform: uppercase;
}}

.cover-meta-val {{
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 8.5pt;
  font-weight: 600;
  color: #ffffff;
}}

/* Body Content Styling */
.body-container {{
  padding: 0;
}}

h1 {{
  font-size: 18pt;
  font-weight: 800;
  line-height: 1.2;
  letter-spacing: -0.5px;
  color: #09090b;
  margin: 0 0 8px 0;
}}

h2 {{
  font-size: 12.5pt;
  font-weight: 700;
  line-height: 1.3;
  color: #09090b;
  margin: 20px 0 10px 0;
  padding-bottom: 4px;
  border-bottom: 1px solid #e4e4e7;
  page-break-after: avoid;
}}

h3 {{
  font-size: 10pt;
  font-weight: 700;
  color: #18181b;
  margin: 16px 0 6px 0;
  page-break-after: avoid;
}}

p {{
  margin: 0 0 10px 0;
  color: #27272a;
}}

strong {{
  font-weight: 700;
  color: #09090b;
}}

/* Institutional Grade Clean Tables */
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0 18px 0;
  font-size: 7.2pt;
  line-height: 1.45;
  page-break-inside: avoid;
  border: 1px solid #e4e4e7;
}}

th {{
  background: #09090b !important;
  color: #ffffff !important;
  font-family: 'JetBrains Mono', monospace;
  font-size: 6.8pt;
  font-weight: 700;
  letter-spacing: 0.6px;
  text-transform: uppercase;
  text-align: left;
  padding: 8px 10px;
  border: 1px solid #27272a;
}}

td {{
  padding: 8px 10px;
  border: 1px solid #e4e4e7;
  color: #27272a;
  vertical-align: top;
  word-wrap: break-word;
  overflow-wrap: break-word;
  box-sizing: border-box;
}}

tr:nth-child(even) td {{
  background: #fafafa;
}}

/* Hardening Matrix (Section 3 Table) */
table.hardening-matrix-table {{
  table-layout: fixed;
}}

table.hardening-matrix-table th:nth-child(1),
table.hardening-matrix-table td:nth-child(1) {{
  width: 32px;
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
}}

table.hardening-matrix-table td:nth-child(2) {{
  width: 25%;
  font-weight: 600;
  color: #09090b;
}}

table.hardening-matrix-table td:nth-child(3) {{
  width: 37%;
  color: #3f3f46;
}}

table.hardening-matrix-table td:nth-child(4) {{
  width: 35%;
  color: #09090b;
}}

/* General / Threat Surface Taxonomy (Section 2.1 Table) */
table:not(.hardening-matrix-table) {{
  table-layout: fixed;
}}

table:not(.hardening-matrix-table) th:nth-child(1),
table:not(.hardening-matrix-table) td:nth-child(1) {{
  width: 18%;
  font-weight: 600;
  color: #09090b;
}}

table:not(.hardening-matrix-table) td:nth-child(2) {{
  width: 26%;
  font-weight: 500;
  color: #09090b;
}}

table:not(.hardening-matrix-table) td:nth-child(3) {{
  width: 28%;
  color: #3f3f46;
}}

table:not(.hardening-matrix-table) td:nth-child(4) {{
  width: 28%;
  color: #09090b;
}}
/* Code Blocks & Matrices */
pre {{
  background: #09090b;
  color: #f4f4f5;
  padding: 10px 12px;
  border-radius: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 6.8pt;
  line-height: 1.35;
  overflow-x: auto;
  margin: 12px 0;
  page-break-inside: avoid;
}}

code {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  background: #f4f4f5;
  padding: 2px 4px;
  border-radius: 3px;
  color: #09090b;
}}

pre code {{
  background: transparent;
  color: inherit;
  padding: 0;
}}

/* Math Blocks */
.math-display {{
  background: #fbfbfb;
  border-left: 3px solid #18181b;
  padding: 8px 12px;
  margin: 10px 0;
  font-family: 'JetBrains Mono', monospace;
  font-size: 8.5pt;
  color: #09090b;
  page-break-inside: avoid;
}}

.math-inline {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  color: #09090b;
  font-weight: 600;
}}

hr {{
  border: 0;
  height: 1px;
  background: #e4e4e7;
  margin: 18px 0;
}}

ul, ol {{
  margin: 0 0 10px 0;
  padding-left: 20px;
}}

li {{
  margin-bottom: 4px;
}}
</style>
</head>
<body>

<!-- Cover Page -->
<div class="cover-page">
  <div class="cover-header">
    <div class="cover-brand-block">
      <img src="{logo_uri}" class="cover-logo" alt="HAICHAIN" />
      <div class="cover-tag">{info['tag']}</div>
    </div>
  </div>
  
  <div class="cover-hero">
    <div class="cover-badge">{info['edition']}</div>
    <div class="cover-title">{info['title']}</div>
    <div class="cover-subtitle">{info['subtitle']}</div>
  </div>
  
  <div class="cover-footer">
    <div class="cover-meta-col">
      <span class="cover-meta-lbl">{info['meta_audience_lbl']}</span>
      <span class="cover-meta-val">{info['meta_audience_val']}</span>
    </div>
    <div class="cover-meta-col">
      <span class="cover-meta-lbl">{info['meta_sec_lbl']}</span>
      <span class="cover-meta-val">{info['meta_sec_val']}</span>
    </div>
    <div class="cover-meta-col">
      <span class="cover-meta-lbl">{info['meta_kern_lbl']}</span>
      <span class="cover-meta-val">{info['meta_kern_val']}</span>
    </div>
  </div>
</div>

<!-- Body Document -->
<div class="body-container">
{body_html}
</div>

</body>
</html>
"""
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if os.path.exists(html_path):
        os.remove(html_path)
        
    if os.path.exists(pdf_path):
        size = os.path.getsize(pdf_path)
        print(f"[✓] Compiled {pdf_filename}: {size:,} bytes")
        app_pdf = os.path.join(WORKSPACE_DIR, "app", pdf_filename)
        shutil.copy2(pdf_path, app_pdf)
        print(f"[✓] Copied to app/{pdf_filename}")
        return True
    else:
        print(f"[✗] Failed to compile {pdf_filename}")
        return False

if __name__ == "__main__":
    print("[*] Starting recompilation of 10 Institutional Risk Reports with balanced logo/tagline layout...")
    langs = ['en', 'vi', 'zh', 'ko', 'fr', 'es', 'ru', 'kk', 'hi', 'he']
    success = []
    for l in langs:
        if generate_pdf_for_lang(l):
            success.append(l)
    print(f"\n[*] Finished: {len(success)}/10 PDFs generated and mirrored to /app/ successfully.")
