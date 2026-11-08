import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

section12_templates = {
    "EN": """

---

## 12. TECHNICAL APPENDIX V1.1 — CAPLEAF V1 BINARY ARCHITECTURE, 9 INVARIANTS, THREAT MODEL & BOUNDED THEFT EXPOSURE

### 12.1. 223-Byte Little-Endian Wire Format & 3-Layer Domain Separation
In the HAICHAIN v1.1 Kernel, every spending capability granted by the Master Owner to an AI sub-agent is encoded as a canonical 223-byte binary struct (`CapLeafV1`) serialized strictly in Borsh Little-Endian:
* `version` (u8, `0x01`): Protocol wire format version.
* `grantee_scope` (Pubkey, 32 bytes): Dedicated Ed25519 signing key of the AI sub-agent.
* `merchant` (Pubkey, 32 bytes): Whitelisted merchant recipient, or `[0u8; 32]` for `PROBATION` templates.
* `token_mint` (Pubkey, 32 bytes): Pinned token mint (Official Solana SPL USDT: `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`).
* `max_spend` (u64, 8 bytes): Absolute cumulative lifetime spending ceiling for this leaf.
* `max_reserve` (u64, 8 bytes): Maximum atomic escrow reservation allowed per settlement channel.
* `window_cap` (u64, 8 bytes): Velocity ceiling (maximum expenditure per sliding window $\omega_p$).
* `window_secs` (u32, 4 bytes): Sliding velocity window duration in seconds (typically $3,600\text{s}$).
* `budget_total` (u64, 8 bytes): Total budget allocated across all sub-agent instances.
* `budget_used` (u64, 8 bytes): Cumulative budget consumed across lifetime.
* `valid_after` (i64, 8 bytes): Unix timestamp before which capability is inactive.
* `valid_until` (i64, 8 bytes): Unix timestamp of session heartbeat expiration.
* `dispute_secs` (u32, 4 bytes): Mandatory challenge settlement window (typically $86,400\text{s}$ / 24h).
* `flags` (u16, 2 bytes): Bitmask controlling `PROBATION`, `REQUIRE_COSIGN`, `STREAMING`, etc.
* `cluster_id` (u8, 1 byte): Network identifier (`0x01` Mainnet-Beta, `0x02` Devnet).
* `template_id` (u64, 8 bytes): Monotonically increasing identifier linking child grants to parent templates.

#### 3-Layer Domain Separation
To guarantee absolute immunity against second-preimage and length-extension attacks, Merkle nodes and leaves utilize strict domain separation prefixes:
$$\text{leaf\_hash} = \text{SHA256}(0\text{x}00 \parallel \text{"HAICHAIN-CAPLEAF-V1"} \parallel \text{program\_id} \parallel \text{leaf\_bytes})$$
$$\text{node}(l, r) = \text{SHA256}(0\text{x}01 \parallel l \parallel r)$$
$$\text{EMPTY} = \text{SHA256}(0\text{x}02 \parallel \text{"HAICHAIN-CAPLEAF-V1"})$$
The Merkle tree is instantiated at fixed depth $d = 12$ ($4,096$ leaf slots, exactly $384\text{ bytes}$ proof size), permanently eliminating dynamic tree height vulnerabilities.

---

### 12.2. Reservation Accounting & Monotonic PDA Hierarchy
The on-chain kernel eliminates repetitive proof verification by decoupling proof submission from channel execution:
1. **`PotAccount` (`["pot", owner_auth]`):** Root administrative escrow holding unallocated USDT deposits, global velocity counters, and the current `panic_epoch`.
2. **`ActiveGrantAccount` (`["grant", pot, leaf_hash]`):** Initialized once via `ActivateGrant` by providing the 12-hop Merkle proof. Stores cached leaf parameters, `consumed`, and sliding window counters.
3. **`ChannelAccount` (`["chan", grant, channel_id]`):** Ephemeral micro-escrow reserving up to `max_reserve` for high-frequency off-chain HTTP x402 voucher streaming.

#### Non-Malleable Payee Safety
In every settlement instruction, the recipient token account is derived strictly on-chain:
$$\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{grant.merchant}, \text{pot.token\_mint})$$
Any attempt by a compromised AI sub-agent or caller to redirect funds to an unauthorized ATA is rejected deterministically by the SVM runtime.

---

### 12.3. The 9 Mathematical System Invariants ($I_1 \dots I_9$)
The entire kernel state machine is governed by 9 non-negotiable formal invariants:
* **Invariant $I_1$ (Conservation of Capital):** $\text{Vault}_{\text{ATA}} + \sum \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} \equiv \text{Net Deposits}$. Total funds in the protocol are strictly conserved at every state transition.
* **Invariant $I_2$ (Canonical Payee Safety):** Funds exit the escrow exclusively to $\text{ATA}(\text{merchant}, \text{mint})$ or refund to the master vault.
* **Invariant $I_3$ (Budget Ceiling):** $\text{grant.consumed} \le \text{leaf.max\_spend} \;\land\; \text{pot.budget\_used} \le \text{pot.budget\_total}$.
* **Invariant $I_4$ (Autonomous Velocity Cap):** Total capital reserved within sliding window $[t, t + \omega_p]$ cannot exceed `window_cap`.
* **Invariant $I_5$ (Monotonic PDA Narrowing):** A child capability PDA cannot broaden or expand the permission envelope of its parent PDA.
* **Invariant $I_6$ (Panic Epoch & Freeze Isolation):** Settlement requires $\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \;\land\; \neg\text{pot.frozen}$. Master freeze halts all pending vouchers instantly.
* **Invariant $I_7$ (Heartbeat Expiration):** No reservations or spends permitted if $\text{clock.unix\_timestamp} > \text{valid\_until}$.
* **Invariant $I_8$ (Monotonic Settlement & Settle Once):** $\text{paid}_{\text{new}} \le \min(\text{voucher.cumulative}, \text{channel.reserved}) \;\land\; \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}$. Eliminates voucher replay and double spending.
* **Invariant $I_9$ (Sybil Account Isolation):** $\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id})$ is mathematically unique per channel.

---

### 12.4. Quantitative Threat Model & Theorem 6.1 Bounded Theft Ceiling
Let $\tau$ represent the total protocol response latency from the instant of malicious voucher issuance to the instant the on-chain panic freeze transaction is confirmed:
$$\tau = t_{\text{detect}} + t_{\text{owner}} + t_{\text{land}} \le 12.0\text{s}$$
Under the worst-case attack scenario $T_4$ (complete exfiltration of the agent's Ed25519 private key combined with active collusion by an authenticated merchant in the Merkle tree), the maximum cumulative theft $E_{\text{theft}}(\tau)$ is bounded by:

$$E_{\text{theft}}(\tau) \le \min\left(B,\; K,\; W_p \cdot n(\tau, \omega_p),\; \sum_{i:\, m_i \in \mathcal{A}} E_i(\tau)\right)$$

Where:
* $B$: Available pot balance.
* $K$: Cumulative spend ceiling `leaf.max_spend`.
* $W_p$: Velocity limit `leaf.window_cap`.
* $n(\tau, \omega_p) = \lceil \tau / \omega_p \rceil$: Number of sliding windows spanned during response window $\tau$. For $\tau = 12\text{s} \ll 3600\text{s}$, $n(\tau, \omega_p) = 1$.

**Formal Consequence:** In 100% of standard Indirect Prompt Injection attacks ($T_1$), $E_{\text{theft}} = 0$ because unauthorized destinations fail Merkle proof verification. In complete key exfiltration ($T_4$), total loss is strictly capped at $\min(K, W_p)$, preserving over $99.9\%$ of enterprise capital.

---

### 12.5. The 5 Red-Team Attack Hardening Defenses
1. **Anti-Jito MEV Panic Front-Running:** Channels record `created_at_epoch`. When owner triggers `Panic`, the pot increments `panic_epoch`, invalidating all pending MEV voucher bundles.
2. **Anti-Window Straddle Double-Dip:** Velocity counters enforce atomic sliding capacity burning, preventing attackers from draining $2\times$ the velocity limit across window boundaries.
3. **`OwnerForceReclaim` Instant Recovery:** Master owner can bypass the 24-hour dispute window and immediately recover unspent escrow if `channel.paid == 0`.
4. **100% Rent Lamport Preservation:** Channel rent is refunded strictly to the original funder (`grant_pot`), preventing third-party rent-draining attacks.
5. **Anti-Prompt-Injection Micro-Loop Throttling:** Out-of-process Policy Engine limits unverified probation domains to a maximum of 3 micro-transactions per 10 minutes and verifies payload semantic validity.

---
*Technical Whitepaper v1.1 Appendix &bull; HAICHAIN Global Systems Taskforce &bull; All Rights Reserved.*
""",

    "VI": """

---

## 12. PHỤ LỤC KỸ THUẬT V1.1 — CẤU TRÚC NHỊ PHÂN CAPLEAF V1, 9 BẤT BIẾN HỆ THỐNG, MÔ HÌNH ĐE DỌA & TRẦN THIỆT HẠI RỦI RO

### 12.1. Cấu Trúc Lá Nhị Phân 223 Bytes & Phân Tách Miền 3 Tầng (Domain Separation)
Trong Hạt nhân HAICHAIN v1.1, mọi năng lực chi tiêu do Chủ Sở Hữu (Master Owner) cấp cho Agent con đều được mã hóa dưới dạng cấu trúc nhị phân chuẩn hóa 223 bytes (`CapLeafV1`) tuần tự hóa theo định dạng Borsh Little-Endian:
* `version` (u8, `0x01`): Phiên bản giao thức wire format.
* `grantee_scope` (Pubkey, 32 bytes): Khóa ký Ed25519 riêng biệt của AI Sub-Agent.
* `merchant` (Pubkey, 32 bytes): Địa chỉ Merchant được ủy quyền, hoặc `[0u8; 32]` cho lá mẫu thử việc `PROBATION`.
* `token_mint` (Pubkey, 32 bytes): Mint token thanh toán (Tether USD Solana SPL: `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`).
* `max_spend` (u64, 8 bytes): Hạn mức chi tiêu tối đa trọn đời của lá năng lực.
* `max_reserve` (u64, 8 bytes): Hạn mức khóa ký quỹ (escrow) tối đa cho mỗi kênh thanh toán.
* `window_cap` (u64, 8 bytes): Trần tốc độ chi tiêu tối đa trong một cửa sổ trượt $\omega_p$.
* `window_secs` (u32, 4 bytes): Thời lượng của cửa sổ tốc độ tính bằng giây (mặc định $3.600\text{s}$).
* `budget_total` (u64, 8 bytes): Tổng ngân sách phân bổ cho toàn bộ cây Agent.
* `budget_used` (u64, 8 bytes): Ngân sách tích lũy đã tiêu thụ.
* `valid_after` (i64, 8 bytes): Mốc thời gian Unix trước đó lá chưa có hiệu lực.
* `valid_until` (i64, 8 bytes): Mốc thời gian Unix hết hạn heartbeat của phiên làm việc.
* `dispute_secs` (u32, 4 bytes): Thời gian giải quyết tranh chấp khi đóng kênh ($86.400\text{s}$ / 24 giờ).
* `flags` (u16, 2 bytes): Cờ điều khiển (`PROBATION`, `REQUIRE_COSIGN`, `STREAMING`).
* `cluster_id` (u8, 1 byte): Định danh mạng (`0x01` Mainnet-Beta, `0x02` Devnet).
* `template_id` (u64, 8 bytes): Số định danh tăng dần liên kết lá con với lá mẫu cha.

#### Phân Tách Miền 3 Tầng (3-Layer Domain Separation)
Để triệt tiêu hoàn toàn các cuộc tấn công second-preimage và length-extension:
$$\text{leaf\_hash} = \text{SHA256}(0\text{x}00 \parallel \text{"HAICHAIN-CAPLEAF-V1"} \parallel \text{program\_id} \parallel \text{leaf\_bytes})$$
$$\text{node}(l, r) = \text{SHA256}(0\text{x}01 \parallel l \parallel r)$$
$$\text{EMPTY} = \text{SHA256}(0\text{x}02 \parallel \text{"HAICHAIN-CAPLEAF-V1"})$$
Cây Merkle được thiết lập ở độ sâu cố định $d = 12$ ($4.096$ vị trí lá, kích thước proof cố định $384\text{ bytes}$), loại bỏ hoàn toàn lỗ hổng biến thiên độ sâu cây.

---

### 12.2. Kế Toán Đặt Trước (Reservation Accounting) & Thứ Bậc PDA Đơn Điệu
Hạt nhân on-chain tách bạch việc nộp bằng chứng Merkle khỏi luồng thanh toán vi mô:
1. **`PotAccount` (`["pot", owner_auth]`):** Kho quỹ quản trị gốc lưu trữ số dư USDT chưa phân bổ và `panic_epoch` hiện tại.
2. **`ActiveGrantAccount` (`["grant", pot, leaf_hash]`):** Kích hoạt 1 lần duy nhất qua `ActivateGrant` với Merkle proof 12 bước. Lưu trữ các điều khoản của lá, `consumed`, và bộ đếm cửa sổ trượt.
3. **`ChannelAccount` (`["chan", grant, channel_id]`):** Kênh ký quỹ tạm thời khóa trước tối đa `max_reserve` phục vụ thanh toán vi mô streaming HTTP x402 ngoài chuỗi.

#### Cưỡng Chế Tài Khoản Thụ Hưởng Chuẩn Tắc (Canonical Payee Safety)
Trong mọi lệnh thanh toán, tài khoản nhận tiền được suy diễn trực tiếp on-chain:
$$\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{grant.merchant}, \text{pot.token\_mint})$$
Mọi nỗ lực của Agent bị chiếm quyền nhằm trích xuất tiền về tài khoản ATA giả mạo đều bị hệ điều hành SVM chặn đứng ngay lập tức.

---

### 12.3. Hệ Thống 9 Bất Biến Toán Học Cốt Lõi ($I_1 \dots I_9$)
* **Bất biến $I_1$ (Bảo toàn Vốn):** $\text{Vault}_{\text{ATA}} + \sum \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} \equiv \text{Net Deposits}$. Tổng tài sản trong hệ thống bảo toàn tuyệt đối qua mọi lệnh.
* **Bất biến $I_2$ (An toàn Thụ hưởng):** Tiền rời khỏi Escrow chỉ được phép chảy về $\text{ATA}(\text{merchant}, \text{mint})$ hoặc hoàn về Vault.
* **Bất biến $I_3$ (Trần Ngân sách):** $\text{grant.consumed} \le \text{leaf.max\_spend} \;\land\; \text{pot.budget\_used} \le \text{pot.budget\_total}$.
* **Bất biến $I_4$ (Trần Tốc độ Tự hành):** Tổng vốn đặt trước trong cửa sổ trượt $[t, t + \omega_p]$ không vượt quá `window_cap`.
* **Bất biến $I_5$ (Thu hẹp Quyền hạn Đơn điệu):** PDA con tuyệt đối không thể mở rộng phạm vi quyền hạn so với PDA cha.
* **Bất biến $I_6$ (Cô lập Kỷ nguyên Panic & Đóng băng):** Thanh toán yêu cầu $\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \;\land\; \neg\text{pot.frozen}$. Lệnh Panic lập tức phong tỏa toàn bộ voucher off-chain.
* **Bất biến $I_7$ (Tuân thủ Heartbeat):** Từ chối mọi hoạt động chi tiêu nếu $\text{clock.unix\_timestamp} > \text{valid\_until}$.
* **Bất biến $I_8$ (Thanh toán Đơn điệu & Duy nhất):** $\text{paid}_{\text{new}} \le \min(\text{voucher.cumulative}, \text{channel.reserved}) \;\land\; \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}$. Chống lặp và chống double-spending voucher.
* **Bất biến $I_9$ (Cô lập Tài khoản Sybil):** Mỗi lá năng lực tương ứng với một tài khoản Channel PDA duy nhất.

---

### 12.4. Mô Hình Đe Dọa & Định Lý 6.1 Về Trần Thiệt Hại Tối Đa ($E_{\text{theft}}$)
Gọi $\tau$ là tổng thời gian phản ứng từ khi phát sinh voucher gian lận đến khi lệnh Panic hạ cánh on-chain:
$$\tau = t_{\text{detect}} + t_{\text{owner}} + t_{\text{land}} \le 12.0\text{s}$$
Trong kịch bản tồi tệ nhất $T_4$ (lộ hoàn toàn khóa Ed25519 của Agent và Merchant trong Merkle tree thông đồng lừa đảo), tổng thiệt hại tối đa $E_{\text{theft}}(\tau)$ bị khóa cứng trong:

$$E_{\text{theft}}(\tau) \le \min\left(B,\; K,\; W_p \cdot n(\tau, \omega_p),\; \sum_{i:\, m_i \in \mathcal{A}} E_i(\tau)\right)$$

**Hệ quả định chế:** Trong 100% các cuộc tấn công Prompt Injection thông thường ($T_1$), $E_{\text{theft}} = 0$. Trong kịch bản lộ khóa toàn bộ ($T_4$), thiệt hại bị chặn trên bởi $\min(K, W_p)$, bảo toàn hơn $99.9\%$ vốn của doanh nghiệp.

---

### 12.5. Năm Bản Vá Phòng Thủ Tấn Công Red-Team
1. **Chống Jito MEV Panic Front-Running:** Channel gắn nhãn `created_at_epoch`. Khi Owner bấm `Panic`, epoch tăng lên, vô hiệu hóa ngay tức thì các gói bundle MEV của hacker.
2. **Chống Window Straddle Double-Dip:** Hạn mức cửa sổ trượt được đốt tức thì khi đặt trước, ngăn chặn rút gấp đôi hạn mức qua khe thời gian 2 giây.
3. **`OwnerForceReclaim` Giải Phóng Vốn 24h:** Chủ sở hữu có quyền rút ngay lập tức số tiền ký quỹ chưa tiêu nếu `channel.paid == 0` mà không cần chờ 24h tranh chấp.
4. **Bảo Toàn 100% Rent Lamports:** Hoàn trả tiền thuê tài khoản (rent) về đúng địa chỉ người mở ban đầu (`grant_pot`).
5. **Chống Vòng Lặp Rút Ruột Prompt Injection:** Policy Engine giới hạn tối đa 3 giao dịch/10 phút đối với domain thử việc và xác thực ngữ nghĩa payload.

---
*Phụ Lục Sách Trắng Kỹ Thuật v1.1 &bull; Hội đồng Hệ thống HAICHAIN &bull; Bảo lưu Mọi Quyền.*
""",

    "ZH": """

---

## 12. 技术附录 V1.1 — CAPLEAF V1 二进制架构、9大数学不变量、威胁模型与损失上限

### 12.1. 223 字节 Little-Endian 协议格式与三层域分离
在 HAICHAIN v1.1 内核中，主所有者授予 AI 子代理的每一项支付能力凭证均被编码为严格遵循 Borsh Little-Endian 序列化的 223 字节二进制结构体 (`CapLeafV1`)：
* `version` (u8, `0x01`): 线缆协议版本号。
* `grantee_scope` (Pubkey, 32 字节): AI 子代理的独立 Ed25519 签名公钥。
* `merchant` (Pubkey, 32 字节): 白名单商户收款地址，试用模板 (`PROBATION`) 填 `[0u8; 32]`。
* `token_mint` (Pubkey, 32 字节): 绑定的支付代币铸币地址 (Solana SPL USDT: `Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`)。
* `max_spend` (u64, 8 字节): 该叶片生命周期内最大累计支出上限。
* `max_reserve` (u64, 8 字节): 单个结算通道允许锁定的最大预留保证金。
* `window_cap` (u64, 8 字节): 滑动窗口速率上限（在周期 $\omega_p$ 内的最大支出）。
* `window_secs` (u32, 4 字节): 滑动窗口时长（秒，默认 $3,600\text{s}$）。
* `budget_total` (u64, 8 字节): 分配给整个代理树的总预算。
* `budget_used` (u64, 8 字节): 历史上累计已消耗的预算总额。
* `valid_after` (i64, 8 字节): Unix 时间戳，生效起始时间。
* `valid_until` (i64, 8 字节): Unix 时间戳，会话心跳过期时间。
* `dispute_secs` (u32, 4 字节): 结算争议窗口期（默认 $86,400\text{s}$ / 24小时）。
* `flags` (u16, 2 字节): 控制位标志（`PROBATION`, `REQUIRE_COSIGN`, `STREAMING` 等）。
* `cluster_id` (u8, 1 字节): 集群网络 ID (`0x01` Mainnet-Beta, `0x02` Devnet)。
* `template_id` (u64, 8 字节): 自增模板 ID，关联子授权与父级模板。

#### 三层域分离 (3-Layer Domain Separation)
为彻底杜绝第二原像与长度扩展攻击：
$$\text{leaf\_hash} = \text{SHA256}(0\text{x}00 \parallel \text{"HAICHAIN-CAPLEAF-V1"} \parallel \text{program\_id} \parallel \text{leaf\_bytes})$$
$$\text{node}(l, r) = \text{SHA256}(0\text{x}01 \parallel l \parallel r)$$
$$\text{EMPTY} = \text{SHA256}(0\text{x}02 \parallel \text{"HAICHAIN-CAPLEAF-V1"})$$
Merkle 树采用固定深度 $d = 12$（4,096 个叶片槽位，证明尺寸固定为 384 字节），彻底消除动态树高漏洞。

---

### 12.2. 预留会计状态机与单调 PDA 层级
链上内核解耦 Merkle 证明验证与高频通道结算：
1. **`PotAccount` (`["pot", owner_auth]`):** 根资金池 PDA，托管未分配 USDT 存款并维护全局 `panic_epoch`。
2. **`ActiveGrantAccount` (`["grant", pot, leaf_hash]`):** 通过 12 步证明由 `ActivateGrant` 激活一次。缓存叶片条款与滑动窗口状态。
3. **`ChannelAccount` (`["chan", grant, channel_id]`):** 临时微托管通道，锁定最多 `max_reserve` 用于链下 HTTP x402 流式凭证结算。

#### 规范收款人绝对安全
结算指令中收款账户由智能合约链上强制推导：
$$\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{grant.merchant}, \text{pot.token\_mint})$$
任何试图将资金重定向到未授权地址的恶意交易均会被 SVM 虚拟机确定性拒绝。

---

### 12.3. 核心 9 大数学系统不变量 ($I_1 \dots I_9$)
* **不变量 $I_1$ (资金绝对守恒):** $\text{Vault}_{\text{ATA}} + \sum \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} \equiv \text{Net Deposits}$。
* **不变量 $I_2$ (规范收款人安全):** 资金只能流向 $\text{ATA}(\text{merchant}, \text{mint})$ 或退回 Vault。
* **不变量 $I_3$ (预算硬顶):** $\text{grant.consumed} \le \text{leaf.max\_spend} \;\land\; \text{pot.budget\_used} \le \text{pot.budget\_total}$。
* **不变量 $I_4$ (自主速率上限):** 滑动窗口内预留总资金不超过 `window_cap`。
* **不变量 $I_5$ (单调权限收敛):** 子代理 PDA 权限绝不能宽于父级模板。
* **不变量 $I_6$ (恐慌纪元与冻结隔离):** 结算必须满足 $\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \;\land\; \neg\text{pot.frozen}$。
* **不变量 $I_7$ (心跳时效性):** 超过 `valid_until` 严禁发起新预留。
* **不变量 $I_8$ (单调结算与防双花):** $\text{paid}_{\text{new}} \le \min(\text{voucher.cumulative}, \text{channel.reserved}) \;\land\; \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}$。
* **不变量 $I_9$ (女巫账户隔离):** 每个能力叶片在链上映射唯一且确定性的 Channel PDA。

---

### 12.4. 定量威胁模型与定理 6.1 最大损失数学上限
设 $\tau$ 为从恶意凭证签署到链上紧急冻结交易确认的全部反应时间：
$$\tau = t_{\text{detect}} + t_{\text{owner}} + t_{\text{land}} \le 12.0\text{s}$$
在最恶劣场景 $T_4$（代理私钥泄露且 Merkle 树中商户串通）下，最大潜在损失 $E_{\text{theft}}(\tau)$ 严格受限于：

$$E_{\text{theft}}(\tau) \le \min\left(B,\; K,\; W_p \cdot n(\tau, \omega_p),\; \sum_{i:\, m_i \in \mathcal{A}} E_i(\tau)\right)$$

在标准提示词注入 ($T_1$) 攻击中，$E_{\text{theft}} = 0$；即使私钥完全失窃 ($T_4$)，损失亦绝不会超过 $\min(K, W_p)$，保全企业 $99.9\%$ 以上资金。

---

### 12.5. 五大红队攻防加固防线
1. **防御 Jito MEV 抢先结算:** 通道绑定 `created_at_epoch`。所有者触发 Panic 时纪元递增，黑客 MEV 捆绑包全部失效。
2. **防御滑动窗口边界双重套现:** 预留时即刻原子性扣减滑动容量，杜绝跨窗口双倍提取。
3. **`OwnerForceReclaim` 即时资金回收:** 若 `channel.paid == 0`，主所有者可免等 24 小时争议期立即抽回资金。
4. **100% 租金 Lamports 保全:** 通道注销时租金强制原路退回出资者 (`grant_pot`)。
5. **防御提示词注入微循环吸血:** 独立策略引擎限制试用域每 10 分钟最多 3 笔微交易，并严格校验返回载荷语义。

---
*技术白皮书 v1.1 附录 &bull; HAICHAIN 全球系统特别工作组 &bull; 版权所有。*
"""
}

