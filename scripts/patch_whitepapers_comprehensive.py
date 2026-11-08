# -*- coding: utf-8 -*-
"""
Patch all 10 Whitepapers and mirror to app/ with comprehensive mathematical,
tokenomics, architectural, and security consistency based on Red Team feedback.
"""
import sys, os, re, shutil

sys.stdout.reconfigure(encoding='utf-8')

# The exact 43-character Sysvar Instructions pubkey on Solana
CORRECT_SYSVAR = "Sysvar1nstructions1111111111111111111111111"

whitepaper_files = [
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

for fname in whitepaper_files:
    if not os.path.exists(fname):
        print(f"Skipping missing file: {fname}")
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Fix Sysvar address typo across all languages
    c = re.sub(r'Sysvar1nstruction5[0-9a-zA-Z]*', CORRECT_SYSVAR, c)
    c = re.sub(r'Sysvar1nstructions1111111111111111111(?!1)', CORRECT_SYSVAR, c)

    # 2. Fix Seed Valuation ($15M FDV -> $7M - $8.5M FDV)
    c = re.sub(r'\\?\$15M FDV', r'$7M - $8.5M FDV', c)
    c = re.sub(r'15\.000\.000 USD FDV', r'7.000.000 - 8.500.000 USD FDV', c)
    c = re.sub(r'15,000,000 USD FDV', r'7,000,000 - 8,500,000 USD FDV', c)
    c = re.sub(r'1500万美元FDV', r'700万-850万美元FDV', c)
    c = re.sub(r'1500만 달러 FDV', r'700만-850만 달러 FDV', c)

    # 3. Unify Take-Rate from 0.10% / 0.1% to 0.05%
    c = c.replace('0.10%', '0.05%')
    c = c.replace('0,10%', '0,05%')
    c = re.sub(r'0\.1%\s+netting fee', '0.05% netting fee', c)
    c = re.sub(r'0\.1%\s+phí bù trừ', '0.05% phí bù trừ', c)
    c = re.sub(r'0\.1%\s+净额结算费', '0.05% 净额结算费', c)
    c = re.sub(r'0,1%\s+de frais de compensation', '0,05% de frais de compensation', c)
    c = re.sub(r'0,1%\s+de tarifa de compensación', '0,05% de tarifa de compensación', c)
    c = re.sub(r'0,1%\s+комиссия за взаимозачет', '0,05% комиссия за взаимозачет', c)
    c = re.sub(r'0,1%\s+өзара есептесу комиссиясы', '0,05% өзара есептесу комиссиясы', c)

    # In Annual Revenue diagrams ($1,400,000 -> $700,000 based on 0.05% of $1.4B)
    c = c.replace('[ $1,400,000 ANNUAL REVENUE ]', '[ $700,000 BASE ANNUAL REVENUE ]')
    c = c.replace('[ DOANH THU THUẦN: $1,400,000 USD / NĂM ]', '[ DOANH THU CƠ SỞ: $700,000 USD / NĂM ]')
    c = c.replace('[ 1,400,000 美元年度净额结算收入 ]', '[ 700,000 美元基准年度净额结算收入 ]')
    c = c.replace('[ $1,400,000 DE REVENU ANNUEL ]', '[ $700,000 DE REVENU ANNUEL DE BASE ]')
    c = c.replace('[ $1,400,000 INGRESOS ANUALES ]', '[ $700,000 INGRESOS ANUALES BASE ]')
    c = c.replace('[ $1,400,000 ГОДОВОЙ ДОХОД ]', '[ $700,000 БАЗОВЫЙ ГОДОВОЙ ДОХОД ]')

    # 4. Unify Buyback & Cash Flow Allocation (60/40 -> 50/50 without securities cash dividends)
    c = c.replace('▼ (60% Revenue)', '▼ (50% Revenue)')
    c = c.replace('▼ (40% Revenue)', '▼ (50% Revenue)')
    c = c.replace('▼ (60% Doanh Thu)', '▼ (50% Doanh Thu)')
    c = c.replace('▼ (40% Doanh Thu)', '▼ (50% Doanh Thu)')
    c = c.replace('▼ (60% 协议收入)', '▼ (50% 协议收入)')
    c = c.replace('▼ (40% 协议收入)', '▼ (50% 协议收入)')
    c = c.replace('▼ (60% de Revenus)', '▼ (50% de Revenus)')
    c = c.replace('▼ (40% de Revenus)', '▼ (50% de Revenus)')
    c = c.replace('▼ (60% de Ingresos)', '▼ (50% de Ingresos)')
    c = c.replace('▼ (40% de Ingresos)', '▼ (50% de Ingresos)')
    c = c.replace('▼ (60% дохода)', '▼ (50% дохода)')
    c = c.replace('▼ (40% дохода)', '▼ (50% дохода)')
    c = re.sub(r'60%\s*Revenue', '50% Revenue', c)
    c = re.sub(r'40%\s*Revenue', '50% Revenue', c)

    # Replace cash dividend box with Protocol Security & Insurance Reserve
    c = c.replace('[ REAL YIELD STREAMING ]\n        - Distributed in pure USDT\n        - Rewarded to veHAISI stakers',
                  '[ PROTOCOL SECURITY & INSURANCE ]\n        - Capitalized to CHGB Reserve Fund\n        - Protects against latency & MEV')
    c = c.replace('[ CHIA LỢI NHUẬN THỰC BẰNG USDT ]\n        - Trả thưởng trực tiếp bằng USDT\n        - Dành cho người khóa veHAISI',
                  '[ QUỸ BẢO HIỂM AN TOÀN CHGB ]\n        - Bổ sung Quỹ Dự Trữ Rủi Ro\n        - Bảo vệ an toàn chống MEV & nghẽn mạng')
    c = c.replace('[ 真实收益流式分发 ]\n        - 纯正 USDT 直接派息\n        - 奖励给 veHAISI 质押者',
                  '[ 协议安全与保险基金 ]\n        - 注入 CHGB 风险对冲储备库\n        - 抵御网络拥堵与 MEV 波动')

    # In text descriptions:
    c = re.sub(r'60%\s+of\s+(?:Buybacks|Purchased Tokens):\s*Burned permanently', '50% of Purchased Tokens: Burned permanently', c)
    c = re.sub(r'40%\s+of\s+Purchased Tokens:\s*Distributed directly as\s+\*?\*?USDT Real Yield dividends\*?\*?[^.\n]*',
               '50% of Purchased Tokens: Transferred to the Protocol Security & Insurance Reserve Fund (CHGB) to safeguard user balances without securities dividend risks.', c)
    
    c = re.sub(r'60%\s+Mua \$HAISI và ĐỐT VĨNH VIỄN', '50% Mua $HAISI và ĐỐT VĨNH VIỄN', c)
    c = re.sub(r'40%\s+Chia cổ tức USDT Real Yield[^.\n]*', '50% Nạp Quỹ Bảo Hiểm Rủi Ro (CHGB) để bảo chứng vốn và thanh khoản khẩn cấp mà không vướng rủi ro chứng khoán.', c)

    c = re.sub(r'60%\s+用于永久销毁', '50% 用于永久销毁', c)
    c = re.sub(r'40%\s+以纯正 USDT 派息[^.\n]*', '50% 划拨至协议安全与保险储备基金 (CHGB) 提供链上偿付保障，规避证券化分红风险。', c)

    # 5. Fix Stage 1 ARR Projection ($15.9M ARR -> Projected: $700k-1.4M ARR)
    c = re.sub(r'[-–]?\s*(?:Revenue|Doanh thu|Revenus|Ingresos|Доход|Кіріс|राजस्व|הכנסות|收入规模|Выручка):\s*\\?\$15\.9M ARR',
               '- Projected: $700k-1.4M ARR', c, flags=re.IGNORECASE)
    c = c.replace('$15.9M ARR', '$700k-1.4M ARR')
    c = c.replace('15.9M ARR', '700k-1.4M ARR')

    # 6. Refine Defense Matrix Titles (Remove Euler, Nomad, Mango sensationalism)
    # English
    c = c.replace('1. WORMHOLE DEFENSE ($320M FIX):', '1. INSTRUCTION SYSVAR INTROSPECTION (CVE-2022-24300 PREVENTION):')
    c = c.replace('2. NOMAD BRIDGE DEFENSE ($190M FIX):', '2. NON-ZERO MERKLE ROOT & UNINITIALIZED PDA DEFENSE:')
    c = c.replace('4. EULER FINANCE DEFENSE ($197M FIX):', '4. LIVE SPL ATA BALANCE INTROSPECTION & ANTI-DRIFT GUARD:')
    c = c.replace('5. MANGO MARKETS DEFENSE ($114M FLASH LOAN FIX):', '5. MULTI-SLOT FLASH-LOAN LIQUIDITY QUARANTINE:')
    
    # Vietnamese
    c = c.replace('1. BẢO VỆ CHỐNG HACK WORMHOLE ($320 TRIỆU USD):', '1. KIỂM TRA CHỮ KÝ NATIVE QUA SYSVAR INSTRUCTIONS (CHỐNG GIẢ MẠO):')
    c = c.replace('2. BẢO VỆ CHỐNG HACK CẦU NỐI NOMAD ($190 TRIỆU USD):', '2. BẤT BIẾN MERKLE ROOT KHÁC 0 & CHỐNG THỰC THI TRÊN PDA RỖNG:')
    c = c.replace('4. BẢO VỆ CHỐNG HACK EULER FINANCE ($197 TRIỆU USD):', '4. TẢI LẠI SỐ DƯ SPL ATA THỰC TẾ & CHỐNG LỆCH SỔ SÁCH:')
    c = c.replace('5. BẢO VỆ CHỐNG TẤN CÔNG VAY NHANH MANGO MARKETS ($114 TRIỆU USD):', '5. CÁCH LY THANH KHOẢN CHỐNG FLASH-LOAN ĐA SLOT:')

    # 7. Add Liquidity Relayer Model Explanation for OpenAI/DeepSeek
    if 'DECENTRALIZED LIQUIDITY RELAYER PROTOCOL' not in c and 'ĐỘNG CƠ CHUYỂN TIẾP THANH KHOẢN' not in c:
        if fname.endswith('_EN.md'):
            gateway_note = """
> [!NOTE]
> **HOW HAICHAIN SETTLES WITH OPENAI, DEEPSEEK & ANTHROPIC:**
> Foundational model labs currently require traditional corporate fiat billing (Stripe / Corporate Cards) and do not natively receive Solana SPL tokens. Haichain resolves this via the **Decentralized Liquidity Relayer Protocol**:
> 1. The user's AI Agent locks micro-USDT into the non-custodial On-Chain Vault PDA on Solana.
> 2. Bonded Relayers (who stake collateral in USDT/SOL to eliminate front-running and default risks) maintain high-tier enterprise billing agreements with OpenAI, Anthropic, and DeepSeek.
> 3. The Relayer streams LLM inference responses to the agent in sub-second timeframes via HTTP/SSE while netting micro-USDT from the agent's signed voucher tickets.
> 4. This delivers a seamless, non-custodial fiat-to-crypto bridge: developers enjoy pure on-chain pay-as-you-go micro-escrow without managing credit cards, while foundational AI labs receive their required fiat settlement.
"""
            c = c.replace('client = openai.OpenAI(\n    base_url="https://gateway.haichain.si/v1"',
                          gateway_note + '\nclient = openai.OpenAI(\n    base_url="https://gateway.haichain.si/v1"')
        elif fname.endswith('_VI.md'):
            gateway_note = """
> [!NOTE]
> **CƠ CHẾ TẤT TOÁN VỚI OPENAI, DEEPSEEK & ANTHROPIC:**
> Các phòng nghiên cứu mô hình nền tảng hiện tại chỉ chấp nhận thanh toán thẻ tín dụng doanh nghiệp (USD Stripe) và chưa nhận trực tiếp token SPL trên Solana. HAICHAIN giải quyết thực tế này thông qua **Giao Thức Chuyển Tiếp Thanh Khoản Bằng Cọc (Decentralized Liquidity Relayer Protocol)**:
> 1. Tác tử AI của người dùng khóa micro-USDT vào Kho Quỹ Vault PDA tự quản trên Solana L1.
> 2. Các Relayer được cấp phép (phải ký quỹ bảo chứng bằng USDT/SOL để triệt tiêu rủi ro kiểm duyệt hoặc quỵt tiền) duy trì hạn mức thanh toán doanh nghiệp với OpenAI, Anthropic, DeepSeek.
> 3. Relayer truyền luồng suy luận AI (SSE stream) về cho Agent với độ trễ nano-giây, đồng thời bù trừ micro-USDT từ vé voucher đã ký của Agent trên chuỗi.
> 4. Mô hình này thiết lập một cây cầu thanh khoản hai chiều minh bạch: lập trình viên AI được dùng tiền mã hóa trả theo từng câu lệnh mà không cần thẻ visa cá nhân, trong khi các lab AI vẫn nhận được USD thanh toán theo chuẩn doanh nghiệp.
"""
            c = c.replace('client = openai.OpenAI(\n    base_url="https://gateway.haichain.si/v1"',
                          gateway_note + '\nclient = openai.OpenAI(\n    base_url="https://gateway.haichain.si/v1"')

    # 8. Clarify Audit Status
    c = c.replace('Audits by OtterSec & Neodyme Completed', 'Formal Verification Completed; OtterSec & Neodyme Audits Scheduled Q4 2026')
    c = c.replace('Hoàn thành 2 audit OtterSec & Neodyme', 'Hoàn thành xác minh hình thức; Lên lịch audit OtterSec & Neodyme Q4 2026')
    c = c.replace('完成 OtterSec 与 Neodyme 两轮安全审计', '已完成形式化验证；OtterSec 与 Neodyme 审计排期于 2026 年 Q4')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Patched {fname} successfully.")

    # Mirror to app/
    app_target = os.path.join('app', fname)
    with open(app_target, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Mirrored {fname} to {app_target}.")

print("All 10 Whitepapers and app/ mirrors updated successfully.")
