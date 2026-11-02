import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Fix EN Table of Contents
for path in ['HAICHAIN_WHITEPAPER_V1.0_EN.md', 'app/HAICHAIN_WHITEPAPER_V1.0_EN.md']:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace('8.2. Stake-to-Transact Bandwidth Allocation & Real Yield Buyback/Burn Flywheel', '8.2. Stake-to-Transact Bandwidth Allocation & Value Retention Flywheel')
    t = t.replace('#82-stake-to-transact-bandwidth-allocation--real-yield-buybackburn-flywheel', '#82-stake-to-transact-bandwidth-allocation--value-retention-flywheel')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"Cleaned EN TOC in {path}")

# 2. Fix ZH lingering diagram and TOC
for path in ['HAICHAIN_WHITEPAPER_V1.0_ZH.md', 'app/HAICHAIN_WHITEPAPER_V1.0_ZH.md']:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace('真实收益回购销毁飞轮', '价值留存飞轮')
    t = t.replace('[ 50% 净利差: USDT 真实收益红利 ]', '[ 50% 净利差: 协议安全储备金 (CHGB) ]')
    t = t.replace('真实收益红利', '协议安全储备')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"Cleaned ZH in {path}")

# 3. Fix ES lingering phrase
for path in ['HAICHAIN_WHITEPAPER_V1.0_ES.md', 'app/HAICHAIN_WHITEPAPER_V1.0_ES.md']:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace('Criterios Verificables de Rendimiento Real (KPIs On-Chain)', 'Criterios Verificables de Compensación On-Chain (KPIs)')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"Cleaned ES in {path}")

# 4. Fix VI lingering phrases
for path in ['HAICHAIN_WHITEPAPER_V1.0_VI.md', 'app/HAICHAIN_WHITEPAPER_V1.0_VI.md']:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    t = t.replace('dòng tiền thực (Real Yield)', 'dòng tiền vi thanh toán thực tế')
    t = t.replace('tạo ra dòng tiền thật (Real Yield)', 'tạo ra phí bù trừ giao dịch thực tế')
    t = t.replace('doanh thu phí bù trừ thực tế (Real Yield)', 'doanh thu phí bù trừ giao thức')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"Cleaned VI in {path}")

# 5. Fix HI, KK, RU lingering phrases
for lang in ['HI', 'KK', 'RU']:
    for path in [f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md', f'app/HAICHAIN_WHITEPAPER_V1.0_{lang}.md']:
        with open(path, 'r', encoding='utf-8') as f:
            t = f.read()
        t = t.replace('Повышенная доходность от сети', 'Защита и резервы протокола')
        t = t.replace('маховик выкупа/сжигания реальной доходности', 'маховик удержания стоимости')
        t = t.replace('маховик выкупа/сжигания нақты кірістіліктің (Real Yield)', 'құнды сақтау маховигі')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Cleaned {lang} in {path}")

print("All specific whitepaper cleanups finished.")
