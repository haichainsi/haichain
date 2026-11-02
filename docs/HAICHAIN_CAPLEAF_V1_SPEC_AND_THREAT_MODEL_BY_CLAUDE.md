# HAICHAIN v1.1 - Đặc tả Lá Năng Lực Merkle & Mô hình đe dọa

Nov 3, 2026 · @LE

## 1. Tổng quan

Tài liệu này đặc tả **Lá Năng Lực (CapLeaf v1)**, đơn vị ủy quyền chi tiêu có ràng buộc người nhận, cùng mô hình đe dọa và công thức thiệt hại tối đa cho lớp chính sách của HAICHAIN trên Solana/x402. Bản này thay mô hình allowance Merkle và Định lý 2 của whitepaper v1.0.

**Cam kết duy nhất:** dù agent bị chiếm quyền hoàn toàn, số tiền có thể mất được tính trước bằng một công thức (mục 6) và không vượt hạn mức chủ sở hữu đã ký.

**Ngoài phạm vi:** chất lượng dịch vụ của provider, việc chủ sở hữu mất khóa passkey, lỗi trong runtime Solana, và lỗi logic của chính chương trình (cần audit và chứng minh hình thức riêng, mục 8).

### Nguyên tắc thiết kế

1. **Người nhận nằm trong lá.** Lá v1.0 chỉ chứa khóa của agent, nên agent bị chiếm quyền trả được cho bất kỳ địa chỉ nào. Giờ mỗi lá khóa một `merchant` và một `mint`.
2. **Kế toán theo reservation.** Mọi hạn mức bị trừ lúc đặt trước tiền vào channel (on-chain). Voucher off-chain chỉ được tiêu trong phần đã đặt trước, nên công thức thiệt hại không phụ thuộc số voucher.
3. **Hai lớp thực thi.** Lớp cứng do chương trình ép (merchant, mint, trần, hạn, epoch). Lớp mềm do policy signer ép ngoài chuỗi (scope chi tiết, ngưỡng bất thường). Công thức mục 6 chỉ dựa vào lớp cứng.
4. **Fail-closed.** Mất kết nối, hết hạn, hay signer ngoại tuyến đều dẫn đến dừng chi, không bao giờ chi tiếp theo mặc định.
5. **Agent chỉ thu hẹp được quyền.** Agent và LLM được gọi `freeze`, không bao giờ được nới trần, kéo dài hạn, đổi merchant hay mở khóa. Chỉ passkey của chủ sở hữu làm được việc đó.

### Thay đổi so với v1.0

| Hạng mục | v1.0 | v1.1 |
| --- | --- | --- |
| Lá | `Pubkey ‖ MaxSpend ‖ ExpirySlot ‖ Nonce` | Thêm `merchant`, `mint`, `scope`, `max_per_call`, cửa sổ tốc độ, `epoch`, `not_before`; hạn tính bằng giây Unix |
| Thu hồi | Đổi root (vô hiệu mọi proof cũ) | `panic_epoch` toàn pot + cờ `revoked` từng lá |
| Ghi on-chain | Mỗi lần chi có thể ghi vào cây | Root chỉ đọc trên đường chi tiêu; trạng thái đếm nằm trong `ActiveGrant` riêng từng lá |
| Proof | Gửi kèm mỗi giao dịch | Chỉ gửi một lần lúc `ActivateGrant` |
| Định lý an toàn | Trần theo từng lá | Trần theo pot, theo cửa sổ thời gian và theo thời gian kiểm soát τ |

## 2. Đặc tả Lá Năng Lực (CapLeaf v1)

Một lá dài cố định **223 byte**, mã hóa little-endian không đệm (tương thích Borsh), băm SHA-256 có domain separation và program ID.

### 2.1 Các trường

| # | Trường | Kiểu | Byte | Ý nghĩa | Lớp thực thi |
| --- | --- | --- | --- | --- | --- |
| 1 | `version` | u8 | 1 | Bằng 1; giá trị khác bị từ chối | Cứng |
| 2 | `pot` | [u8;32] | 32 | PDA của Pot sở hữu lá | Cứng |
| 3 | `agent` | [u8;32] | 32 | Khóa phiên ed25519 của agent được phép chi | Cứng |
| 4 | `merchant` (MerchantPubkey) | [u8;32] | 32 | Authority nhận tiền. Token account nhận luôn là ATA(merchant, mint), chương trình tự dẫn xuất, không nhận địa chỉ từ người gọi | Cứng |
| 5 | `mint` | [u8;32] | 32 | SPL mint (USDC), phải nằm trong danh sách mint của pot | Cứng |
| 6 | `max_spend` (MaxSpend) | u64 | 8 | Trần tích lũy trọn đời của lá, theo đơn vị nhỏ nhất của mint (USDC có 6 chữ số thập phân) | Cứng |
| 7 | `max_reserve` | u64 | 8 | Trần mỗi lần `Reserve`, tức kích thước một đợt đặt trước vào channel | Cứng |
| 8 | `window_cap` | u64 | 8 | Tổng được đặt trước trong một cửa sổ cố định | Cứng |
| 9 | `window_secs` | u32 | 4 | Độ dài cửa sổ, tối thiểu 60 giây | Cứng |
| 10 | `scope_class` | u32 | 4 | Bitmask nhóm dịch vụ: bit0 DATA_API, bit1 LLM_INFERENCE, bit2 COMPUTE, bit3 BROWSER, bit4 HUMAN_TASK; bit còn lại dự trữ, phải bằng 0 | Mềm (xem 2.3) |
| 11 | `scope_ref` | [u8;32] | 32 | SHA-256 của tài liệu `ScopePolicy` chuẩn hóa (origin, path prefix, method, đơn giá tối đa, `max_per_call`) | Mềm |
| 12 | `nonce` | u64 | 8 | Nonce phát hành, duy nhất trong một pot; làm `leaf_hash` duy nhất, phát hành lại sau thu hồi phải dùng nonce mới | Cứng (PDA `init`) |
| 13 | `not_before` | i64 | 8 | Thời điểm Unix (giây) lá bắt đầu hiệu lực | Cứng |
| 14 | `expiry` | i64 | 8 | Thời điểm Unix hết hạn; lúc activate phải thỏa `expiry ≤ now + MAX_TTL` của pot | Cứng |
| 15 | `epoch` | u32 | 4 | Bằng `pot.panic_epoch` lúc phát hành | Cứng |
| 16 | `flags` | u16 | 2 | bit0 `REQUIRE_COSIGN` (cần chữ ký policy signer), bit1 `PROBATION` (merchant thử việc, tính vào ngân sách merchant mới); bit 2–15 phải bằng 0 | Cứng |

