import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Translations of Section 8.2 for each language
wp_sec8_content = {
    'ES': """### 8.2. Asignación de Ancho de Banda por Staking y Volante de Retención de Valor
Para neutralizar permanentemente la **Espiral de Muerte de Velocidad del Token (Teorema de Pfeffer)** y eliminar por completo los riesgos de clasificación como valor bajo la prueba Howey de EE. UU. y el reglamento MiCA de la UE, Haichain estructura $HAISI como un **Activo de Utilidad Productiva**:

```
           VOLANTE DE STAKING DE UTILIDAD Y RETENCIÓN DE VALOR DE HAICHAIN
           
       [ Flotas de Agentes Empresariales Ejecutando Micro-Llamadas de Alta Frecuencia ]
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[ Niveles Opcionales de Staking veHAISI ]       [ Ingresos de Comisiones en USDC/USDT Puro ]
├── Ancho de banda otorgado por capital bloqueado  ├── Comisión de compensación del 0.05%
│   Asignación Diaria = k * sqrt(Staked * Tiempo)  │   estrictamente en stablecoins verificadas
└── Descuentos escalonados de tarifas hasta el 80% └── 100% canalizado a la Tesorería del Protocolo
           │                                                 │
           ▼                                                 ▼
[ Oferta Circulante de $HAISI Contraída ]       [ Motor Autónomo de Recompra TWAP ]
                                                ├── 50% de Ingresos: Recompra TWAP y QUEMA PERMANENTE
                                                │   (Oferta Deflacionaria Neta)
                                                └── 50% de Ingresos: Reserva del Protocolo
                                                    (Fondo de Seguro CHGB)
```

#### 1. Arquitectura de Doble Riel y Niveles Opcionales de Descuento veHAISI
Haichain implementa un sistema de doble riel sin fricción:
- **Agentes Estándar y Desarrolladores:** Pagan por transacción estrictamente en stablecoins verificadas (USDC/USDT) sin staking obligatorio de tokens, preservando la ergonomía "Invisible Web3".
- **Enjambres Empresariales y Flotas de Alto Volumen:** Pueden bloquear opcionalmente $HAISI (`veHAISI`) para privilegios de infraestructura:
  $$\\text{Asignación Diaria de Transacciones} = k \\cdot \\sqrt{\\text{Staked } \\$HAISI \\times \\text{Duración del Bloqueo}}$$
  * *Descuentos Escalonados de Tarifas:* Hasta un 80% de reducción en comisiones netas de compensación al bloquear de 3 a 36 meses.
  * *Enrutamiento de Vía Rápida Dedicado Sub-5ms:* Enrutamiento de mempool dedicado para enjambres de misión crítica.
  * *Compensación de Fondo sin Gas:* Reclamación de alquiler patrocinada por el protocolo y limpieza de anuladores.

#### 2. Motor Programático de Recompra y Deflación
En lugar de distribuir dividendos directos en efectivo (lo que introduce graves riesgos de clasificación como valor bajo las regulaciones de la SEC y MiCA), el 100% de las comisiones del protocolo recaudadas se enrutan mediante contrato inteligente:
- **50% Recompra y Quema Autónoma TWAP:** Recompra diaria programática en los DEX de Solana (Raydium, Meteora) y destrucción criptográfica inmediata (`burn`), contrayendo continuamente la oferta circulante sin generar expectativas de ganancias por dividendos.
- **50% Reservas del Protocolo y Bono de Gas de Hardware Criptográfico (CHGB):** Colateralización directa del fondo automatizado de resolución de disputas, amortiguador de seguros de relayers y respaldo de liquidación cross-chain.
""",

    'FR': """### 8.2. Allocation de Bande Passante par Staking et Volant de Rétention de Valeur
Pour neutraliser définitivement la **Spirale Mortelle de Vélocité des Jetons (Théorème de Pfeffer)** tout en éliminant complètement les risques de qualification en titre financier (test de Howey aux États-Unis et réglementation MiCA dans l'UE), Haichain structure $HAISI comme un **Actif d'Utilité Productive**:

```
          VOLANT DE STAKING D'UTILITÉ ET DE RÉTENTION DE VALEUR HAICHAIN
          
       [ Flottes d'Agents Entreprise Exécutant des Micro-Appels Haute Fréquence ]
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[ Niveaux Optionnels de Staking veHAISI ]       [ Revenus de Micro-Frais en USDC/USDT Pur ]
├── Bande passante accordée via capital verrouillé ├── Commission de compensation de 0.05%
│   Allocation Quotidienne = k * sqrt(Staké * Temps)│   strictement en stablecoins vérifiés
└── Réductions échelonnées de frais jusqu'à 80%    └── 100% acheminé vers la Trésorerie du Protocole
           │                                                 │
           ▼                                                 ▼
[ Masse Circulante de $HAISI Contractée ]       [ Moteur Autonome de Rachat TWAP ]
                                                ├── 50% des Recettes: Rachat TWAP et BRÛLAGE DÉFINITIF
                                                │   (Masse Monétaire Déflationniste Nette)
                                                └── 50% des Recettes: Réserve du Protocole
                                                    (Fonds d'Assurance CHGB)
```

#### 1. Architecture à Double Voie et Niveaux Optionnels de Réduction veHAISI
Haichain applique un système à double voie sans friction:
- **Agents Standards et Développeurs:** Paient par transaction strictement en stablecoins vérifiés (USDC/USDT) sans staking obligatoire de jetons, préservant l'ergonomie "Invisible Web3".
- **Essaims Entreprise et Flottes à Haut Volume:** Peuvent verrouiller optionnellement $HAISI (`veHAISI`) pour des privilèges d'infrastructure:
  $$\\text{Allocation Quotidienne de Transactions} = k \\cdot \\sqrt{\\text{Staké } \\$HAISI \\times \\text{Durée de Verrouillage}}$$
  * *Réductions de Frais Échelonnées:* Jusqu'à 80% de réduction sur les frais nets de compensation pour un verrouillage de 3 à 36 mois.
  * *Routage Rapide Dédié Sub-5ms:* Routage mempool dédié pour les essaims critiques.
  * *Compensation d'Arrière-Plan Sans Gas:* Récupération de loyer sponsorisée par le protocole et nettoyage des nullifiers.

#### 2. Moteur Programmatique de Rachat et Déflation
Plutôt que de distribuer des dividendes directs en espèces (ce qui introduit d'importants risques de requalification juridique sous les réglementations SEC et MiCA), 100% des frais de protocole collectés sont acheminés par contrat intelligent:
- **50% Rachat et Brûlage Autonome TWAP:** Rachat quotidien automatisé sur les DEX Solana (Raydium, Meteora) et destruction cryptographique immédiate (`burn`), contractant continuellement la masse circulante sans créer d'attente de profits sous forme de dividendes.
- **50% Réserves du Protocole et Caution de Gas Matériel Cryptographique (CHGB):** Collatéralisation directe du pool automatisé de règlement des litiges, matelas d'assurance des relayeurs et filet de sécurité de liquidation cross-chain.
""",

    'RU': """### 8.2. Распределение пропускной способности через стейкинг и маховик удержания стоимости
Для окончательного предотвращения **Смертельной спирали скорости обращения токенов (теорема Пфеффера)** и полного исключения рисков признания ценной бумагой по тесту Хауи в США и регламенту MiCA в ЕС, Haichain позиционирует $HAISI как **Продуктивный утилитарный актив**:

```
        МАХОВИК УТИЛИТАРНОГО СТЕЙКИНГА И УДЕРЖАНИЯ СТОИМОСТИ HAICHAIN
        
       [ Корпоративные флоты агентов, выполняющие высокочастотные микровызовы ]
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[ Опциональные уровни стейкинга veHAISI ]       [ Чистый доход протокола в USDC/USDT ]
├── Пропускная способность за заблокированный капитал ├── Комиссия за взаимозачет 0.05%
│   Дневной лимит = k * sqrt(Стейкинг * Время)   │   исключительно в проверенных стейблкоинах
└── Ступенчатые скидки на комиссии до 80%        └── 100% направляется в казначейство протокола
           │                                                 │
           ▼                                                 ▼
[ Сокращение оборотного предложения $HAISI ]    [ Автономный механизм выкупа TWAP ]
                                                ├── 50% дохода: TWAP выкуп и БЕЗВОЗВРАТНОЕ СЖИГАНИЕ
                                                │   (Чистая дефляционная эмиссия)
                                                └── 50% дохода: Резерв протокола
                                                    (Страховой фонд CHGB)
```

#### 1. Двухрельсовая архитектура и опциональные уровни скидок veHAISI
Haichain реализует бесшовную двухрельсовую систему:
- **Стандартные агенты и разработчики:** Оплачивают транзакции исключительно проверенными стейблкоинами (USDC/USDT) без обязательного стейкинга токенов, сохраняя эргономику «Invisible Web3».
- **Корпоративные рои и высоконагруженные флоты:** Могут опционально блокировать $HAISI (`veHAISI`) для получения инфраструктурных привилегий:
  $$\\text{Дневной лимит транзакций} = k \\cdot \\sqrt{\\text{Стейкинг } \\$HAISI \\times \\text{Срок блокировки}}$$
  * *Ступенчатые скидки:* До 80% снижения чистых комиссий клиринга при блокировке от 3 до 36 месяцев.
  * *Выделенная быстрая маршрутизация (<5 мс):* Прямой доступ к мемпулу для критически важных роев.
  * *Фоновый клиринг без газа:* Спонсируемый протоколом возврат ренты хранилищ и очистка нуллификаторов.

#### 2. Программный механизм выкупа и дефляции
Вместо распределения прямых денежных дивидендов (что создает критические регуляторные риски ценных бумаг согласно SEC и MiCA), 100% собранных комиссий протокола программно распределяются смарт-контрактом:
- **50% Автономный TWAP выкуп и сжигание:** Программный ежедневный выкуп на DEX Solana (Raydium, Meteora) и немедленное криптографическое уничтожение (`burn`), непрерывно сжимающее доступное предложение без создания ожиданий прибыли от дивидендов.
- **50% Резервы протокола и аппаратный залог газа (CHGB):** Прямое обеспечение пула автоматического разрешения споров, страховой буфер ретрансляторов и ликвидационный щит.
""",

    'KO': """### 8.2. 스테이킹 기반 대역폭 할당 및 가치 유지 플라이휠
토큰 유통 속도 증가로 인한 가치 희석(**페퍼의 정리 / Pfeffer's Theorem**)을 근본적으로 차단하고 미국 SEC Howey 테스트 및 EU MiCA 증권성 분류 리스크를 원천 제거하기 위해, Haichain은 $HAISI를 **생산적 유틸리티 자산**으로 설계했습니다:

```
           HAICHAIN 유틸리티 스테이킹 및 가치 유지 플라이휠
           
       [ 초고주파 마이크로 호출을 실행하는 엔터프라이즈 에이전트 군집 ]
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[ 선택적 veHAISI 스테이킹 등급 ]                 [ 순수 USDC/USDT 상계 수수료 수익 ]
├── 락업 자본 비례 네트워크 대역폭 제공         ├── 0.05% 정산 수수료 수취
│   일일 트랜잭션 허용량 = k * sqrt(스테이킹 * 기간)│   엄격히 검증된 스테이블코인으로만 징수
└── 최대 80% 계층형 수수료 할인 제공             └── 100% 프로토콜 금고로 직행
           │                                                 │
           ▼                                                 ▼
[ $HAISI 유통 공급량 수축 ]                     [ 자율 알고리즘 TWAP 바이백 엔진 ]
                                                ├── 수익의 50%: TWAP 바이백 및 영구 소각(BURN)
                                                │   (순수 디플레이션 공급 구조)
                                                └── 수익의 50%: 프로토콜 준비금
                                                    (CHGB 보험 및 분쟁 기금)
```

#### 1. 듀얼 레일 아키텍처 및 선택적 veHAISI 할인 등급
Haichain은 마찰 없는 듀얼 레일 시스템을 강제합니다:
- **일반 에이전트 및 개발자:** 토큰 강제 스테이킹 없이 검증된 스테이블코인(USDC/USDT)으로만 건당 결제하며, 완전한 "Invisible Web3" 사용자 경험을 보장합니다.
- **엔터프라이즈 군집 및 대규모 플릿:** 인프라 특권을 위해 $HAISI(`veHAISI`)를 선택적으로 락업할 수 있습니다:
  $$\\text{일일 허용 트랜잭션} = k \\cdot \\sqrt{\\text{스테이킹 } \\$HAISI \\times \\text{락업 기간}}$$
  * *계층형 수수료 할인:* 3개월~36개월 락업 시 순 청산 수수료 최대 80% 감면.
  * *5ms 이하 전용 패스트패스 라우팅:* 미션 크리티컬 군집을 위한 전용 멤풀 라우팅.
  * *무가스 백그라운드 청산:* 프로토콜 지원 계정 임대료 회수 및 널리파이어 정리.

#### 2. 프로그래밍 방식 바이백 및 디플레이션 엔진
직접적인 현금 배당 분배(SEC 및 MiCA 규제 하에서 심각한 증권성 리스크 초래) 대신, 징수된 프로토콜 수수료의 100%는 스마트 계약을 통해 자율적으로 집행됩니다:
- **50% 자율 알고리즘 TWAP 바이백 및 소각:** Solana DEX(Raydium, Meteora)를 통한 일일 바이백 후 즉각적인 암호학적 소각(`burn`)을 실행하여 배당 기대 이익 없이 유통량을 지속 감축합니다.
- **50% 프로토콜 준비금 및 암호 하드웨어 가스 본드(CHGB):** 분쟁 해결 풀 담보, 릴레이어 보험 버퍼 및 크로스체인 청산 방어 기금으로 직접 할당됩니다.
""",

    'ZH': """### 8.2. 质押换带宽机制与价值留存飞轮
为了从根本上消除代币高周转率带来的价值稀释（**费弗定理 / Pfeffer's Theorem**），并彻底杜绝美国 SEC Howey 测试与欧盟 MiCA 法规下的证券分类风险，Haichain 将 $HAISI 架构为纯粹的**生产型实用资产**：

```
                 HAICHAIN 实用质押与价值留存飞轮
                 
            [ 执行超高频微调用的企业级智能体集群 ]
                              │
         ┌────────────────────┴────────────────────┐
         ▼                                         ▼
[ 可选 veHAISI 质押等级 ]                 [ 纯正 USDC/USDT 净额结算微费率收入 ]
├── 锁仓资本授予网络带宽配额              ├── 0.05% 结算费严格以经过验证的
│   每日限额 = k * sqrt(质押量 * 锁仓时间) │   合规稳定币全额捕获
└── 最高享 80% 阶梯式费率折扣             └── 100% 自动注入协议国库
         │                                         │
         ▼                                         ▼
[ $HAISI 流通盘持续收缩 ]                 [ 链上自主 TWAP 回购引擎 ]
                                          ├── 50% 收入: TWAP 回购并永久销毁 (BURN)
                                          │   (纯净通缩型供应结构)
                                          └── 50% 收入: 协议储备金
                                              (CHGB 硬件风险保险池)
```

#### 1. 双轨并行架构与可选 veHAISI 折扣等级
Haichain 严格执行无摩擦的双轨并行机制：
- **标准智能体与开发者：** 按次结算，完全使用合规稳定币 (USDC/USDT) 支付，无需强制质押任何代币，保留极致流畅的 "Invisible Web3" 人性化体验。
- **企业级智能体集群与高频舰队：** 可自主选择锁仓 $HAISI (`veHAISI`) 以解锁基础设施级特权：
  $$\\text{每日交易额度} = k \\cdot \\sqrt{\\text{质押 } \\$HAISI \\times \\text{锁仓时长}}$$
  * *阶梯式费率减免：* 锁仓 3 至 36 个月可享受高达 80% 的净清算费率折扣。
  * *低于 5ms 的专用快速通道路由：* 针对关键业务智能体群的专用内存池直连通道。
  * *零 Gas 费后台自动化结算：* 协议全额补贴账户租金回收与作废状态清理。

#### 2. 程序化回购与通缩引擎
我们坚决不分发任何直接现金股息（以彻底杜绝 SEC 及 MiCA 监管下的证券化法律风险），所有捕获的协议费率 100% 由智能合约自动分配：
- **50% 自主 TWAP 回购与永久销毁：** 每日在 Solana DEX (Raydium, Meteora) 上程序化执行回购并立即执行链上销毁 (`burn`)，持续收紧二级市场流通盘，杜绝任何股息收益预期。
- **50% 协议储备金与加密硬件燃气保证金 (CHGB)：** 全额注资至自动化争议仲裁资金池、中继器保险缓冲池以及跨链清算兜底金库。
""",

    'HI': """### 8.2. Распределение пропускной способности через стейкинг и маховик удержания стоимости
Для окончательного предотвращения **Смертельной спирали скорости обращения токенов (теорема Пфеффера)** и полного исключения рисков признания ценной бумагой по тесту Хауи в США и регламенту MiCA в ЕС, Haichain позиционирует $HAISI как **Продуктивный утилитарный актив**:

```
        МАХОВИК УТИЛИТАРНОГО СТЕЙКИНГА И УДЕРЖАНИЯ СТОИМОСТИ HAICHAIN
        
       [ Корпоративные флоты агентов, выполняющие высокочастотные микровызовы ]
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[ Опциональные уровни стейкинга veHAISI ]       [ Чистый доход протокола в USDC/USDT ]
├── Пропускная способность за заблокированный капитал ├── Комиссия за взаимозачет 0.05%
│   Дневной лимит = k * sqrt(Стейкинг * Время)   │   исключительно в проверенных стейблкоинах
└── Ступенчатые скидки на комиссии до 80%        └── 100% направляется в казначейство протокола
           │                                                 │
           ▼                                                 ▼
[ Сокращение оборотного предложения $HAISI ]    [ Автономный механизм выкупа TWAP ]
                                                ├── 50% дохода: TWAP выкуп и БЕЗВОЗВРАТНОЕ СЖИГАНИЕ
                                                │   (Чистая дефляционная эмиссия)
                                                └── 50% дохода: Резерв протокола
                                                    (Страховой фонд CHGB)
```

#### 1. Двухрельсовая архитектура и опциональные уровни скидок veHAISI
Haichain реализует бесшовную двухрельсовую систему:
- **Стандартные агенты и разработчики:** Оплачивают транзакции исключительно проверенными стейблкоинами (USDC/USDT) без обязательного стейкинга токенов, сохраняя эргономику «Invisible Web3».
- **Корпоративные рои и высоконагруженные флоты:** Могут опционально блокировать $HAISI (`veHAISI`) для получения инфраструктурных привилегий.

#### 2. Программный механизм выкупа и дефляции
Вместо распределения прямых денежных дивидендов (что создает критические регуляторные риски ценных бумаг согласно SEC и MiCA), 100% собранных комиссий протокола программно распределяются:
- **50% Автономный TWAP выкуп и сжигание (Burn).**
- **50% Резервы протокола и аппаратный залог газа (CHGB).**
""",

    'KK': """### 8.2. Стейкинг арқылы өткізу қабілетін бөлу және құнды сақтау маховигі
Токен айналымы жылдамдығының өсуі салдарынан құнның төмендеуін (**Пфеффер теоремасы**) біржола жою және АҚШ Howey сынағы мен ЕО MiCA бағалы қағаздар классификациясы тәуекелдерін толығымен алып тастау үшін, Haichain $HAISI токенін **Өнімді утилитарлық актив** ретінде құрастырады:

```
        HAICHAIN УТИЛИТАРЛЫҚ СТЕЙКИНГ ЖӘНЕ ҚҰНДЫ САҚТАУ МАХОВИГІ
        
       [ Жоғары жиілікті микрошақыруларды орындайтын корпоративтік агенттер ]
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[ veHAISI қосымша стейкинг деңгейлері ]          [ Таза USDC/USDT комиссиялық түсімдері ]
├── Бұғатталған капитал арқылы өткізу қабілеті  ├── 0.05% клиринг комиссиясы
│   Күндік лимит = k * sqrt(Стейкинг * Уақыт)    │   қатаң түрде тексерілген стейблкоиндерде
└── 80%-ға дейінгі жеңілдіктер                   └── 100% Хаттама қазынасына жіберіледі
           │                                                 │
           ▼                                                 ▼
[ $HAISI айналымдағы көлемін қысқарту ]          [ Автономды TWAP кері сатып алу қозғалтқышы ]
                                                ├── Түсімнің 50%-ы: TWAP кері сатып алу және ӨРТЕУ
                                                │   (Таза дефляциялық ұсыныс)
                                                └── Түсімнің 50%-ы: Хаттама резерві
                                                    (CHGB сақтық қоры)
```

#### 1. Қос рельсті архитектура және veHAISI қосымша жеңілдіктер деңгейлері
Haichain үйкеліссіз қос рельсті жүйені талап етеді:
- **Стандартты агенттер мен әзірлеушілер:** Транзакция үшін тек тексерілген стейблкоиндермен (USDC/USDT) төлейді, токендерді міндетті стейкингсіз пайдаланады ("Invisible Web3" эргономикасы).
- **Корпоративтік агенттер шоғыры:** Инфрақұрылымдық артықшылықтар үшін $HAISI (`veHAISI`) токенін қосымша бұғаттай алады:
  * Жеңілдетілген комиссиялар: 3-тен 36 айға дейін бұғаттау кезінде таза клиринг комиссияларына 80%-ға дейін жеңілдік.
  * 5 мс-тан төмен арнайы жылдам бағыттау.

#### 2. Бағдарламалық кері сатып алу және дефляция қозғалтқышы
Тікелей ақшалай дивидендтерді үлестірудің орнына (бұл SEC және MiCA ережелері бойынша бағалы қағаздар қаупін тудырады), жиналған комиссиялардың 100%-ы смарт-келісімшарт арқылы бөлінеді:
- **50% Автономды TWAP кері сатып алу және өртеу (Burn):** Нарықтағы айналымды бағалы қағаз дивидендтеріне үміт артпай тұрақты қысқарту.
- **50% Хаттама резервтері мен аппараттық газ облигациясы (CHGB):** Дауларды шешу және ретрансляторларды сақтандыру қоры.
""",

    'HE': """### 8.2. הקצאת רוחב פס לפי החזקה ומנוע שימור ערך
כדי לנטרל לצמיתות את **סחרור המוות של מהירות הטוקן (משפט פפר)** ותוך ביטול מוחלט של סיכוני סיווג ניירות ערך תחת מבחן Howey של ה-SEC ותקנות MiCA של האיחוד האירופי, Haichain מעצבת את $HAISI כ**נכס תועלת יצרני**:

```
                 HAICHAIN מנוע החזקת תועלת ושימור ערך
                 
          [ ציי סוכנים ארגוניים המבצעים מיקרו-קריאות בתדר גבוה ]
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[ שכבות החזקה אופציונליות של veHAISI ]          [ הכנסות מעמלות סליקה ב-USDC/USDT ]
├── רוחב פס המוענק באמצעות הון נעול               ├── עמלת קיזוז של 0.05%
│   הקצאה יומית = k * sqrt(החזקה * זמן)          │   הנגבית אך ורק בסטייבלקוינס מאומתים
└── הנחות מדורגות בעמלות עד 80%                   └── 100% מנותב לקופת הפרוטוקול
           │                                                 │
           ▼                                                 ▼
[ כיווץ היצע ה-$HAISI שבמחזור ]                 [ מנוע רכישה חוזרת TWAP אוטונומי ]
                                                ├── 50% מההכנסות: רכישה חוזרת ושרפה לצמיתות
                                                │   (היצע דפלציוני נטו)
                                                └── 50% מההכנסות: עתודות הפרוטוקול
                                                    (קרן ביטוח CHGB)
```

#### 1. ארכיטקטורת מסילה כפולה ושכבות הנחה אופציונליות של veHAISI
Haichain אוכפת מערכת מסילה כפולה ללא חיכוך:
- **סוכנים ומפתחים רגילים:** משלמים לכל עסקה אך ורק בסטייבלקוינס מאומתים (USDC/USDT) ללא צורך בהחזקת טוקנים מחייבת, תוך שמירה על חוויית "Invisible Web3".
- **נחילי סוכנים ארגוניים:** יכולים לנעול $HAISI באופן אופציונלי (`veHAISI`) עבור זכויות תשתית: הנחות של עד 80% בעמלות וניתוב בעדיפות גבוהה.

#### 2. מנוע רכישה חוזרת ודפלציה פרוגרמטי
במקום לחלק דיבידנדים ישירים במזומן (מה שיוצר סיכונים משפטיים חמורים של סיווג כנייר ערך לפי תקנות ה-SEC ו-MiCA), 100% מעמלות הפרוטוקול מנותבות דרך חוזה חכם:
- **50% רכישה חוזרת אוטונומית TWAP ושרפה (Burn):** רכישה יומית בבורסות מבוזרות של Solana והשמדה קריפטוגרפית מיידית ללא יצירת ציפייה לרווח מדיבידנדים.
- **50% עתודות פרוטוקול וערבות גז חומרה קריפטוגרפית (CHGB):** כיסוי ישיר של קרן יישוב סכסוכים וביטוח ריליירים.
"""
}

