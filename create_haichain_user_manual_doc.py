# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive, step-by-step Haichain User Manual in Word (.docx) format.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, hex_color):
    """Set background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
    """Set internal cell padding (in twips: 20 twips = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_callout_box(cell, bg_color="F1F5F9", border_color="0284C7"):
    """Style a cell as an executive callout box with a thick left border."""
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="36" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

def set_table_borders(table, border_color="CBD5E1"):
    """Set sleek borders for standard table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="8" w:space="0" w:color="{border_color}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="12" w:space="0" w:color="{border_color}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def build_haichain_manual(output_path):
    doc = docx.Document()
    
    # 0.8 inch margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # Color Palette
    NAVY = RGBColor(15, 37, 55)       # Primary Header (#0F2537)
    BLUE = RGBColor(2, 132, 199)      # Accent Blue (#0284C7)
    CHARCOAL = RGBColor(31, 41, 55)   # Body Text (#1F2937)
    MUTED = RGBColor(100, 116, 139)   # Subtitles (#64748B)
    GREEN = RGBColor(16, 149, 106)    # Positive / Success (#10B981)
    RED = RGBColor(220, 38, 38)       # Warning / Panic Stop (#DC2626)
    
    # Base Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = CHARCOAL
    normal_style.paragraph_format.line_spacing = 1.18
    normal_style.paragraph_format.space_after = Pt(4)
    normal_style.paragraph_format.space_before = Pt(0)
    
    # ----------------- COVER / HEADER -----------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(6)
    title_p.paragraph_format.space_after = Pt(2)
    run_badge = title_p.add_run("TÀI LIỆU HƯỚNG DẪN THỰC HÀNH CHÍNH THỨC | OFFICIAL USER GUIDE\n")
    run_badge.font.size = Pt(9)
    run_badge.font.bold = True
    run_badge.font.color.rgb = BLUE
    
    run_title = title_p.add_run("HƯỚNG DẪN SỬ DỤNG NỀN TẢNG HAICHAIN")
    run_title.font.size = Pt(24)
    run_title.font.bold = True
    run_title.font.color.rgb = NAVY
    
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(12)
    run_sub = sub_p.add_run("Cẩm Nang Từng Bước Từ A - Z Cho Người Dùng, Lập Trình Viên & Nhà Đầu Tư")
    run_sub.font.size = Pt(12)
    run_sub.font.bold = True
    run_sub.font.color.rgb = BLUE
    
    # Metadata Overview Bar
    meta_table = doc.add_table(rows=1, cols=4)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    meta_items = [
        ("Phiên Bản Giao Thức", "Kernel v6.9.3 (Solana)"),
        ("Phương Thức Xác Thực", "Passkey / FaceID / TouchID"),
        ("Mạng Thử Nghiệm", "Solana Devnet Live"),
        ("Tài Sản Giao Dịch", "USDT & $HAI Token")
    ]
    
    col_widths = [Inches(1.7), Inches(1.8), Inches(1.7), Inches(1.7)]
    for i, (label, val) in enumerate(meta_items):
        cell = meta_table.cell(0, i)
        cell.width = col_widths[i]
        set_cell_background(cell, "F8FAFC")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r_lbl = p.add_run(f"{label}\n")
        r_lbl.font.size = Pt(8.5)
        r_lbl.font.color.rgb = MUTED
        r_val = p.add_run(val)
        r_val.font.size = Pt(9.5)
        r_val.font.bold = True
        r_val.font.color.rgb = NAVY
        
    set_table_borders(meta_table, "E2E8F0")
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ----------------- LỜI MỞ ĐẦU -----------------
    callout_tbl = doc.add_table(rows=1, cols=1)
    callout_cell = callout_tbl.cell(0, 0)
    set_callout_box(callout_cell, "F0F9FF", "0284C7")
    cp = callout_cell.paragraphs[0]
    cp.paragraph_format.space_after = Pt(2)
    c_bold = cp.add_run("Lời Khuyên Dành Cho Bạn Trước Khi Bắt Đầu: ")
    c_bold.font.bold = True
    c_bold.font.color.rgb = NAVY
    cp.add_run(
        "HAICHAIN được thiết kế theo triết lý 'Invisible Web3' (Blockchain vô hình). "
        "Bạn KHÔNG cần phải học các thuật ngữ khó hiểu như 12 từ khóa hạt giống (seed phrase), mã hóa Borsh hay phí gas Solana. "
        "Mọi thao tác quản lý tiền cho AI đều dễ dàng như việc sử dụng Apple Pay hoặc tài khoản ngân hàng điện tử hằng ngày, "
        "nhưng tài sản của bạn lại được bảo vệ bằng các rào cản mật mã cấp quân sự."
    )

    # ----------------- PHẦN 1: BƯỚC ĐẦU LÀM QUEN & TẠO HŨ TIỀN -----------------
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(4)
    r1 = h1.add_run("PHẦN 1: BƯỚC ĐẦU LÀM QUEN - ĐĂNG NHẬP & TẠO HŨ TIỀN CHO AI")
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = NAVY

    doc.add_paragraph(
        "Để bắt đầu ủy quyền tài chính cho AI làm việc thay bạn, bạn chỉ cần thực hiện 3 bước cơ bản sau đây:"
    )

    # Bước 1.1
    p_s1 = doc.add_paragraph()
    p_s1.paragraph_format.space_before = Pt(6)
    p_s1.paragraph_format.space_after = Pt(2)
    r_s1 = p_s1.add_run("Bước 1.1: Truy Cập & Đăng Nhập Bằng Passkey Sinh Trắc Học (FaceID/TouchID)")
    r_s1.font.bold = True
    r_s1.font.size = Pt(11)
    r_s1.font.color.rgb = BLUE

    p_s1_body = doc.add_paragraph()
    p_s1_body.add_run(
        "1. Mở trình duyệt web và truy cập vào ứng dụng tại: https://haichain.si (hoặc môi trường nội bộ http://localhost:3000/app/dashboard.html).\n"
        "2. Nhấn nút [Connect Wallet] ở góc trên bên phải màn hình.\n"
        "3. Bạn có 2 lựa chọn kết nối linh hoạt:\n"
        "   • Cách 1 (Khuyên dùng - Nhanh nhất): Chọn [Biometric Passkey]. Trình duyệt sẽ yêu cầu xác thực FaceID, TouchID hoặc mã PIN thiết bị của bạn. Tài khoản của bạn được khởi tạo ngay lập tức mà không cần cài đặt ví phụ.\n"
        "   • Cách 2 (Dành cho người dùng Web3): Kết nối thông qua ví Phantom hoặc Solflare có sẵn trên trình duyệt."
    )

    # Bước 1.2
    p_s2 = doc.add_paragraph()
    p_s2.paragraph_format.space_before = Pt(6)
    p_s2.paragraph_format.space_after = Pt(2)
    r_s2 = p_s2.add_run("Bước 1.2: Nạp Tiền Vào Hũ Chi Tiêu (Master Spending Pot)")
    r_s2.font.bold = True
    r_s2.font.size = Pt(11)
    r_s2.font.color.rgb = BLUE

    p_s2_body = doc.add_paragraph()
    p_s2_body.add_run(
        "Thay vì trả thuê bao tháng cố định $150 - $450 cho các dịch vụ AI, bạn chỉ cần nạp một số tiền nhỏ (ví dụ: $5.00 hoặc $10.00 USDT) vào hũ chi tiêu:\n"
        "1. Tại tab [Overview & Vault], nhấp vào nút [+ Add Funds (0% Gas)].\n"
        "2. Chọn hình thức nạp tiền thuận tiện nhất cho bạn:\n"
        "   • Apple Pay / Google Pay / Thẻ Quốc Tế: Thanh toán 1 chạm, tiền được quy đổi tự động sang USDT on-chain.\n"
        "   • Quét mã VietQR (Dành cho Việt Nam): Quét mã QR chuyển khoản ngân hàng thông thường; hệ thống đối tác thanh khoản tự động ghi nhận số dư tức thì.\n"
        "   • Nạp bằng USDT Solana: Chuyển USDT trực tiếp từ sàn Binance, Bybit hoặc ví cá nhân vào địa chỉ Vault hiển thị trên màn hình.\n"
        "3. Cơ chế Bao cấp Phí Gas (Gasless Paymaster): Bạn nạp bao nhiêu tiền thì tài khoản có đúng bấy nhiêu tiền để dùng. Hệ thống máy chủ HAICHAIN tự động chi trả toàn bộ phí mạng Solana."
    )

    # Bước 1.3
    p_s3 = doc.add_paragraph()
    p_s3.paragraph_format.space_before = Pt(6)
    p_s3.paragraph_format.space_after = Pt(2)
    r_s3 = p_s3.add_run("Bước 1.3: Thiết Lập Hạn Mức Tốc Độ Chi Tiêu (Autonomous Velocity Cap)")
    r_s3.font.bold = True
    r_s3.font.size = Pt(11)
    r_s3.font.color.rgb = BLUE

    p_s3_body = doc.add_paragraph()
    p_s3_body.add_run(
        "Để ngăn chặn rủi ro AI chạy lặp vô tận (infinite loop) gây tốn tiền:\n"
        "• Trên giao diện hiển thị thanh [Autonomous Velocity Cap], mặc định được đặt mức an toàn tối đa $10.00.\n"
        "• Bạn có thể điều chỉnh hạn mức chi tiêu tối đa mỗi giờ hoặc mỗi ngày (ví dụ: tối đa $1.00/giờ).\n"
        "• Nếu các tác tử AI vượt quá hạn mức này, hợp đồng thông minh trên Solana sẽ tự động từ chối giao dịch tiếp theo cho đến khi bạn xác nhận lại."
    )

    # ----------------- PHẦN 2: KẾT NỐI CLAUDE DESKTOP & CURSOR -----------------
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(14)
    h2.paragraph_format.space_after = Pt(4)
    r2 = h2.add_run("PHẦN 2: KẾT NỐI VỚI CLAUDE DESKTOP & CURSOR IDE QUA GIAO THỨC MCP")
    r2.font.size = Pt(13)
    r2.font.bold = True
    r2.font.color.rgb = NAVY

    doc.add_paragraph(
        "HAICHAIN hỗ trợ giao thức chuẩn Model Context Protocol (MCP) của Anthropic, "
        "cho phép trợ lý ảo Claude hoặc trình soạn thảo mã nguồn Cursor tự động thanh toán các dịch vụ tính toán mà không cần bạn can thiệp thủ công:"
    )

    # Claude Desktop
    p_c1 = doc.add_paragraph()
    p_c1.paragraph_format.space_before = Pt(6)
    p_c1.paragraph_format.space_after = Pt(2)
    r_c1 = p_c1.add_run("Cách 2.1: Kết Nối 1-Click Với Claude Desktop")
    r_c1.font.bold = True
    r_c1.font.size = Pt(11)
    r_c1.font.color.rgb = BLUE

    doc.add_paragraph(
        "1. Mở file cấu hình `claude_desktop_config.json` trên máy tính của bạn:\n"
        "   • Trên Windows: Bấm tổ hợp phím Windows + R, dán `%APPDATA%\\Claude\\claude_desktop_config.json` rồi bấm Enter.\n"
        "   • Trên macOS: Mở thư mục `~/Library/Application Support/Claude/claude_desktop_config.json`.\n"
        "2. Thêm đoạn mã sau vào phần \"mcpServers\":"
    )

    # Code block in table
    code_tbl = doc.add_table(rows=1, cols=1)
    code_cell = code_tbl.cell(0, 0)
    set_cell_background(code_cell, "1E293B")
    set_cell_margins(code_cell, top=100, bottom=100, left=140, right=140)
    p_code = code_cell.paragraphs[0]
    p_code.paragraph_format.space_after = Pt(0)
    r_code = p_code.add_run(
        '{\n'
        '  "mcpServers": {\n'
        '    "haichain": {\n'
        '      "command": "node",\n'
        '      "args": ["c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js"],\n'
        '      "env": {\n'
        '        "SOLANA_RPC_URL": "https://api.devnet.solana.com"\n'
        '      }\n'
        '    }\n'
        '  }\n'
        '}'
    )
    r_code.font.name = "Consolas"
    r_code.font.size = Pt(9.0)
    r_code.font.color.rgb = RGBColor(241, 245, 249)

    doc.add_paragraph(
        "3. Khởi động lại ứng dụng Claude Desktop. Bạn sẽ thấy biểu tượng chiếc búa (Tools) kích hoạt sẵn 3 công cụ tự động của HAICHAIN:\n"
        "   • `get_agent_spending_pot_balance`: Kiểm tra số dư khả dụng.\n"
        "   • `execute_micro_payment`: Tự động thanh toán vi mô On-chain cho dịch vụ vừa dùng.\n"
        "   • `trigger_emergency_panic`: Cầu dao khẩn cấp ngắt quyền hoạt động ngay lập tức."
    )

    # Cursor / Windsurf
    p_c2 = doc.add_paragraph()
    p_c2.paragraph_format.space_before = Pt(6)
    p_c2.paragraph_format.space_after = Pt(2)
    r_c2 = p_c2.add_run("Cách 2.2: Kết Nối Với Cursor IDE / Windsurf")
    r_c2.font.bold = True
    r_c2.font.size = Pt(11)
    r_c2.font.color.rgb = BLUE

    doc.add_paragraph(
        "1. Trong trình biên dịch Cursor, nhấn `Ctrl + Shift + J` (hoặc mở Cài đặt Cursor) -> chọn mục **Features** -> cuộn xuống **MCP Servers**.\n"
        "2. Nhấp vào nút **+ Add New MCP Server** và điền thông số:\n"
        "   • Tên (Name): `haichain`\n"
        "   • Kiểu (Type): `command`\n"
        "   • Lệnh (Command): `node \"c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js\"`\n"
        "3. Khi đèn tín hiệu chuyển sang màu xanh lá cây (Enabled), Cursor Agent đã sẵn sàng thanh toán chi phí API tự động."
    )

    # Sample Prompts
    p_c3 = doc.add_paragraph()
    p_c3.paragraph_format.space_before = Pt(6)
    p_c3.paragraph_format.space_after = Pt(2)
    r_c3 = p_c3.add_run("Các Câu Lệnh Mẫu (Prompts) Để Ra Lệnh Cho AI")
    r_c3.font.bold = True
    r_c3.font.size = Pt(11)
    r_c3.font.color.rgb = BLUE

    p_prompts = doc.add_paragraph()
    p_prompts.add_run(
        "Bạn chỉ cần trò chuyện bằng ngôn ngữ tự nhiên trong Claude hoặc Cursor, AI sẽ tự động thực thi các hành động tài chính an toàn:\n"
        "• Kiểm tra số dư: \"Hãy kiểm tra giúp tôi số dư trong quỹ chi tiêu HAICHAIN hiện còn bao nhiêu?\"\n"
        "• Thanh toán dịch vụ: \"Tôi vừa thu thập xong dữ liệu nghiên cứu, hãy thanh toán $0.0012 USDT cho dịch vụ cào web qua HAICHAIN.\"\n"
        "• Xử lý sự cố: \"Phát hiện bot có dấu hiệu chạy lặp bất thường, hãy ngắt cầu chì khẩn cấp ngay lập tức!\""
    )

    # ----------------- PHẦN 3: SỬ DỤNG CÁC TÍNH NĂNG TRÊN DASHBOARD -----------------
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(14)
    h3.paragraph_format.space_after = Pt(4)
    r3 = h3.add_run("PHẦN 3: HƯỚNG DẪN CHI TIẾT CÁC TÍNH NĂNG TRÊN BẢNG ĐIỀU KHIỂN (DASHBOARD)")
    r3.font.size = Pt(13)
    r3.font.bold = True
    r3.font.color.rgb = NAVY

    features = [
        ("Tab 1: Overview & Master Vault (Tổng Quan & Quản Lý Hũ Tiền)",
         "• Hiển thị số dư thực tế theo thời gian thực (ví dụ: $8.4500 USDT) và số lượng Action Credits tương đương.\n"
         "• Thu hồi tiền cọc rent thừa (Rent Lamports Recycled): Cơ chế thông minh của Solana giúp thu hồi 100% tiền phí tạo tài khoản về ví mẹ khi giao dịch kết thúc.\n"
         "• Nút [Withdraw to Cold Wallet]: Rút toàn bộ số dư USDT chưa sử dụng về ví lưu trữ an toàn hoặc tài khoản ngân hàng bất kỳ lúc nào."),

        ("Tab 2: AI Agent Swarm (Quản Trị Bầy Đàn Tác Tử AI)",
         "• Cho phép bạn quản lý danh sách nhiều con bot khác nhau (ví dụ: Bot nghiên cứu, Bot viết mã, Bot giao dịch).\n"
         "• Cấp vé năng lực Merkle (Issue Capability Ticket): Đặt ranh giới cứng cho từng con bot (Ví dụ: Bot A chỉ được tiêu tối đa $0.05/lệnh, Bot B chỉ được tiêu $0.01/lệnh).\n"
         "• Phân quyền nghiêm ngặt: Chọn chế độ READ_ONLY (chỉ đọc) hoặc CODE_ONLY (chỉ chạy mã), cấm tuyệt đối bot chuyển tiền ra ví ngoài."),

        ("Tab 3: AI Playground (Phòng Thử Nghiệm Thanh Toán Vi Mô Tức Thì)",
         "• Nơi bạn trải nghiệm trực tiếp cách bot trả tiền cho các mô hình AI đỉnh cao (OpenAI o1/o3, Claude 3.5 Sonnet, DeepSeek, Together AI).\n"
         "• Bấm nút gửi truy vấn: Bạn sẽ thấy cỗ máy bù trừ trừ đúng $0.0008 USDT chỉ trong 400 mili-giây.\n"
         "• Cơ chế Ký quỹ Co giãn (Elastic Escrow): Hệ thống tạm khóa một khoản đệm dự phòng nhỏ; khi mô hình AI trả lời xong, tiền thừa lập tức hoàn trả lại tài khoản của bạn ngay lập tức."),

        ("Tab 4: Audit Ledger (Sổ Cái Kiểm Toán Minh Bạch Tuyệt Đối)",
         "• Mọi giao dịch nạp tiền, trừ tiền vi mô, hoàn tiền hay ngắt khẩn cấp đều được ghi vĩnh viễn trên chuỗi khối Solana.\n"
         "• Mỗi dòng giao dịch đều đính kèm mã chữ ký (Tx Signature). Bạn chỉ cần nhấp chuột vào mã để mở trực tiếp trang Solana Explorer kiểm chứng tính xác thực độc lập."),

        ("Tab 5: Vesting Vault (Dành Cho Nhà Đầu Tư Sở Hữu Token $HAI)",
         "• Tra cứu số lượng token $HAI được phân bổ từ vòng Pre-Seed hoặc TGE.\n"
         "• Theo dõi biểu đồ mở khóa tuyến tính (Linear Vesting Schedule) từng giây trên hợp đồng thông minh.\n"
         "• Nhấn nút [Claim Token] để rút lượng token đã mở khóa về ví cá nhân theo đúng cam kết minh bạch.")
    ]

    for title, desc in features:
        p_ft = doc.add_paragraph()
        p_ft.paragraph_format.space_before = Pt(6)
        p_ft.paragraph_format.space_after = Pt(2)
        r_ft = p_ft.add_run(f"► {title}")
        r_ft.font.bold = True
        r_ft.font.size = Pt(11)
        r_ft.font.color.rgb = BLUE

        p_fd = doc.add_paragraph()
        p_fd.paragraph_format.space_after = Pt(4)
        p_fd.add_run(desc)

    # ----------------- PHẦN 4: NÚT DỪNG KHẨN CẤP (PANIC KILL-SWITCH) -----------------
    h4 = doc.add_paragraph()
    h4.paragraph_format.space_before = Pt(14)
    h4.paragraph_format.space_after = Pt(4)
    r4 = h4.add_run("PHẦN 4: HƯỚNG DẪN KÍCH HOẠT NÚT DỪNG KHẨN CẤP (PANIC KILL-SWITCH)")
    r4.font.size = Pt(13)
    r4.font.bold = True
    r4.font.color.rgb = NAVY

    doc.add_paragraph(
        "Nút dừng khẩn cấp (Emergency Panic Stop) là chiếc phao cứu sinh tối thượng bảo vệ bạn khỏi bất kỳ rủi ro nào từ AI:"
    )

    panic_box = doc.add_table(rows=1, cols=1)
    p_cell = panic_box.cell(0, 0)
    set_callout_box(p_cell, "FEF2F2", "DC2626")
    p_p = p_cell.paragraphs[0]
    p_p.paragraph_format.space_after = Pt(2)
    p_bold = p_p.add_run("CƠ CHẾ BẢO VỆ PHẢN ỨNG DƯỚI 400 MILI-GIÂY:\n")
    p_bold.font.bold = True
    p_bold.font.size = Pt(10.5)
    p_bold.font.color.rgb = RED
    p_p.add_run(
        "Khi kích hoạt Panic Stop, một giao dịch ưu tiên cao (Priority Transaction) sẽ được bắn trực tiếp vào mạng lưới Solana. "
        "Hợp đồng thông minh lập tức lật cờ on-chain 'panic_kill_switch_tripped' = TRUE. "
        "Ngay lập tức, 100% các quyền chi tiêu của bot bị tước bỏ vĩnh viễn, "
        "toàn bộ số tiền còn lại trong hũ được tự động rút thẳng về ví an toàn của bạn trong chưa đầy 0.4 giây."
    )

    doc.add_paragraph(
        "\nCác cách kích hoạt Nút Dừng Khẩn Cấp:\n"
        "• Cách 1 (Trên Web Dashboard): Nhấn nút màu đỏ [Emergency Stop] (hoặc nút [Panic] trên điện thoại) ở góc trên thanh điều hướng.\n"
        "• Cách 2 (Trong Claude Desktop / Cursor): Nhập câu lệnh: \"Kích hoạt Panic Stop khẩn cấp!\" -> AI sẽ gọi công cụ `trigger_emergency_panic`.\n"
        "• Cách 3 (Dành cho Lập trình viên qua SDK): Gọi hàm `client.triggerPanicKillSwitch()` trong mã nguồn."
    )

    # ----------------- PHẦN 5: CÂU HỎI THƯỜNG GẶP (FAQ) -----------------
    h5 = doc.add_paragraph()
    h5.paragraph_format.space_before = Pt(14)
    h5.paragraph_format.space_after = Pt(4)
    r5 = h5.add_run("PHẦN 5: CÂU HỎI THƯỜNG GẶP (FAQ) & XỬ LÝ SỰ CỐ NHANH")
    r5.font.size = Pt(13)
    r5.font.bold = True
    r5.font.color.rgb = NAVY

    faq_items = [
        ("1. Nếu máy tính hoặc điện thoại của tôi bị mất hoặc hỏng thì tiền trong hũ có mất không?",
         "Hoàn toàn không. Tài khoản Passkey của bạn được đồng bộ an toàn qua Apple iCloud Keychain hoặc Google Password Manager. Bạn chỉ cần đăng nhập FaceID/mật khẩu Google trên thiết bị mới là khôi phục toàn bộ quyền kiểm soát hũ tiền."),

        ("2. Nếu tác tử AI gọi API nhưng nhà cung cấp bị lỗi mạng hoặc sập máy chủ, tôi có bị mất tiền không?",
         "Không bị mất tiền. HAICHAIN sử dụng cơ chế Xác minh Cam kết Hai Giai Đoạn (2-Phase Commit WASM Sandbox). Tiền chỉ thực sự chuyển đi khi API trả về kết quả hợp lệ có chữ ký mật mã. Nếu bị lỗi mạng hoặc timeout, 100% số tiền cọc tạm tính sẽ tự động hoàn trả lại hũ tiền của bạn."),

        ("3. Tại sao tôi không thấy hiển thị phí gas Solana khi thực hiện giao dịch?",
         "HAICHAIN tích hợp sẵn trạm thanh toán phí gas tự động (Gasless Paymaster Relay). Toàn bộ phí mạng siêu nhỏ trên Solana do hệ sinh thái HAICHAIN bao cấp, giúp bạn có trải nghiệm thanh toán mượt mà giống hệt ứng dụng ngân hàng thông thường."),

        ("4. Tôi là nhà đầu tư Pre-Seed, làm sao để tôi kiểm tra số token $HAI của mình?",
         "Bạn chỉ cần truy cập vào tab [Vesting Vault] trên Dashboard, kết nối ví Solana mà bạn đã dùng để tham gia vòng đầu tư. Hệ thống hợp đồng thông minh sẽ tự động đọc dữ liệu on-chain và hiển thị chính xác số token của bạn cùng thời gian mở khóa từng ngày.")
    ]

    for q, a in faq_items:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(6)
        p_q.paragraph_format.space_after = Pt(2)
        r_q = p_q.add_run(q)
        r_q.font.bold = True
        r_q.font.size = Pt(10.5)
        r_q.font.color.rgb = NAVY

        p_a = doc.add_paragraph()
        p_a.paragraph_format.space_after = Pt(4)
        p_a.paragraph_format.left_indent = Inches(0.2)
        p_a.add_run(a)

    # ----------------- FOOTER / CONTACT -----------------
    p_foot = doc.add_paragraph()
    p_foot.paragraph_format.space_before = Pt(18)
    p_foot.paragraph_format.space_after = Pt(2)
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_foot = p_foot.add_run("HAICHAIN OPERATIONAL DOCUMENTATION 2026 | HUMAN + AI SYMBIOSIS\n")
    r_foot.font.bold = True
    r_foot.font.size = Pt(9.5)
    r_foot.font.color.rgb = NAVY
    r_contact = p_foot.add_run("Trang chủ: https://haichain.si  •  Hỗ trợ kỹ thuật: support@haichain.si")
    r_contact.font.size = Pt(9)
    r_contact.font.color.rgb = BLUE

    # Save
    doc.save(output_path)
    print(f"User manual successfully created at: {output_path}")

if __name__ == "__main__":
    output_file = os.path.abspath("HAICHAIN_USER_MANUAL_STEP_BY_STEP_VI.docx")
    build_haichain_manual(output_file)
