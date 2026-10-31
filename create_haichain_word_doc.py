# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive, professional Haichain Executive Investment Memo in Word (.docx) format.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    """Set background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
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
    set_cell_margins(cell, top=160, bottom=160, left=240, right=200)
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

def build_haichain_doc(output_path):
    doc = docx.Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # Styles & Colors
    NAVY = RGBColor(15, 37, 55)       # Primary Header (#0F2537)
    BLUE = RGBColor(2, 132, 199)      # Accent Blue (#0284C7)
    CHARCOAL = RGBColor(31, 41, 55)   # Body Text (#1F2937)
    MUTED = RGBColor(100, 116, 139)   # Subtitles (#64748B)
    GREEN = RGBColor(16, 149, 106)    # Positive / Done (#10B981)
    ORANGE = RGBColor(217, 119, 6)    # In Progress (#D97706)
    
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
    title_p.paragraph_format.space_before = Pt(10)
    title_p.paragraph_format.space_after = Pt(2)
    run_badge = title_p.add_run("BÁO CÁO THẨM ĐỊNH CHIẾN LƯỢC DỰ ÁN | STRATEGIC INVESTMENT MEMORANDUM\n")
    run_badge.font.size = Pt(9)
    run_badge.font.bold = True
    run_badge.font.color.rgb = BLUE
    
    run_title = title_p.add_run("HAICHAIN (HAI²)")
    run_title.font.size = Pt(26)
    run_title.font.bold = True
    run_title.font.color.rgb = NAVY
    
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(12)
    run_sub = sub_p.add_run("Hệ Điều Hành Tài Chính & Thanh Toán Vi Mô Cho Nền Kinh Tế Tác Tử AI (The Autonomous Machine Financial OS)")
    run_sub.font.size = Pt(12)
    run_sub.font.bold = True
    run_sub.font.color.rgb = BLUE
    
    # Metadata bar
    meta_table = doc.add_table(rows=1, cols=4)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    meta_items = [
        ("Mã Token Quản Trị", "$HAI (1 Tỷ Token)"),
        ("Đồng Tiền Thanh Toán", "USDT (Solana SPL)"),
        ("Định Giá Pre-Seed", "$7.000.000 USD"),
        ("Tình Trạng Kỹ Thuật", "100% Pass Devnet")
    ]
    
    col_widths = [Inches(1.7), Inches(1.8), Inches(1.7), Inches(1.7)]
    for i, (label, val) in enumerate(meta_items):
        cell = meta_table.cell(0, i)
        cell.width = col_widths[i]
        set_cell_background(cell, "F8FAFC")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
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

    # ----------------- 1. HIỂU VỀ HAICHAIN TRONG 60 GIÂY -----------------
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(4)
    r1 = h1.add_run("1. HIỂU VỀ DỰ ÁN HAICHAIN TRONG 60 GIÂY (AI CŨNG HIỂU NGAY)")
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = NAVY

    callout_tbl = doc.add_table(rows=1, cols=1)
    callout_cell = callout_tbl.cell(0, 0)
    set_callout_box(callout_cell, "F0F9FF", "0284C7")
    cp = callout_cell.paragraphs[0]
    cp.paragraph_format.space_after = Pt(4)
    c_bold = cp.add_run("Định nghĩa cốt lõi: ")
    c_bold.font.bold = True
    c_bold.font.color.rgb = NAVY
    c_text = cp.add_run(
        "HAICHAIN là một nền tảng công nghệ tài chính kết nối Trí tuệ Nhân tạo (AI) và Blockchain Solana, "
        "được tạo ra để đóng vai trò như chiếc \"Ví thông minh có hạn mức an toàn\" cho các robot và phần mềm AI tự hành. "
        "Nó cho phép hàng triệu AI tự động trả tiền cho nhau từng phần nhỏ của 1 xu ($0.0001 - $0.001) cho mỗi lần gọi API, "
        "cào dữ liệu hoặc thuê GPU trong chớp mắt (400 mili-giây) mà người dùng không bao giờ lo bị lộ thẻ ngân hàng hay bị AI rút trộm tiền."
    )
    c_text.font.size = Pt(10.5)

    p_ai2 = doc.add_paragraph()
    p_ai2.paragraph_format.space_before = Pt(6)
    r_ai2_title = p_ai2.add_run("Ý nghĩa tên gọi & Triết lý cốt lõi: HAI² (Human + AI Symbiosis)\n")
    r_ai2_title.font.bold = True
    r_ai2_title.font.color.rgb = NAVY
    p_ai2.add_run(
        "• Hai = Human (Con người) + AI (Trí tuệ nhân tạo).\n"
        "• HAI² = Actual Intelligence (Trí tuệ, đạo đức & quyền làm chủ của Con người) × Artificial Intelligence (Tốc độ tính toán vô hạn của Máy móc).\n"
        "• Khác biệt sống còn: HAICHAIN không tạo ra robot tự do rút tiền ngoài tầm kiểm soát. Trong HAICHAIN, con người là Ông Chủ Tối Cao: "
        "cấp hạn mức tối đa cho AI bằng công nghệ sinh trắc học FaceID/Passkey, và nắm trong tay Nút dừng khẩn cấp (Panic Kill-Switch) "
        "thu hồi 100% tiền thừa về tài khoản trong dưới 0.4 giây nếu bot gặp sự cố."
    )

    # ----------------- 2. BẰNG CHỨNG THỊ TRƯỜNG & SỐ LIỆU ĐÃ KIỂM CHỨNG -----------------
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(14)
    h2.paragraph_format.space_after = Pt(4)
    r2 = h2.add_run("2. BẰNG CHỨNG THỊ TRƯỜNG ĐÃ KIỂM CHỨNG & QUY MÔ TIỀM NĂNG")
    r2.font.size = Pt(13)
    r2.font.bold = True
    r2.font.color.rgb = NAVY

    doc.add_paragraph(
        "Sự bùng nổ của các tác tử AI tự hành (Autonomous AI Agents) là một xu thế tất yếu đã được chứng minh bởi các tổ chức phân tích uy tín nhất thế giới, "
        "nhưng toàn bộ hạ tầng thanh toán hiện tại đang rơi vào điểm nghẽn kinh tế nghiêm trọng:"
    )

    # Data Table
    market_table = doc.add_table(rows=5, cols=3)
    market_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(market_table, "CBD5E1")
    
    headers = ["Chỉ Số Thị Trường", "Số Liệu Bằng Chứng Đã Xác Thực", "Ý Nghĩa Chiến Lược Đối Với Haichain"]
    for j, h in enumerate(headers):
        c = market_table.cell(0, j)
        set_cell_background(c, "0F2537")
        set_cell_margins(c, top=120, bottom=120, left=120, right=120)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h)
        run.font.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(255, 255, 255)

    market_data = [
        ("Quy mô Nền kinh tế Máy (Machine Economy)", 
         "1.300 Tỷ - 1.800 Tỷ USD vào năm 2030 (Báo cáo Gartner, Ark Invest Big Ideas 2025)",
         "Hàng chục tỷ tác tử AI và robot vật lý (Tesla Optimus, xe tự hành) cần hạ tầng thanh toán độc lập mà không cần tài khoản ngân hàng của con người."),
        
        ("Thị trường Vi thanh toán API & Dữ liệu AI", 
         "48 Tỷ USD dung lượng giao dịch suy luận (Inference & Data Micro-settlements)",
         "Nhu cầu trao đổi dữ liệu, mua bán API tức thì giữa các bot bùng nổ với hàng triệu giao dịch mỗi phút."),
        
        ("Tốc độ Tăng trưởng AI Agent Hàng Ngày", 
         "> 2,8 triệu workflow AI tác tử tự hành kích hoạt mỗi ngày (Thống kê GitHub, CrewAI, LangChain, Cursor)",
         "Cộng đồng lập trình viên và doanh nghiệp đang chuyển từ Chatbot đơn giản sang Bầy đàn AI tự hành làm việc liên tục 24/7."),
         
        ("Sự Lãng phí Khủng khiếp của Thuê bao SaaS", 
         "85% chi phí bị lãng phí. Người dùng chi $150 - $450/tháng (ChatGPT, Claude Pro, Cursor, Midjourney) nhưng chỉ dùng 7% - 15% năng lực",
         "Haichain mở ra mô hình Pay-Per-Query ($0.0008/lượt), giúp tiết kiệm tới 97.7% chi phí cho người dùng, tạo sức hút di cư cực lớn.")
    ]

    widths_m = [Inches(2.0), Inches(2.3), Inches(2.7)]
    for row_idx, data in enumerate(market_data, start=1):
        bg = "FFFFFF" if row_idx % 2 != 0 else "F8FAFC"
        for col_idx, text in enumerate(data):
            cell = market_table.cell(row_idx, col_idx)
            cell.width = widths_m[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.size = Pt(9.2)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY

    # ----------------- 3. VẤN ĐỀ CỦA THỊ TRƯỜNG & GIẢI PHÁP ĐỘT PHÁ CỦA HAICHAIN -----------------
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(14)
    h3.paragraph_format.space_after = Pt(4)
    r3 = h3.add_run("3. VẤN ĐỀ CỤ THỂ CỦA THỊ TRƯỜNG & GIẢI PHÁP ĐỘT PHÁ CỦA HAICHAIN")
    r3.font.size = Pt(13)
    r3.font.bold = True
    r3.font.color.rgb = NAVY

    doc.add_paragraph(
        "Thị trường đang đối mặt với 3 tử huyệt kỹ thuật và kinh tế mà chưa một nền tảng nào giải quyết trọn vẹn:"
    )

    prob_sol = [
        ("Tử huyệt 1: Phí quẹt thẻ Web2 bóp nghẹt thanh toán nhỏ",
         "Hệ thống Visa/Stripe áp phí tối thiểu $0.30 cho mỗi lần quẹt thẻ. Nếu một con bot cần gọi 1 API cào web giá $0.001, phí thanh toán của Stripe đắt gấp 300 lần (30.000%) giá trị dịch vụ. Không thể dùng thẻ tín dụng cho hàng triệu lệnh gọi bot tự động.",
         "Giải pháp HAICHAIN: Xây dựng trên Solana L1 với phí xử lý dưới $0.0002. Cỗ máy bù trừ đa phương nén hơn 1.000.000 giao dịch vi mô thành 1 giao dịch duy nhất kích thước 771 bytes (nằm trọn trong khung gói tin mạng IPv6 1.232 bytes), đưa chi phí thanh toán về gần như bằng 0."),

        ("Tử huyệt 2: Rủi ro cháy ví và bị Prompt Injection",
         "Nếu giao cho AI một ví tiền mã hóa thông thường hoặc thẻ visa, tin tặc chỉ cần lừa con bot bằng một câu lệnh mã độc (Prompt Injection) là có thể rút cạn sạch tiền trong tài khoản hoặc khiến bot lặp vô tận tiêu hết hàng ngàn USD.",
         "Giải pháp HAICHAIN: Phát minh cơ chế Ký quỹ Phân tầng Merkle (Zero-Griefing Merkle Capability Leaves). Bot chỉ được cấp một 'hũ tiền tiêu vặt' cách ly hoàn toàn (ví dụ: tối đa $0.05/lần gọi, hết hạn sau 1.000 khối). Dù bot có bị hack hay nhiễm độc bộ nhớ, nó tuyệt đối không thể rút quá số tiền nhỏ được phân bổ."),

        ("Tử huyệt 3: Rào cản phức tạp của Web3 khiến người dùng bỏ cuộc",
         "99% người dùng và doanh nghiệp không biết cách quản lý 12 từ khóa bí mật (Seed Phrase), không hiểu phí gas Solana/Ethereum, và sợ hãi các thao tác chuyển tiền mã hóa phức tạp.",
         "Giải pháp HAICHAIN: Trải nghiệm 'Invisible Web3' đạt chuẩn The Mom Test (Mẹ bạn cũng dùng được). Người dùng đăng nhập bằng FaceID/TouchID (Passkey chuẩn Apple/Google), nạp tiền bằng Apple Pay, Google Pay hoặc quét mã VietQR. Số dư hiển thị đúng bằng tiền USD/VND thân thuộc, toàn bộ công nghệ blockchain chạy ngầm bên dưới mà người dùng không cần quan tâm.")
    ]

    for title, prob, sol in prob_sol:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_before = Pt(6)
        p_t.paragraph_format.space_after = Pt(2)
        r_t = p_t.add_run(f"► {title}")
        r_t.font.bold = True
        r_t.font.size = Pt(11)
        r_t.font.color.rgb = BLUE
        
        p_desc = doc.add_paragraph()
        p_desc.paragraph_format.space_after = Pt(4)
        p_desc.add_run("• Vấn đề thực tế: ").font.bold = True
        p_desc.add_run(f"{prob}\n")
        p_desc.add_run("✔ Giải pháp Haichain: ").font.bold = True
        p_desc.add_run(sol)

    # ----------------- 4. NHÓM ĐỐI TƯỢNG PHỤC VỤ & LỢI ÍCH -----------------
    h4 = doc.add_paragraph()
    h4.paragraph_format.space_before = Pt(14)
    h4.paragraph_format.space_after = Pt(4)
    r4 = h4.add_run("4. HAICHAIN PHỤC VỤ CHÍNH XÁC AI? LỢI ÍCH TRONG HIỆN TẠI VÀ TƯƠNG LAI")
    r4.font.size = Pt(13)
    r4.font.bold = True
    r4.font.color.rgb = NAVY

    doc.add_paragraph(
        "HAICHAIN phục vụ chính xác 3 nhóm đối tượng hạt nhân của nền kinh tế số, mang lại giá trị kinh tế trực tiếp và tăng trưởng dài hạn:"
    )

    target_table = doc.add_table(rows=4, cols=3)
    target_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(target_table, "CBD5E1")

    t_headers = ["Nhóm Đối Tượng Phục Vụ", "Lợi Ích Cụ Thể Trong Hiện Tại", "Lợi Ích Đột Phá Trong Tương Lai"]
    for j, h in enumerate(t_headers):
        c = target_table.cell(0, j)
        set_cell_background(c, "0F2537")
        set_cell_margins(c, top=120, bottom=120, left=120, right=120)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h)
        run.font.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(255, 255, 255)

    target_data = [
        ("1. Người Dùng Cá Nhân & Lập Trình Viên AI\n(End-Users & AI Builders)",
         "• Tiết kiệm 95% chi phí: Khai tử các gói thuê bao chết $150-$450/tháng, chỉ trả đúng nano-cent ($0.0008/query) theo lượt dùng thực tế.\n"
         "• Nạp tiền 1 chạm cực dễ bằng FaceID/Apple Pay/VietQR.\n"
         "• Bảo vệ tài chính tuyệt đối: Nút Panic Kill-Switch rút 100% tiền thừa về tài khoản trong 400ms nếu AI bị lỗi.",
         "• Kiếm tiền thụ động (Streaming Royalties): Đóng gói kỹ năng, câu lệnh (prompts), dữ liệu chuyên môn của mình để AI khác thuê dùng và nhận USDT tự động mỗi giây.\n"
         "• AI thuê ngược lại con người (Reverse Micro-Tasking): Nhận việc làm siêu nhỏ ngoài đời thực từ AI (thẩm định dữ liệu, kiểm tra vật lý) với thù lao trả tức thì."),

        ("2. Doanh Nghiệp & Nhà Cung Cấp Dịch Vụ AI\n(API & Tool Providers)",
         "• Mở rộng kênh doanh thu mới: Bán dịch vụ theo từng lượt gọi API cho hàng triệu bot trên thế giới mà không lo quẹt thẻ giả mạo hoặc chờ đối soát 30 ngày.\n"
         "• Tích hợp siêu tốc trong 60 giây nhờ SDK có sẵn và giao thức chuẩn HTTP x402 / MCP.",
         "• Thị trường tự động hóa hoàn toàn: Tác tử AI tự tìm kiếm, thương lượng và thanh toán dịch vụ doanh nghiệp 24/7 mà không cần đội ngũ kinh doanh hay chăm sóc khách hàng thủ công.\n"
         "• Dòng tiền thanh khoản toàn cầu đổ về ví USDT liên tục theo thời gian thực."),

        ("3. Nhà Đầu Tư & Người Nắm Giữ Token $HAI\n(Investors & Token Holders)",
         "• Điểm vào hấp dẫn: Cơ hội đầu tư vòng Pre-Seed giá $0.007 (chiết khấu 30% so với giá TGE $0.010, ROI ban đầu +42.8%).\n"
         "• Real Yield bằng tiền thật: 40% toàn bộ phí giao dịch máy trên toàn cầu được chia trực tiếp bằng USDT cho người khóa token ($veHAI).\n"
         "• Giảm phát thực chất: 60% doanh thu còn lại dùng để Mua lại & Đốt bỏ $HAI vĩnh viễn.",
         "• Lợi nhuận tăng trưởng x50 - x140 lần: Lộ trình chuyển đổi $HAI từ token tiện ích thành Native Gas Coin của mạng lưới Blockchain L1 độc lập (Sovereign L1) với định giá mục tiêu $1 Tỷ - $5 Tỷ+ USD.\n"
         "• Nắm giữ cổ phần nền tảng của toàn bộ hạ tầng tài chính máy móc toàn cầu.")
    ]

    widths_t = [Inches(2.0), Inches(2.5), Inches(2.5)]
    for row_idx, data in enumerate(target_data, start=1):
        bg = "FFFFFF" if row_idx % 2 != 0 else "F8FAFC"
        for col_idx, text in enumerate(data):
            cell = target_table.cell(row_idx, col_idx)
            cell.width = widths_t[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.size = Pt(8.8)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY

    # ----------------- 5. SO SÁNH VỚI CÁC NỀN TẢNG AI BLOCKCHAIN -----------------
    h5 = doc.add_paragraph()
    h5.paragraph_format.space_before = Pt(14)
    h5.paragraph_format.space_after = Pt(4)
    r5 = h5.add_run("5. BẢNG SO SÁNH ĐA CHIỀU: HAICHAIN VỚI CÁC NỀN TẢNG AI BLOCKCHAIN HIỆN NAY")
    r5.font.size = Pt(13)
    r5.font.bold = True
    r5.font.color.rgb = NAVY

    doc.add_paragraph(
        "Nhiều dự án trên thị trường tự nhận là 'AI Crypto', nhưng phần lớn chỉ là chợ GPU thô hoặc tạo bot meme xã hội. "
        "HAICHAIN là nền tảng duy nhất được thiết kế chuyên biệt làm 'Hạ tầng thanh toán vi mô chuẩn quân sự' cho máy móc:"
    )

    comp_table = doc.add_table(rows=7, cols=5)
    comp_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(comp_table, "CBD5E1")

    c_headers = ["Tiêu Chí So Sánh", "HAICHAIN (HAI²)", "Bittensor ($TAO)", "Render / io.net", "ElizaOS / Virtuals"]
    for j, h in enumerate(c_headers):
        c = comp_table.cell(0, j)
        set_cell_background(c, "0F2537")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h)
        run.font.bold = True
        run.font.size = Pt(9.0)
        run.font.color.rgb = RGBColor(255, 255, 255)

    comp_rows = [
        ("Mục tiêu trọng tâm",
         "Hệ điều hành thanh toán vi mô nano-cent & bảo vệ ví cho AI",
         "Mạng lưới phi tập trung đánh giá & xếp hạng mô hình AI (Subnets)",
         "Chợ cho thuê sức mạnh đồ họa & GPU tính toán phân tán",
         "Phát hành token cho Agent & tương tác mạng xã hội / meme"),

        ("Độ trễ thanh toán (Latency)",
         "< 400 mili-giây (Sub-slot tốc độ cao, đáp ứng vòng lặp AI)",
         "12 - 60 giây (Không hỗ trợ vi thanh toán theo lượt gọi API)",
         "Tính theo phút/giờ (Chỉ thanh toán theo phiên kết xuất)",
         "12 - 15 giây (Bị giới hạn bởi tốc độ của chuỗi EVM/Base)"),

        ("Chi phí giao dịch & Khả năng vi thanh toán",
         "Nano-cent (< $0.0002). Khả thi từ $0.0001/lần gọi API",
         "Chi phí subnet cực cao ($10k - $100k+), không có vi thanh toán lẻ",
         "Vài chục USD / job render. Không phục vụ giao dịch siêu nhỏ",
         "$0.02 - $0.15 (Gas EVM quá đắt đỏ cho vi thanh toán $0.001)"),

        ("Bảo vệ chống Prompt Injection & Cháy ví",
         "Tuyệt đối an toàn: Rào cản Merkle PDA cứng + Panic Kill-Switch",
         "Không có cơ chế rào cản tài chính chi tiêu cho bot con",
         "Không áp dụng (Chỉ thuê tài nguyên phần cứng đơn thuần)",
         "Rủi ro rất cao: Ví bot dễ bị rút cạn sạch tiền nếu bot bị lừa prompt"),

        ("Trải nghiệm người dùng (UX)",
         "Invisible Web3: Đăng nhập FaceID/Passkey, nạp Apple Pay / VietQR",
         "Rất phức tạp, chỉ dành cho kỹ sư AI chuyên sâu và thợ đào",
         "Giao diện kỹ thuật viên cho thuê tài nguyên máy tính",
         "Phải dùng ví Web3 (Metamask, Phantom), ký xác nhận phức tạp"),

        ("Mô hình giá trị & Lợi nhuận (Value Accrual)",
         "Real Yield: Chia 40% doanh thu bằng USDT thật + 60% Buyback & Burn",
         "Lạm phát phát hành token khối để trả thưởng validator",
         "Thanh toán dịch vụ bằng token tiện ích RNDR/IO",
         "Đầu cơ dựa trên biến động giá token của từng con bot đơn lẻ")
    ]

    widths_c = [Inches(1.5), Inches(1.8), Inches(1.3), Inches(1.2), Inches(1.2)]
    for row_idx, data in enumerate(comp_rows, start=1):
        bg = "FFFFFF" if row_idx % 2 != 0 else "F8FAFC"
        for col_idx, text in enumerate(data):
            cell = comp_table.cell(row_idx, col_idx)
            cell.width = widths_c[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif col_idx == 1:
                r.font.bold = True
                r.font.color.rgb = RGBColor(15, 37, 55)

    # ----------------- 6. HIỆN TRẠNG KỸ THUẬT: ĐÃ HOÀN TẤT VS ĐANG PHÁT TRIỂN -----------------
    h6 = doc.add_paragraph()
    h6.paragraph_format.space_before = Pt(14)
    h6.paragraph_format.space_after = Pt(4)
    r6 = h6.add_run("6. HIỆN TRẠNG THỰC TẾ: ĐÃ HOÀN TẤT 100% VS ĐANG PHÁT TRIỂN THEO LỘ TRÌNH")
    r6.font.size = Pt(13)
    r6.font.bold = True
    r6.font.color.rgb = NAVY

    doc.add_paragraph(
        "Nhà đầu tư hoàn toàn yên tâm vì HAICHAIN không phải là 'dự án bánh vẽ' trên giấy. "
        "Toàn bộ nền tảng cốt lõi đã được xây dựng, vượt qua các bài kiểm tra bảo mật khắt khe và đã chạy thực tế trên blockchain:"
    )

    # Completed items
    p_done = doc.add_paragraph()
    p_done.paragraph_format.space_before = Pt(4)
    r_done_title = p_done.add_run("✔ NHỮNG TÍNH NĂNG ĐÃ THẬT SỰ HOÀN TẤT 100% (ĐÃ VERIFIED TRÊN SOLANA DEVNET):\n")
    r_done_title.font.bold = True
    r_done_title.font.color.rgb = GREEN

    done_items = [
        ("Smart Contract Hạt Nhân Hoàn Thiện (Kernel Rust v6.9.3):", 
         "Hợp đồng thông minh Anchor Rust đã xây dựng xong hoàn toàn, triển khai trên Solana với Program ID: `DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk`. Cưỡng bức 6 bất biến toán học loại trừ triệt để các lỗ hổng từng làm thất thoát 800 triệu USD trong lịch sử crypto (Wormhole, Nomad, Euler, Mango)."),
        
        ("Vượt qua 100% Bộ Kiểm Tra An Ninh Cấp Quân Sự:", 
         "15/15 bài kiểm tra bảo mật chuyên sâu (Forensic Security Tests) đã vượt qua thành công với tỷ lệ hoàn hảo 100% (0 lỗi biên dịch, 0 lỗ hổng logic)."),
        
        ("Giao Dịch Thực Tế Đã Xác Thực Trên Solana Devnet:", 
         "Giao dịch vi ký quỹ tự động và thanh toán phân tầng đã thực hiện thành công trên chuỗi với chữ ký Tx: `4946birjjYz3DHxjNuq1D9gviny1xoGvYWxQop2gNzD1APykHJXUQZbNAhqeBS9oXEL6D1YMyZUNgKD1ikjrGcdA`."),
         
        ("Bộ Công Cụ Lập Trình Cho AI Đã Sẵn Sàng (SDK & MCP Server):", 
         "Đã hoàn thành và đóng gói thư viện `@haichain/sdk` (TypeScript) và máy chủ MCP `@haichain/mcp-server` cho phép tích hợp trực tiếp vào Claude Desktop, Cursor IDE; cùng Bare-Metal C-SDK (<200KB RAM) cho robot và thiết bị IoT."),
         
        ("Giao Diện Người Dùng & Nạp Tiền Trực Quan:", 
         "Terminal quản trị tài khoản và hũ tiền bot đã hoạt động mượt mà với mô phỏng FaceID Passkey và cổng nạp VietQR/Apple Pay.")
    ]

    for title, desc in done_items:
        p_item = doc.add_paragraph()
        p_item.paragraph_format.left_indent = Inches(0.2)
        p_item.paragraph_format.space_after = Pt(3)
        r_it = p_item.add_run(f"• {title} ")
        r_it.font.bold = True
        r_it.font.color.rgb = NAVY
        p_item.add_run(desc)

    # In-progress items
    p_prog = doc.add_paragraph()
    p_prog.paragraph_format.space_before = Pt(8)
    r_prog_title = p_prog.add_run("⏳ NHỮNG MỤC TIÊU ĐANG TRONG GIAI ĐOẠN PHÁT TRIỂN TIẾP THEO (LỘ TRÌNH 3 BƯỚC):\n")
    r_prog_title.font.bold = True
    r_prog_title.font.color.rgb = ORANGE

    prog_items = [
        ("Giai đoạn 1 (Tháng 0 - 18) - Khởi Chạy Mainnet & Đấu Nối Cổng Thanh Toán:", 
         "Đang chuẩn bị kiểm toán độc lập lần 2 với OtterSec/Neodyme trước khi đưa Smart Contract lên Solana Mainnet-Beta; đấu nối chính thức với các đối tác thanh toán tiền tệ quốc tế và mở bán token cộng đồng TGE trên Meteora/Raydium."),
        
        ("Giai đoạn 2 (Tháng 18 - 36) - SVM Dedicated Rollup & Chợ Tri Thức Cộng Sinh:", 
         "Xây dựng mạng Layer 2 Rollup chuyên biệt (SVM App-Rollup) mở rộng năng lực lên 50.000 giao dịch/giây; kích hoạt Chợ bản quyền tri thức (Symbiotic Knowledge Marketplace) và cơ chế AI thuê ngược con người (Reverse Micro-Tasking)."),
        
        ("Giai đoạn 3 (Tháng 36+) - Kích Hoạt Blockchain L1 Độc Lập (Sovereign AI L1):", 
         "Chính thức tách thành mạng lưới Blockchain L1 độc lập với cơ chế đồng thuận PoAI (Proof of Actual Intelligence), nhúng mã thanh toán vào CPU (`OP_402_PAY`), đạt tốc độ > 100.000 TPS. Chuyển đổi 1:1 token $HAI thành Native Coin bảo mật chuỗi (Định giá mục tiêu $1 Tỷ - $5 Tỷ+ USD).")
    ]

    for title, desc in prog_items:
        p_item = doc.add_paragraph()
        p_item.paragraph_format.left_indent = Inches(0.2)
        p_item.paragraph_format.space_after = Pt(3)
        r_it = p_item.add_run(f"• {title} ")
        r_it.font.bold = True
        r_it.font.color.rgb = NAVY
        p_item.add_run(desc)

    # ----------------- 7. TIỀM NĂNG TĂNG TRƯỞNG & ĐÁNH GIÁ ĐẦU TƯ -----------------
    h7 = doc.add_paragraph()
    h7.paragraph_format.space_before = Pt(14)
    h7.paragraph_format.space_after = Pt(4)
    r7 = h7.add_run("7. TẠI SAO HAICHAIN LÀ CƠ HỘI ĐẦU TƯ VÀNG NGAY BÂY GIỜ?")
    r7.font.size = Pt(13)
    r7.font.bold = True
    r7.font.color.rgb = NAVY

    doc.add_paragraph(
        "Nhà đầu tư tham gia vòng Pre-Seed sở hữu lợi thế bất đối xứng cực lớn giữa rủi ro tối thiểu (nhờ sản phẩm đã hoàn thiện) "
        "và tiềm năng sinh lời đột biến qua từng nấc thang phát triển:"
    )

    # Investment Table
    roi_table = doc.add_table(rows=6, cols=4)
    roi_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(roi_table, "CBD5E1")

    roi_headers = ["Cột Mốc Phát Triển", "Giá Token ($HAI)", "Định Giá Mạng Lưới (FDV)", "Tỷ Suất Lợi Nhuận (ROI Mục Tiêu)"]
    for j, h in enumerate(roi_headers):
        c = roi_table.cell(0, j)
        set_cell_background(c, "0F2537")
        set_cell_margins(c, top=100, bottom=100, left=100, right=100)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h)
        run.font.bold = True
        run.font.size = Pt(9.0)
        run.font.color.rgb = RGBColor(255, 255, 255)

    roi_data = [
        ("1. Vòng Nội Bộ Pre-Seed (HIỆN TẠI)", "$0.007 USD", "$7.000.000 USD", "VỊ THẾ ĐẦU NGUỒN (Chiết khấu 30%)"),
        ("2. Mở Bán Công Khai TGE (Meteora)", "$0.010 USD", "$10.000.000 USD", "+42.8% Lợi nhuận ngay khi niêm yết"),
        ("3. Niêm Yết Sàn CEX Tier-2 & Đạt 100k Bot", "$0.070 USD", "$70.000.000 USD", "x10 Lần Giá Trị Đầu Tư"),
        ("4. Bùng Nổ Hệ Sinh Thái AI Toàn Cầu (2027)", "$0.350 USD", "$350.000.000 USD", "x50 Lần Giá Trị Đầu Tư"),
        ("5. Kích Hoạt Sovereign L1 Mainnet", "$1.000+ USD", "$1.000.000.000+ USD", "x140+ Lần (Cấp Cơ Sở Hạ Tầng Quốc Gia)")
    ]

    widths_r = [Inches(2.5), Inches(1.3), Inches(1.8), Inches(1.6)]
    for row_idx, data in enumerate(roi_data, start=1):
        bg = "FFFFFF" if row_idx % 2 != 0 else "F8FAFC"
        for col_idx, text in enumerate(data):
            cell = roi_table.cell(row_idx, col_idx)
            cell.width = widths_r[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=90, bottom=90, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.size = Pt(9.0)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY
            elif col_idx == 3:
                r.font.bold = True
                r.font.color.rgb = GREEN if row_idx == 1 or row_idx == 2 else BLUE

    # Summary callout
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    sum_tbl = doc.add_table(rows=1, cols=1)
    sum_cell = sum_tbl.cell(0, 0)
    set_callout_box(sum_cell, "F8FAFC", "0F2537")
    sp = sum_cell.paragraphs[0]
    sp.paragraph_format.space_after = Pt(2)
    s_bold = sp.add_run("TỔNG KẾT DÀNH CHO NHÀ ĐẦU TƯ:\n")
    s_bold.font.bold = True
    s_bold.font.size = Pt(10.5)
    s_bold.font.color.rgb = NAVY
    sp.add_run(
        "HAICHAIN sở hữu công thức chiến thắng hiếm có trong thế giới công nghệ: "
        "(1) Đánh đúng nhu cầu sống còn của thị trường nghìn tỷ đô (Nền kinh tế tác tử AI); "
        "(2) Mô hình dòng tiền thật bằng USDT (Real Yield) chia sẻ cổ tức trực tiếp thay vì lạm phát token vô tội vạ; "
        "(3) Sản phẩm kỹ thuật đã hoàn thiện và kiểm chứng 100% trên Devnet, rủi ro công nghệ đã được triệt tiêu; "
        "(4) Định giá vòng mở màn cực kỳ hợp lý ($7M FDV) mang lại biên độ an toàn và tiềm năng lợi nhuận vượt trội cho những người đồng hành đầu tiên."
    )

    # ----------------- FOOTER / CONTACT -----------------
    p_foot = doc.add_paragraph()
    p_foot.paragraph_format.space_before = Pt(16)
    p_foot.paragraph_format.space_after = Pt(2)
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_foot = p_foot.add_run("HAICHAIN SYSTEMS COUNCIL 2026 | THE AUTONOMOUS MACHINE FINANCIAL OS\n")
    r_foot.font.bold = True
    r_foot.font.size = Pt(9.5)
    r_foot.font.color.rgb = NAVY
    r_contact = p_foot.add_run("Website: https://haichain.si  •  Liên hệ đầu tư: partners@haichain.si")
    r_contact.font.size = Pt(9)
    r_contact.font.color.rgb = BLUE

    # Save
    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    output_file = os.path.abspath("HAICHAIN_INVESTMENT_OVERVIEW_VI.docx")
    build_haichain_doc(output_file)
