import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

diagrams = {
    'ES': """```
ARQUITECTURA DE FLUJO DE CAJA DEL PROTOCOLO $HAISI

[ VOLUMEN GLOBAL DE NETTING DE MÁQUINAS: $1.400M / AÑO ]
│
▼ (Take-Rate del Protocolo: 0.05% ~ 5 bps)
[ $700.000 DE INGRESO BASE ANUAL ]
│
┌────────────────┴────────────────┐
▼ (50% del Ingreso)               ▼ (50% del Ingreso)
[ RECOMPRA TWAP Y QUEMA ]           [ SEGURIDAD DEL PROTOCOLO Y CHGB ]
- Compras de mercado en DEX         - Capitalizado al Fondo CHGB
- Deflación permanente de oferta    - Protege la solvencia de la red
```""",

    'FR': """```
ARCHITECTURE DES FLUX DE TRÉSORERIE DU PROTOCOLE $HAISI

[ VOLUME GLOBAL DE COMPENSATION DES MACHINES: 1,4 Md$ / AN ]
│
▼ (Prélèvement du Protocole: 0,05% ~ 5 bps)
[ 700 000 $ DE REVENU DE BASE ANNUEL ]
│
┌────────────────┴────────────────┐
▼ (50% des Recettes)              ▼ (50% des Recettes)
[ RACHAT TWAP ET BRÛLAGE ]          [ SÉCURITÉ DU PROTOCOLE ET CHGB ]
- Achats sur DEX au marché          - Capitalisé dans le Fonds CHGB
- Déflation permanente de l'offre   - Protège la solvabilité du réseau
```""",

    'RU': """```
АРХИТЕКТУРА ДЕНЕЖНЫХ ПОТОКОВ ПРОТОКОЛА $HAISI

[ ОБЩИЙ ОБЪЕМ ВЗАИМОЗАЧЕТА МАШИН: $1.4 МЛРД / ГОД ]
│
▼ (Комиссия протокола: 0.05% ~ 5 bps)
[ $700,000 БАЗОВОГО ГОДОВОГО ДОХОДА ]
│
┌────────────────┴────────────────┐
▼ (50% дохода)                    ▼ (50% дохода)
[ TWAP ВЫКУП И СЖИГАНИЕ ]           [ БЕЗОПАСНОСТЬ ПРОТОКОЛА И CHGB ]
- Рыночные покупки на DEX          - Направляется в фонд CHGB
- Постоянная дефляция предложения  - Защищает платежеспособность сети
```""",

    'HI': """```
АРХИТЕКТУРА ДЕНЕЖНЫХ ПОТОКОВ ПРОТОКОЛА $HAISI

[ ОБЩИЙ ОБЪЕМ ВЗАИМОЗАЧЕТА МАШИН: $1.4 МЛРД / ГОД ]
│
▼ (Комиссия протокола: 0.05% ~ 5 bps)
[ $700,000 БАЗОВОГО ГОДОВОГО ДОХОДА ]
│
┌────────────────┴────────────────┐
▼ (50% дохода)                    ▼ (50% дохода)
[ TWAP ВЫКУП И СЖИГАНИЕ ]           [ БЕЗОПАСНОСТЬ ПРОТОКОЛА И CHGB ]
- Рыночные покупки на DEX          - Направляется в фонд CHGB
- Постоянная дефляция предложения  - Защищает платежеспособность сети
```""",

    'KK': """```
$HAISI ХАТТАМАСЫНЫҢ ҚАРЖЫЛЫҚ АҒЫНДАР АРХИТЕКТУРАСЫ

[ ЖАЛПЫ МАШИНАЛЫҚ КЛИРИНГ КӨЛЕМІ: $1.4 МЛРД / ЖЫЛ ]
│
▼ (Хаттама комиссиясы: 0.05% ~ 5 bps)
[ $700,000 БАЗАЛЫҚ ЖЫЛДЫҚ ТҮСІМ ]
│
┌────────────────┴────────────────┐
▼ (Түсімнің 50%-ы)                ▼ (Түсімнің 50%-ы)
[ TWAP КЕРІ САТЫП АЛУ ЖӘНЕ ӨРТЕУ ]  [ ХАТТАМА ҚАУІПСІЗДІГІ ЖӘНЕ CHGB ]
- DEX нарығынан сатып алулар        - CHGB қорына бағытталады
- Айналымды тұрақты қысқарту        - Желінің төлем қабілетін қорғайды
```""",

    'KO': """```
$HAISI 프로토콜 현금 흐름 아키텍처

[ 글로벌 기계 상계 볼륨: 연간 $14억 ($1.4B) ]
│
▼ (프로토콜 테이크레이트: 0.05% ~ 5 bps)
[ 연간 기본 수익: $700,000 USD ]
│
┌────────────────┴────────────────┐
▼ (수익의 50%)                    ▼ (수익의 50%)
[ TWAP 바이백 및 영구 소각 ]        [ 프로토콜 보안 및 CHGB 기금 ]
- DEX 시장가 매수 집행             - CHGB 보험 기금으로 적립
- 유통량의 영구적 디플레이션       - 네트워크 지불 지급 능력 수호
```""",

    'ZH': """```
$HAISI 协议现金流架构

[ 全球机器净额结算规模: 14 亿美元 / 年 ]
│
▼ (协议捕获费率: 0.05% ~ 5 bps)
[ 700,000 美元基础年收入 ]
│
┌────────────────┴────────────────┐
▼ (50% 收入)                      ▼ (50% 收入)
[ TWAP 回购并永久销毁 ]             [ 协议安全与 CHGB 风险储备 ]
- 链上 DEX 自动化二级市场回购       - 全额注入 CHGB 保险基金
- 永久缩减代币流通总量             - 捍卫网络清偿能力与偿付安全
```"""
}