Tổng: 1 + 32×4 + 8×3 + 4×2 + 32 + 8×3 + 4 + 2 = 223 byte. Một lá chỉ gắn **một** merchant và **một** mint, nên không có "tập người nhận" trong v1. Muốn trả nhiều merchant thì phát hành nhiều lá.

### 2.2 Mã hóa và băm

```text
TAG        = "HAICHAIN-CAPLEAF-V1"            (ASCII, không có byte kết thúc)
leaf_hash  = SHA256( 0x00 || TAG || program_id || leaf_bytes )
node(l,r)  = SHA256( 0x01 || l || r )          (theo vị trí, không sắp xếp)
EMPTY      = SHA256( 0x02 || TAG )             (lá đệm cho vị trí trống)
```

- **Domain separation.** Tiền tố 0x00/0x01/0x02 ngăn nhầm lẫn giữa lá, nút trong và lá đệm (tấn công second-preimage). `program_id` gắn lá vào một deployment, nên lá devnet không dùng lại được trên mainnet.
- **Cây.** Nhị phân đầy đủ, độ sâu cố định `d` (mặc định 12, tức 4.096 lá, proof 384 byte + chỉ số vị trí u32). Verifier bắt buộc `độ dài proof == pot.tree_depth`, chặn việc giả độ sâu.
- **Chữ ký của chủ sở hữu.** Không ký từng lá. Chủ sở hữu ký giao dịch `PublishRoot` bằng passkey (secp256r1, xác thực bằng precompile). Trước khi ký, giao diện tin cậy phải hiển thị từng lá đã giải mã dưới dạng đọc được (tên merchant và địa chỉ, trần, hạn).

### 2.3 Lớp cứng và lớp mềm

Chương trình on-chain không thấy được dịch vụ có được giao hay không, và khóa agent bị chiếm có thể khai bất kỳ `scope` nào trong voucher. Vì vậy:

- **Cứng (chương trình bắt buộc):** `merchant`, `mint`, `max_spend`, `max_reserve`, `window_*`, `expiry`, `epoch`, `nonce`. Công thức thiệt hại ở mục 6 chỉ dùng các trường này.
- **Mềm (policy signer bắt buộc ngoài chuỗi):** `scope_class`, `scope_ref`. Voucher mang `scope_class` và băm tài nguyên để làm bằng chứng kiểm toán và tranh chấp. Chương trình chỉ kiểm tra `voucher.scope_class ⊆ leaf.scope_class`. An ninh không được dựa vào hai trường này.

## 3. Quy tắc xác minh, tiêu thụ hạn mức và thu hồi

Hạn mức bị trừ **lúc đặt trước (`Reserve`)**, không phải lúc voucher được ký. Mọi quy tắc dưới đây cưỡng chế bằng chương trình on-chain, trừ khi ghi rõ là lớp mềm.

### 3.1 Tài khoản on-chain

| Tài khoản | Seeds | Trường chính |
| --- | --- | --- |
| `Pot` | `["pot", owner_id]` | `owner_auth`, `policy_root`, `tree_depth`, `root_seq`, `panic_epoch`, `frozen`, `valid_until` (heartbeat), `max_ttl`, `mint_allowlist`, `cosigner`, `budget_total`, `budget_used`, `window_cap`, `window_secs`, `window_start`, `window_used` |
| `ActiveGrant` | `["grant", pot, leaf_hash]` | Bản sao điều khoản của lá, `consumed`, `window_start`, `window_used`, `revoked` |
| `Channel` | `["chan", grant, channel_id]` | `reserved`, `paid`, `agent_key`, `payee_ata`, `close_requested_at`, `dispute_secs` |

`consumed` tăng khi `Reserve` và giảm khi hoàn phần chưa dùng. `window_used` **không** giảm khi hoàn, để cửa sổ giữ vai trò giới hạn tốc độ. `Settle` không đổi `consumed`.

### 3.2 Tập lệnh