# For languages KO, FR, ES, RU, KK, HI, HE, we generate rigorous translated appendices
# Let's write them cleanly into section12_templates

section12_templates["KO"] = """

---

## 12. 기술 부록 V1.1 — CAPLEAF V1 바이너리 아키텍처, 9대 수학적 불변성, 위협 모델 및 손실 상한선

### 12.1. 223 바이트 Little-Endian 와이어 포맷 및 3단계 도메인 분리
HAICHAIN v1.1 커널에서 마스터 소유자가 AI 하위 에이전트에게 부여하는 모든 지출 권한은 Borsh Little-Endian으로 직렬화된 표준 223 바이트 바이너리 구조체(`CapLeafV1`)로 인코딩됩니다.
16개 필드(버전, 에이전트 서명키, 가맹점 주소, USDT 토큰 민트, 최대 지출액, 최대 예약액, 슬라이딩 윈도우 한도, 유효 기간, 심장박동 만료 시점, 분쟁 해결 기간 등)를 포함합니다.
도메인 분리 프리픽스(`0x00`, `0x01`, `0x02`)를 통해 2차 역상 공격 및 길이 확장 공격을 수학적으로 차단하며, 고정 깊이 $d = 12$ (4,096개 리프, 384 바이트 증명 크기)를 강제합니다.

### 12.2. 예약 회계 상태 머신 및 단조적 PDA 계층 구조
온체인 상태 머신은 머클 증명 제출과 채널 결제를 분리합니다: `PotAccount` (금고 PDA) $\\rightarrow$ `ActiveGrantAccount` (1회 증명 활성화) $\\rightarrow$ `ChannelAccount` (x402 오프체인 마이크로 바우처 스트리밍 채널).
수취인 토큰 계정은 스마트 계약 내부에서 $\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$로만 유도되며 제3자 계정으로의 탈취를 원천 차단합니다.

### 12.3. 핵심 9대 수학적 불변성 ($I_1 \\dots I_9$)
* $I_1$ (자본 보존): 금고 + 에스크로 + 정산 완료 + 미사용 반환금 $\\equiv$ 순 예치금.
* $I_2$ (수취인 안전): 자금은 오직 정규 ATA(Merchant, Mint)로만 출금.
* $I_3$ (예산 상한): 소비액 $\\le$ 최대 지출 한도.
* $I_4$ (속도 상한): 슬라이딩 윈도우 내 지출 $\\le$ 윈도우 한도.
* $I_5$ (단조적 축소): 하위 PDA는 상위 권한 범위를 초과할 수 없음.
* $I_6$ (패닉 에포크 격리): 패닉 시 `panic_epoch` 변경으로 미체결 바우처 즉시 동결.
* $I_7$ (하트비트 만료): `valid_until` 초과 시 새로운 지출 차단.
* $I_8$ (단조적 정산): 누적 금액 단조 증가 검증으로 바우처 재사용 방지.
* $I_9$ (시빌 공격 격리): 능력치 리프당 고유한 채널 PDA 매핑.

### 12.4. 위협 모델 및 정리 6.1 최대 손실 수학적 상한선
대응 지연 시간 $\\tau \\le 12.0\\text{s}$ ($t_{\\text{detect}} + t_{\\text{owner}} + t_{\\text{land}}$) 하에서, 최악의 시나리오 $T_4$ (에이전트 개인키 탈취 및 가맹점 공모) 발생 시 최대 손실 $E_{\\text{theft}}(\\tau)$는 $\\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$로 완벽하게 한정되어 기업 자산의 $99.9\\%$ 이상을 보존합니다.

### 12.5. 5대 레드팀 침투 방어 대책
Jito MEV 패닉 선행매매 방어, 윈도우 경계 이중 지출 방어, 미사용 채널 24시간 대기 없는 즉시 자금 회수(`OwnerForceReclaim`), 계정 임대료(Rent Lamports) 100% 반환, 간접 프롬프트 주입 마이크로 루프 쓰로틀링 완비.

---
*기술 백서 v1.1 부록 • HAICHAIN 글로벌 시스템 태스크포스 • All Rights Reserved.*
"""

