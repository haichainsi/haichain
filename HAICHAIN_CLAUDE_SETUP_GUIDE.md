# HƯỚNG DẪN KẾT NỐI 1-CLICK HAICHAIN VỚI CLAUDE DESKTOP & CURSOR
**HAICHAIN Protocol v6.9.3 — Universal Autonomous Agent Financial Kernel**

---

## I. TỔNG QUAN
Tài liệu này hướng dẫn cách kết nối **Claude Desktop** hoặc **Cursor IDE** với **HAICHAIN MCP Server** để AI Agent của bạn có thể:
1. Tự động kiểm tra số dư Quỹ chi tiêu (Spending Pot) trên Solana.
2. Tự động thực hiện các khoản thanh toán vi mô (Micro-payments) từ $0.0001 - $0.05 USDT theo từng tác vụ.
3. Kích hoạt Cầu dao ngắt khẩn cấp (Panic Kill-Switch < 400ms) khi phát hiện dấu hiệu bất thường.

---

## II. KẾT NỐI VỚI CLAUDE DESKTOP (CHỈ VỚI 1 BƯỚC)

### Bước 1: Mở file cấu hình của Claude Desktop
Tùy vào hệ điều hành của bạn, file cấu hình `claude_desktop_config.json` nằm tại:

* **Trên Windows:**
  Nhấn `Windows + R`, gõ:
  ```text
  %APPDATA%\Claude\claude_desktop_config.json
  ```
* **Trên macOS:**
  Mở Finder hoặc Terminal:
  ```text
  ~/Library/Application Support/Claude/claude_desktop_config.json
  ```

### Bước 2: Dán đoạn cấu hình sau vào file
```json
{
  "mcpServers": {
    "haichain": {
      "command": "node",
      "args": [
        "c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js"
      ],
      "env": {
        "SOLANA_RPC_URL": "https://api.devnet.solana.com"
      }
    }
  }
}
```
*(Lưu ý: Nếu bạn cài đặt ở thư mục khác, chỉ cần thay đổi đường dẫn tới file `mcp-server/dist/index.js`).*

### Bước 3: Khởi động lại Claude Desktop
* Tắt hoàn toàn Claude Desktop và mở lại.
* Ở góc dưới bên phải khung chat, bạn sẽ thấy biểu tượng chiếc búa (Tools) với **3 công cụ mới của HAICHAIN**:
  1. `get_agent_spending_pot_balance`: Kiểm tra số dư quỹ chi tiêu.
  2. `execute_micro_payment`: Ký và gửi thanh toán vi mô On-chain thật trên Solana.
  3. `trigger_emergency_panic`: Ngắt khẩn cấp toàn bộ quyền của bot.

---

## III. KẾT NỐI VỚI CURSOR / WINDSURF

1. Mở **Cursor Settings** -> vào mục **Features** -> **MCP Servers**.
2. Bấm **+ Add New MCP Server**:
   * **Name:** `haichain`
   * **Type:** `command`
   * **Command:** `node "c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js"`
3. Trạng thái sẽ chuyển sang màu xanh lá cây (**Enabled**). Khi đó bạn có thể yêu cầu Cursor Composer thanh toán hoặc kiểm tra hạn mức trực tiếp.

---

## IV. CÂU LỆNH MẪU ĐỂ RA LỆNH CHO CLAUDE

Bạn có thể mở Claude Desktop và gõ thử các câu lệnh:

* *"Hãy kiểm tra số dư ví Spending Pot của tôi trên HAICHAIN"* $\rightarrow$ Claude tự gọi `get_agent_spending_pot_balance`.
* *"Tôi vừa hoàn thành tác vụ nghiên cứu, hãy thanh toán $0.0025 USDT cho công cụ phân tích"* $\rightarrow$ Claude tự gọi `execute_micro_payment` và trả về link Solana Explorer xác nhận.
* *"Phát hiện hành vi bất thường, hãy kích hoạt cầu dao khẩn cấp ngắt quyền bot ngay lập tức"* $\rightarrow$ Claude tự gọi `trigger_emergency_panic`.

---

## V. KIỂM CHỨNG GIAO DỊCH TRÊN BLOCKCHAIN
Tất cả các giao dịch thanh toán và lệnh Panic của Claude đều được ghi nhận trực tiếp trên sổ cái Solana Blockchain. Bạn có thể nhấp chuột vào đường link trả về để kiểm tra trạng thái **Confirmed** tại:
[https://explorer.solana.com/?cluster=devnet](https://explorer.solana.com/?cluster=devnet)