| Lệnh | Người ký | Hiệu ứng |
| --- | --- | --- |
| `PublishRoot(root, depth)` | Passkey chủ sở hữu | Đặt `policy_root`, tăng `root_seq` |
| `ActivateGrant(leaf, proof, index)` | Bất kỳ ai (trả rent) | Kiểm tra proof, tạo `ActiveGrant`. Yêu cầu `leaf.pot == pot`, `leaf.epoch == panic_epoch`, `not_before ≤ now < expiry ≤ now + max_ttl`, `!frozen`, mint trong allowlist, các bit dự trữ bằng 0 |
| `ActivateChild(template, merchant)` | Agent + cosigner | Chỉ cho lá mẫu `PROBATION` (xem 3.4) |
| `Reserve(grant, channel_id, amount)` | Agent (+ cosigner nếu `REQUIRE_COSIGN`) | Kiểm tra ở 3.3, chuyển tiền từ vault vào escrow của `Channel` |
| `Settle(channel, voucher)` | Bất kỳ ai nộp | Trả `min(voucher.cumulative, reserved) − paid` cho `payee_ata`, tăng `paid` |
| `CloseChannel` | Hai bên, hoặc agent đơn phương | Đơn phương mở cửa sổ tranh chấp `dispute_secs`; hết hạn thì phần dư về vault |
| `RevokeGrant(grant)` | Passkey chủ sở hữu | `revoked = true` |
| `Freeze` | Chủ sở hữu, agent hoặc cosigner | `frozen = true` (chỉ thu hẹp quyền) |
| `Panic` | Passkey chủ sở hữu hoặc khóa panic chuyên dụng | `frozen = true`, `panic_epoch += 1` |
| `Unfreeze` | Chỉ passkey chủ sở hữu | `frozen = false` |
| `Heartbeat(valid_until)` | Passkey chủ sở hữu | `valid_until = min(valid_until, now + max_heartbeat)` |

Voucher gồm `channel_id`, `cumulative` (tổng lũy kế, đơn điệu tăng), `seq`, `scope_class`, `resource_hash`, `expiry`, chữ ký ed25519 của agent. Settle bằng tổng lũy kế nên nộp lại voucher cũ hoặc nộp hai lần không trả thêm tiền.

### 3.3 Điều kiện của `Reserve`

```text
require !pot.frozen
require now <= pot.valid_until                       // heartbeat còn hiệu lực
require !grant.revoked
require grant.epoch == pot.panic_epoch
require grant.not_before <= now < grant.expiry
require amount <= grant.max_reserve
require grant.consumed + amount <= grant.max_spend
roll_window(grant); require grant.window_used + amount <= grant.window_cap
require pot.budget_used + amount <= pot.budget_total
roll_window(pot);   require pot.window_used + amount <= pot.window_cap
require payee_ata == ATA(grant.merchant, grant.mint)  // chương trình tự dẫn xuất
require cosigner_signed if grant.flags & REQUIRE_COSIGN
effects: consumed, window_used, budget_used += amount; vault -> channel escrow
```

Cửa sổ là cửa sổ cố định. Kẻ tấn công có thể dùng hết hạn mức ở cuối một cửa sổ và hết lần nữa ở đầu cửa sổ kế, nên công thức ở mục 6 luôn cộng thêm một cửa sổ.

### 3.4 Lá mẫu `PROBATION` (merchant chưa biết)

Để agent tự trả cho merchant mới mà không cần chủ sở hữu ký lại, chủ sở hữu ký trước một **lá mẫu**: `merchant` = 32 byte 0, cờ `PROBATION | REQUIRE_COSIGN`. Các trường của lá mẫu mang nghĩa ngân sách:

- `max_spend`: tổng ngân sách thử việc cho mọi merchant mới (trọn đời).
- `window_cap`: ngân sách thử việc mỗi cửa sổ.
- `max_reserve`: hạn mức của mỗi lá con (mỗi merchant mới).

`ActivateChild` tạo một `ActiveGrant` con với `max_spend = max_reserve = template.max_reserve`, hết hạn không muộn hơn lá mẫu, và **trừ ngay `max_reserve` vào `consumed` và `window_used` của lá mẫu**. Khoản trừ này không hoàn lại. Cosigner xác minh bằng chứng domain-payee (tệp `.well-known` ký bởi merchant) trước khi đồng ký. Đây là lớp mềm. Lớp cứng vẫn giới hạn tổng chi cho merchant mới bằng ngân sách của lá mẫu, kể cả khi cosigner bị lừa.

### 3.5 Thu hồi

| Cấp | Cơ chế | Chặn được gì | Không chặn được gì |
| --- | --- | --- | --- |
| Toàn pot | `Panic` (tăng `panic_epoch`) hoặc `Freeze` | Mọi `Reserve` và `ActivateGrant` mới | Tiền đã nằm trong escrow của channel |
| Từng lá | `RevokeGrant` | `Reserve` mới trên lá đó | Tiền đã nằm trong escrow |
| Tự nhiên | `expiry`, `valid_until` | Mọi `Reserve` sau mốc | Tiền đã nằm trong escrow |

Hai lưu ý thiết kế:

1. **Thay root không thu hồi lá đã activate.** Muốn vô hiệu một lá đã activate, dùng `RevokeGrant`. Thay root chỉ ngăn lá chưa activate.
2. **Panic không đòi lại tiền đã đặt trước.** Nếu đòi lại, agent bị chiếm quyền cùng merchant thông đồng vẫn rút được phần voucher đã ký, còn merchant trung thực thì mất tiền dịch vụ đã giao. Vì không đòi lại, thiệt hại tối đa sau panic bằng tổng phần đã đặt trước, và phần này đã nằm trong các trần của mục 6 vì hạn mức bị trừ lúc đặt trước. Đây là quyết định cần đội kỹ sư xác nhận (mục 8).

## 4. Tích hợp x402 và state channel

Lá được kiểm tra **trước khi ký voucher** và **lại** khi `Reserve`. Hai lần kiểm tra này phủ nhau: lần đầu (ngoài chuỗi, policy engine) bắt lỗi sớm, lần sau (on-chain) là ranh giới không thể vượt.

