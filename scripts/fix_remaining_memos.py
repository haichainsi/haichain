import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Fix HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md', 'r', encoding='utf-8') as f:
    vi_content = f.read()

# Replace lines 70-76 in VI.md with the derisked section 3 from VI_EN.md
old_sec3 = """### 3. TIERED REVENUE ENGINE ($15.9M ARR) & REAL YIELD CASH FLOW
* **Blended 3-Tier Settlement Engine:**
* **Tier 1 (Consumer AI):** 100,000 lightweight agents @ $3.40/mo = $4.1M volume ($4.1k protocol fee @ 0.10%).
* **Tier 2 (B2B Agent Swarms):** 15,000 enterprise agent workflows ($350/mo average volume) = $63M volume ($63k fee).
* **Tier 3 (Institutional GPU & API Clearing):** 1,200 enterprise pipelines ($50,000/mo volume) = $720M volume ($1.44M - $3.6M fee @ 0.20-0.50%).
* **Ecosystem Services:** zkTLS Verification Fees ($0.001/proof) + Priority State Channel Liquidity Spreads generate robust blended $15.9M ARR.
* **Token Value Accrual:** 50% of all global settlement fees fund automated continuous **Buyback & Burn**; 50% distributed as **Real Yield (USDC/USDT)** to veHAI governance stakers."""

new_sec3 = """### 3. TIERED MICRO-FEE CAPACITY & DEFENSIBLE TOKENOMICS ($0.7M - $1.4M PROTOCOL TAKE-RATE)
* **Blended 3-Tier Settlement Engine:**
* **Tier 1 (Consumer AI):** 100,000 lightweight agents @ $3.40/mo = $4.1M volume ($4.1k protocol fee @ 0.10%).
* **Tier 2 (B2B Agent Swarms):** 15,000 enterprise agent workflows ($350/mo average volume) = $63M volume ($63k fee).
* **Tier 3 (Institutional GPU & API Clearing):** 1,200 enterprise pipelines ($50,000/mo volume) = $720M volume ($1.44M - $3.6M fee @ 0.20-0.50%).
* **Protocol Take-Rate Economics:** At a conservative 0.05% - 0.10% protocol take-rate on $1.4B annualized network micro-settlement capacity, HAICHAIN generates a sustainable **$700,000 - $1,400,000 USD/year** in protocol reserves (strictly matching Whitepaper Section 7).
* **Token Value Accrual (Howey Test Compliant Utility):** 50% of protocol fees fund automated continuous **Buyback & Burn**; 50% allocated to Protocol Reserves & CHGB. Zero passive dividend distributions (non-security utility architecture)."""

if old_sec3 in vi_content:
    vi_content = vi_content.replace(old_sec3, new_sec3)
    with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md', 'w', encoding='utf-8') as f:
        f.write(vi_content)
    print("Fixed HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md")

# Fix KK.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_KK.md', 'r', encoding='utf-8') as f:
    kk_content = f.read()

kk_target = "* **Токен құнын арттыру:** Барлық жаһандық комиссияның 50%-ы **Кері сатып алу және өртеуге (Buyback & Burn)** жұмсалады; 50%-ы veHAI стейкерлеріне **Таза стейблкоин (USDC/USDT)** ретінде Real Yield түрінде таратылады."
kk_replacement = "* **Токен құнын арттыру (Howey тест талаптарына сәйкес):** Хаттама комиссияларының 50%-ы автоматты түрде **Кері сатып алу және өртеуге (Buyback & Burn)** жұмсалады; 50%-ы Протокол резервтеріне және CHGB сақтық қорына бөлінеді (пассивті дивидендсіз, утилитарлық модель)."
if kk_target in kk_content:
    kk_content = kk_content.replace(kk_target, kk_replacement)
    with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_KK.md', 'w', encoding='utf-8') as f:
        f.write(kk_content)
    print("Fixed HAICHAIN_PRESEED_ONE_PAGER_MEMO_KK.md")

# Fix KO.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_KO.md', 'r', encoding='utf-8') as f:
    ko_content = f.read()

ko_target = "* **토큰 가치 축적:** 글로벌 결제 수수료의 50%는 자동 **바이백 및 소각(Buyback & Burn)**에 투입되며, 50%는 veHAI 거버넌스 스테이커에게 **순수 스테이블코인(USDC/USDT) 리얼 일드(Real Yield)**로 배분됩니다."
ko_replacement = "* **토큰 가치 축적 (Howey 테스트 준수 유틸리티):** 프로토콜 수수료의 50%는 자동 **바이백 및 영구 소각(Buyback & Burn)**에 투입되며, 50%는 프로토콜 준비금 및 CHGB(분쟁/보험 기금)에 배분됩니다. 수동적 배당금 분배가 일체 없는 비증권형 유틸리티 아키텍처입니다."
if ko_target in ko_content:
    ko_content = ko_content.replace(ko_target, ko_replacement)
    with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_KO.md', 'w', encoding='utf-8') as f:
        f.write(ko_content)
    print("Fixed HAICHAIN_PRESEED_ONE_PAGER_MEMO_KO.md")

# Fix ZH.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_ZH.md', 'r', encoding='utf-8') as f:
    zh_content = f.read()

zh_target = re.search(r'\*\s+\*\*代币价值捕获[^\n]*\n', zh_content)
if zh_target:
    zh_old_line = zh_target.group(0)
    zh_new_line = "* **代币价值捕获 (符合 Howey 测试的功能型实用设计):** 协议微费率的 50% 注入自动持续 **回购与永久销毁 (Buyback & Burn)**；50% 分配至协议储备金与硬件燃气保证金 (CHGB) 风险保险池。零被动股息分红 (纯正非证券级实用架构)。\n"
    zh_content = zh_content.replace(zh_old_line, zh_new_line)
    with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_ZH.md', 'w', encoding='utf-8') as f:
        f.write(zh_content)
    print("Fixed HAICHAIN_PRESEED_ONE_PAGER_MEMO_ZH.md")

print("Memos update script finished.")