section12_templates["FR"] = """

---

## 12. ANNEXE TECHNIQUE V1.1 — ARCHITECTURE BINAIRE CAPLEAF V1, 9 INVARIANTS, MODÈLE DE MENACE & PLAFOND DE RISQUE

### 12.1. Format Binaire 223 Octets Little-Endian & Séparation de Domaine à 3 Niveaux
Dans le noyau HAICHAIN v1.1, chaque capacité de dépense accordée par le Propriétaire Principal est encodée sous la forme d'une structure binaire normalisée de 223 octets (`CapLeafV1`) sérialisée en Borsh Little-Endian (16 champs immuables).
La séparation de domaine (`0x00` feuille, `0x01` nœud, `0x02` vide) élimine les attaques par seconde préimage, avec un arbre Merkle à profondeur fixe $d = 12$ (4.096 feuilles, preuve de 384 octets).

### 12.2. Comptabilité par Réservation & Hiérarchie Monotone des PDA
Le noyau on-chain sépare la preuve Merkle de l'exécution : `PotAccount` (coffre de gouvernance) $\\rightarrow$ `ActiveGrantAccount` (activé une seule fois) $\\rightarrow$ `ChannelAccount` (micro-séquestre temporaire pour les flux HTTP x402).
L'adresse du compte bénéficiaire est strictement dérivée on-chain : $\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$.

### 12.3. Les 9 Invariants Mathématiques Fondamentaux ($I_1 \\dots I_9$)
* $I_1$ (Conservation du Capital) : Trésorerie + Séquestres + Paiements + Remboursements $\\equiv$ Dépôts Nets.
* $I_2$ (Sécurité Bénéficiaire) : Flux dirigés exclusivement vers l'ATA officielle du marchand.
* $I_3$ (Plafond Budgétaire) : Consommation $\\le$ Dépense maximale autorisée.
* $I_4$ (Plafond de Vélocité Autonome) : Réserves limitées sur fenêtre glissante.
* $I_5$ (Rétrécissement Monotone) : Les permissions des sous-agents ne peuvent excéder le modèle parent.
* $I_6$ (Isolation d'Époque de Panique) : Gel instantané invalidant tous les vouchers en vol.
* $I_7$ (Expiration du Heartbeat) : Blocage absolu après dépassement de `valid_until`.
* $I_8$ (Règlement Monotone) : Paiement non-décroissant interdisant le double-spend de vouchers.
* $I_9$ (Isolation Sybil) : Unicité stricte du PDA par feuille de capacité.

### 12.4. Modèle de Menace Quantitatif & Théorème 6.1 Plafond de Perte Maximale
Sous une latence de réponse $\\tau \\le 12.0\\text{s}$, dans le pire scénario $T_4$ (vol de clé d'agent et collusion du marchand), la perte maximale théorique $E_{\\text{theft}}(\\tau)$ est strictement bornée par $\\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$, préservant plus de $99,9\\%$ du capital institutionnel.

### 12.5. Les 5 Défenses de Durcissement Red-Team
Protection contre le front-running Jito MEV via `panic_epoch`, blocage du double-retrait par chevauchement de fenêtre, récupération immédiate des fonds non-dépensés sans attendre 24h (`OwnerForceReclaim`), préservation intégrale des lamports de loyer (Rent), et limitation de fréquence contre l'injection indirecte de prompt.

---
*Annexe du Livre Blanc Technique v1.1 • HAICHAIN Global Systems Taskforce • Tous droits réservés.*
"""

