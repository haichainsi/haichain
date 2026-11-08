import unicodedata, re, sys, glob

sys.stdout.reconfigure(encoding='utf-8')

def dw(s):
    return sum(2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1 for c in s)

def fix_specific_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Fix Cross-Paradigm Minimum fee line in all languages to width 102
    # In ES:
    text = text.replace(
        "|  Tarifa Mínima Práctica Tarifa fija de $0.30       $0.02 - $0.50 pico de gas  $0.000001 (Compresión 1,000:1 / $0.001 Base)  |",
        "|  Tarifa Mínima Práctica Tarifa fija de $0.30       $0.02 - $0.50 pico de gas  $0.000001 (Netting)   |"
    )
    # In FR:
    text = text.replace(
        "|  Frais Minimum Pratique Frais fixes de $0.30       $0.02 - $0.50 pic de gas   $0.000001 (Compression 1 000:1 / $0,001 Base)  |",
        "|  Frais Minimum Pratique Frais fixes de $0.30       $0.02 - $0.50 pic de gas   $0.000001 (Netting)   |"
    )
    # In KO:
    text = text.replace(
        "|  실질 최소 수수료        $0.30 고정 기본 수수료        $0.02 - $0.50 가스 급증    $0.000001 (1,000:1 압축 네팅 / $0.001 베이스) |",
        "|  실질 최소 수수료        $0.30 고정 기본 수수료        $0.02 - $0.50 가스 급증    $0.000001 (Netting)   |"
    )
    # In HE:
    text = text.replace(
        "|  Minimum Practical Fee  $0.30 fixed fee floor     $0.02 - $0.50 gas spike    $0.000001 (דחיסת 1,000:1 / $0.001 בסיס)   |",
        "|  Minimum Practical Fee  $0.30 fixed fee floor     $0.02 - $0.50 gas spike    $0.000001 (Netting)   |"
    )

    # 2. Fix Mom-Test box in VI:
    old_vi_mom = """  +---------------------------------------------------------------------------------+
  |                       QUY TRÌNH TIẾP CẬN VÔ HÌNH (INVISIBLE WEB3)               |
  +---------------------------------------------------------------------------------+
  |                                                                                 |
  |   [ 1. PASSKEY SINH TRẮC ] ───► [ 2. NẠP TIỀN 1 CHẠM ] ───► [ 3. HŨ TIỀN AN TOÀN ] |
  |  - Apple FaceID / TouchID     - Apple Pay / Google Pay   - Hạn mức $10.00 cô lập |
  |  - WebAuthn Secure Enclave    - Chuyển khoản Instant QR / Card- Chống cháy ví tuyệt đối |
  |  - Không cần giữ 12 từ khóa   - Không cần KYC sàn Crypto - Cầu chì ngắt mạch tự động |
  |                                                                                 |
  +---------------------------------------------------------------------------------+"""
    
    new_vi_mom = """  +---------------------------------------------------------------------------------+
  |                       QUY TRÌNH TIẾP CẬN VÔ HÌNH (INVISIBLE WEB3)               |
  +---------------------------------------------------------------------------------+
  |                                                                                 |
  |   [ 1. PASSKEY SINH TRẮC ] ───► [ 2. NẠP TIỀN 1 CHẠM ] ───► [ 3. HŨ TIỀN AN TOÀN ]   |
  |  - Apple FaceID / TouchID     - Apple Pay / Google Pay     - Hạn mức $10.00 cô lập|
  |  - WebAuthn Secure Enclave    - Instant QR / Thẻ Card      - Chống cháy ví tuyệt đối|
  |  - Không cần 12 từ khóa       - Không cần KYC sàn Crypto   - Cầu chì ngắt tự động  |
  |                                                                                 |
  +---------------------------------------------------------------------------------+"""
    text = text.replace(old_vi_mom, new_vi_mom)

    # 3. Fix VI Competitor Table lines 155-156
    text = text.replace(
        "| (Coinbase / Linux Fdn/ủy quyền token Solana; Lỗ hổng thiếu trần chi tiêu  Cây năng lực đa tầng (Multi-delegate); Hũ PDA   |",
        "| (Coinbase / Linux Fdn/ủy quyền token Solana; Lỗ hổng thiếu trần chi tiêu  Cây năng lực Merkle đa tầng; Hũ PDA cô lập;     |"
    )
    text = text.replace(
        "| Solana x Google Cloud)client (V12 audit); Thiếu mạch ngắt tự hành on-chain cô lập; Bounded Loss Theorem triệt tiêu rủi ro |",
        "| Solana x Google Cloud)client (V12 audit); Thiếu mạch ngắt tự hành on-chain; Bounded Loss Theorem triệt tiêu cháy ví.     |"
    )

    # 4. Fix Mom-Test box in FR:
    text = text.replace(
        "   |   [ 1. PASSKEY BIOMÉTRIQUE ] ───► [ 2. ON-RAMP UNIVERSEL ] ───► [ 3. FONDS SÉCURISÉ ]|",
        "   |   [ 1. PASSKEY BIOMÉTRIQUE ] ──► [ 2. ON-RAMP UNIVERSEL ] ──► [ 3. FONDS SÉCURISÉ ] |"
    )

    # 5. Fix Mom-Test box in KO:
    text = text.replace(
        "   |   [ 1. 생체인식 패스키 ] ───► [ 2. 범용 법정화폐 온램프 ] ───► [ 3. 안전 지출 금고 ] |",
        "   |   [ 1. 생체인식 패스키 ] ───► [ 2. 범용 법정화폐 온램프 ] ───► [ 3. 안전 지출 금고 ]   |"
    )

    # 6. Fix Mom-Test box in ES:
    text = text.replace(
        "   |   [ 1. PASSKEY BIOMÉTRICA ] ───► [ 2. ON-RAMP UNIVERSAL ] ───► [ 3. FONDO SEGURO ]|",
        "   |   [ 1. PASSKEY BIOMÉTRICA ] ───► [ 2. ON-RAMP UNIVERSAL ] ───► [ 3. FONDO SEGURO ] |"
    )

    # 7. Fix EN Box 3 Line 284:
    text = text.replace(
        "| (Coinbase / Linux Fdn/token limitation on Solana; Unconstrained client companion); Multi-delegate Merkle capability;|",
        "| (Coinbase / Linux Fdn/token limitation on Solana; Unconstrained client companion); Multi-delegate Merkle capability |"
    )

    # 8. Fix ES Box 3 Line 275:
    text = text.replace(
        "| (Coinbase / Linux Fdn/de 1 delegado SPL; Falta de topes de gasto en    compatible); Capacidad Merkle multidelegada; Fondos|",
        "| (Coinbase / Linux Fdn/de 1 delegado SPL; Falta de topes de gasto en   compatible); Capacidad Merkle multidelegada; Fondos |"
    )

    # 9. Fix FR Box 3 Lines 274-276:
    text = text.replace(
        "| HTTP x402 & Pay.sh    Canaux de transport HTTP/proxy bruts; Limite d'un Couche de Politiques et de Coffre Programmable     |",
        "| HTTP x402 & Pay.sh    Canaux de transport HTTP/proxy bruts; Limite d'un Couche de Politiques et Coffre Programmable        |"
    )
    text = text.replace(
        "| (Coinbase / Linux Fdn/seul délégué SPL; Absence de plafonds de dépenses (module complémentaire); Arbre Merkle multi-délégué;|",
        "| (Coinbase / Linux Fdn/seul délégué SPL; Absence de plafonds de dépenses (module complémentaire); Arbre Merkle multi-délégué |"
    )
    text = text.replace(
        "| Solana x Google Cloud)client (audit V12); Sans disjoncteur on-chain ni  Fonds PDA isolés; Coupe-circuit d'urgence < 400ms; |",
        "| Solana x Google Cloud)client (audit V12); Sans disjoncteur on-chain     Fonds PDA isolés; Coupe-circuit d'urgence < 400ms; |"
    )

    # 10. Fix FR Box 5 Line 413:
    text = text.replace(
        "|   - Feuille de Capacité Liée à un 4-Uplet: Hash(Pubkey || MaxSpend || Exp || Nonce)|",
        "|   - Feuille de Capacité Liée à un 4-Uplet: Hash(Pubkey || MaxSpend || Exp || Nonce)      |"
    )

    # 11. Fix KO Box 3 Lines 273-275:
    text = text.replace(
        "| HTTP x402 및 Pay.sh   원시 HTTP/프록시 전송 파이프; Solana SPL 토큰상  프로그래밍 가능 정책 및 금고 계층 (드롭인 호환 |",
        "| HTTP x402 및 Pay.sh   원시 HTTP/프록시 전송 파이프; Solana SPL 토큰상  프로그래밍 가능 정책 및 금고 계층 (호환 레이어)|"
    )
    text = text.replace(
        "| (Coinbase / Linux Fdn/단일 델리게이트 제약; 클라이언트 기본 지출 상한 부재  연동); 다중 델리게이트 Merkle 역량 트리; 격리된 |",
        "| (Coinbase / Linux Fdn/단일 델리게이트 제약; 클라이언트 기본 지출 상한 부재  연동); 다중 델리게이트 Merkle 역량 트리; 격리된  |"
    )
    text = text.replace(
        "| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자     PDA 지출 포트; 400ms 미만 패닉 킬스위치; 유계   |",
        "| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자     PDA 지출 포트; 400ms 미만 패닉 킬스위치; 유계    |"
    )

    # 12. Fix RU Box 3 Line 287:
    text = text.replace(
        "| Solana x Google Cloud)расходов на клиенте (аудит V12); Нет предохрани- Изолированные PDA-хранилища; Аварийный рубильник   |",
        "| Solana x Google Cloud)расходов на клиенте (аудит V12); Нет предохрани- Изолированные PDA-хранилища; Аварийный рубильник    |"
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

for f in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    fix_specific_file(f)
print("Applied manual fixes to specific files.")
