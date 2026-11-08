import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# De-risk WEBSITE_SHOWCASE_PITCH.md
with open('WEBSITE_SHOWCASE_PITCH.md', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Real Yield Staking', 'Ve-Governance Utility Staking')
text = text.replace('40% tổng doanh thu phí USDT này được chia trực tiếp', '50% phí giao thức được phân bổ vào Quỹ Dự trữ Giao thức & Bảo hiểm Rủi ro (CHGB)')
text = text.replace('60% tổng doanh thu phí USDT còn lại được hợp đồng', '50% phí giao thức được hợp đồng')
text = text.replace('60% Buyback & Burn vs 40% Real Yield Staking', '50% Buyback & Burn + 50% Protocol Reserve (CHGB)')
text = text.replace('Trả Cổ Tức Real Yield', 'Dự Trữ Bảo Hiểm CHGB')
text = text.replace('Trả cổ tức', 'Dự trữ bảo hiểm')
text = text.replace('trả cổ tức', 'dự trữ bảo hiểm')
text = text.replace('Cổ tức', 'Dự trữ')
text = text.replace('cổ tức', 'dự trữ')
text = text.replace('EBITDA $15.9M', 'Protocol Take-Rate $0.7M - $1.4M')
text = text.replace('$15.9M', '$1.4M')

with open('WEBSITE_SHOWCASE_PITCH.md', 'w', encoding='utf-8') as f:
    f.write(text)
print("De-risked WEBSITE_SHOWCASE_PITCH.md")

# De-risk HAICHAIN_SOVEREIGN_AI_L1_ENDGAME_ROADMAP.md
with open('HAICHAIN_SOVEREIGN_AI_L1_ENDGAME_ROADMAP.md', 'r', encoding='utf-8') as f:
    r_text = f.read()

r_text = r_text.replace('Staking veHAI nhận 40% doanh thu USDT thực (Real Yield), 60% dùng để Buyback & Burn',
                        'Staking veHAI nhận ưu đãi giảm phí vi mô, 50% Buyback & Burn + 50% Quỹ Dự Trữ CHGB (Không chia cổ tức, Howey Compliant)')
with open('HAICHAIN_SOVEREIGN_AI_L1_ENDGAME_ROADMAP.md', 'w', encoding='utf-8') as f:
    f.write(r_text)
print("De-risked HAICHAIN_SOVEREIGN_AI_L1_ENDGAME_ROADMAP.md")