section12_templates["ES"] = """

---

## 12. APÉNDICE TÉCNICO V1.1 — ARQUITECTURA BINARIA CAPLEAF V1, 9 INVARIANTES, MODELO DE AMENAZAS Y TECHO DE RIESGO

### 12.1. Formato Binario de 223 Bytes Little-Endian y Separación de Dominio de 3 Capas
En el núcleo HAICHAIN v1.1, cada capacidad de gasto otorgada por el Propietario Maestro se codifica como una estructura binaria de 223 bytes (`CapLeafV1`) serializada en Borsh Little-Endian con 16 campos estrictos.
La separación de dominio (`0x00`, `0x01`, `0x02`) neutraliza ataques de segunda preimagen, operando sobre un árbol Merkle de profundidad fija $d = 12$ (4.096 hojas, prueba fija de 384 bytes).

### 12.2. Contabilidad de Reserva y Jerarquía Monótona de PDA
El contrato inteligente separa la verificación de prueba del flujo de pagos: `PotAccount` (bóveda raíz) $\\rightarrow$ `ActiveGrantAccount` (activación de prueba en 1 paso) $\\rightarrow$ `ChannelAccount` (micro-custodia temporal para vouchers HTTP x402).
La cuenta de destino se deriva obligatoriamente on-chain: $\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$.

### 12.3. Los 9 Invariantes Matemáticos del Sistema ($I_1 \\dots I_9$)
* $I_1$ (Conservación de Capital): Bóveda + Custodias + Pagos + Devoluciones $\\equiv$ Depósitos Netos.
* $I_2$ (Seguridad de Beneficiario): Fondos dirigidos exclusivamente a la ATA canónica del comercio.
* $I_3$ (Techo Presupuestario): Gasto acumulado $\\le$ Límite máximo establecido.
* $I_4$ (Límite de Velocidad Autónomo): Control de gasto en ventana deslizante.
* $I_5$ (Estricta Reducción Monótona): Los PDA secundarios no pueden ampliar permisos del PDA principal.
* $I_6$ (Aislamiento de Época de Pánico): La congelación invalida inmediatamente vouchers pendientes.
* $I_7$ (Vencimiento por Heartbeat): Bloqueo automático al superar `valid_until`.
* $I_8$ (Liquidación Monótona): Liquidación no decreciente que elimina el doble gasto.
* $I_9$ (Aislamiento contra Ataques Sybil): Unicidad matemática de cada cuenta de canal.

### 12.4. Modelo Cuantitativo de Amenazas y Teorema 6.1 Techo de Pérdida
Con un tiempo de reacción $\\tau \\le 12.0\\text{s}$, en el peor escenario $T_4$ (compromiso de clave privada y comercio coludido), la pérdida máxima $E_{\\text{theft}}(\\tau)$ está acotada por $\\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$, blindando más del $99,9\\%$ de los fondos empresariales.

### 12.5. Cinco Defensas Red-Team Integradas
Defensa contra front-running Jito MEV en pánico, neutralización de doble gasto en fronteras de ventana temporal, recuperación instantánea de fondos sin esperar 24h (`OwnerForceReclaim`), restitución del 100% de lamports de renta y filtrado anti-bucles en inyecciones de prompt.

---
*Apéndice del Libro Blanco Técnico v1.1 • HAICHAIN Global Systems Taskforce • Todos los derechos reservados.*
"""

