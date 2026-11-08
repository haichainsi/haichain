import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Diagram replacements for each language
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

def update_ch8_diagram(wp_path):
    filename = os.path.basename(wp_path)
    lang_match = re.search(r'HAICHAIN_WHITEPAPER_V1.0_([A-Z_]+)\.md', filename)
    if not lang_match:
        return
    lang = lang_match.group(1)
    if lang not in diagrams:
        return
    
    with open(wp_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Locate the old diagram in Chapter 8
    # Search for pattern around 60% and 40% in code block
    old_diag_pat = r'```[^\n]*\n(?:ARQUITECTURA|ARCHITECTURE|АРХИТЕКТУРА|\$HAISI)[^\n]*\n.*?▼\s*\((?:60%|수익의\s*60%)[^\n]*\n.*?```'
    m = re.search(old_diag_pat, text, re.DOTALL)
    if m:
        text = text[:m.start()] + diagrams[lang].strip() + text[m.end():]
        with open(wp_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated Chapter 8 intro diagram in {wp_path}")
    else:
        print(f"Old diagram not found in {wp_path}")

for p in glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md') + glob.glob('app/HAICHAIN_WHITEPAPER_V1.0_*.md'):
    update_ch8_diagram(p)

print("Chapter 8 intro diagram update finished.")
