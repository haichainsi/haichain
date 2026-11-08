import unicodedata, re, sys, glob, os

sys.stdout.reconfigure(encoding='utf-8')

def dw(s):
    return sum(2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1 for c in s)

def make_box_line(indent, inner_text, target_w):
    pref = f"{indent}|"
    inner = inner_text.rstrip()
    pad = target_w - dw(pref) - dw(inner) - 1
    if pad < 0:
        # compress spaces if possible
        excess = -pad
        inner = re.sub(r' {2,}', lambda m: ' ' * max(1, len(m.group(0)) - excess), inner, count=excess)
        pad = target_w - dw(pref) - dw(inner) - 1
    if pad < 0:
        return f"{pref}{inner}|"
    return f"{pref}{inner}{' ' * pad}|"

def fix_vi_mom_test(text):
    old_box_pat = r'  \+---------------------------------------------------------------------------------\+\n  \|                       QUY TRÌNH TIẾP CẬN VÔ HÌNH \(INVISIBLE WEB3\)               \|\n  \+---------------------------------------------------------------------------------\+\n.*?\+---------------------------------------------------------------------------------\+'
    target = 85
    indent = "  "
    border = f"{indent}+{'-' * (target - len(indent) - 2)}+"
    
    rows = [
        border,
        make_box_line(indent, "                       QUY TRÌNH TIẾP CẬN VÔ HÌNH (INVISIBLE WEB3)", target),
        border,
        make_box_line(indent, "", target),
        make_box_line(indent, "   [ 1. PASSKEY SINH TRẮC ] ──► [ 2. NẠP TIỀN 1 CHẠM ] ──► [ 3. HŨ AN TOÀN ]", target),
        make_box_line(indent, "  - Apple FaceID / TouchID     - Apple Pay / Google Pay     - Hạn mức $10.00 cô lập", target),
        make_box_line(indent, "  - WebAuthn Secure Enclave    - Instant QR / Thẻ Card      - Chống cháy ví", target),
        make_box_line(indent, "  - Không cần giữ 12 từ khóa   - Không cần KYC sàn Crypto   - Cầu chì ngắt tự động", target),
        make_box_line(indent, "", target),
        border
    ]
    new_box = "\n".join(rows)
    return re.sub(old_box_pat, new_box, text, flags=re.DOTALL)

def fix_vi_competitor_table(text):
    # Target width 117
    # Fix the HTTP x402 lines
    old_row1 = r'\|\s*\(Coinbase / Linux Fdn/ủy quyền token Solana; Lỗ hổng thiếu trần chi tiêu.*?\n'
    new_row1 = "| (Coinbase / Linux Fdn/ủy quyền token Solana; Lỗ hổng thiếu trần chi tiêu  Cây năng lực Merkle đa tầng; Hũ PDA cô lập;     |\n"
    text = re.sub(old_row1, new_row1, text)
    
    old_row2 = r'\|\s*Solana x Google Cloud\)client \(V12 audit\); Thiếu mạch ngắt tự hành on-chain.*?\n'
    new_row2 = "| Solana x Google Cloud)client (V12 audit); Thiếu mạch ngắt tự hành on-chain; Bounded Loss Theorem triệt tiêu cháy ví.     |\n"
    text = re.sub(old_row2, new_row2, text)
    return text

def fix_en_competitor_table(text):
    # Target 117
    old_row = r'\|\s*\(Coinbase / Linux Fdn/token limitation on Solana; Unconstrained client companion\); Multi-delegate Merkle capability.*?\n'
    new_row = "| (Coinbase / Linux Fdn/token limitation on Solana; Unconstrained client companion); Multi-delegate Merkle capability        |\n"
    text = re.sub(old_row, new_row, text)
    return text

def fix_es_competitor_table(text):
    old_row = r'\|\s*\(Coinbase / Linux Fdn/de 1 delegado SPL; Falta de topes de gasto en.*?\n'
    new_row = "| (Coinbase / Linux Fdn/de 1 delegado SPL; Falta de topes de gasto en   compatible); Capacidad Merkle multidelegada; Fondos  |\n"
    text = re.sub(old_row, new_row, text)
    return text