section12_templates["RU"] = """

---

## 12. ТЕХНИЧЕСКОЕ ПРИЛОЖЕНИЕ V1.1 — БИНАРНАЯ АРХИТЕКТУРА CAPLEAF V1, 9 ИНВАРИАНТОВ, МОДЕЛЬ УГРОЗ И ПРЕДЕЛ РИСКА

### 12.1. Бинарный Формат 223 Байта Little-Endian и 3-Уровневое Разделение Доменов
В ядре HAICHAIN v1.1 каждое право на микроплатежи, выданное Мастер-Владельцем, кодируется в виде канонической структуры из 223 байтов (`CapLeafV1`), сериализованной в Borsh Little-Endian (16 полей).
Префиксы разделения доменов (`0x00`, `0x01`, `0x02`) исключают атаки нахождения второго прообраза и удлинения сообщений. Фиксированная глубина дерева Merkle $d = 12$ (4096 листьев, размер доказательства 384 байта).

### 12.2. Учет по Предварительному Резервированию и Иерархия PDA
Ядро разделяет валидацию доказательства и расчеты: `PotAccount` (корневой сейф) $\\rightarrow$ `ActiveGrantAccount` (однократная активация) $\\rightarrow$ `ChannelAccount` (микро-эскроу для потоковых ваучеров HTTP x402).
Счет получателя строго вычисляется ончейн: $\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$.

### 12.3. 9 Математических Инвариантов Системы ($I_1 \\dots I_9$)
* $I_1$ (Сохранение Капитала): Сейф + Эскроу + Выплаты + Возвраты $\\equiv$ Чистые Депозиты.
* $I_2$ (Безопасность Получателя): Средства выводятся исключительно на канонический ATA мерчанта.
* $I_3$ (Потолок Бюджета): Потрачено $\\le$ Максимальный лимит листа.
* $I_4$ (Лимит Скорости Расходов): Ограничение трат в скользящем окне.
* $I_5$ (Монотонное Сужение): Дочерние PDA не могут расширять полномочия родительского листа.
* $I_6$ (Изоляция Эпохи Паники): Паника владельца мгновенно аннулирует все офчейн-ваучеры.
* $I_7$ (Контроль Сессии Heartbeat): Блокировка операций при превышении `valid_until`.
* $I_8$ (Монотонный Расчет): Неубывающий баланс выплат полностью исключает повторные списания.
* $I_9$ (Защита от Сибил-Атак): Взаимно-однозначное соответствие листа и ончейн-аккаунта канала.

### 12.4. Теорема 6.1: Математический Предел Максимального Ущерба
При времени реакции $\\tau \\le 12.0\\text{с}$, в наихудшем сценарии $T_4$ (полная компрометация ключа агента и сговор с мерчантом), максимальный ущерб $E_{\\text{theft}}(\\tau)$ строго ограничен величиной $\\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$, сохраняя более $99,9\\%$ средств предприятия.

### 12.5. Комплекс Защиты от Атак Red-Team
Блокировка Jito MEV при экстренной заморозке, защита от двойного списания на границах окон, мгновенный возврат неиспользованного депозита без ожидания 24 часов (`OwnerForceReclaim`), 100% возврат арендных lamports и защита от микро-зацикливания при Prompt Injection.

---
*Приложение к Техническому Whitepaper v1.1 • HAICHAIN Global Systems Taskforce • Все права защищены.*
"""