### 4.1 Luồng một lần gọi

1. Agent gọi tài nguyên, merchant trả HTTP 402 kèm `PaymentRequired { payee, mint, amount, scheme, resource, expires }`.
2. **Policy engine chạy ngoài tiến trình LLM** đối chiếu: `payee == leaf.merchant`, `mint == leaf.mint`, `amount ≤ ScopePolicy.max_per_call`, `resource` khớp origin và path trong `scope_ref`. Sai một điều là từ chối, không hỏi lại LLM.
3. Nếu chưa có channel: `Reserve(≤ max_reserve)` tạo channel mới với `payee_ata` cố định.
4. Agent ký voucher tăng dần (`cumulative`) và gửi trong header thanh toán.
5. Merchant kiểm chữ ký và `cumulative ≤ reserved`, giao dịch vụ, trả biên lai có chữ ký.
6. Merchant `Settle` định kỳ hoặc khi đóng. Agent `CloseChannel`, phần dư về vault.

Khóa ký của agent nằm trong policy engine, không bao giờ nằm trong ngữ cảnh hay bộ nhớ mô hình. LLM chỉ đề xuất `PaymentIntent { resource, max_amount }`.

### 4.2 Trả trước và trả sau

| Chế độ | Khi nào ký voucher | Rủi ro khi provider gian lận | Khuyến nghị |
| --- | --- | --- | --- |
| Trả trước | Trước khi giao | Mất tối đa giá một lần gọi, `c` | Chỉ dùng khi provider đã qua thử việc và `c` nhỏ |
| Trả sau theo đoạn | Sau khi agent xác nhận từng đoạn đã giao (ví dụ mỗi N token) | Mất tối đa một bước tăng, `δ` | Mặc định |

Việc "xác nhận đoạn đã giao" chỉ là kiểm tra định dạng, độ dài và chữ ký biên lai. Không có cách on-chain nào chứng minh nội dung đúng.

### 4.3 Ràng buộc domain với payee

Địa chỉ nhận nằm trong phản hồi 402 do chính trang web kiểm soát, nên trang bị chiếm có thể đổi payee. Hai biện pháp:

- **Merchant đã biết:** payee nằm trong lá do chủ sở hữu ký. Domain bị chiếm và đổi payee thì không khớp lá, hệ thống từ chối (fail-closed).
- **Merchant mới:** tệp `/.well-known/haichain-payee.json` chứa `{origin, payee, mint, valid_until}` do khóa payee ký. Cosigner xác minh rồi mới đồng ký `ActivateChild` (mục 3.4). Bản chất chỉ chứng minh "người kiểm soát domain cũng kiểm soát khóa payee", không chứng minh merchant trung thực.

### 4.4 Cửa sổ tranh chấp và việc merchant ngoại tuyến

`dispute_secs` mặc định **24 giờ**, đo bằng một đồng hồ duy nhất (Unix time của chương trình), thay cho 300 slot (~120 giây) của v1.0. Nếu agent đóng đơn phương và merchant không nộp voucher trong cửa sổ, phần chưa `Settle` quay về vault và merchant mất khoản đó. Merchant nên chạy watchtower và `Settle` ít nhất mỗi `dispute_secs / 2`, hoặc khi voucher chưa thanh toán vượt một ngưỡng.

## 5. Mô hình đe dọa

Mô hình này giả định **LLM, nội dung web và provider đều có thể độc hại**, và chỉ tin vào chủ sở hữu cùng chương trình on-chain. Mục tiêu là giới hạn thiệt hại, không phải ngăn mọi tấn công.

### 5.1 Tài sản

| Tài sản | Cần giữ |
| --- | --- |
| Số dư vault USDC của pot | Toàn vẹn: không được rút trái phép |
| Passkey chủ sở hữu | Bí mật |
| Khóa phiên của agent | Bí mật, thu hồi được, phạm vi hẹp |
| Root chính sách và các lá | Toàn vẹn |
| Biên lai và nhật ký | Toàn vẹn, không chối bỏ được |
| Khả dụng của agent | Được phép hy sinh để đổi lấy an toàn (fail-closed) |

### 5.2 Thành phần và mức tin cậy

| Thành phần | Tin cậy | Được làm | Không được làm |
| --- | --- | --- | --- |
| Chủ sở hữu, passkey, giao diện duyệt | Tuyệt đối (A1, A2) | Ký root, thu hồi, mở khóa | N/A |
| Chương trình on-chain | Cao, sau audit (A3) | Cưỡng chế lớp cứng | Tự nâng quyền; upgrade authority nằm sau multisig và timelock |
| Policy engine giữ khóa agent | Một phần, có thể bị chiếm | Ký voucher trong trần | Nới trần, đổi merchant, mở khóa |
| Cosigner | Một phần (lớp mềm) | Đồng ký `Reserve`, `ActivateChild`; `Freeze` | Nới trần, trả tiền một mình |
| LLM, công cụ, nội dung web | **Không** | Đề xuất `PaymentIntent`, gọi `Freeze` | Giữ khóa, tự ký, thấy khóa |
| Merchant, provider | **Không** | Nhận tiền trong lá | Nhận ngoài lá, đòi quá voucher |
| RPC, relayer | Chỉ tin về khả dụng | Chuyển giao dịch | Sửa nội dung đã ký |

### 5.3 Giả định

