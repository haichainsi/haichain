import re
import shutil

def patch_whitepaper_vi():
    path = 'HAICHAIN_WHITEPAPER_V1.0_VI.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Gas cost precision & compression
    content = content.replace(
        'Vi tiện ích thực sự ($0.000001 sàn bù trừ);',
        'Vi tiện ích thực sự ($0.000001 sau khi gom lô nén trạng thái / $0.001 phí gốc);'
    )
    content = content.replace(
        'với mức phí $0.000001, các luồng suy luận AI',
        'với mức phí cơ sở ~$0.001 (được nén xuống $0.000001/tick qua gom lô 1.000 micro-voucher), các luồng suy luận AI'
    )

    # 2. State channel dispute challenge window
    old_channel = """sau khoảng thời gian khóa ấn định (ví dụ 60 giây), Agent có quyền gọi hàm `close_channel_expired` trên Solana để rút 100% số tiền còn lại về tài khoản chính, đảm bảo tuyệt đối không có rủi ro thất thoát vốn."""
    new_channel = """sau khoảng thời gian ấn định, Agent có quyền gửi yêu cầu đóng kênh `request_channel_close`. Kênh sẽ bước vào Cửa Sổ Thử Thách (Dispute Challenge Window - 300 slots / ~120 giây) cho phép Nhà cung cấp nộp voucher mới nhất có chữ ký để đối soát và quyết toán công bằng. Nếu hết 300 slots mà Nhà cung cấp không phản hồi hoặc xác nhận số dư hợp lệ, số tiền còn lại sẽ được hoàn 100% về ví Agent mà không có bất kỳ rủi ro thất thoát vốn nào."""
    content = content.replace(old_channel, new_channel)

    # 3. Captcha upgrade to RLHF / Human Sign-off
    content = content.replace(
        '(captcha vật lý, thẩm định đạo đức, phán đoán ngữ cảnh nhạy cảm)',
        '(thẩm định đạo đức, phê duyệt giao dịch tài chính nhạy cảm, phán đoán ngữ cảnh pháp lý chuyên sâu)'
    )
    content = content.replace(
        'Nhiệm vụ: CAPTCHA, cảm xúc, giao diện',
        'Nhiệm vụ: Phê duyệt ủy quyền (Human Sign-off), gán nhãn RLHF, thẩm định giao dịch nhạy cảm'
    )

    # 4. MiCA & Stablecoin clarity
    content = content.replace(
        'khuôn khổ pháp lý liên minh Châu Âu (EU AI Act, GDPR, MiCA, SEPA)',
        'khuôn khổ pháp lý liên minh Châu Âu (EU AI Act, GDPR, MiCA với Circle USDC & EURC, SEPA)'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched HAICHAIN_WHITEPAPER_V1.0_VI.md")
    shutil.copyfile(path, 'app/HAICHAIN_WHITEPAPER_V1.0_VI.md')
    print("Synced to app/HAICHAIN_WHITEPAPER_V1.0_VI.md")

def patch_whitepaper_en():
    path = 'HAICHAIN_WHITEPAPER_V1.0_EN.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Gas cost precision & compression
    content = content.replace(
        '$0.000001 (Netting)',
        '$0.000001 (1,000:1 Compressed Netting / $0.001 Base)'
    )
    content = content.replace(
        'Pure micro-utility ($0.000001 netting floor);',
        'Pure micro-utility ($0.000001 via 1,000:1 batch compression / $0.001 base);'
    )
    content = content.replace(
        'While Solana L1 achieves 400ms finality with $0.000001 transaction fees,',
        'While Solana L1 achieves 400ms finality with ~$0.001 base transaction fees ($0.000001 per tick via 1,000:1 state channel batch compression),'
    )

    # 2. State channel dispute challenge window
    old_en_channel = """the Agent invokes `close_channel_expired` upon expiry timer expiration (e.g., 60 seconds), retracting 100% of unconsumed collateral with zero capital loss risk."""
    new_en_channel = """the Agent invokes `request_channel_close`. The channel enters a formal 300-slot (~120s) Dispute Challenge Window allowing the provider to submit the latest signed voucher for equitable settlement. If the provider does not contest or verifies full clearance within 300 slots, 100% of remaining unconsumed collateral is securely unlocked to the Agent with zero capital loss risk."""
    content = content.replace(old_en_channel, new_en_channel)

    # 3. Captcha upgrade to RLHF / Human Sign-off
    content = content.replace(
        'Sentiment, CAPTCHA, UI validation',
        'Sentiment, RLHF, Human Sign-Off validation'
    )

    # 4. MiCA & Stablecoin clarity
    content = content.replace(
        'European Union regulations (EU AI Act, GDPR, MiCA, SEPA)',
        'European Union regulations (EU AI Act, GDPR, MiCA compliant via Circle USDC & EURC, SEPA)'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched HAICHAIN_WHITEPAPER_V1.0_EN.md")
    shutil.copyfile(path, 'app/HAICHAIN_WHITEPAPER_V1.0_EN.md')
    print("Synced to app/HAICHAIN_WHITEPAPER_V1.0_EN.md")

patch_whitepaper_vi()
patch_whitepaper_en()