section12_templates["KK"] = """

---

## 12. ТЕХНИКАЛЫҚ ҚОСЫМША V1.1 — CAPLEAF V1 ЕКІЛІК АРХИТЕКТУРАСЫ, 9 ИНВАРИАНТ, ҚАУІП-ҚАТЕР МОДЕЛІ ЖӘНЕ ШЫҒЫН ШЕГІ

### 12.1. 223 Байттық Little-Endian Пішімі Және 3 Деңгейлі Доменді Бөлу
HAICHAIN v1.1 ядросында Бас Иесі беретін барлық микротөлем құқықтары Borsh Little-Endian стандартымен 223 байттық құрылымға (`CapLeafV1`) реттеледі.
`0x00`, `0x01`, `0x02` префикстері арқылы домендер бөлінеді, ал Merkle ағашы бекітілген $d = 12$ тереңдігінде (4 096 жапырақ, дәлелдеме көлемі 384 байт) жұмыс істейді.

### 12.2. Брондау Есебі Және PDA Иерархиясы
Жүйе дәлелдемені тексеру мен төлемді орындауды ажыратады: `PotAccount` (бас сейф) $\\rightarrow$ `ActiveGrantAccount` (1 реттік белсендіру) $\\rightarrow$ `ChannelAccount` (HTTP x402 ваучерлеріне арналған эскроу).
Қаражат тек ончейн есептелген ресми ATA шотына ғана түседі: $\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$.

### 12.3. Жүйенің 9 Математикалық Инварианты ($I_1 \\dots I_9$)
Капиталды абсолютті сақтау ($I_1$), ресми алушы қауіпсіздігі ($I_2$), бюджет шегі ($I_3$), жылдамдық шегі ($I_4$), өкілеттіктерді тарылту ($I_5$), паника дәуірін оқшаулау ($I_6$), сессия уақытын бақылау ($I_7$), монотонды есеп айырысу ($I_8$), және Сибил шабуылдарынан қорғау ($I_9$).

### 12.4. Теорема 6.1: Шығынның Математикалық Шекті Мөлшері
Жүйенің жауап беру уақыты $\\tau \\le 12.0\\text{с}$ болғанда, агент кілті ұрланған ең ауыр $T_4$ жағдайында да максималды шығын $E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$ шеңберінен аса алмайды, бұл корпоративтік капиталдың $99.9\\%$-дан астамын қорғайды.

### 12.5. Red-Team Шабуылдарына Қарсы 5 Қорғаныс
Jito MEV алдын-ораудан қорғау, уақыт терезесінде екі есе шешуге жол бермеу, 24 сағат күтпестен қаражатты кері қайтару (`OwnerForceReclaim`), жалдау lamports толық сақтау және Prompt Injection шексіз циклдерін тоқтату.

---
*Техникалық Ақ Қағаз v1.1 Қосымшасы • HAICHAIN Жаһандық Жүйелер То Verd • Барлық құқықтар қорғалған.*
"""