- **A1.** Passkey chủ sở hữu không bị lộ và chủ sở hữu hiểu điều mình ký.
- **A2.** Giao diện duyệt hiển thị đúng nội dung các lá (trusted display). Nếu giao diện bị chiếm thì chủ sở hữu có thể ký root độc hại và mọi bảo đảm mất. Giảm nhẹ bằng hiển thị root trên thiết bị thứ hai.
- **A3.** Chương trình thỏa các bất biến I1–I9 (mục 8) và upgrade authority không bị chiếm.
- **A4.** Solana không reorg sâu sau mức `confirmed`. `Reserve` là sự kiện gây mất tiền nên đợi mức `confirmed` trước khi giao dịch vụ; khoản lớn đợi `finalized`.
- **A5.** Issuer USDC không đóng băng vault (rủi ro ngoài phạm vi).
- **A6.** Đồng hồ `Clock::unix_timestamp` lệch tối đa vài giây so với thời gian thực.
- **A7.** Kênh `Freeze` tới policy engine hoạt động trong thời gian đã đo τ_ctrl (mục 6).

### 5.4 Kẻ tấn công

| Mã | Kẻ tấn công | Năng lực |
| --- | --- | --- |
| T1 | Nội dung độc hại (prompt injection, tool poisoning) | Điều khiển văn bản mà LLM đọc, không có khóa |
| T2 | Agent runtime bị chiếm (RCE, lộ khóa phiên) | Có khóa phiên, ký được mọi voucher trong trần |
| T3 | Provider gian lận | Kiểm soát một merchant, có thể nói dối về việc đã giao |
| T4 | T2 kết hợp T3 | Có khóa phiên và có merchant nhận tiền |
| T5 | Hạ tầng: mất kết nối, tắc nghẽn, chặn RPC | Làm trễ hoặc chặn giao dịch, không sửa được nội dung đã ký |
| T6 | Kẻ lừa chủ sở hữu duyệt (social engineering) | Khiến chủ sở hữu ký một root hoặc lá bất lợi |

**Ngoài phạm vi:** mất passkey, chiếm upgrade authority, lỗi giao thức Solana, và issuer USDC đóng băng ví.

## 6. Công thức thiệt hại tối đa (Max Exposure)

Trong khoảng thời gian τ kể từ lúc chi sai đầu tiên, thiệt hại tối đa bằng **phần nhỏ nhất trong các trần cứng** mà chương trình ép, không cần biết agent hành xử ra sao. "Thiệt hại" ở đây là số tiền rời vault vào escrow qua `Reserve`, tính chặn trên vì phần dư chưa dùng có thể được hoàn lại.

### 6.1 Ký hiệu

| Ký hiệu | Ý nghĩa | Nguồn |
| --- | --- | --- |
| B | Số dư vault | On-chain |
| M_i, S_i | `max_spend` và `consumed` hiện tại của lá i | Lá, `ActiveGrant` |
| W_i, ω_i | `window_cap` và `window_secs` của lá i | Lá |
| R_i | `max_reserve` của lá i | Lá |
| K | `budget_total − budget_used` của pot | `Pot` |
| W_p, ω_p | `window_cap`, `window_secs` của pot | `Pot` |
| 𝒜 | Tập merchant do kẻ tấn công kiểm soát | Giả định tấn công |
| τ | Thời gian kiểm soát: từ lúc chi sai đầu tiên đến lúc không còn `Reserve` mới nào thành công | Đo được, xem 6.3 |

### 6.2 Công thức

**(1) Số cửa sổ tối đa chạm tới trong τ.** Cộng một cửa sổ vì cửa sổ cố định cho phép dồn ở biên (mục 3.3).

```latex
n(\tau,\omega)=\left\lceil \frac{\tau}{\omega} \right\rceil + 1
```

**(2) Trần một lá.**

```latex
E_i(\tau)=\min\bigl(M_i-S_i,\; W_i\cdot n(\tau,\omega_i)\bigr)
```

**(3) Trần của cả pot.** Mọi kịch bản đều rút từ cùng một pot nên **không cộng dồn** vượt quá vế này.

```latex
E_{pot}(\tau)=\min\Bigl(B,\; K,\; W_p\cdot n(\tau,\omega_p),\; \sum_i E_i(\tau)\Bigr)
```

**(4) Mất trộm (tiền đến tay kẻ tấn công).** Chỉ có những lá trỏ tới merchant của kẻ tấn công mới tính. Nếu 𝒜 rỗng thì mất trộm bằng 0 và phần còn lại chỉ là chi phí lãng phí tại merchant hợp lệ.

```latex
E_{theft}(\tau)=\min\Bigl(E_{pot}(\tau),\; \sum_{i:\,m_i\in\mathcal{A}} E_i(\tau)\Bigr)
```

**(5) Lá mẫu thử việc.** Lá mẫu là một lá bình thường đối với công thức (2). Trong kịch bản xấu nhất, toàn bộ ngân sách của nó rơi vào các merchant Sybil thuộc 𝒜, nên số lượng merchant mới không làm tăng trần.

```latex
E_{prob}(\tau)=E_{tpl}(\tau)
```

**(6) Provider gian lận merchant j.** Trần cứng là (2) tính đến lúc bộ ngắt mạch của agent dừng chi, τ_f. Nếu policy engine trung thực thì có thêm trần mềm: trả trước mất tối đa `c_j · f` (f là số lần giao hụt liên tiếp trước khi dừng), trả sau theo đoạn mất tối đa `δ_j`.

```latex
E_{fraud}(j)=\min\bigl(E_j(\tau_f),\; c_j\, f\bigr)\quad\text{(trả trước)},\qquad E_{fraud}(j)=\min\bigl(E_j(\tau_f),\; \delta_j\bigr)\quad\text{(trả sau)}
```