# Cleanup phrases across the documents
cleanups = [
    (r'\*\s+\*\*El 40% de los Tokens Comprados:\*\*[^\n]*\n', '* **El 50% de las Tarifas Recaudadas:** Se asigna a Reservas del Protocolo y al fondo de seguros CHGB para protección de solvencia.\n'),
    (r'\*\s+\*\*40% des Jetons Rachetés:\*\*[^\n]*\n', '* **50% des Frais Collectés:** Sont alloués aux Réserves du Protocole et au fonds de garantie CHGB pour protéger la solvabilité.\n'),
    (r'\*\s+\*\*40% выкупленных токенов:\*\*[^\n]*\n', '* **50% собранных комиссий:** Направляются в Резервы протокола и фонд CHGB для защиты платежеспособности.\n'),
    (r'\*\s+\*\*매수 자산의 40%:\*\*[^\n]*\n', '* **징수된 수수료의 50%:** 프로토콜 준비금 및 CHGB 보험 기금으로 적립되어 네트워크 지급 능력을 수호합니다.\n'),
    (r'\*\s+\*\*40% 回购代币:\*\*[^\n]*\n', '* **捕获费率的 50%:** 分配至协议安全储备金与 CHGB 风险保险池，全额捍卫网络清偿能力。\n'),
    (r'\[\s*50%\s*чистой маржи:\s*Доходность в USDT\s*\]', '[ 50% чистой маржи: Резерв протокола CHGB ]'),
    (r'capturando millones en flujos de efectivo de rendimiento real', 'capturando millones en flujos de compensación de alta frecuencia'),
    (r'capturant des millions en flux de trésorerie de rendement réel', 'capturant des millions en flux de micro-règlements machine'),
    (r'аккумулируя миллионные потоки реальной доходности', 'аккумулируя миллионные потоки микрорасчетов'),
    (r'аккумулируя миллионные потоки нақты кірістіліктің \(Real Yield\)', 'аккумулируя миллионные потоки микроесеп айырысулардың'),
    (r'수백만 달러의 실제 수익 현금 흐름을 창출', '수백만 달러의 고빈도 마이크로 결제 흐름을 처리'),
    (r'捕获数以百万计的真实收益现金流', '捕获数以百万计的高频机器清算微费率流')
]

for p in glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md') + glob.glob('app/HAICHAIN_WHITEPAPER_V1.0_*.md'):
    filename = os.path.basename(p)
    m = re.search(r'HAICHAIN_WHITEPAPER_V1.0_([A-Z_]+)\.md', filename)
    if not m:
        continue
    lang = m.group(1)
    if lang in ['EN', 'VI']:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    
    orig = text
    # 1. Replace diagram
    if lang in diagrams:
        block_match = re.search(r'```[^`]*?60%[^`]*?```', text, re.DOTALL)
        if block_match:
            text = text[:block_match.start()] + diagrams[lang].strip() + text[block_match.end():]
            print(f"Replaced 60/40 diagram in {p}")
            
    # 2. Run cleanups
    for pat, rep in cleanups:
        text = re.sub(pat, rep, text)
        
    if text != orig:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved cleaned {p}")

print("Whitepaper cleanup finished.")