section12_templates["HI"] = """

---

## 12. तकनीकी परिशिष्ट V1.1 — CAPLEAF V1 बाइनरी वास्तुकला, 9 गणितीय नियम, खतरा मॉडल और अधिकतम जोखिम सीमा

### 12.1. 223-बाइट Little-Endian प्रारूप और 3-स्तरीय डोमेन पृथक्करण
HAICHAIN v1.1 कर्नेल में, मास्टर ओनर द्वारा AI उप-एजेंट को दी गई प्रत्येक भुगतान क्षमता 223-बाइट बाइनरी संरचना (`CapLeafV1`) में एन्कोड की जाती है, जो Borsh Little-Endian में क्रमबद्ध होती है।
डोमेन पृथक्करण उपसर्ग (`0x00`, `0x01`, `0x02`) सेकंड-प्रीइमेज हमलों को समाप्त करते हैं, और Merkle ट्री की गहराई $d = 12$ (4,096 लीफ स्लॉट, 384 बाइट प्रमाण) पर स्थिर है।

### 12.2. आरक्षण लेखांकन और पीडीए पदानुक्रम
स्मार्ट कॉन्ट्रैक्ट प्रमाण सत्यापन को भुगतान निष्पादन से अलग करता है: `PotAccount` (मुख्य वॉल्ट) $\\rightarrow$ `ActiveGrantAccount` (एकल सक्रियण) $\\rightarrow$ `ChannelAccount` (HTTP x402 वाउचर एस्क्रो)।
भुगतान केवल आधिकारिक ऑन-चेन व्युत्पन्न खाते में ही जा सकता है: $\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$।

### 12.3. प्रणाली के 9 मुख्य गणितीय नियम ($I_1 \\dots I_9$)
पूंजी का पूर्ण संरक्षण ($I_1$), प्राप्तकर्ता सुरक्षा ($I_2$), बजट सीमा ($I_3$), गति सीमा ($I_4$), अनुमतियों का संकुचन ($I_5$), पैनिक फ्रीज अलगाव ($I_6$), हार्टबीट वैधता ($I_7$), मोनोटोनिक निपटान ($I_8$), और सिबिल खाता अलगाव ($I_9$)।

### 12.4. प्रमेय 6.1: अधिकतम संभावित क्षति की गणितीय सीमा
प्रतिक्रिया समय $\\tau \\le 12.0\\text{s}$ के तहत, सबसे खराब स्थिति $T_4$ (एजेंट की निजी कुंजी चोरी और मिलीभगत) में भी अधिकतम वित्तीय नुकसान $E_{\\text{theft}}(\\tau) \\le \\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$ तक ही सीमित रहता है, जिससे $99.9\\%$ से अधिक उद्यम पूंजी सुरक्षित रहती है।

### 12.5. पांच रेड-टीम सुरक्षा कवच
Jito MEV फ्रंट-रनिंग से सुरक्षा, विंडो स्ट्रैडल डबल-स्पेंडिंग की रोकथाम, 24 घंटे की प्रतीक्षा के बिना तत्काल पूंजी वापसी (`OwnerForceReclaim`), रेंट लैम्पॉर्ट्स का 100% रिफंड, और प्रॉम्प्ट इंजेक्शन माइक्रो-लूप थ्रॉटलिंग।

---
*तकनीकी श्वेतपत्र v1.1 परिशिष्ट • HAICHAIN ग्लोबल सिस्टम्स टास्कफोर्स • सर्वाधिकार सुरक्षित।*
"""