**(7) Chủ sở hữu vắng mặt.** Hiệu lực của `Reserve` bị chặn bởi `valid_until` và `expiry`, nên thời gian vắng được cắt ở mốc gần nhất trong ba mốc (t = hiện tại, v = `valid_until`, e_i = `expiry` của lá i):

```latex
E_{off}(T_{off})=E_{pot}\bigl(\min(T_{off},\; v-t,\; \max_i e_i - t)\bigr)
```

**(8) Merchant chịu thiệt.** Nếu watchtower của merchant ngoại tuyến lâu hơn `dispute_secs`, merchant mất phần voucher chưa `Settle` U_j, và U_j ≤ `reserved` của channel. Đây là thiệt hại của merchant, không phải của pot.

Chú ý trực giác: E_i ≈ *tốc độ cho phép × thời gian kiểm soát + một đến hai cửa sổ*, bị chặn trên bởi trần trọn đời M_i − S_i.

### 6.3 Thời gian kiểm soát τ

τ = t_detect + t_act + t_land. Hàng đầu có hai đường, và đường có cosigner nhanh hơn rất nhiều.

| Đường | Công thức | Áp dụng khi |
| --- | --- | --- |
| Cosigner ngừng ký | τ = t_detect + t_cosign_stop | Lá có `REQUIRE_COSIGN`; kẻ chiếm khóa agent vẫn không `Reserve` được khi cosigner từ chối |
| `Panic` trên chuỗi | τ = t_detect + t_owner + t_land | Lá không cần cosigner; t_owner là thời gian chủ sở hữu chạm passkey, t_land là thời gian giao dịch hạ cánh (có thể kéo dài khi mạng tắc nghẽn) |

Các thành phần phải **đo trên devnet rồi mainnet** và công bố p50, p95, p99. Không dùng số giả định làm cam kết. Khuyến nghị của tài liệu này: mọi lá có `max_spend` vượt một ngưỡng do chủ sở hữu đặt phải bật `REQUIRE_COSIGN`.

### 6.4 Các đòn bẩy điều chỉnh

- **Giảm W_i, W_p:** giảm trực tiếp phần burst và tốc độ.
- **Giảm τ:** bật cosigner, thêm phát hiện bất thường theo tốc độ chi.
- **Giảm K:** ngân sách theo kỳ (ví dụ hàng tháng) là trần cuối cùng khi τ lớn.
- **Rút ngắn `valid_until` và `expiry`:** ép chủ sở hữu "còn sống" một cách định kỳ, biến mất kết nối thành dừng chi.

## 7. Kịch bản tấn công

Kịch bản xấu nhất của một pot là **T4** (khóa agent bị chiếm cùng merchant thông đồng), với thiệt hại E_theft(τ) ở công thức (4). Các kịch bản còn lại đều bằng hoặc nhỏ hơn mức này. Cột "Lớp" cho biết kiểm soát do chương trình ép (Cứng), do policy engine hay cosigner ép (Mềm), hay chỉ là quy trình.

### 7.1 Prompt injection (T1) và lừa chủ sở hữu (T6)

| Mã | Kịch bản | Kiểm soát | Lớp | Thiệt hại tối đa |
| --- | --- | --- | --- | --- |
| PI-1 | Ép agent trả đến địa chỉ lạ | `payee_ata` tự dẫn xuất từ `leaf.merchant` | Cứng | 0 (chỉ mất phí giao dịch); E_theft = 0 vì 𝒜 rỗng |
| PI-2 | Ép agent gọi lặp, đốt ngân sách tại merchant hợp lệ | Trần cửa sổ, M_i, bộ ngắt mạch theo tốc độ | Cứng + Mềm | E_i(τ) theo (2); lãng phí, không phải mất trộm |
| PI-3 | Trang hợp lệ bị chiếm, phản hồi 402 đổi payee | Đối chiếu payee với lá trước khi ký; on-chain từ chối nếu lọt | Cứng + Mềm | 0 |
| PI-4 | Dụ agent xin merchant mới thuộc kẻ tấn công | Lá mẫu `PROBATION` + cosigner xác minh domain-payee | Mềm + ngân sách cứng | E_prob(τ) = E_tpl(τ) |
| PI-5 | Gợi ý LLM nâng trần hoặc mở khóa | Không có lệnh nâng trần cho agent; `Unfreeze` chỉ passkey | Cứng | 0 |
| PI-6 | Tool poisoning gọi `Freeze` liên tục (từ chối dịch vụ) | `Freeze` chỉ thu hẹp quyền; cảnh báo khi tần suất bất thường | Cứng | 0 tiền; mất khả dụng |
| PI-7 | Ép LLM lộ khóa | Khóa nằm trong policy engine, không trong ngữ cảnh | Kiến trúc | 0 nếu kiến trúc đúng; nếu khóa lộ thì chuyển sang T2 |
| PI-8 | Lừa chủ sở hữu duyệt lá nới trần (T6) | Duyệt bằng passkey trên giao diện tin cậy, tóm tắt đọc được, ngưỡng cần nhiều người duyệt | Quy trình | Toàn bộ trần mới được duyệt. Không có bảo vệ mật mã |

PI-8 là giới hạn thật của thiết kế: mọi hệ thống dựa vào chữ ký người dùng đều phụ thuộc việc người đó hiểu điều mình ký (A1, A2).

### 7.2 Provider gian lận và thông đồng (T2, T3, T4)