def update_whitepaper(wp_path):
    filename = os.path.basename(wp_path)
    lang_match = re.search(r'HAICHAIN_WHITEPAPER_V1.0_([A-Z_]+)\.md', filename)
    if not lang_match:
        return
    lang = lang_match.group(1)
    if lang not in wp_sec8_content:
        return
    
    with open(wp_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Also fix Table of Contents if it mentions Real Yield or Rendimiento Real
    text = re.sub(r'\[8\.2\.[^\]]*(?:Rendimiento Real|Rendement Réel|Real Yield|нақты кірістіліктің|реальной доходности|리얼 일드|真实收益|תשואה ממשית)[^\]]*\]', 
                  lambda m: m.group(0).replace('Rendimiento Real', 'Retención de Valor')
                                      .replace('Rendement Réel', 'Rétention de Valeur')
                                      .replace('Real Yield', 'Value Retention')
                                      .replace('реальной доходности', 'удержания стоимости')
                                      .replace('нақты кірістіліктің (Real Yield)', 'құнды сақтау')
                                      .replace('리얼 일드 바이백 소각', '가치 유지')
                                      .replace('真实收益回购销毁', '价值留存')
                                      .replace('מתשואה ממשית', 'שימור ערך'), 
                  text)
    
    # Also replace introductory references to capturing millions in real yield in Chapter 1 / preamble
    text = re.sub(r'(?:rendimiento real|rendement réel|реальной доходности|нақты кірістіліктің \(Real Yield\)|리얼 일드|真实收益)\s+([^\n.]*flujos|[^\n.]*flux|[^\n.]*потоки|[^\n.]*түсім|[^\n.]*현금 흐름|[^\n.]*现金流)', 
                  r'de comisiones de micro-liquidación \1', text, flags=re.IGNORECASE)

    # Locate Section 8.2 and Next Section
    pattern = r'(###\s+8\.2\.[^\n]+)(.*?)(###\s+8\.3\.|##\s+CHƯƠNG\s+9|##\s+CHAPTER\s+9|##\s+CAPÍTULO\s+9|##\s+CHAPITRE\s+9|##\s+ГЛАВА\s+9|##\s+9\s+ТАРАУ|##\s+제\s*9\s*장|##\s+第\s*9\s*章|##\s+פרק\s+9|##\s+अध्याय\s+9)'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        print(f"Could not locate 8.2 boundary in {wp_path}")
        return
    
    next_header = m.group(3)
    new_text = text[:m.start()] + wp_sec8_content[lang].strip() + "\n\n" + next_header + text[m.end():]
    
    with open(wp_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f"Successfully de-risked {wp_path}")

for p in glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md') + glob.glob('app/HAICHAIN_WHITEPAPER_V1.0_*.md'):
    update_whitepaper(p)

print("Whitepaper de-risking script completed.")