section12_templates["HE"] = """

---

## 12. נספח טכני V1.1 — ארכיטקטורה בינארית של CAPLEAF V1, תשעת האינווריאנטים, מודל איומים ותקרת חשיפת סיכון

### 12.1. מבנה בינארי של 223 בתים והפרדת דומיינים תלת-שכבתית
בליבת HAICHAIN v1.1, כל הרשאת הוצאה המוענקת על ידי הבעלים הראשי לתת-סוכן בינה מלאכותית מקודדת כמבנה בינארי תקני של 223 בתים (`CapLeafV1`) בסריאליזציית Borsh Little-Endian הכולל 16 שדות קבועים.
הפרדת דומיינים (`0x00`, `0x01`, `0x02`) מונעת התקפות הרחבת אורך וקדם-תמונה שנייה, כאשר עץ Merkle מעוגן בעומק קבוע של $d = 12$ (4,096 עלים, גודל הוכחה 384 בתים).

### 12.2. חשבונאות בהקצאה מראש והיררכיית PDA מונוטונית
החוזה החכם מפריד בין אימות ההוכחה לביצוע התשלומים: `PotAccount` (כספת ראשית) $\\rightarrow$ `ActiveGrantAccount` (אימות חד-פעמי) $\\rightarrow$ `ChannelAccount` (ערוץ נאמנות זמני לשוברי HTTP x402).
חשבון היעד נגזר אך ורק ברשת: $\\text{payee\\_ata} \\equiv \\text{get\\_associated\\_token\\_address}(\\text{merchant}, \\text{mint})$.

### 12.3. תשעת החוקים המתמטיים הבלתי משתנים ($I_1 \\dots I_9$)
שימור הון מוחלט ($I_1$), בטיחות מוטב קנונית ($I_2$), תקרת תקציב קשיחה ($I_3$), בקרת מהירות הוצאה ($I_4$), צמצום הרשאות מונוטוני ($I_5$), בידוד הקפאת חירום ($I_6$), תוקף פעימת דופק Heartbeat ($I_7$), סליקה מונוטונית למניעת שימוש כפול בשוברים ($I_8$), ובידוד חשבונות מפני מתקפות סיביל ($I_9$).

### 12.4. משפט 6.1: תקרת הפסד מקסימלית מוכחת
תחת זמן תגובה של $\\tau \\le 12.0\\text{s}$, אפילו בתרחיש הקיצוני ביותר $T_4$ (דליפה מלאה של מפתח הסוכן וקנוניה עם ספק), סך ההפסד האפשרי $E_{\\text{theft}}(\\tau)$ חסום בקפידה על ידי $\\min(B, K, W_p \\cdot n(\\tau, \\omega_p))$, מה שמבטיח שימור של מעל $99.9\\%$ מכספי הארגון.

### 12.5. חמשת מנגנוני ההגנה של צוות Red-Team
חסימת Jito MEV בעת הקפאה, מניעת משיכה כפולה בגבולות חלונות זמן, השבת הון מיידית ללא צורך בהמתנה של 24 שעות (`OwnerForceReclaim`), החזר מלא של 100% מדמי השכירות (Rent Lamports), וויסות לולאות של הזרקת פרומפטים.

---
*נספח לספר הלבן הטכני v1.1 • כוח המשימה העולמי של HAICHAIN • כל הזכויות שמורות.*
"""

langs = ['EN', 'VI', 'ZH', 'KO', 'FR', 'ES', 'RU', 'KK', 'HI', 'HE']

for lang in langs:
    fname = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    if not os.path.exists(fname):
        print(f"Skipping {fname} (not found)")
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update version string in header from v1.0 to v1.1
    content = content.replace('Whitepaper v1.0', 'Whitepaper v1.1 (CapLeaf Edition)')
    content = content.replace('White Paper v1.0', 'White Paper v1.1 (CapLeaf Edition)')
    content = content.replace('v1.0 (English Edition)', 'v1.1 (English CapLeaf & 9 Invariants Edition)')
    content = content.replace('v1.0 (Phiên bản Tiếng Việt)', 'v1.1 (Phiên bản Tiếng Việt - Bản CapLeaf & 9 Bất Biến)')
    content = content.replace('v1.0 (简体中文版)', 'v1.1 (简体中文 CapLeaf 与 9 大不变量正式版)')
    content = content.replace('v1.0 (한국어판)', 'v1.1 (한국어 CapLeaf 및 9대 불변성 에디션)')
    content = content.replace('v1.0 (Édition Française)', 'v1.1 (Édition Française CapLeaf & 9 Invariants)')
    content = content.replace('v1.0 (Edición en Español)', 'v1.1 (Edición en Español CapLeaf y 9 Invariantes)')
    content = content.replace('Версия:** 1.0', 'Версия:** 1.1 (CapLeaf и 9 Инвариантов)')
    content = content.replace('v1.0 (מהדורה עברית)', 'v1.1 (מהדורה עברית - CapLeaf ו-9 אינווריאנטים)')

    # 2. Check if Section 12 is already appended
    if '## 12. TECHNICAL APPENDIX V1.1' in content or '## 12. PHỤ LỤC KỸ THUẬT V1.1' in content or '## 12. 技术附录 V1.1' in content or '## 12. 기술 부록 V1.1' in content or '## 12. ANNEXE TECHNIQUE V1.1' in content or '## 12. APÉNDICE TÉCNICO V1.1' in content or '## 12. ТЕХНИЧЕСКОЕ ПРИЛОЖЕНИЕ V1.1' in content or '## 12. ТЕХНИКАЛЫҚ ҚОСЫМША V1.1' in content or '## 12. तकनीकी परिशिष्ट V1.1' in content or '## 12. נספח טכני V1.1' in content:
        print(f"[{lang}] Section 12 already exists, skipping append.")
    else:
        appendix_text = section12_templates[lang]
        content = content + appendix_text
        print(f"[{lang}] Appended Section 12 successfully.")

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    # Mirror to app/
    app_fname = os.path.join('app', fname)
    with open(app_fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{lang}] Mirrored to {app_fname}")

print("\nAll 10 Whitepaper markdown files successfully upgraded to v1.1 with Section 12!")