def fix_fr_competitor_table(text):
    old_row1 = r'\|\s*\(Coinbase / Linux Fdn/seul délégué SPL; Absence de plafonds de dépenses \(module complémentaire\); Arbre Merkle multi-délégué.*?\n'
    new_row1 = "| (Coinbase / Linux Fdn/seul délégué SPL; Absence de plafonds de dépenses (module complémentaire); Arbre Merkle multi-délégué  |\n"
    text = re.sub(old_row1, new_row1, text)
    
    old_row2 = r'\|\s*Solana x Google Cloud\)client \(audit V12\); Sans disjoncteur on-chain.*?\n'
    new_row2 = "| Solana x Google Cloud)client (audit V12); Sans disjoncteur on-chain     Fonds PDA isolés; Coupe-circuit d'urgence < 400ms; |\n"
    text = re.sub(old_row2, new_row2, text)
    return text

def fix_fr_mom_test(text):
    # Target 86
    old_row = r'   \|\s*\[ 1\. PASSKEY BIOMÉTRIQUE \].*?\[ 3\. FONDS SÉCURISÉ \]\s*\|\n'
    new_row = "   |   [ 1. PASSKEY BIOMÉTRIQUE ] ──► [ 2. ON-RAMP UNIVERSEL ] ──► [ 3. FONDS SÉCURISÉ ]  |\n"
    text = re.sub(old_row, new_row, text)
    return text

def fix_fr_six_invariants(text):
    # Target 83
    old_row = r'\|\s*- Feuille de Capacité Liée à un 4-Uplet: Hash\(Pubkey \|\| MaxSpend \|\| Exp \|\| Nonce\).*?\n'
    new_row = "|   - Feuille de Capacité Liée à 4-Uplet: Hash(Pubkey || MaxSpend || Exp || Nonce) |\n"
    text = re.sub(old_row, new_row, text)
    return text

def fix_he_competitor_table(text):
    # Target 117
    old_row1 = r'\|\s*HTTP x402 & Pay\.sh\s*צינורות תעבורה ופרוקסי גולמיים;.*?\n'
    new_row1 = "| HTTP x402 & Pay.sh    צינורות תעבורה ופרוקסי גולמיים; מגבלת נציג בודד  שכבת מדיניות וכספות ניתנת לתכנות; עץ מרקל     |\n"
    text = re.sub(old_row1, new_row1, text)
    
    old_row2 = r'\|\s*Solana x Google Cloud\)ללא מפסקי זרם בשרשרת וללא מנגנון חילוט לספקים\..*?\n'
    new_row2 = "| Solana x Google Cloud)ללא מפסקי זרם בשרשרת וללא מנגנון חילוט לספקים.   מפסק פאניקה < 400ms; משפט ההפסד החסום.       |\n"
    text = re.sub(old_row2, new_row2, text)
    return text

def fix_ko_mom_test(text):
    # Target 86
    old_row = r'   \|\s*\[ 1\. 생체인식 패스키 \].*?\[ 3\. 안전 지출 금고 \]\s*\|\n'
    new_row = "   |   [ 1. 생체인식 패스키 ] ──► [ 2. 범용 법정화폐 온램프 ] ──► [ 3. 안전 지출 금고 ]   |\n"
    text = re.sub(old_row, new_row, text)
    return text

def fix_ko_competitor_table(text):
    # Target 117
    old_row1 = r'\|\s*HTTP x402 및 Pay\.sh.*?프로그래밍 가능 정책 및 금고 계층.*?\n'
    new_row1 = "| HTTP x402 및 Pay.sh   원시 HTTP/프록시 전송 파이프; Solana SPL 토큰상  프로그래밍 가능 정책 및 금고 계층 (호환 레이어)     |\n"
    text = re.sub(old_row1, new_row1, text)
    
    old_row2 = r'\|\s*\(Coinbase / Linux Fdn/단일 델리게이트 제약; 클라이언트 기본 지출 상한 부재.*?\n'
    new_row2 = "| (Coinbase / Linux Fdn/단일 델리게이트 제약; 클라이언트 기본 지출 상한 부재  연동); 다중 델리게이트 Merkle 역량 트리; 격리된       |\n"
    text = re.sub(old_row2, new_row2, text)
    
    old_row3 = r'\|\s*Solana x Google Cloud\)\(V12 감사 취약점\); 온체인 자율 차단기 및 공급자.*?\n'
    new_row3 = "| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자     PDA 지출 포트; 400ms 미만 패닉 킬스위치; 유계         |\n"
    text = re.sub(old_row3, new_row3, text)
    return text

