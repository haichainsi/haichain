# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

whitepapers = [
    'HAICHAIN_WHITEPAPER_V1.0_EN.md',
    'HAICHAIN_WHITEPAPER_V1.0_VI.md',
    'HAICHAIN_WHITEPAPER_V1.0_ZH.md',
    'HAICHAIN_WHITEPAPER_V1.0_ES.md',
    'HAICHAIN_WHITEPAPER_V1.0_FR.md',
    'HAICHAIN_WHITEPAPER_V1.0_KO.md',
    'HAICHAIN_WHITEPAPER_V1.0_RU.md',
    'HAICHAIN_WHITEPAPER_V1.0_KK.md',
    'HAICHAIN_WHITEPAPER_V1.0_HI.md',
    'HAICHAIN_WHITEPAPER_V1.0_HE.md'
]

for fname in whitepapers:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()

    # Diagram 1: Replace REAL YIELD column with PROTOCOL SECURITY & INSURANCE
    c = c.replace('[ REAL YIELD STREAMING ]', '[ PROTOCOL SECURITY & CHGB ]')
    c = c.replace('- Distributed in pure USDT', '- Capitalized to CHGB Fund')
    c = c.replace('- Rewarded to veHAISI stakers', '- Protects network solvency ')

    c = c.replace('[ CHIA LỢI NHUẬN THỰC BẰNG USDT ]', '[ QUỸ BẢO HIỂM AN TOÀN CHGB ]   ')
    c = c.replace('- Trả thưởng trực tiếp bằng USDT', '- Nạp Quỹ Dự Trữ Rủi Ro    ')
    c = c.replace('- Dành cho người khóa veHAISI', '- Bảo chứng thanh khoản ví    ')

    c = c.replace('[ 真实收益流式分发 ]', '[ 协议安全与 CHGB 储备 ]')
    c = c.replace('- 纯正 USDT 直接派息', '- 划拨至风险准备金')
    c = c.replace('- 奖励给 veHAISI 质押者', '- 提供链上偿付保障')

    # Diagram 2: Replace 60%/40% with 50%/50%
    c = c.replace('├── 60% of Buybacks BURNED FOREVER', '├── 50% of Buybacks BURNED FOREVER')
    c = c.replace('└── 40% Distributed as USDT Yield\n                                                    to long-term veHAISI Stakers',
                  '└── 50% Allocated to Protocol Reserve\n                                                    (CHGB Insurance Fund)')
    c = c.replace('└── 40% Distributed as USDT Yield', '└── 50% Allocated to Protocol Reserve')

    c = c.replace('├── 60% Mua $HAISI và ĐỐT VĨNH VIỄN', '├── 50% Mua $HAISI và ĐỐT VĨNH VIỄN')
    c = c.replace('└── 40% Chia cổ tức USDT Real Yield\n                                                    cho người cọc hạn (veHAISI)',
                  '└── 50% Nạp Quỹ Bảo Hiểm Rủi Ro CHGB\n                                                    (Bảo vệ thanh khoản khẩn cấp)')
    c = c.replace('└── 40% Chia cổ tức USDT Real Yield', '└── 50% Nạp Quỹ Bảo Hiểm Rủi Ro CHGB')

    c = c.replace('├── 60% 回购代币永久销毁', '├── 50% 回购代币永久销毁')
    c = c.replace('└── 40% 纯 USDT 真实收益分红', '└── 50% 划拨至协议保险准备金')

    # Compulsory Staking -> Dual-Rail / Optional veHAISI
    c = c.replace('[ Compulsory $HAISI Staking (veHAISI) ]', '[ Optional veHAISI Staking Tiers ]   ')
    c = c.replace('[ Cọc Bắt Buộc $HAISI (veHAISI) ]', '[ Cọc veHAISI Tùy Chọn & Phân Tầng ]')
    c = c.replace('[ 强制性 $HAISI 质押 (veHAISI) ]', '[ 可选 veHAISI 质押等级制度 ]      ')

    # Sub-sections
    c = c.replace('#### 1. The Stake-to-Transact Bandwidth Invariant\nAutonomous swarms and enterprise clients cannot simply consume network throughput with transient gas. The kernel enforces a bandwidth allocation constraint:',
                  '#### 1. Dual-Rail Architecture & Optional veHAISI Discount Tiers\nHaichain enforces a zero-friction dual-rail system: standard AI agents pay per transaction in pure USDT with zero mandatory token staking. High-volume enterprise fleets may optionally lock $HAISI (veHAISI) for up to 80% fee reductions and bandwidth priority:')

    c = c.replace('#### 1. Bất Biến Phân Bổ Băng Thông (Stake-to-Transact)\nDoanh nghiệp và các nhà phát triển bầy đàn tác tử không thể chỉ nạp USDT để gọi bot vô hạn định. Hợp đồng thông minh cưỡng bức bất biến hạn mức:',
                  '#### 1. Kiến Trúc Đường Ray Kép & Phân Tầng Giảm Phí veHAISI Tùy Chọn\nHAICHAIN vận hành cơ chế đường ray kép không rào cản: người dùng phổ thông trả phí từng câu lệnh bằng 100% USDT mà không bắt buộc phải mua hay cọc token $HAISI. Các doanh nghiệp vận hành bầy đàn quy mô lớn có thể tùy chọn khóa $HAISI (veHAISI) để nhận ưu đãi giảm tới 80% phí giao dịch và ưu tiên băng thông:')

    # Re-save file and mirror to app/
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)

    app_target = os.path.join('app', fname)
    with open(app_target, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Diagrams patched in {fname} and mirrored to {app_target}.")

print("Diagram patching completed across all 10 whitepapers.")
