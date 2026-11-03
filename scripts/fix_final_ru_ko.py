import sys, re

sys.stdout.reconfigure(encoding='utf-8')

# Fix RU, HI, KK Box 9 borders
for fn in ['HAICHAIN_WHITEPAPER_V1.0_RU.md', 'HAICHAIN_WHITEPAPER_V1.0_HI.md', 'HAICHAIN_WHITEPAPER_V1.0_KK.md']:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace the 65-dash border around HAI-VM
    text = text.replace(
        "  +-----------------------------------------------------------------+\n  |             ФУНДАМЕНТАЛЬНЫЙ L1 ДЛЯ АВТОНОМНЫХ МАШИН (HAI-VM)",
        "  +-------------------------------------------------------------------------+\n  |             ФУНДАМЕНТАЛЬНЫЙ L1 ДЛЯ АВТОНОМНЫХ МАШИН (HAI-VM)"
    )
    text = text.replace(
        "  | - Аппаратный отзыв средств < 400 мс в защищенное хранилище              |\n  +-----------------------------------------------------------------+",
        "  | - Аппаратный отзыв средств < 400 мс в защищенное хранилище              |\n  +-------------------------------------------------------------------------+"
    )
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed {fn} Box 9")

# Fix KO Box 1 & Box 3
with open('HAICHAIN_WHITEPAPER_V1.0_KO.md', 'r', encoding='utf-8') as f:
    ko = f.read()

# Box 1 lines 186 and 188:
ko = ko.replace(
    "|  프롬프트 주입 탈취 위험 신용카드 전액 무단 결제       마스터 EOA 지갑 자산 전액 탈취 수학적으로 제로 (PDA) |",
    "|  프롬프트 주입 위험      카드 전액 무단 결제           마스터 EOA 자산 전액 탈취  수학적 0 (PDA)    |"
)
ko = ko.replace(
    "|  긴급 취소 / 패닉 회수   지급 거절 절차 (60-90일 소요) 온체인 영구적 자산 손실    원탭 물리적 패닉 (<400ms)|",
    "|  긴급 패닉 회수          지급 거절 절차 (60-90일 소요) 온체인 영구적 자산 손실    1-탭 패닉 (<400ms)|"
)

# Box 3 lines 273 and 275:
ko = ko.replace(
    "| HTTP x402 및 Pay.sh   원시 HTTP/프록시 파이프; Solana SPL 토큰 상 제약 프로그래밍 가능 정책 및 금고 계층 (호환 레이어)     |",
    "| HTTP x402 및 Pay.sh   원시 HTTP/프록시 파이프; SPL 제약        프로그래밍 가능 정책 및 금고 계층 (호환 레이어)     |"
)
ko = ko.replace(
    "| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자 PDA 포트; 400ms 미만 패닉 킬스위치; 유계 손실 |",
    "| Solana x Google Cloud)(V12 감사); 온체인 자율 차단기 및 공급자 PDA 포트; 400ms 미만 패닉 킬스위치; 손실 한계 정리|"
)

with open('HAICHAIN_WHITEPAPER_V1.0_KO.md', 'w', encoding='utf-8') as f:
    f.write(ko)
print("Fixed KO Box 1 and Box 3")
