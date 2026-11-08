import re, sys, unicodedata

sys.stdout.reconfigure(encoding='utf-8')

def dw(s):
    return sum(2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1 for c in s)

# Perfect 117-char rows for HTTP x402 across all languages:

en_rows = """| HTTP x402 & Pay.sh    Raw HTTP/proxy transport pipes; Single-delegate Programmable Policy & Vault Layer (drop-in  |
| (Coinbase / Linux Fdn/token limit on Solana; No client spending caps  companion); Multi-delegate Merkle capability;|
| Solana x Google Cloud)(V12 audit CVEs); Lacks on-chain kill switch    Isolated PDA pots; Panic Circuit Breaker in  |
|                       and missing provider slashing mechanisms.       < 400ms; Bounded Loss Theorem (zero drain).  |"""

vi_rows = """| HTTP x402 & Pay.sh    Chỉ là ống dẫn HTTP/proxy thô; Giới hạn 1       Lớp Quản trị Chính sách & Hũ PDA cô lập;     |
| (Coinbase / Linux Fdn/delegate token Solana; Lỗ hổng thiếu trần chi   Cây năng lực Merkle đa tầng (Multi-delegate);|
| Solana x Google Cloud)tiêu client (V12 audit); Thiếu mạch ngắt tự     Mạch ngắt tự hành < 400ms; Bounded Loss      |
|                       hành on-chain và thiếu cơ chế phạt nhà mạng.    triệt tiêu hoàn toàn rủi ro cháy ví.         |"""

es_rows = """| HTTP x402 y Pay.sh    Tuberías de transporte HTTP/proxy brutas; Límite Capa de Políticas y Bóvedas Programables    |
| (Coinbase / Linux Fdn/de 1 delegado SPL; Falta de topes de gasto en   (capa compatible); Capacidad Merkle multi-   |
| Solana x Google Cloud)clientes (auditoría V12); Sin disyuntores        delegada; Fondos PDA aislados; Disyuntor en  |
|                       autónomos on-chain ni slashing a proveedores.   < 400ms; Teorema de Pérdida Acotada.         |"""

fr_rows = """| HTTP x402 & Pay.sh    Canaux de transport HTTP/proxy bruts; Limite d'un Couche de Politiques et Coffre Programmable |
| (Coinbase / Linux Fdn/seul délégué SPL; Absence de plafonds de         (module d'extension); Arbre Merkle multi-    |
| Solana x Google Cloud)dépenses client (audit V12); Sans disjoncteur    délégué; Fonds PDA isolés; Coupe-circuit en  |
|                       on-chain ni pénalité (slashing) fournisseur.    < 400ms; Théorème de Perte Bornée.           |"""

ko_rows = """| HTTP x402 및 Pay.sh   원시 HTTP/프록시 전송 파이프; Solana SPL 토큰상  프로그래밍 가능 정책 및 금고 계층 (호환 레이어)     |
| (Coinbase / Linux Fdn/단일 델리게이트 제약; 클라이언트 지출 상한 부재 다중 델리게이트 Merkle 역량 트리; 격리된       |
| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자 PDA 지출 포트; 400ms 미만 패닉 킬스위치; 유계   |
|                       슬래싱 메커니즘 부재.                           손실 정리 증명 (지갑 탈취 원천 차단).         |"""

ru_rows = """| HTTP x402 и Pay.sh    Базовые HTTP/прокси транспортные каналы;         Программируемый слой политик и хранилищ     |
| (Coinbase / Linux Fdn/Ограничение SPL в 1 делегата; Отсутствие лимитов (совместимый слой); Дерево возможностей     |
| Solana x Google Cloud)расходов на клиенте (аудит V12); Нет предохрани- Merkle; Изолированные PDA-хранилища;       |
|                       телей и слэшинга поставщиков на блокчейне.       Аварийный рубильник < 400 мс; Защита.       |"""

hi_rows = """| HTTP x402 & Pay.sh    कच्चे HTTP/प्रॉक्सी पाइप; सोलाना पर 1 डेलिगेट की  प्रोग्रामेबल नीति और वॉल्ट लेयर (ड्रॉप-इन); |
| (Coinbase / Linux Fdn/सीमा; क्लाइंट-साइड खर्च सीमा का अभाव (V12 ऑडिट); मल्टी-डेलिगेट Merkle क्षमता ट्री; पृथक PDA |
| Solana x Google Cloud)ऑन-चेन सर्किट ब्रेकर और प्रदाता स्लैशिंग तंत्र   वॉल्ट; 400ms से कम में पैनिक कटऑफ; बाउंडेड  |
|                       की कमी।                                         लॉस प्रमेय (वॉल्ट ड्रेन से पूर्ण सुरक्षा)।   |"""

kk_rows = """| HTTP x402 және Pay.sh Қарапайым HTTP/прокси көлік құбырлары;          Бағдарламаланатын саясат және сейф қабаты   |
| (Coinbase / Linux Fdn/Solana SPL-де 1 ғана делегат шектеуі; Клиентте   (үйлесімді серіктес); Көп делегатты Merkle; |
| Solana x Google Cloud)шығыс шектерінің жоқтығы (V12 аудиті); Ончейн    Оқшауланған PDA сейфтері; 400 мс жылдам     |
|                       ажыратқыштар мен слэшингтің жоқтығы.            паника өшіргіші; Шектелген шығын теоремасы.  |"""

def replace_matrix_rows(filepath, new_rows_block):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Pattern to match the HTTP x402 row block in the competitor matrix
    pattern = r'\|\s*HTTP x402[^\n]*\n(?:\|\s*(?:\(Coinbase|Solana| \s*)[^\n]*\n)+'
    
    m = re.search(pattern, text)
    if m:
        text = text[:m.start()] + new_rows_block + "\n" + text[m.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Replaced HTTP x402 row in {filepath}")
    else:
        print(f"Could not find HTTP x402 pattern in {filepath}")

replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_EN.md', en_rows)
replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_VI.md', vi_rows)
replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_ES.md', es_rows)
replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_FR.md', fr_rows)
replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_KO.md', ko_rows)
replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_RU.md', ru_rows)
replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_HI.md', hi_rows)
replace_matrix_rows('HAICHAIN_WHITEPAPER_V1.0_KK.md', kk_rows)