def fix_ru_box9(text):
    # Line 1001: make top border 77 chars
    old_b9_pat = r'  \+-----------------------------------------------------------------\+\n  \|             ФУНДАМЕНТАЛЬНЫЙ L1 ДЛЯ АВТОНОМНЫХ МАШИН \(HAI-VM\)            \|\n.*?\+-----------------------------------------------------------------\+'
    top = "  +-------------------------------------------------------------------------+"
    new_b9 = f"""{top}
  |             ФУНДАМЕНТАЛЬНЫЙ L1 ДЛЯ АВТОНОМНЫХ МАШИН (HAI-VM)            |
  | - Нативный опкод OP_402_PAY: Обмен ценностью в наноцентах без барьеров  |
  | - Унифицированные Soulbound DID: Прослеживаемость и правовая чистота    |
  | - Аппаратный отзыв средств < 400 мс в защищенное хранилище              |
{top}"""
    return re.sub(old_b9_pat, new_b9, text, flags=re.DOTALL)

def fix_ru_competitor_table(text):
    old_row = r'\|\s*Solana x Google Cloud\)расходов на клиенте \(аудит V12\); Нет предохрани-.*?\n'
    new_row = "| Solana x Google Cloud)расходов на клиенте (аудит V12); Нет предохрани- Изолированные PDA-хранилища; Аварийный рубильник   |\n"
    text = re.sub(old_row, new_row, text)
    return text

def apply_all():
    # Process EN
    with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
        en = f.read()
    en = fix_en_competitor_table(en)
    with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'w', encoding='utf-8') as f:
        f.write(en)
        
    # Process VI
    with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'r', encoding='utf-8') as f:
        vi = f.read()
    vi = fix_vi_mom_test(vi)
    vi = fix_vi_competitor_table(vi)
    with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'w', encoding='utf-8') as f:
        f.write(vi)
        
    # Process ES
    with open('HAICHAIN_WHITEPAPER_V1.0_ES.md', 'r', encoding='utf-8') as f:
        es = f.read()
    es = fix_es_competitor_table(es)
    with open('HAICHAIN_WHITEPAPER_V1.0_ES.md', 'w', encoding='utf-8') as f:
        f.write(es)
        
    # Process FR
    with open('HAICHAIN_WHITEPAPER_V1.0_FR.md', 'r', encoding='utf-8') as f:
        fr = f.read()
    fr = fix_fr_competitor_table(fr)
    fr = fix_fr_mom_test(fr)
    fr = fix_fr_six_invariants(fr)
    with open('HAICHAIN_WHITEPAPER_V1.0_FR.md', 'w', encoding='utf-8') as f:
        f.write(fr)
        
    # Process HE
    with open('HAICHAIN_WHITEPAPER_V1.0_HE.md', 'r', encoding='utf-8') as f:
        he = f.read()
    he = fix_he_competitor_table(he)
    with open('HAICHAIN_WHITEPAPER_V1.0_HE.md', 'w', encoding='utf-8') as f:
        f.write(he)
        
    # Process KO
    with open('HAICHAIN_WHITEPAPER_V1.0_KO.md', 'r', encoding='utf-8') as f:
        ko = f.read()
    ko = fix_ko_mom_test(ko)
    ko = fix_ko_competitor_table(ko)
    with open('HAICHAIN_WHITEPAPER_V1.0_KO.md', 'w', encoding='utf-8') as f:
        f.write(ko)
        
    # Process RU
    with open('HAICHAIN_WHITEPAPER_V1.0_RU.md', 'r', encoding='utf-8') as f:
        ru = f.read()
    ru = fix_ru_box9(ru)
    ru = fix_ru_competitor_table(ru)
    with open('HAICHAIN_WHITEPAPER_V1.0_RU.md', 'w', encoding='utf-8') as f:
        f.write(ru)
        
    print("All specific fixes applied.")

if __name__ == '__main__':
    apply_all()