| Mã | Kịch bản | Kiểm soát | Thiệt hại tối đa |
| --- | --- | --- | --- |
| PF-1 | Nhận tiền không giao (trả trước) | Trả sau theo đoạn, `max_reserve`, bộ ngắt mạch sau f lần hụt | min(E_j(τ_f), c_j · f) |
| PF-2 | Giao thiếu hoặc kém (trả sau) | Chỉ ký voucher cho đoạn đã xác nhận | min(E_j(τ_f), δ_j) |
| PF-3 | Đòi quá voucher hoặc nộp voucher cũ | `cumulative` đơn điệu; chi trả ≤ `reserved` | 0 vượt phần đã ký |
| PF-4 | Nộp voucher sau `Panic` | Panic không đòi lại tiền đã đặt trước (mục 3.5) | ≤ `reserved` tại lúc panic, đã nằm trong E_j |
| PF-5 | Khóa payee của provider bị chiếm | Lá khóa payee cũ; chủ sở hữu `RevokeGrant` và ký lá mới khi provider đổi khóa | E_j(τ) cho đến lúc thu hồi |
| PF-6 | **T4:** khóa agent bị chiếm cùng merchant thông đồng | Trần pot, cosigner, phát hiện bất thường | E_theft(τ) theo (4), đây là mức xấu nhất |
| PF-7 | Không hợp tác đóng channel (giữ thanh khoản) | Cửa sổ tranh chấp, tiền không mất | Khóa tối đa `reserved` trong `dispute_secs` |
| PF-8 | Sybil: nhiều merchant mới | Ngân sách lá mẫu (mục 3.4) | E_tpl(τ) |

### 7.3 Mất kết nối và sự cố hạ tầng (T5)

| Mã | Sự cố | Hành vi hệ thống | Thiệt hại tối đa |
| --- | --- | --- | --- |
| NC-1 | Agent mất kết nối provider giữa lời gọi | Voucher gần nhất đã ký, provider có thể giữ | δ_j, tức một bước tăng |
| NC-2 | Agent mất kết nối Solana | Không `Reserve` được, chỉ ký được voucher trong phần đã đặt trước | 0 thêm |
| NC-3 | Chủ sở hữu ngoại tuyến, không panic được | `valid_until` và `expiry` dừng chi | E_off(T_off) theo (7) |
| NC-4 | Mạng tắc, `Panic` land chậm | τ dài hơn; đường cosigner không phụ thuộc chuỗi | E_pot(τ) với τ lớn hơn |
| NC-5 | Cosigner hoặc policy engine ngoại tuyến | Fail-closed: lá `REQUIRE_COSIGN` không `Reserve` được | 0; mất khả dụng |
| NC-6 | Watchtower của merchant ngoại tuyến lâu hơn `dispute_secs` | Merchant mất voucher chưa `Settle` | U_j (thiệt hại của merchant) |
| NC-7 | RPC bị chặn hoặc nói dối | Chương trình xác minh mọi giao dịch, RPC chỉ ảnh hưởng khả dụng | 0 tiền |
| NC-8 | Reorg sau `confirmed` | `Reserve` có thể biến mất sau khi provider đã giao | Giá trị đã giao trên khoản chưa `finalized`; khoản lớn đợi `finalized` (A4) |

## 8. Ví dụ số, bất biến, test vector và điểm còn mở

### 8.1 Ví dụ số

Một pot có B = $50, K = $30, W_p = $4 mỗi giờ (ω_p = 1 giờ). Ba lá, đều có ω = 1 giờ, S_i = 0:

| Lá | Merchant | M_i | W_i (mỗi giờ) |
| --- | --- | --- | --- |
| G1 | Provider LLM | $20 | $2 |
| G2 | API tìm kiếm | $5 | $0,50 |
| G3 | Dịch vụ tính toán | $10 | $3 |

Thiệt hại tối đa E_pot(τ) theo thời gian kiểm soát (n = ⌈τ/ω⌉ + 1):

| τ | n | E_1 | E_2 | E_3 | Σ E_i | W_p · n | E_pot | % của B | Vế chặn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 phút | 2 | $4 | $1 | $6 | $11 | $8 | **$8** | 16% | W_p · n |
| 2 giờ | 3 | $6 | $1,50 | $9 | $16,50 | $12 | **$12** | 24% | W_p · n |
| 8 giờ | 9 | $18 | $4,50 | $10 | $32,50 | $36 | **$30** | 60% | K |
| 24 giờ | 25 | $20 | $5 | $10 | $35 | $100 | **$30** | 60% | K |

Các trường hợp cụ thể ở τ = 15 phút:

- **Mất trộm (4):** nếu 𝒜 là merchant của G1 thì min(8, 4) = $4; G2 là $1; G3 là $6. Nếu 𝒜 rỗng thì $0, phần tối đa $8 chỉ là lãng phí tại merchant hợp lệ.
- **Lá mẫu thử việc (5):** với M_tpl = $0,50, W_tpl = $0,10 mỗi giờ thì E_prob = min(0,50; 0,10 × 2) = $0,20, dù có bao nhiêu merchant Sybil.
- **Provider gian lận (6)** trên G3, τ_f = 30 giây (n = 2, E_3 = $6): trả trước với c = $0,50 và f = 3 mất tối đa $1,50; trả sau theo đoạn với δ = $0,002 mất tối đa $0,002.
- **Chủ sở hữu vắng 24 giờ (7):** nếu không có heartbeat, τ = 24 giờ và E = $30. Nếu `valid_until` chỉ cách hiện tại 4 giờ thì n = 5, E_1 = $10, E_2 = $2,50, E_3 = $10, Σ = $22,50, W_p · n = $20, nên E_off = **$20**.

### 8.2 Bất biến cần chứng minh

