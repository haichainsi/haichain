import unicodedata, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def dw(s):
    return sum(2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1 for c in s)

# 1. FR Mom-Test
with open('HAICHAIN_WHITEPAPER_V1.0_FR.md', 'r', encoding='utf-8') as f:
    fr = f.read()
# Replace line 316
fr = re.sub(
    r'   \|\s*\[ 1\. PASSKEY BIOMÉTRIQUE \].*?\[ 3\. FONDS SÉCURISÉ \]\s*\|',
    '   |   [ 1. PASSKEY BIOMÉTRIQUE ] -> [ 2. ON-RAMP UNIVERSEL ] -> [ 3. FONDS SÉCURISÉ ]    |',
    fr
)
with open('HAICHAIN_WHITEPAPER_V1.0_FR.md', 'w', encoding='utf-8') as f:
    f.write(fr)
print("FR Mom-Test fixed.")

# 2. RU, HI, KK Box 9
for fpath in ['HAICHAIN_WHITEPAPER_V1.0_RU.md', 'HAICHAIN_WHITEPAPER_V1.0_HI.md', 'HAICHAIN_WHITEPAPER_V1.0_KK.md']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace top/bottom borders of HAI-VM box if they have 65 dashes
    content = content.replace(
        "  +-----------------------------------------------------------------+",
        "  +-------------------------------------------------------------------------+"
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed HAI-VM borders in {fpath}")

# 3. KO Box 3
with open('HAICHAIN_WHITEPAPER_V1.0_KO.md', 'r', encoding='utf-8') as f:
    ko = f.read()

# Replace the 5 lines that have dw > 117 in KO:
ko = ko.replace(
    "| (Fetch.ai / SingNet)  수 초 단위 BFT 지연 시간; 네이티브 유선 오프코드 부재; 명령어 OP_402_PAY (> 100,000 TPS, 0 CPI);     |",
    "| (Fetch.ai / SingNet)  수 초 단위 BFT 지연 시간; 유선 오프코드 부재;   네이티브 OP_402_PAY (> 100k TPS, 0 CPI);     |"
)
ko = ko.replace(
    "| Virtuals Protocol     Base 상의 단일 스레드 EVM 상태 쓰기 락 경쟁; 이더리움  Sealevel 32개 파티션 경합 방지 ATA; 99.999%   |",
    "| Virtuals Protocol     Base 상 단일 스레드 EVM 쓰기 락 병목; 이더리움  Sealevel 32개 파티션 경합 방지 ATA; 99.999%  |"
)
ko = ko.replace(
    "| 레거시 Web2 결제 레일 $0.30 + 2.9% 고정 기본 수수료 ($0.0002 API 호출에     순수 마이크로 효용 ($0.000001 순액 정산 하한);  |",
    "| 레거시 Web2 결제 레일 $0.30 + 2.9% 고정 기본 수수료 ($0.0002 호출에   순수 마이크로 효용 ($0.000001 순액 정산 하한);|",
)
ko = ko.replace(
    "| HTTP x402 및 Pay.sh   원시 HTTP/프록시 전송 파이프; Solana SPL 토큰상  프로그래밍 가능 정책 및 금고 계층 (호환 레이어)     |",
    "| HTTP x402 및 Pay.sh   원시 HTTP/프록시 파이프; Solana SPL 토큰 상 제약 프로그래밍 가능 정책 및 금고 계층 (호환 레이어)     |"
)
ko = ko.replace(
    "| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자 PDA 지출 포트; 400ms 미만 패닉 킬스위치; 유계   |",
    "| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자 PDA 포트; 400ms 미만 패닉 킬스위치; 유계 손실 |"
)

with open('HAICHAIN_WHITEPAPER_V1.0_KO.md', 'w', encoding='utf-8') as f:
    f.write(ko)
print("KO Box 3 lines adjusted.")