| # | Bất biến |
| --- | --- |
| I1 | Bảo toàn: vault + tổng escrow + tổng đã trả + tổng đã hoàn = tổng nạp − tổng rút của chủ sở hữu |
| I2 | Tiền do đường agent, cosigner hay merchant kích hoạt chỉ đến `ATA(leaf.merchant, leaf.mint)` hoặc về vault |
| I3 | Với mọi lá: `consumed ≤ max_spend`; với pot: `budget_used ≤ budget_total` |
| I4 | Tổng `Reserve` trong một cửa sổ cố định ≤ `window_cap` (lá và pot) |
| I5 | Không lệnh nào do agent, cosigner hay merchant ký có thể nới trần, kéo dài `expiry` hay `valid_until`, đổi merchant hay mint, đổi root, hoặc `Unfreeze` |
| I6 | Không `Reserve` hay `ActivateGrant` thành công khi `frozen` hoặc epoch lệch |
| I7 | Không `Reserve` khi `now ≥ expiry` hoặc `now > valid_until`; `ActivateGrant` yêu cầu `expiry ≤ now + max_ttl` |
| I8 | `paid ≤ min(cumulative lớn nhất đã nộp, reserved)`, không giảm, và nộp lại voucher không trả thêm |
| I9 | Mỗi `leaf_hash` chỉ tạo được một `ActiveGrant` |

Công cụ đề xuất: fuzzing bằng Trident, kiểm chứng hình thức I1–I9 bằng Certora Solana Prover hoặc công cụ tương đương, property test cho Merkle, và **audit độc lập**. 15 bài test tự chạy không thay được audit.

### 8.3 Test vector

Chạy bằng Python `hashlib`, proof đã được tái xây dựng và khớp root. Địa chỉ là giá trị giữ chỗ (byte lặp), không phải địa chỉ thật. Cây 4 lá (độ sâu 2) để minh họa; triển khai thật dùng độ sâu của pot.

```text
program_id  = 0xAA x 32
pot         = 0x11 x 32
agent       = 0x22 x 32
merchant    = 0x33 x 32
mint        = 0x44 x 32
max_spend   = 5_000_000      (5,00 USDC)
max_reserve = 100_000        (0,10 USDC)
window_cap  = 500_000        (0,50 USDC)
window_secs = 3600
scope_class = 1              (DATA_API)
scope_ref   = SHA256("GET https://api.example.com/v1/search")
            = 671219d325e544db054aa89ded3799e6dac69c78d0d134fd5ced69a77d341e7c
nonce       = 1
not_before  = 1793664000     (2026-11-03 00:00 UTC)
expiry      = 1793750400     (24 giờ sau)
epoch       = 0
flags       = 0

leaf_bytes (223 byte, 64 ký tự hex mỗi dòng) =
0111111111111111111111111111111111111111111111111111111111111111
1122222222222222222222222222222222222222222222222222222222222222
2233333333333333333333333333333333333333333333333333333333333333
3344444444444444444444444444444444444444444444444444444444444444
44404b4c0000000000a08601000000000020a1070000000000100e0000010000
00671219d325e544db054aa89ded3799e6dac69c78d0d134fd5ced69a77d341e
7c01000000000000000024e96a000000008075ea6a00000000000000000000

leaf_hash   = 64e35d5494c5a2fcfd9f08c0b7a390295f39a5638d542a3e6a92a29bf862d6c6

Lá 1..3: cùng tham số, merchant = 0x55 x 32, 0x66 x 32, 0x77 x 32, nonce = 1
proof[0] (lá 1)         = c750366dee343808a8012e208f669385efa0bd09db7814a72af702204869090e
proof[1] (nút bên phải) = 61b82cff26167572de36a00d7851124060de45c29fdf9af76cd51c31b5349c55
root                    = fd07b9c68eb18341387d34b3732bf70198e9e2ef0e4f378484d9bd82e8f72d2f
EMPTY                   = 5356c70898f581c2674b86fb8bea19ec9eee3876ff0fa2e4950041e239e87c4d
```

### 8.4 Điểm còn mở cần đội kỹ sư quyết định

1. **Panic có đòi lại tiền đã đặt trước không.** Mặc định là không (mục 3.5). Đổi lại là bảo vệ merchant trung thực.
2. **Xác thực passkey trên chuỗi.** Phụ thuộc precompile secp256r1 (SIMD-0075); cần kiểm tra trạng thái kích hoạt trên mainnet. Nếu chưa có, phải dùng ví MPC, khi đó A1 yếu đi và whitepaper không được gọi hệ thống là phi lưu ký hoàn toàn.
3. **Ai vận hành cosigner** (HAICHAIN hay chủ sở hữu tự chạy), có chạy trong TEE không, và ảnh hưởng tới tư cách lưu ký (cần luật sư).
4. **Chi phí:** rent của `ActiveGrant` và `Channel`, và CU của proof độ sâu 12 (12 lần băm SHA-256 cộng giải mã). Cần đo trên devnet.
5. **Đo τ** (t_detect, t_owner, t_land, t_cosign_stop) và công bố p50, p95, p99.
6. **Định dạng `ScopePolicy`:** đề xuất JSON chuẩn hóa theo RFC 8785 (JCS) trước khi băm.
7. **Đối chiếu x402:** kiểm tra đặc tả x402 mới nhất trước khi cố định định dạng header voucher và scheme. Tài liệu này chưa đối chiếu với bản đặc tả hiện hành.
8. **Bản Sui:** schema lá, voucher và biên lai giữ nguyên, thể hiện bằng Move với `AgentCap` không `copy`/`drop`. Đây là việc riêng, không nằm trong v1.1.
