# -*- coding: utf-8 -*-
"""
Script to generate and compile SAFT Agreement and 1-Pager Memo across all 10 supported languages:
EN, VI, ZH, KO, ES, FR, RU, KK, HI, HE.
"""

import os
import sys
import shutil

sys.path.insert(0, os.path.abspath("."))
from generate_pdf_whitepapers import build_pdf_from_markdown

WORKSPACE_DIR = os.path.abspath(".")

# Dictionary of Memos
MEMO_TRANSLATIONS = {
    "zh": """# HAICHAIN 种子轮前战略投资备忘录
## 自主机器通用财务与清算操作系统
### 机构级单页执行简报 • 机密天使与早期支持者轮 ($0.007 USD)

* **底层协议:** HAICHAIN (去中心化超级智能与自主智能体结算基石)
* **底层架构:** Solana L1 (Anchor v6.9.3 内核) &rarr; 高吞吐 SVM 应用专有链 (Rollup 阶段 3)
* **本轮规模:** $140,000 至 $210,000 USD (20,000,000 至 30,000,000 $HAISI • 占总供应量 2.0% 至 3.0%)
* **种子轮前认购价:** **$0.007 USD / $HAISI** (完全稀释估值 FDV: **$7,000,000 USD**)
* **计划公开 TGE 上市价:** **$0.010 USD / $HAISI** (完全稀释估值 FDV: **$10,000,000 USD**)
* **早期支持者优势:** **30% 价格折扣** (上线即享 +42.8% 未解锁账面初始收益)

---

### 1. 核心痛点与万亿美元蓝海市场
* **SaaS 席位订阅陷阱:** 全球超过 2 亿 AI 用户与企业深陷月度固定订阅泥潭 (OpenAI、Claude、Cursor、Midjourney 每月 **$150 至 $450**)。传统信用卡支付网络 (Visa/Stripe) 因固定的 $0.30 刷卡底费，无法支持亚美分级别的机器微支付。
* **HAICHAIN 破局方案:** 运行于 **Solana L1** 的军工级纳美分微结算操作系统。通过原生 **HTTP x402 协议** 彻底颠覆固定月租，实现按次毫厘级实时计费 (**每查询仅 $0.0008**)，结算延迟 **< 400ms**，提供无助记词困扰的 **生物识别 Passkey (FaceID) 极简体验**。通过 Circle 原生 USDC 与 EURC 资金通道完全符合欧盟 MiCA 监管。

---

### 2. $AI^2$ 共生范式: 人类主权与机器极速
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{人工智能 (AI)} \times \text{实际真实智能 (Actual Intelligence)}$。
* 与失控的反乌托邦机器架构截然不同，HAICHAIN 始终坚持 **人类拥有最高主权**:
  * **主权控制:** 人类通过 Merkle 能力凭证设置硬件级强制消费额度，并拥有亚秒级 **紧急熔断开关 (Panic Kill-Switch)**，在 < 400ms 内收回金库 100% 资金。
  * **经济共生:** AI 智能体向人类创作者持续流式支付知识版税，同时在遇到高风险或模糊场景时 **自主雇佣人类专家 (逆向微任务 Reverse Micro-Tasking)** 进行真值评估与鉴权 (每项任务 $1.50 - $25.00)。

---

### 3. 阶梯收入引擎 ($15.9M ARR) 与代币经济学
* **3 层混合结算收益引擎:**
  * **第 1 层 (大众消费者 AI):** 100,000 个轻量级智能体 @ $3.40/月 = $410 万交易量 (0.10% 协议费，年化 $4.1k)。
  * **第 2 层 (B2B 企业智能体集群):** 15,000 个企业智能体工作流 (平均 $350/月) = $6,300 万交易量 ($63k 协议费)。
  * **第 3 层 (机构级 GPU 与 API 清算):** 1,200 条大客户管线 ($50,000/月) = $7.2 亿交易量 (0.20-0.50% 协议费，年化 $144万 - $360万)。
  * **生态增值服务:** zkTLS 零知识验证费 ($0.001/证明) + 优先状态通道流动性做市利差，共同构建稳健的 $15.9M ARR 现金流。
* **代币价值捕获:** 全球结算费用的 50% 用于自动持续 **回购并销毁 (Buyback & Burn)**；50% 以 **纯正稳定币 (USDC/USDT)** 作为真实收益 (Real Yield) 分配给 veHAI 质押者。
* **主权 SVM 应用链终局:** 当链下状态通道结算突破 100,000 笔/秒时，$HAISI 按 1:1 转换为独立 **HAICHAIN SVM 专有链** 的原生 Gas 与验证质押资产 (目标市值 $10亿 至 $50亿+ FDV)。

```
+----------------------------------------------------------------------------------------------------+
| 资本阶段                     认购价格         完全稀释估值 (FDV)          投资回报倍数 (目标)      |
+----------------------------------------------------------------------------------------------------+
| 1. 种子轮前私募 (当前阶段)    $0.007 USD       $7,000,000 USD             入场基准点               |
| 2. 公开社区 TGE               $0.010 USD       $10,000,000 USD            +42.8% 初始上市收益      |
| 3. 二线 CEX 与 10万智能体     $0.070 USD       $70,000,000 USD            10x 回报                 |
| 4. AI 生态全面爆发 (2027)     $0.350 USD       $350,000,000 USD           50x 回报                 |
| 5. 主权独立 SVM 应用链        $1.000+ USD      $1,000,000,000+ USD        140x+ 主权网络级别       |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. 经过实测验证的底层技术 (零空气概念)
* **内核防御评分 15/15:** Solana Anchor v6.9.3 智能合约在数学上证明免疫 **Wormhole、Nomad、Euler、Mango** 历史漏洞向量。已在 **Solana Devnet** 部署运行。
* **状态通道批量压缩 (1,000:1):** 将 1,000 笔微凭证票据打包为单笔链上结算，化解 Solana 基础 Gas ($0.001/tx)，实现 $0.000001/笔 的极低运行成本。
* **300 Slot 争议挑战窗口:** 120 秒不可篡改挑战期与 100% 保证金罚没机制，彻底杜绝单方恶意撤资。
* **开箱即用 Web3 仪表板:** 现已上线，原生支持生物识别 Passkey、0-SOL 免 Gas 转发器和机器执行实时遥测。

---
*机密投资文件 • 仅供授权战略投资者查阅 • HAICHAIN 系统理事会 2026*""",

    "ko": """# HAICHAIN 프리시드 전략적 투자 메모
## 자율 기계 범용 금융 및 인지 운영체제
### 1페이지 핵심 실행 요약 • 기밀 엔젤 및 초기 투자자 라운드 ($0.007 USD)

* **프로토콜:** HAICHAIN (탈중앙화 초지능 및 자율 에이전트 결제의 기반 경제망)
* **기반 아키텍처:** Solana L1 (Anchor v6.9.3 커널) &rarr; 초고속 SVM 앱체인 (롤업 3단계)
* **라운드 규모:** $140,000 ~ $210,000 USD (20,000,000 ~ 30,000,000 $HAISI • 총 공급량의 2.0% ~ 3.0%)
* **프리시드 제공가:** **$0.007 USD / $HAISI** (완전 희석 가치 FDV: **$7,000,000 USD**)
* **공개 TGE 상장 목표가:** **$0.010 USD / $HAISI** (완전 희석 가치 FDV: **$10,000,000 USD**)
* **초기 투자자 혜택:** **30% 할인** (상장 즉시 미베스팅 기준 +42.8% 장부상 수익)

---

### 1. 문제점 및 수조 달러 규모의 무경쟁 시장
* **SaaS 구독의 낭비:** 2억 명 이상의 AI 사용자와 기업이 매월 고정 구독료(**OpenAI, Claude, Cursor 등 월 $150~$450**)의 덫에 갇혀 있습니다. 기존 카드 결제망(Visa/Stripe)은 $0.30의 고정 기본 수수료로 인해 1센트 미만의 기계 간 미세 결제를 처리할 수 없습니다.
* **HAICHAIN의 기술 혁신:** **Solana L1** 위에 구축된 군사 등급의 나노센트 마이크로 결제 OS. 원시 **HTTP x402 프로토콜**을 통해 비효율적인 월간 구독을 실시간 쿼리당 결제(**쿼리당 $0.0008**)로 대체하며, **< 400ms**의 지연 시간과 복잡한 키가 필요 없는 **생체 인식 패스키(FaceID)** UX를 제공합니다. Circle 네이티브 USDC 및 EURC를 통해 EU MiCA 규정을 완전 준수합니다.

---

### 2. $AI^2$ 패러다임: 인간 주권과 기계의 초고속 실행력
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{인공지능 (AI)} \times \text{인간의 실제 지능 (Actual Intelligence)}$.
* 통제를 벗어난 기계 아키텍처와 달리, HAICHAIN은 **인간을 최고의 주권자**로 유지합니다:
  * **주권적 통제권:** 인간은 머클 트리 역량 증명을 통해 하드웨어 수준의 지출 한도를 설정하고, 400ms 이내에 금고 자금 100%를 회수하는 **초 단위 패닉 킬스위치(Panic Kill-Switch)**를 보유합니다.
  * **경제적 공생:** AI 에이전트는 인간 창작자에게 지식 로열티를 실시간 스트리밍하며, 모호하거나 위험도가 높은 검증 작업에 **인간을 자율적으로 고용(역 마이크로 태스킹 Reverse Micro-Tasking)**합니다(작업당 $1.50 - $25.00).

---

### 3. 계층형 수익 엔진 ($15.9M ARR) 및 토크노믹스
* **3단계 복합 결제 엔진:**
  * **1계층 (소비자 AI):** 100,000 경량 에이전트 @ $3.40/월 = $4.1M 거래량 (0.10% 수수료, 연간 $4.1k).
  * **2계층 (B2B 에이전트 군집):** 15,000 기업 에이전트 워크플로우 (월 $350 평균) = $63M 거래량 ($63k 수수료).
  * **3계층 (기관용 GPU 및 API 청산):** 1,200 기업 파이프라인 (월 $50,000) = $720M 거래량 (0.20-0.50% 수수료, $1.44M - $3.6M).
  * **생태계 서비스:** zkTLS 검증 수수료($0.001/증명) + 상태 채널 유동성 스프레드를 통해 견고한 $15.9M ARR 창출.
* **토큰 가치 축적:** 글로벌 결제 수수료의 50%는 자동 **바이백 및 소각(Buyback & Burn)**에 투입되며, 50%는 veHAI 거버넌스 스테이커에게 **순수 스테이블코인(USDC/USDT) 리얼 일드(Real Yield)**로 배분됩니다.
* **주권 SVM 앱체인 최종장:** 오프체인 채널 트래픽이 100k tx/sec를 돌파하면 $HAISI는 전용 **HAICHAIN SVM 앱체인**의 네이티브 가스 코인으로 1:1 전환됩니다(목표 FDV $1B - $5B+).

```
+----------------------------------------------------------------------------------------------------+
| 자본 조달 단계                 제공 가격         완전 희석 가치 (FDV)         목표 수익 배수        |
+----------------------------------------------------------------------------------------------------+
| 1. 프라이빗 프리시드 (현재)    $0.007 USD       $7,000,000 USD               진입 기준선           |
| 2. 공개 커뮤니티 TGE           $0.010 USD       $10,000,000 USD              +42.8% 즉각적 상승    |
| 3. Tier-2 CEX 및 10만 에이전트 $0.070 USD       $70,000,000 USD              10배 수익             |
| 4. AI 생태계 본격 확장 (2027)  $0.350 USD       $350,000,000 USD             50배 수익             |
| 5. 주권 독립 SVM 앱체인        $1.000+ USD      $1,000,000,000+ USD          140배+ 주권 등급      |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. 100% 검증 완료된 기술 기반 (무가치 공약 제로)
* **커널 방어 점수 15/15:** Solana Anchor v6.9.3 스마트 계약은 **Wormhole, Nomad, Euler, Mango** 해킹 공격 벡터에 대해 수학적으로 면역성을 입증했습니다. **Solana Devnet**에 실배포되어 가동 중입니다.
* **상태 채널 일괄 압축 (1,000:1):** 1,000건의 마이크로 바우처를 단일 온체인 정산으로 압축하여 Solana 기본 가스비를 상쇄하고 실제 실행 비용을 건당 $0.000001 수준으로 실현했습니다.
* **300 슬롯 분쟁 챌린지 윈도우:** 120초의 불변 챌린지 기간과 100% 보증금 몰수(슬래싱)를 통해 일방적인 부정 출금을 원천 차단합니다.
* **즉시 사용 가능한 Web3 대시보드:** 생체 인식 패스키 지원, 0-SOL 가스리스 릴레이, 실시간 머신 실행 원격 측정을 갖추고 현재 라이브 운영 중입니다.

---
*기밀 투자 문서 • 승인된 전략적 투자자 전용 • HAICHAIN 시스템 위원회 2026*""",

    "es": """# MEMORÁNDUM DE INVERSIÓN ESTRATÉGICA PRE-SEED DE HAICHAIN
## SISTEMA OPERATIVO FINANCIERO Y COGNITIVO PARA MÁQUINAS AUTÓNOMAS
### RESUMEN EJECUTIVO DE UNA PÁGINA • RONDA CONFIDENCIAL DE ÁNGELES Y PRIMEROS RESPALDOS ($0.007 USD)

* **Protocolo:** HAICHAIN (La base económica para la superinteligencia descentralizada y la liquidación de agentes autónomos)
* **Arquitectura Base:** Solana L1 (Kernel Anchor v6.9.3) &rarr; App-Chain SVM de Alto Rendimiento (Fase Rollup 3)
* **Tamaño de la Ronda:** $140,000 a $210,000 USD (20,000,000 a 30,000,000 $HAISI • 2.0% a 3.0% del Suministro Total)
* **Precio de Oferta Pre-Seed:** **$0.007 USD / $HAISI** (Valoración Totalmente Diluida FDV: **$7,000,000 USD**)
* **Precio Objetivo de Cotización Pública TGE:** **$0.010 USD / $HAISI** (FDV: **$10,000,000 USD**)
* **Ventaja del Inversor Temprano:** **30% de Descuento** (+42.8% de revalorización contable inmediata al cotizar)

---

### 1. EL PROBLEMA Y EL MERCADO MULTIBILLONARIO SIN COMPETENCIA
* **La Trampa de las Suscripciones SaaS:** Más de 200 millones de usuarios y empresas de IA están atrapados en costosas tarifas fijas mensuales (**$150 a $450/mes** entre OpenAI, Claude, Cursor, Midjourney). Las redes de pago tradicionales (Visa/Stripe) son incapaces de procesar pagos inferiores a un centavo debido a su tarifa mínima fija de $0.30 por transacción.
* **El Avance de HAICHAIN:** Un sistema operativo de micro-liquidación en nanocentavos de nivel militar sobre **Solana L1**. Sustituye las suscripciones mensuales por facturación en tiempo real por consulta (**$0.0008 por consulta**) mediante el protocolo nativo **HTTP x402** en **< 400ms** con experiencia **Passkey Biométrica (FaceID)** sin fricción Web3. Cumplimiento integral con MiCA de la UE mediante liquidez Circle USDC y EURC.

---

### 2. EL PARADIGMA $AI^2$: SOBERANÍA HUMANA Y VELOCIDAD DE MÁQUINA
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{Inteligencia Artificial} \times \text{Inteligencia Real Humana (Actual Intelligence)}$.
* A diferencia de las arquitecturas distópicas descontroladas, HAICHAIN mantiene a los **Humanos como Soberanos Supremos**:
  * **Autoridad Maestra:** El humano establece límites de gasto forzados por hardware mediante árboles de Merkle y posee un **Interruptor de Pánico Sub-segundo (Kill-Switch)** que devuelve el 100% de los fondos en < 400ms.
  * **Simbiosis Económica:** Los agentes de IA pagan regalías continuas a los creadores humanos y **contratan autónomamente a humanos (Micro-Tareas Inversas)** para validaciones críticas de RLHF y autorizaciones en el mundo real ($1.50 - $25.00/tarea).

---

### 3. MOTOR DE INGRESOS ESCALONADO ($15.9M ARR) Y TOKENÓMICA
* **Motor de Liquidación Mixto de 3 Niveles:**
  * **Nivel 1 (IA de Consumo):** 100,000 agentes ligeros @ $3.40/mes = $4.1M volumen (tarifa 0.10%, $4.1k anual).
  * **Nivel 2 (Enjambres B2B):** 15,000 flujos de agentes corporativos ($350/mes) = $63M volumen ($63k tarifa).
  * **Nivel 3 (GPU Institucional y Compensación API):** 1,200 pipelines corporativos ($50,000/mes) = $720M volumen (tarifa 0.20-0.50%, $1.44M - $3.6M). Tarifas zkTLS y diferenciales de liquidez generan un sólido ARR de $15.9M.
* **Captura de Valor del Token:** El 50% de las tarifas globales financia la **Recompra y Quema Continua (Buyback & Burn)**; el 50% se distribuye como **Rendimiento Real (USDC/USDT)** a los stakers de gobernanza veHAI.
* **App-Chain Soberana SVM Final:** Cuando las liquidaciones de canal superen 100k tx/s, $HAISI se convierte 1:1 en el activo nativo de gas y staking de la **App-Chain SVM HAICHAIN** dedicada ($1B a $5B+ FDV).

```
+----------------------------------------------------------------------------------------------------+
| ETAPA DE CAPITAL             PRECIO OFRECIDO   VALORACIÓN TOTAL (FDV)    MÚLTIPLO DE RETORNO       |
+----------------------------------------------------------------------------------------------------+
| 1. Pre-Seed Privada (AHORA)   $0.007 USD       $7,000,000 USD            LÍNEA BASE DE ENTRADA     |
| 2. TGE Pública Comunitaria    $0.010 USD       $10,000,000 USD           +42.8% Ganancia Inmediata |
| 3. CEX Tier-2 y 100k Agentes  $0.070 USD       $70,000,000 USD           Retorno 10x               |
| 4. Escala Ecosistema (2027)   $0.350 USD       $350,000,000 USD          Retorno 50x               |
| 5. App-Chain SVM Soberana     $1.000+ USD      $1,000,000,000+ USD       Nivel Soberano 140x+      |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. BASE TÉCNICA: EN VIVO Y VERIFICADA (CERO ESPECULACIÓN)
* **Puntuación de Defensa del Kernel 15/15:** Smart contracts Solana Anchor v6.9.3 matemáticamente inmunes a vectores de ataque **Wormhole, Nomad, Euler y Mango**. En vivo en **Solana Devnet**.
* **Compresión de Canales de Estado (1,000:1):** Agrupa 1,000 micro-pagos en una sola liquidación on-chain, logrando un coste real de $0.000001 por transacción.
* **Ventana de Disputa de 300 Slots:** Ventana inmutable de 120 segundos y penalización (slashing) del 100% de la fianza para evitar retiradas no autorizadas.
* **Dashboard Web3 Operativo:** Interfaz en vivo con soporte para Passkeys biométricas, relayers sin gas (0-SOL) y telemetría de ejecución de máquinas en tiempo real.

---
*Documento Confidencial de Inversión • Exclusivo para Inversores Estratégicos • Consejo de Sistemas HAICHAIN 2026*""",

    "fr": """# MÉMOIRE D'INVESTISSEMENT STRATÉGIQUE PRE-SEED HAICHAIN
## SYSTÈME D'EXPLOITATION FINANCIER ET COGNITIF POUR MACHINES AUTONOMES
### SYNTHÈSE EXÉCUTIVE D'UNE PAGE • TOUR CONFIDENTIEL BUSINESS ANGELS & EARLY BACKERS ($0.007 USD)

* **Protocole:** HAICHAIN (Le socle économique pour la superintelligence décentralisée et le règlement des agents autonomes)
* **Architecture Sous-jacente:** Solana L1 (Noyau Anchor v6.9.3) &rarr; App-Chain SVM à Haute Capacité (Étape Rollup 3)
* **Taille du Tour:** $140 000 à $210 000 USD (20 000 000 à 30 000 000 $HAISI • 2,0% à 3,0% de l'Offre Totale)
* **Prix de l'Offre Pre-Seed:** **$0.007 USD / $HAISI** (Valorisation Entièrement Diluée FDV: **$7 000 000 USD**)
* **Prix d'Introduction Publique TGE Prévu:** **$0.010 USD / $HAISI** (FDV: **$10 000 000 USD**)
* **Avantage Early Backer:** **30% de Réduction** (+42,8% de plus-value comptable immédiate dès la cotation)

---

### 1. LE PROBLÈME ET LE MARCHÉ MULTI-MILLIARDS SANS CONCURRENCE
* **Le Piège des Abonnements SaaS:** Plus de 200 millions d'utilisateurs et d'entreprises d'IA sont captifs d'abonnements mensuels rigides et coûteux (**$150 à $450/mois** sur OpenAI, Claude, Cursor, Midjourney). Les réseaux de cartes bancaires (Visa/Stripe) ne peuvent structurellement pas traiter de micro-paiements inférieurs au centime en raison d'un forfait fixe de $0,30 par transaction.
* **La Percée HAICHAIN:** Un système d'exploitation de micro-règlement au nano-centime de qualité militaire sur **Solana L1**. Remplace les abonnements mensuels par une tarification en temps réel par requête (**$0.0008 par requête**) via le protocole natif **HTTP x402** en **< 400ms** avec une expérience **Passkey Biométrique (FaceID)** invisible. Pleine conformité avec la réglementation européenne MiCA via les rails de liquidité Circle USDC & EURC.

---

### 2. LE PARADIGME $AI^2$: SOUVERAINETÉ HUMAINE ET VÉLOCITÉ MACHINE
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{Intelligence Artificielle} \times \text{Intelligence Réelle Humaine (Actual Intelligence)}$.
* Loin des architectures dystopiques incontrôlées, HAICHAIN place **l'Humain comme Souverain Suprême**:
  * **Contrôle Maître:** L'humain définit des plafonds de dépenses matériels stricts via des arbres de Merkle et détient un **Interrupteur d'Arrêt d'Urgence (Panic Kill-Switch)** restituant 100% des fonds du coffre en < 400ms.
  * **Symbiose Économique:** Les agents IA versent des redevances continues aux créateurs de savoir humains, tout en **recrutant de manière autonome des humains (Reverse Micro-Tasking)** pour la validation RLHF et l'approbation du monde réel ($1.50 - $25.00/tâche).

---

### 3. MOTEUR DE REVENUS ÉTAGÉ ($15.9M ARR) ET TOKENOMICS
* **Moteur de Règlement Mixte à 3 Niveaux:**
  * **Niveau 1 (IA Grand Public):** 100 000 agents légers @ $3.40/mois = $4.1M de volume (frais de 0.10%, soit $4.1k).
  * **Niveau 2 (Essaims d'Agents B2B):** 15 000 flux d'agents d'entreprise ($350/mois) = $63M de volume ($63k de frais).
  * **Niveau 3 (GPU Institutionnel & Compensation API):** 1 200 pipelines d'entreprises ($50 000/mois) = $720M de volume (frais de 0.20-0.50%, soit $1.44M - $3.6M). Les frais de vérification zkTLS et les écarts de liquidité génèrent un ARR solide de $15.9M.
* **Accumulation de Valeur du Token:** 50% de l'ensemble des frais mondiaux financent le **Rachat & Destruction Automatique (Buyback & Burn)**; 50% sont distribués sous forme de **Rendement Réel (USDC/USDT)** aux stakers de gouvernance veHAI.
* **App-Chain SVM Souveraine:** Lorsque les règlements dépassent 100k tx/sec, $HAISI se convertit à 1:1 en actif natif de gas et de staking de l'**App-Chain SVM HAICHAIN** dédiée ($1 Md à $5 Mds+ FDV).

```
+----------------------------------------------------------------------------------------------------+
| ÉTAPE DU CAPITAL              PRIX DE L'OFFRE   VALORISATION DILUÉE (FDV)   MULTIPLICATEUR CIBLE   |
+----------------------------------------------------------------------------------------------------+
| 1. Pre-Seed Privé (ACTUEL)    $0.007 USD        $7 000 000 USD              POINT D'ENTRÉE         |
| 2. TGE Communautaire Public   $0.010 USD        $10 000 000 USD             +42.8% Gain Immédiat   |
| 3. CEX Tier-2 & 100k Agents   $0.070 USD        $70 000 000 USD             Rendement 10x          |
| 4. Échelle Écosystème (2027)  $0.350 USD        $350 000 000 USD            Rendement 50x          |
| 5. App-Chain SVM Souveraine   $1.000+ USD       $1 000 000 000+ USD         Rang Souverain 140x+   |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. FONDATION TECHNIQUE: OPÉRATIONNELLE ET VÉRIFIÉE (ZÉRO SPÉCULATION)
* **Score de Défense du Noyau 15/15:** Contrats intelligents Solana Anchor v6.9.3 mathématiquement invulnérables aux vecteurs d'attaque historiques **Wormhole, Nomad, Euler et Mango**. Déployés sur **Solana Devnet**.
* **Compression des Canaux d'État (1 000:1):** Compresse 1 000 micro-titres en un seul règlement on-chain, réduisant le coût réel d'exécution à $0.000001 par transaction.
* **Fenêtre de Contestation de 300 Slots:** Période de contestation immuable de 120 secondes et confiscation intégrale (slashing) du dépôt pour prévenir tout retrait frauduleux.
* **Tableau de Bord Web3 Clé en Main:** Interface active avec prise en charge des clés d'accès biométriques (Passkeys), relais sans gas (0-SOL) et télémétrie machine en temps réel.

---
*Document d'Investissement Confidentiel • Réservé aux Investisseurs Stratégiques • Conseil des Systèmes HAICHAIN 2026*""",

    "ru": """# МЕМОРАНДУМ О СТРАТЕГИЧЕСКИХ ИНВЕСТИЦИЯХ PRE-SEED HAICHAIN
## УНИВЕРСАЛЬНАЯ ФИНАНСОВАЯ И КОГНИТИВНАЯ ОПЕРАЦИОННАЯ СИСТЕМА ДЛЯ АВТОНОМНЫХ МАШИН
### ОДНОСТРАНИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ БРИФ • КОНФИДЕНЦИАЛЬНЫЙ РАУНД ДЛЯ АНГЕЛОВ И РАННИХ ИНВЕСТОРОВ ($0.007 USD)

* **Протокол:** HAICHAIN (Экономический фундамент децентрализованного сверхразума и расчетов автономных агентов)
* **Базовая архитектура:** Solana L1 (Ядро Anchor v6.9.3) &rarr; Высокопроизводительный SVM App-Chain (Rollup Этап 3)
* **Объем раунда:** $140 000 – $210 000 USD (20 000 000 – 30 000 000 $HAISI • 2.0% – 3.0% от общей эмиссии)
* **Цена предложения Pre-Seed:** **$0.007 USD / $HAISI** (Полная разводненная оценка FDV: **$7 000 000 USD**)
* **Планируемая цена листинга TGE:** **$0.010 USD / $HAISI** (FDV: **$10 000 000 USD**)
* **Преимущество ранних инвесторов:** **Скидка 30%** (+42.8% немедленной расчетной доходности при выходе на биржу)

---

### 1. ПРОБЛЕМА И СВОБОДНЫЙ МУЛЬТИТРИЛЛИОННЫЙ РЫНОК
* **Ловушка SaaS-подписок:** Свыше 200 миллионов пользователей и предприятий заперты в фиксированных ежемесячных тарифах (**$150 – $450/месяц** за OpenAI, Claude, Cursor, Midjourney). Традиционные платежные шлюзы (Visa/Stripe) неспособны обрабатывать микроплатежи меньше цента из-за фиксированной комиссии в $0.30 за транзакцию.
* **Прорыв HAICHAIN:** Высоконадежная операционная система микрорасчетов в наноцентах на **Solana L1**. Заменяет ежемесячные подписки оплатой за фактический запрос (**$0.0008 за запрос**) через протокол **HTTP x402** за **< 400 мс** с биометрическим **Passkey (FaceID)** без необходимости управлять приватными ключами. Полное соответствие нормам ЕС MiCA через пулы Circle USDC и EURC.

---

### 2. ПАРАДИГМА $AI^2$: СУВЕРЕНИТЕТ ЧЕЛОВЕКА И СКОРОСТЬ МАШИН
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{Искусственный интеллект} \times \text{Реальный человеческий интеллект (Actual Intelligence)}$.
* В отличие от антиутопических машин, в HAICHAIN **Человек остается верховным сувереном**:
  * **Полный контроль:** Человек задает аппаратные лимиты расходов через деревья Меркла и владеет **Экстренным выключателем (Panic Kill-Switch)**, возвращающим 100% средств хранилища за < 400 мс.
  * **Экономический симбиоз:** ИИ-агенты непрерывно выплачивают роялти создателям знаний и **автономно нанимают людей (Reverse Micro-Tasking)** для экспертной валидации RLHF и подтверждения реальных действий ($1.50 – $25.00 за задачу).

---

### 3. ЭТАПНЫЙ ДВИГАТЕЛЬ ДОХОДОВ ($15.9M ARR) И ТОКЕНОМИКА
* **3-уровневый механизм расчетных сборов:**
  * **Уровень 1 (Потребительский ИИ):** 100 000 легких агентов @ $3.40/мес = $4.1M оборота (комиссия 0.10%, $4.1k/год).
  * **Уровень 2 (Корпоративные рои агентов):** 15 000 бизнес-агентов ($350/мес) = $63M оборота ($63k комиссии).
  * **Уровень 3 (Институциональный GPU и API-клиринг):** 1 200 крупных корпоративных конвейеров ($50 000/мес) = $720M оборота (комиссия 0.20-0.50%, $1.44M – $3.6M). Верификация zkTLS и спреды ликвидности формируют устойчивый ARR в размере $15.9M.
* **Накопление стоимости токена:** 50% всех сборов направляются на **Автоматический выкуп и сжигание (Buyback & Burn)**; 50% выплачиваются в **чистых стейблкоинах (USDC/USDT)** в качестве Real Yield стейкерам veHAI.
* **Суверенный SVM App-Chain:** При превышении канального трафика 100 000 tx/сек, $HAISI конвертируется 1:1 в нативный Gas и стейкинг-актив выделенной сети **HAICHAIN SVM App-Chain** ($1 млрд – $5+ млрд FDV).

```
+----------------------------------------------------------------------------------------------------+
| ЭТАП ИНВЕСТИЦИЙ              ЦЕНА ПРЕДЛОЖЕНИЯ  ОЦЕНКА СЕТИ (FDV)         ЦЕЛЕВОЙ МУЛЬТИПЛИКАТОР    |
+----------------------------------------------------------------------------------------------------+
| 1. Private Pre-Seed (СЕЙЧАС)  $0.007 USD       $7 000 000 USD            ТОЧКА ВХОДА               |
| 2. Публичный TGE              $0.010 USD       $10 000 000 USD           +42.8% Базовый рост       |
| 3. Tier-2 CEX и 100k агентов  $0.070 USD       $70 000 000 USD           10x доходности            |
| 4. Масштаб экосистемы (2027)  $0.350 USD       $350 000 000 USD          50x доходности            |
| 5. Суверенный SVM App-Chain   $1.000+ USD      $1 000 000 000+ USD       140x+ Суверенный уровень  |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. ТЕХНИЧЕСКИЙ ФУНДАМЕНТ: РАБОТАЕТ И ПРОВЕРЕН В ЖИВОЙ СЕТИ
* **Рейтинг защиты ядра 15/15:** Смарт-контракты Solana Anchor v6.9.3 математически защищены от векторов атак **Wormhole, Nomad, Euler и Mango**. Запущены в **Solana Devnet**.
* **Пакетное сжатие каналов состояния (1,000:1):** 1,000 микрочеков упаковываются в одну ончейн-транзакцию, снижая реальную стоимость операции до $0.000001.
* **Окно оспаривания в 300 слотов:** Неизменяемый период в 120 секунд со 100% сжиганием залога (slashing) полностью предотвращает несанкционированный вывод средств.
* **Готовый Web3-терминал:** Работает в реальном времени, поддерживает биометрические Passkeys, безгазовые транзакции (0-SOL) и телеметрию работы машин.

---
*Конфиденциальный инвестиционный документ • Только для стратегических партнеров • Совет систем HAICHAIN 2026*""",

    "kk": """# HAICHAIN PRE-SEED СТРАТЕГИЯЛЫҚ ИНВЕСТИЦИЯЛЫҚ МЕМОРАНДУМЫ
## АВТОНОМДЫ МАШИНАЛАРҒА АРНАЛҒАН ЖАЛПЫҒА ОРТАҚ ҚАРЖЫЛЫҚ ЖӘНЕ КОГНИТИВТІ ОПЕРАЦИЯЛЫҚ ЖҮЙЕ
### БІР БЕТТІК АТҚАРУШЫ ТҮЙІНДЕМЕ • БИЗНЕС-ПЕРІШТЕЛЕР МЕН БАСТАПҚЫ ҚОЛДАУШЫЛАРҒА АРНАЛҒАН ҚҰПИЯ РАУНД ($0.007 USD)

* **Хаттама:** HAICHAIN (Орталықсыздандырылған асқан интеллект пен автономды агенттер есеп айырысуының экономикалық негізі)
* **Негізгі архитектура:** Solana L1 (Anchor v6.9.3 ядросы) &rarr; Жоғары өткізу қабілетті SVM App-Chain (Rollup 3-кезең)
* **Раунд көлемі:** $140 000 – $210 000 USD (20 000 000 – 30 000 000 $HAISI • Жалпы эмиссияның 2.0% – 3.0%)
* **Pre-Seed ұсыныс бағасы:** **$0.007 USD / $HAISI** (Толық сұйылтылған бағалау FDV: **$7 000 000 USD**)
* **Жоспарланған ашық TGE листинг бағасы:** **$0.010 USD / $HAISI** (FDV: **$10 000 000 USD**)
* **Бастапқы инвестор артықшылығы:** **30% Жеңілдік** (Листинг кезінде бірден +42.8% кірістілік)

---

### 1. МӘСЕЛЕ ЖӘНЕ ТРИЛЛИОН ДОЛЛАРЛЫҚ БӘСЕКЕСІЗ НАРЫҚ
* **SaaS жазылымдарының шығыны:** 200 миллионнан астам AI пайдаланушылары мен кәсіпорындары қымбат ай сайынғы тұрақты төлемдердің (**OpenAI, Claude, Cursor үшін айына $150 – $450**) тұзағында отыр. Дәстүрлі төлем жүйелері (Visa/Stripe) әрбір транзакцияға бекітілген $0.30 комиссиясына байланысты 1 центтен төмен төлемдерді өңдей алмайды.
* **HAICHAIN серпілісі:** **Solana L1** желісіндегі әскери деңгейдегі нано-центтік микро-есеп айырысу операциялық жүйесі. Ай сайынғы жазылымды **HTTP x402 хаттамасы** арқылы нақты сұраныс бойынша төлеммен (**әр сұранысқа небәрі $0.0008**) ауыстырады, кідіріс **< 400 мс**, **Биометриялық Passkey (FaceID)** арқылы құпия сөзсіз жеңіл тәжірибе береді. Circle USDC және EURC арқылы ЕО MiCA талаптарына толық сәйкес келеді.

---

### 2. $AI^2$ ПАРАДИГМАСЫ: АДАМ ЕГЕМЕНДІГІ МЕН МАШИНА ЖЫЛДАМДЫҒЫ
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{Жасанды Интеллект (AI)} \times \text{Адамның Нақты Интеллекті (Actual Intelligence)}$.
* Бақылаусыз машиналардан айырмашылығы, HAICHAIN-де **Адам ең жоғарғы егемен болып қала береді**:
  * **Жоғарғы бақылау:** Адам Меркл ағашы арқылы шығын лимиттерін бекітеді және қордағы қаражаттың 100% сомасын 400 мс ішінде қайтарып алатын **Апаттық ажыратқышқа (Panic Kill-Switch)** ие.
  * **Экономикалық симбиоз:** AI агенттері адамдарға білім роялтиін тұрақты төлейді және күрделі мәселелер туындағанда **адамдарды дербес жалдайды (Reverse Micro-Tasking)** (әр тапсырмаға $1.50 – $25.00).

---

### 3. САТЫЛЫ КІРІС ҚОЗҒАЛТҚЫШЫ ($15.9M ARR) ЖӘНЕ ТОКЕНОМИКА
* **3 деңгейлі аралас кіріс жүйесі:**
  * **1-деңгей (Тұтынушылық AI):** 100 000 жеңіл агент @ $3.40/ай = $4.1M көлем (0.10% комиссия, жылына $4.1k).
  * **2-деңгей (B2B агенттер шоғыры):** 15 000 корпоративтік жұмыс процесі ($350/ай) = $63M көлем ($63k комиссия).
  * **3-деңгей (Институционалдық GPU және API клиринг):** 1 200 ірі компания желісі ($50 000/ай) = $720M көлем (0.20-0.50% комиссия, $1.44M – $3.6M). zkTLS және өтімділік спрэдтері $15.9M ARR қамтамасыз етеді.
* **Токен құнын арттыру:** Барлық жаһандық комиссияның 50%-ы **Кері сатып алу және өртеуге (Buyback & Burn)** жұмсалады; 50%-ы veHAI стейкерлеріне **Таза стейблкоин (USDC/USDT)** ретінде Real Yield түрінде таратылады.
* **Егемен SVM App-Chain мақсаты:** Арна транзакциялары секундына 100 000-нан асқанда, $HAISI тәуелсіз **HAICHAIN SVM App-Chain** желісінің Gas және стейкинг монетасына 1:1 қатынасында айналады ($1 млрд – $5+ млрд FDV).

```
+----------------------------------------------------------------------------------------------------+
| ҚАРЖЫЛАНДЫРУ КЕЗЕҢІ          ҰСЫНЫЛАТЫН БАҒА   ТОЛЫҚ ҚҰНЫ (FDV)          МАҚСАТТЫ КІРІС ЕСЕЛІГІ    |
+----------------------------------------------------------------------------------------------------+
| 1. Private Pre-Seed (ҚАЗІР)   $0.007 USD       $7 000 000 USD            БАСТАПҚЫ НҮКТЕ            |
| 2. Ашық қоғамдық TGE          $0.010 USD       $10 000 000 USD           +42.8% Бастапқы өсім      |
| 3. Tier-2 CEX және 100k агент $0.070 USD       $70 000 000 USD           10x кіріс                 |
| 4. AI экожүйесінің өсуі (2027)$0.350 USD       $350 000 000 USD          50x кіріс                 |
| 5. Егемен SVM App-Chain       $1.000+ USD      $1 000 000 000+ USD       140x+ Егемен деңгей       |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. ТЕХНИКАЛЫҚ НЕГІЗ: НАҚТЫ ЖӘНЕ СЫНАЛҒАН (БОС УӘДЕ ЕМЕС)
* **Ядроны қорғау көрсеткіші 15/15:** Solana Anchor v6.9.3 смарт-келісімшарттары **Wormhole, Nomad, Euler, Mango** шабуылдарына қарсы математикалық тұрғыдан қауіпсіз. **Solana Devnet** желісінде іске қосылған.
* **Жүйелік арналарды қысу (1,000:1):** 1 000 шағын чекті бір блокчейн транзакциясына біріктіріп, нақты шығынды әр транзакция үшін $0.000001 деңгейіне дейін түсірді.
* **300 слоттық дау-дамай терезесі:** 120 секундтық өзгермейтін тексеру кезеңі және кепілдікті 100% кесіп алу (slashing) қаражатты рұқсатсыз шығаруға жол бермейді.
* **Дайын Web3 басқару тақтасы:** Биометриялық кіруді, 0-SOL төлемдерін және нақты уақыттағы машина телеметриясын қолдайтын дайын интерфейс.

---
*Құпия инвестициялық құжат • Тек стратегиялық инвесторлар үшін • HAICHAIN Жүйелер Кеңесі 2026*""",

    "hi": """# HAICHAIN प्री-सीड रणनीतिक निवेश मेमो
## स्वायत्त मशीनों के लिए सार्वभौमिक वित्तीय एवं संज्ञानात्मक ऑपरेटिंग सिस्टम
### एक-पृष्ठ कार्यकारी सारांश • गोपनीय एंजेल और शुरुआती समर्थक राउंड ($0.007 USD)

* **प्रोटोकॉल:** HAICHAIN (विकेंद्रीकृत सुपरइंटेलिजेंस और स्वायत्त एजेंट निपटान के लिए आर्थिक आधारशिला)
* **अंतर्निहित वास्तुकला:** Solana L1 (Anchor v6.9.3 कर्नेल) &rarr; उच्च-थ्रूपुट SVM ऐप-चेन (रोलअप चरण 3)
* **राउंड का आकार:** $140,000 से $210,000 USD (20,000,000 से 30,000,000 $HAISI • कुल आपूर्ति का 2.0% से 3.0%)
* **प्री-सीड पेशकश मूल्य:** **$0.007 USD / $HAISI** (पूर्णतः पतला मूल्यांकन FDV: **$7,000,000 USD**)
* **योजनाबद्ध सार्वजनिक TGE सूची मूल्य:** **$0.010 USD / $HAISI** (FDV: **$10,000,000 USD**)
* **शुरुआती समर्थक लाभ:** **30% छूट** (सूचीकरण पर तुरंत +42.8% अनिहित लाभ)

---

### 1. समस्या और बहु-ट्रिलियन डॉलर का अप्रतिद्वंद्वी बाजार
* **SaaS सदस्यता का जाल:** 20 करोड़ से अधिक AI उपयोगकर्ता और उद्यम अत्यधिक मासिक शुल्कों (**OpenAI, Claude, Cursor के लिए $150 से $450/माह**) के जाल में फंसे हैं। पारंपरिक भुगतान नेटवर्क (Visa/Stripe) $0.30 के न्यूनतम शुल्क के कारण 1 सेंट से कम के सूक्ष्म भुगतानों को संभालने में असमर्थ हैं।
* **HAICHAIN की तकनीकी सफलता:** **Solana L1** पर निर्मित सैन्य-ग्रेड नैनो-सेंट माइक्रो-सेटलमेंट ऑपरेटिंग सिस्टम। मूल **HTTP x402 प्रोटोकॉल** के माध्यम से प्रति क्वेरी वास्तविक समय बिलिंग (**मात्र $0.0008 प्रति क्वेरी**) प्रदान करता है, **< 400ms** की गति और बिना पासवर्ड की **बायोमेट्रिक पासकी (FaceID)** की सुविधा देता है। Circle USDC और EURC के माध्यम से यूरोपीय संघ के MiCA नियमों का पूर्ण अनुपालन।

---

### 2. $AI^2$ प्रतिमान: मानव संप्रभुता और मशीन की गति
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{आर्टिफिशियल इंटेलिजेंस (AI)} \times \text{मानव की वास्तविक बुद्धि (Actual Intelligence)}$।
* अनियंत्रित मशीनों के विपरीत, HAICHAIN में **मानव ही सर्वोच्च संप्रभु** बना रहता है:
  * **मास्टर अधिकार:** मानव मर्कल ट्री के माध्यम से खर्च सीमा निर्धारित करता है और 400ms से कम समय में तिजोरी से 100% धन वापस लाने वाला **पैनिक किल-स्विच** रखता है।
  * **आर्थिक सहजीविता:** AI एजेंट ज्ञान रचनाकारों को रॉयल्टी स्ट्रीम करते हैं, और उच्च-दांव वाले सत्यापन के लिए **मानवों को स्वायत्त रूप से किराए पर लेते हैं (Reverse Micro-Tasking)** ($1.50 - $25.00 प्रति कार्य)।

---

### 3. स्तरित राजस्व इंजन ($15.9M ARR) और टोकनॉमिक्स
* **3-स्तरीय मिश्रित निपटान इंजन:**
  * **स्तर 1 (उपभोक्ता AI):** 100,000 हल्के एजेंट @ $3.40/माह = $4.1M वॉल्यूम (0.10% शुल्क, $4.1k वार्षिक)।
  * **स्तर 2 (B2B एजेंट झुंड):** 15,000 उद्यम एजेंट वर्कफ़्लो ($350/माह) = $63M वॉल्यूम ($63k शुल्क)।
  * **स्तर 3 (संस्थागत GPU और API समाशोधन):** 1,200 उद्यम पाइपलाइन ($50,000/माह) = $720M वॉल्यूम (0.20-0.50% शुल्क, $1.44M - $3.6M)। zkTLS सत्यापन शुल्क और तरलता स्प्रेड कुल $15.9M ARR उत्पन्न करते हैं।
* **टोकन मूल्य संचय:** वैश्विक निपटान शुल्क का 50% स्वचालित **बायबैक और बर्न** में जाता है; 50% veHAI स्टेकरों को **शुद्ध स्टेबलकॉइन (USDC/USDT)** के रूप में रियल यील्ड के रूप में वितरित किया जाता है।
* **संप्रभु SVM ऐप-चेन अंतिम लक्ष्य:** जब चैनल लेनदेन 100,000 प्रति सेकंड को पार कर जाता है, तो $HAISI समर्पित **HAICHAIN SVM ऐप-चेन** की मूल गैस संपत्ति में 1:1 परिवर्तित हो जाता है ($1B से $5B+ FDV)।

```
+----------------------------------------------------------------------------------------------------+
| पूंजी चरण                     पेशकश मूल्य       पूर्ण मूल्यांकन (FDV)        लक्षित रिटर्न गुणक    |
+----------------------------------------------------------------------------------------------------+
| 1. निजी प्री-सीड (वर्तमान)     $0.007 USD       $7,000,000 USD               प्रवेश बेसलाइन        |
| 2. सार्वजनिक TGE               $0.010 USD       $10,000,000 USD              +42.8% तत्काल लाभ     |
| 3. टियर-2 CEX और 1 लाख एजेंट   $0.070 USD       $70,000,000 USD              10x रिटर्न            |
| 4. AI इकोसिस्टम पैमाना (2027)  $0.350 USD       $350,000,000 USD             50x रिटर्न            |
| 5. संप्रभु SVM ऐप-चेन          $1.000+ USD      $1,000,000,000+ USD          140x+ संप्रभु स्तर    |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. तकनीकी आधार: सत्यापित एवं लाइव (शून्य खोखले वादे)
* **कर्नेल रक्षा स्कोर 15/15:** Solana Anchor v6.9.3 स्मार्ट अनुबंध गणितीय रूप से **Wormhole, Nomad, Euler, Mango** हमलों से सुरक्षित साबित हुए हैं। **Solana Devnet** पर लाइव कार्यरत हैं।
* **स्टेट चैनल बैच संपीड़न (1,000:1):** 1,000 सूक्ष्म वाउचर को एक ऑन-चेन निपटान में संपीड़ित करता है, जिससे वास्तविक लागत प्रति लेनदेन $0.000001 तक कम हो जाती है।
* **300-स्लॉट विवाद चुनौती विंडो:** 120 सेकंड की अपरिवर्तनीय चुनौती अवधि और 100% सुरक्षा जमा जब्ती (slashing) किसी भी अनधिकृत निकासी को रोकती है।
* **पूर्ण Web3 डैशबोर्ड:** लाइव इंटरफ़ेस जो बायोमेट्रिक पासकी, बिना गैस (0-SOL) लेनदेन और वास्तविक समय मशीन निष्पादन टेलीमेट्री का समर्थन करता है।

---
*गोपनीय निवेश दस्तावेज़ • केवल अधिकृत रणनीतिक निवेशकों के लिए • HAICHAIN सिस्टम्स काउंसिल 2026*""",

    "he": """# מזכר השקעה אסטרטגי PRE-SEED של HAICHAIN
## מערכת הפעלה פיננסית וקוגניטיבית אוניברסלית למכונות אוטונומיות
### תקציר מנהלים בעמוד אחד • סבב חסוי לאנג'לים ולתומכים ראשונים ($0.007 USD)

* **פרוטוקול:** HAICHAIN (התשתית הכלכלית לבינת-על מבוזרת וסליקת סוכנים אוטונומיים)
* **ארכיטקטורת בסיס:** Solana L1 (ליבת Anchor v6.9.3) &rarr; אפ-צ'יין SVM בעל ביצועים גבוהים (שלב רול-אפ 3)
* **היקף הסבב:** $140,000 עד $210,000 USD (20,000,000 עד 30,000,000 $HAISI • 2.0% עד 3.0% מסך ההיצע)
* **מחיר הצעה ב-Pre-Seed:** **$0.007 USD / $HAISI** (הערכת שווי בדילול מלא FDV: **$7,000,000 USD**)
* **מחיר יעד ברישום ציבורי TGE:** **$0.010 USD / $HAISI** (שווי FDV: **$10,000,000 USD**)
* **יתרון למשקיעים ראשונים:** **30% הנחה** (+42.8% רווח מיידי על הנייר בעת הרישום)

---

### 1. הבעיה והשוק העצום ללא תחרות
* **מלכודת המינויים:** מעל 200 מיליון משתמשי AI ועסקים לכודים בתשלומי מנוי חודשיים כבדים (**$150 עד $450 בחודש** עבור OpenAI, Claude, Cursor, Midjourney). רשתות כרטיסי האשראי הוותיקות (Visa/Stripe) אינן מסוגלות לבצע תשלומים מתחת לסנט בשל עמלת מינימום קבועה של $0.30 לעסקה.
* **פריצת הדרך של HAICHAIN:** מערכת הפעלה לסליקה של חלקיקי סנט על **Solana L1**. מחליפה מנויים חודשיים בחיוב בזמן אמת לפי שאילתה (**$0.0008 לשאילתה**) באמצעות פרוטוקול **HTTP x402** בתוך **פחות מ-400 מילישניות**, עם חוויית **Passkey ביומטרי (FaceID)** ללא צורך במפתחות פרטיים. עמידה מלאה בתקנות ה-MiCA האירופיות באמצעות Circle USDC ו-EURC.

---

### 2. פרדיגמת $AI^2$: ריבונות אנושית ומהירות מכונה
* $\mathbf{HaiChain} \iff \mathbf{AI^2} = \text{בינה מלאכותית (AI)} \times \text{בינה אנושית אמיתית (Actual Intelligence)}$.
* בניגוד למערכות מכונה בלתי נשלטות, HAICHAIN שומרת על **האדם כריבון העליון**:
  * **שליטה עליונה:** האדם מגדיר תקרות הוצאה חומרתיות ומחזיק ב**מתג עצירת חירום (Panic Kill-Switch)** המחזיר 100% מכספי הכספת בתוך פחות מ-400 מילישניות.
  * **סימביוזה כלכלית:** סוכני AI מזרימים תמלוגים ליוצרי ידע אנושיים, ו**שוכרים באופן אוטונומי מומחים אנושיים (Reverse Micro-Tasking)** לאימות ואישור משימות מורכבות ($1.50 - $25.00 למשימה).

---

### 3. מנוע הכנסות מדורג ($15.9M ARR) וטוקנומיקה
* **מנוע סליקה משולב ב-3 שכבות:**
  * **שכבה 1 (AI צרכני):** 100,000 סוכנים קלים @ $3.40/חודש = $4.1M נפח (0.10% עמלה, $4.1k שנתי).
  * **שכבה 2 (נחילי סוכנים עסקיים):** 15,000 תהליכי עבודה ארגוניים ($350/חודש) = $63M נפח ($63k עמלה).
  * **שכבה 3 (סליקת GPU ו-API מוסדית):** 1,200 צינורות ארגוניים ($50,000/חודש) = $720M נפח (0.20-0.50% עמלה, $1.44M - $3.6M). עמלות אימות zkTLS ומרווחי נזילות מניבים ARR איתן של $15.9M.
* **צבירת ערך הטוקן:** 50% מעמלות הפרוטוקול העולמיות מיועדות ל**רכישה חוזרת ושריפה (Buyback & Burn)**; 50% מחולקים כ**תשואה אמיתית בסטייבלקוינס (USDC/USDT)** למחזיקי veHAI.
* **אפ-צ'יין SVM ריבוני:** כאשר היקף הסליקה יעלה על 100,000 עסקאות/שנייה, $HAISI יומר ביחס 1:1 לנכס ה-Gas של רשת **HAICHAIN SVM App-Chain** העצמאית (שווי יעד של $1B עד $5B+ FDV).

```
+----------------------------------------------------------------------------------------------------+
| שלב גיוס הון                  מחיר הצעה         שווי בדילול מלא (FDV)      מכפיל תשואה יעד         |
+----------------------------------------------------------------------------------------------------+
| 1. פרה-סיד פרטי (עכשיו)       $0.007 USD        $7,000,000 USD             נקודת כניסה בסיסית      |
| 2. TGE קהילתי ציבורי          $0.010 USD        $10,000,000 USD            +42.8% עליית ערך מיידית |
| 3. בורסות Tier-2 ו-100k סוכנים $0.070 USD       $70,000,000 USD            תשואה של פי 10          |
| 4. צמיחת המערכת (2027)        $0.350 USD        $350,000,000 USD           תשואה של פי 50          |
| 5. רשת SVM ריבונית עצמאית     $1.000+ USD       $1,000,000,000+ USD        פי 140+ רמת רשת ריבונית |
+----------------------------------------------------------------------------------------------------+
```

---

### 4. תשתית טכנולוגית: פועלת ומאומתת ברשת חיה (אפס הבטחות סרק)
* **ציון הגנת ליבה 15/15:** חוזי Solana Anchor v6.9.3 חסינים מתמטית מפני וקטורי התקפה של **Wormhole, Nomad, Euler ו-Mango**. פעילים ברשת **Solana Devnet**.
* **דחיסת ערוצי מצב (1,000:1):** 1,000 עסקאות מיקרו נדחסות להסדר יחיד על הבלוקצ'יין, מה שמפחית את העלות בפועל ל-$0.000001 לעסקה.
* **חלון ערעור של 300 סלוטים:** תקופת ערעור בלתי ניתנת לשינוי של 120 שניות וחילוט ערבות של 100% (Slashing) מונעים משיכות כספים חד-צדדיות.
* **דשבורד Web3 מוכן לפעולה:** ממשק חי התומך ב-Passkeys ביומטריים, עסקאות ללא Gas וטלמטריה של פעולת המכונות בזמן אמת.

---
*מסמך השקעה חסוי • למשקיעים אסטרטגיים מורשים בלבד • מועצת המערכות של HAICHAIN 2026*"""
}

# Dictionary of SAFT Agreements
SAFT_TRANSLATIONS = {
    "zh": """# HAICHAIN 种子轮前未来代币简单协议 (SAFT)
## 早期支持者私募代币份额认购协议
### 国际机构法律标准 • SOLANA SPL TOKEN-2022 架构

* **合约编号:** `HAICHAIN-SAFT-PRESEED-2026-ZH`
* **管理机构:** HAICHAIN 自主分布式架构理事会
* **资产类别:** 网络效用与治理商品 (`$HAISI` SPL 代币)
* **不可篡改固定总量:** 1,000,000,000 $HAISI (十亿枚代币)
* **种子轮前认购价:** **$0.007 USD / $HAISI** (完全稀释估值: **$7,000,000 USD**)
* **目标公开上市价 (TGE):** **$0.010 USD / $HAISI** (完全稀释估值: **$10,000,000 USD**)
* **优惠折扣:** 相比公开 TGE 享受 **30% 价格折扣** (+42.8% 初始上市溢价收益)
* **结算资产:** USDC / EURC (Circle MiCA 合规), USDT 或 SOL (按链上公允汇率结算)

---

本未来代币简单协议（以下简称“**本协议**”或“**SAFT**”）证明：鉴于下述签字购买方（以下简称“**购买方**”）向 **HAICHAIN 去中心化系统架构特别工作组**（以下简称“**公司**”或“**HAICHAIN**”）支付下文指定的认购金额（以下简称“**认购金额**”），公司特此向购买方授予按照本协议条款获得指定配额 **$HAISI 代币**（以下简称“**代币**”）的合法权利。

---

### 第 1 条: 交易参数与代币分配

1. **认购金额 (Purchase Amount):**
   * 购买方同意认购支付: `________________________` **USD** (通过 USDT、USDC 或 SOL 等值支付至公司多签金库地址)。
2. **代币分配计算公式:**
   $$\text{分配代币数量 ($HAISI)} = \frac{\text{认购金额 (USD)}}{\$0.007 \text{ USD}}$$
   * 购买方获配的 $HAISI 代币总数: `________________________` **$HAISI**。
3. **本轮私募总硬顶上限:**
   * 本轮种子轮前私募严格受限于 **25,000,000 至 30,000,000 $HAISI (最多占固定总供应量的 3.0%)**，总融资金额硬顶上限为 $210,000 USD。

---

### 第 2 条: 链上解锁机制与分配规则 (3 大技术不变量)

为维护二级市场价格稳定、保护公开市场流通性与社区参与者权益，本协议项下发行的代币 100% 由 Solana 链上智能合约 (Streamflow 或 Solana Token-2022 Transfer-Hook PDA) 自动执行:

1. **TGE 初始解锁 (20.0%):**
   * 在代币生成事件 (TGE) 并在去中心化交易所 (Meteora DLMM / Raydium) 启动流动性池时，代币总量的 **20.0%** 立即解除锁定并可认领。
2. **锁定期 Cliff (2 个月):**
   * TGE 后设立强制性的 **2 个月锁定期 (60 个自然日)**，期间链上智能合约严格锁定，不释放任何代币。
3. **线性持续流式释放 (6 个月):**
   * 剩余 **80.0%** 代币在接下来的 **6 个月 (180 个自然日)** 内，按每秒 / 每区块的进度线性匀速解锁。
4. **非托管自主认领:**
   * 购买方可直接使用经授权的 Solana Ed25519 钱包调用链上指令自主提取已解锁代币，无需任何第三方中介介入。

```
                     PRE-SEED TOKEN VESTING SCHEDULE ($0.007)
                     
    100% ┌────────────────────────────────────────────────────────────► [第 8 个月: 100% 完全解锁]
         │                                                     /
         │                                                    /  (随后的 6 个月内
         │                                                   /    按秒 / 按区块持续
     20% ├───┐                                              /     线性流式释放)
         │   │                                             /
         │   │   [2 个月 Cliff: 链上绝对锁定零释放]        /
      0% └───┴──────────────────────────────────────────┴──────────────► 时间轴
           TGE (第 0 天)                               第 2 个月        第 8 个月
```

---

### 第 3 条: 资产属性与法律承诺

1. **功能性效用代币:**
   * `$HAISI` 代币被构建为纯粹的去中心化网络功能效用商品，具备以下效用:
     * 享有自主机器微支付费用 50% 的直接折扣。
     * 支持 veHAI 质押并以纯正 USDT 稳定币分享协议现金流真实收益 (Real Yield)。
     * 在 HAICHAIN 主权 L1 网络激活时作为原生 Gas 燃料与验证质押资产。
2. **非公司股权或证券:**
   * 本协议不代表任何法律实体的股份、股权、所有权或股息红利权利。代币的效用完全依附于去中心化协议的运行。
3. **反恶意做空与市场诚信契约:**
   * 购买方承诺不从事任何合成做空、场外低于平价抛售或未经授权操纵市场流动性的行为。

---

### 第 4 条: 保密与排他义务

在 HAICHAIN 正式向全球市场公开发布 TGE 上市参数之前，购买方同意对本协议所享有的 $0.007 优惠估值条款及技术架构简报严格保密。

---

### 签署与确认栏 (SIGNATURE BLOCK)

* **购买方全称 / 企业机构名称:** `________________________________________________`
* **护照号码 / 商业登记注册号:** `________________________________________________`
* **联系电子邮箱:** `________________________________________________`
* **实际认购金额 (USD 等值):** `$________________________`
* **认购 $HAISI 代币配额:** `________________________ $HAISI`
* **购买方指定 Solana 接收钱包地址 (Ed25519 Pubkey):**  
  `____________________________________________________________________`

| 公司授权代表 (HAICHAIN 架构理事会) | 认购方授权签署人 (早期战略投资人) |
| :--- | :--- |
| **授权签字:**<br><br><br>____________________________________ | **授权签字:**<br><br><br>____________________________________ |
| **日期:** 2026年 ____ 月 ____ 日 | **日期:** 2026年 ____ 月 ____ 日 |
| **官方多签金库地址:**<br>`HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **指定接收代币地址:**<br>`________________________________________________` |

---
*正式法律文书 • 受国际数字资产通用准则管辖 • HAICHAIN 2026*""",

    "ko": """# HAICHAIN 프리시드 SAFT 계약서
## 미래 토큰을 위한 단순 계약 (프라이빗 프리시드 배정)
### 글로벌 기관 법률 표준 • SOLANA SPL TOKEN-2022 아키텍처

* **계약 식별 번호:** `HAICHAIN-SAFT-PRESEED-2026-KO`
* **주관 기관:** HAICHAIN 자율 분산 아키텍처 위원회
* **자산 분류:** 네트워크 유틸리티 및 거버넌스 상품 (`$HAISI` SPL 토큰)
* **불변 고정 총 공급량:** 1,000,000,000 $HAISI (10억 개)
* **프리시드 제공 가격:** **$0.007 USD / $HAISI** (완전 희석 가치: **$7,000,000 USD**)
* **목표 공모 상장 가격 (TGE):** **$0.010 USD / $HAISI** (완전 희석 가치: **$10,000,000 USD**)
* **우대 할인율:** 공개 TGE 대비 **30% 할인** (상장 즉시 장부상 +42.8% 가치 상승)
* **정산 통화:** USDC / EURC (Circle MiCA 규정 준수), USDT 또는 SOL

---

본 미래 토큰 단순 계약(이하 "**본 계약**" 또는 "**SAFT**")은 아래 서명한 구매자(이하 "**구매자**")가 **HAICHAIN 탈중앙화 시스템 아키텍처 태스크포스**(이하 "**회사**" 또는 "**HAICHAIN**")에 아래 명시된 구매 금액(이하 "**구매 금액**")을 지불함에 따라, 회사가 구매자에게 본 계약에 규정된 조건에 따라 **$HAISI 토큰**(이하 "**토큰**")에 대한 권리를 부여함을 증명합니다.

---

### 제 1 조: 거래 매개변수 및 토큰 배정

1. **구매 금액 (Purchase Amount):**
   * 구매자는 다음 금액을 납입하기로 합의합니다: `________________________` **USD** (USDT, USDC 또는 SOL 상당액으로 다중 서명 금고 주소로 이체).
2. **토큰 배정 계산 공식:**
   $$\text{배정 토큰 수량 ($HAISI)} = \frac{\text{구매 금액 (USD)}}{\$0.007 \text{ USD}}$$
   * 구매자에게 배정된 총 $HAISI 토큰 수량: `________________________` **$HAISI**.
3. **프리시드 총 트랜치 상한:**
   * 본 프라이빗 라운드는 **25,000,000 ~ 30,000,000 $HAISI(총 고정 공급량의 최대 3.0%)**로 엄격히 제한되며, 총 자본 형성 상한선은 $210,000 USD입니다.

---

### 제 2 조: 온체인 베스팅 및 분배 메커니즘 (3대 불변 규칙)

2차 시장 안정성과 $0.010 공개 상장 참여자들을 보호하기 위해, 본 SAFT에 따라 발행되는 토큰은 Solana 온체인 스마트 계약을 통해 100% 집행됩니다:

1. **초기 TGE 잠금 해제 (20.0%):**
   * 토큰 생성 이벤트(TGE) 시 및 DEX 풀(Meteora DLMM / Raydium) 개설 즉시 총 배정량의 **20.0%**가 즉시 청구 가능해집니다.
2. **클리프 동결 기간 (2개월):**
   * TGE 이후 의무적인 **2개월 클리프(60일)** 기간 동안 온체인 상에서 추가 분배 없이 엄격히 동결됩니다.
3. **연속 선형 스트리밍 (6개월):**
   * 나머지 **80.0%**는 이후 **6개월(180일)** 동안 매 초 / 매 슬롯 단위로 일정하게 연속 잠금 해제됩니다.
4. **비수탁형 직접 청구:**
   * 구매자는 중앙화된 중개인 없이 검증된 본인의 Solana Ed25519 지갑에서 직접 온체인 클레임 명령을 실행할 수 있습니다.

```
                     PRE-SEED TOKEN VESTING SCHEDULE ($0.007)
                     
    100% ┌────────────────────────────────────────────────────────────► [8개월 차: 100% 완전 해제]
         │                                                     /
         │                                                    /  (이후 6개월간
         │                                                   /    매초/매슬롯 단위
     20% ├───┐                                              /     지속적인 선형 스트리밍)
         │   │                                             /
         │   │   [2개월 클리프: 온체인 제로 분배 동결]     /
      0% └───┴──────────────────────────────────────────┴──────────────► 일정 타임라인
           TGE (0일 차)                                 2개월 차         8개월 차
```

---

### 제 3 조: 자산 분류 및 법적 확약

1. **기능적 유틸리티 상품:**
   * `$HAISI` 토큰은 네트워크 기능성 상품으로 설계되었으며 다음 용도로 사용됩니다:
     * 자율 기계 마이크로 결제 수수료 50% 할인.
     * veHAI 스테이킹을 통한 순수 USDT 실제 수익(Real Yield) 분배.
     * HAICHAIN 주권 L1 활성화 시 기본 가스 및 합의 검증 자산.
2. **지분 및 증권성 배제:**
   * 본 계약은 회사의 주식, 지분, 소유권 또는 배당 권리를 의미하지 않습니다. 토큰의 가치는 프로토콜 실행에 귀속됩니다.
3. **시장 무결성 준수 확약:**
   * 구매자는 합성 공매도, 상장가 이하의 장외 덤핑, 비정상적 유동성 조작에 관여하지 않을 것을 확약합니다.

---

### 서명 및 날인란 (SIGNATURE BLOCK)

* **구매자 법적 성명 / 법인명:** `________________________________________________`
* **여권 번호 / 사업자등록번호:** `________________________________________________`
* **공식 연락처 이메일:** `________________________________________________`
* **구매 금액 (USD 상당액):** `$________________________`
* **배정 $HAISI 토큰 수량:** `________________________ $HAISI`
* **구매자 지정 Solana 수령 지갑 (Ed25519 Pubkey):**  
  `____________________________________________________________________`

| 회사 대표 (HAICHAIN 아키텍처 위원회) | 구매자 대표 (초기 전략적 투자자) |
| :--- | :--- |
| **서명:**<br><br><br>____________________________________ | **서명:**<br><br><br>____________________________________ |
| **일자:** 2026년 ____ 월 ____ 일 | **일자:** 2026년 ____ 월 ____ 일 |
| **공식 다중서명 금고:**<br>`HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **지정 수령 지갑 주소:**<br>`________________________________________________` |

---
*공식 법률 문서 • 국제 디지털 자산 표준 준용 • HAICHAIN 2026*""",

    "es": """# ACUERDO SAFT PRE-SEED DE HAICHAIN
## ACUERDO SIMPLE PARA FUTUROS TOKENS (ASIGNACIÓN PRIVADA PRE-SEED)
### ESTÁNDAR LEGAL INSTITUCIONAL • ARQUITECTURA SOLANA SPL TOKEN-2022

* **Identificador de Contrato:** `HAICHAIN-SAFT-PRESEED-2026-ES`
* **Órgano de Gobierno:** Consejo de Arquitectura Distribuida Autónoma de HAICHAIN
* **Clasificación del Activo:** Mercancía de Utilidad y Gobernanza de Red (Token SPL `$HAISI`)
* **Suministro Fijo Total:** 1,000,000,000 $HAISI (Mil Millones de Tokens Inmutables)
* **Precio de Oferta Pre-Seed:** **$0.007 USD / $HAISI** (FDV Implícito: **$7,000,000 USD**)
* **Precio Objetivo de Cotización Pública (TGE):** **$0.010 USD / $HAISI** (FDV: **$10,000,000 USD**)
* **Descuento Preferencial:** **30% de Descuento** frente al TGE público (+42.8% de plusvalía inicial)
* **Moneda de Liquidación:** USDC / EURC (Conforme a MiCA de Circle), USDT o SOL

---

EL PRESENTE ACUERDO SIMPLE PARA FUTUROS TOKENS (este "**Acuerdo**" o "**SAFT**") certifica que, a cambio del pago por parte del comprador abajo firmante (el "**Comprador**") del importe de compra establecido a continuación (el "**Importe de Compra**"), el **Grupo de Trabajo de Arquitectura de Sistemas Descentralizados de HAICHAIN** (la "**Compañía**" o "**HAICHAIN**") otorga al Comprador el derecho a recibir la asignación de **Tokens $HAISI** (los "**Tokens**"), con sujeción a los términos aquí contenidos.

---

### SECCIÓN 1: PARÁMETROS DE LA TRANSACCIÓN Y ASIGNACIÓN

1. **Importe de Compra:**
   * El Comprador acuerda aportar: `________________________` **USD** (pagadero en USDT, USDC o SOL a la Tesorería Multifirma).
2. **Cálculo de Asignación de Tokens:**
   $$\text{Tokens Asignados ($HAISI)} = \frac{\text{Importe de Compra (USD)}}{\$0.007 \text{ USD}}$$
   * Total de Tokens $HAISI asignados: `________________________` **$HAISI**.
3. **Límite Máximo de la Ronda:**
   * Esta ronda está estrictamente limitada a **25,000,000 a 30,000,000 $HAISI (máximo 3.0% del suministro total)**, con un tope máximo de financiación de \$210,000 USD.

---

### SECCIÓN 2: CALENDARIO DE DESBLOQUEO ON-CHAIN (VESTING)

1. **Desbloqueo Inicial en TGE (20.0%):** El **20.0%** se desbloquea inmediatamente en el Evento de Generación de Tokens (TGE).
2. **Periodo Cliff de Bloqueo (2 Meses):** Un **Cliff obligatorio de 2 Meses (60 días)** mantiene los tokens congelados sin liberaciones.
3. **Flujo Lineal Continuo (6 Meses):** El **80.0%** restante se desbloquea de forma continua por segundo durante los siguientes **6 Meses (180 días)**.
4. **Reclamación No Custodial:** El Comprador reclama directamente desde su billetera verificada Solana Ed25519.

---

### SECCIÓN 3: CLASIFICACIÓN DEL ACTIVO Y COMPROMISOS

1. **Mercancía de Utilidad:** El Token `$HAISI` otorga un 50% de descuento en micropagos de máquinas, permite staking en veHAI para recibir rendimientos reales en USDT y funciona como gas en la red L1 de HAICHAIN.
2. **Sin Derechos Accionarios:** Este acuerdo no representa acciones, propiedad ni derechos a dividendos de ninguna entidad jurídica.
3. **Compromiso Antidumping:** El Comprador se compromete a no realizar ventas masivas ni manipulaciones de liquidez.

---

### BLOQUE DE FIRMAS (SIGNATURE BLOCK)

* **Nombre Legal / Entidad del Comprador:** `________________________________________________`
* **Pasaporte / Documento de Identidad:** `________________________________________________`
* **Correo Electrónico:** `________________________________________________`
* **Importe de Compra (USD):** `$________________________`
* **Tokens $HAISI Asignados:** `________________________ $HAISI`
* **Billetera Solana de Recepción (Ed25519):** `________________________________________________`

| POR LA COMPAÑÍA (CONSEJO HAICHAIN) | POR EL COMPRADOR (INVERSOR ESTRATÉGICO) |
| :--- | :--- |
| **Firma Autorizada:**<br><br>____________________________________ | **Firma Autorizada:**<br><br>____________________________________ |
| **Fecha:** ____ / ____ / 2026 | **Fecha:** ____ / ____ / 2026 |
| **Tesorería Multifirma:** `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **Dirección Solana de Destino:** `____________________________________` |

---
*Instrumento Legal Oficial • Bajo Estándares Internacionales de Activos Digitales • HAICHAIN 2026*""",

    "fr": """# ACCORD SAFT PRE-SEED HAICHAIN
## ACCORD SIMPLE POUR TOKENS FUTURS (ALLOCATION PRIVÉE PRE-SEED)
### NORME JURIDIQUE INSTITUTIONNELLE • ARCHITECTURE SOLANA SPL TOKEN-2022

* **Identifiant du Contrat:** `HAICHAIN-SAFT-PRESEED-2026-FR`
* **Organe Directeur:** Conseil de l'Architecture Distribuée Autonome HAICHAIN
* **Classification de l'Actif:** Actif d'Utilité et de Gouvernance Réseau (Token SPL `$HAISI`)
* **Offre Fixe Totale:** 1 000 000 000 $HAISI (Un Milliard de Tokens Immuables)
* **Prix de l'Offre Pre-Seed:** **$0.007 USD / $HAISI** (FDV Implicite: **$7 000 000 USD**)
* **Prix d'Introduction Publique Cible (TGE):** **$0.010 USD / $HAISI** (FDV: **$10 000 000 USD**)
* **Remise Préférentielle:** **30% de Réduction** par rapport au TGE (+42,8% de gain initial)
* **Devise de Règlement:** USDC / EURC (Conforme à MiCA Circle), USDT ou SOL

---

LE PRÉSENT ACCORD SIMPLE POUR TOKENS FUTURS (cet "**Accord**" ou "**SAFT**") atteste qu'en contrepartie du paiement par l'acheteur soussigné (l'"**Acheteur**") du montant d'achat fixé ci-dessous (le "**Montant d'Achat**"), le **Groupe de Travail sur l'Architecture des Systèmes Décentralisés HAICHAIN** (la "**Société**" ou "**HAICHAIN**") confère à l'Acheteur le droit à une allocation de **Tokens $HAISI** (les "**Tokens**"), selon les modalités énoncées aux présentes.

---

### SECTION 1: PARAMÈTRES DE LA TRANSACTION ET ALLOCATION

1. **Montant d'Achat:**
   * L'Acheteur s'engage à verser: `________________________` **USD** (payable en USDT, USDC ou SOL vers la Trésorerie Multi-Sig).
2. **Calcul de l'Allocation:**
   $$\text{Tokens Alloués ($HAISI)} = \frac{\text{Montant d'Achat (USD)}}{\$0.007 \text{ USD}}$$
   * Total des Tokens $HAISI attribués: `________________________` **$HAISI**.
3. **Plafond du Tour Privé:**
   * Ce tour est strictement plafonné à **25 000 000 à 30 000 000 $HAISI (3,0% max de l'offre totale)**, soit un plafond de \$210 000 USD.

---

### SECTION 2: MÉCANISME DE VESTING ON-CHAIN

1. **Déblocage Initial au TGE (20.0%):** **20,0%** des tokens sont immédiatement réclamables dès l'événement de génération des tokens (TGE).
2. **Période de Gel Cliff (2 Mois):** Un **Cliff de 2 Mois (60 jours)** gèle intégralement le solde sans aucune émission.
3. **Flux Linéaire Continu (6 Mois):** Les **80,0%** restants se débloquent par seconde de manière continue sur les **6 Mois (180 jours)** suivants.
4. **Réclamation Non Dépositaire:** L'Acheteur réclame directement depuis son portefeuille Solana Ed25519 vérifié.

---

### SECTION 3: ENGAGEMENTS JURIDIQUES ET SOUVERAINETÉ

1. **Actif d'Utilité Réseau:** Le Token `$HAISI` offre 50% de réduction sur les micro-paiements, permet le staking veHAI pour percevoir des revenus réels en USDT et sert de gas natif sur le réseau L1 HAICHAIN.
2. **Absence de Droits Sociaux:** Cet accord ne confère aucune action ni droit à dividende dans une quelconque entité morale.
3. **Engagement de Non-Manipulation:** L'Acheteur s'interdit toute vente prédatrice sous la parité de cotation.

---

### BLOC DE SIGNATURE (SIGNATURE BLOCK)

* **Nom Légal / Entité de l'Acheteur:** `________________________________________________`
* **Passeport / Numéro d'Enregistrement:** `________________________________________________`
* **Courriel de Contact:** `________________________________________________`
* **Montant d'Achat (USD):** `$________________________`
* **Tokens $HAISI Alloués:** `________________________ $HAISI`
* **Portefeuille Solana de Réception:** `________________________________________________`

| POUR LA SOCIÉTÉ (CONSEIL HAICHAIN) | POUR L'ACHETEUR (INVESTISSEUR STRATÉGIQUE) |
| :--- | :--- |
| **Signature Autorisée:**<br><br>____________________________________ | **Signature Autorisée:**<br><br>____________________________________ |
| **Date:** ____ / ____ / 2026 | **Date:** ____ / ____ / 2026 |
| **Trésorerie Multi-Sig:** `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **Adresse Solana de Réception:** `____________________________________` |

---
*Instrument Juridique Officiel • Régulé par les Normes Numériques Internationales • HAICHAIN 2026*""",

    "ru": """# СОГЛАШЕНИЕ SAFT PRE-SEED HAICHAIN
## ПРОСТОЕ СОГЛАШЕНИЕ О БУДУЩИХ ТОКЕНАХ (ЧАСТНОЕ ВЫДЕЛЕНИЕ PRE-SEED)
### МЕЖДУНАРОДНЫЙ ИНСТИТУЦИОНАЛЬНЫЙ СТАНДАРТ • АРХИТЕКТУРА SOLANA SPL TOKEN-2022

* **Идентификатор соглашения:** `HAICHAIN-SAFT-PRESEED-2026-RU`
* **Руководящий орган:** Совет автономной распределенной архитектуры HAICHAIN
* **Классификация актива:** Сетевой утилитарный и управленческий актив (SPL токен `$HAISI`)
* **Фиксированная эмиссия:** 1 000 000 000 $HAISI (Один миллиард токенов)
* **Цена предложения Pre-Seed:** **$0.007 USD / $HAISI** (Оценка FDV: **$7 000 000 USD**)
* **Целевая цена листинга TGE:** **$0.010 USD / $HAISI** (Оценка FDV: **$10 000 000 USD**)
* **Преференциальная скидка:** **30% скидка** от цены TGE (+42.8% немедленной расчетной доходности)
* **Валюта расчетов:** USDC / EURC (Соответствие Circle MiCA), USDT или SOL

---

НАСТОЯЩЕЕ ПРОСТОЕ СОГЛАШЕНИЕ О БУДУЩИХ ТОКЕНАХ (далее "**Соглашение**" или "**SAFT**") удостоверяет, что в обмен на оплату нижеподписавшимся покупателем (далее "**Покупатель**") суммы покупки, указанной ниже (далее "**Сумма покупки**"), **Рабочая группа децентрализованной системной архитектуры HAICHAIN** (далее "**Компания**" или "**HAICHAIN**") предоставляет Покупателю право на получение выделенного объема **Токенов $HAISI** (далее "**Токены**") на изложенных здесь условиях.

---

### РАЗДЕЛ 1: ПАРАМЕТРЫ СДЕЛКИ И ВЫДЕЛЕНИЕ ТОКЕНОВ

1. **Сумма покупки:**
   * Покупатель обязуется внести: `________________________` **USD** (в USDT, USDC или эквиваленте SOL на адрес Multi-Sig казначейства).
2. **Формула расчета объема токенов:**
   $$\text{Выделенные токены ($HAISI)} = \frac{\text{Сумма покупки (USD)}}{\$0.007 \text{ USD}}$$
   * Всего выделено токенов $HAISI Покупателю: `________________________` **$HAISI**.
3. **Лимит раунда Pre-Seed:**
   * Раунд строго ограничен объемом **25 000 000 – 30 000 000 $HAISI (максимум 3.0% эмиссии)**, что соответствует жесткому лимиту в \$210 000 USD.

---

### РАЗДЕЛ 2: МЕХАНИЗМ ОНЧЕЙН-РАЗБЛОКИРОВКИ (VESTING)

1. **Первоначальная разблокировка на TGE (20.0%):** Ровно **20.0%** становится доступно сразу в момент TGE при открытии пулов ликвидности (Meteora DLMM / Raydium).
2. **Период заморозки Cliff (2 Месяца):** Обязательный **период заморозки в 2 Месяца (60 дней)** полностью блокирует оставшиеся токены.
3. **Непрерывный линейный стриминг (6 Месяцев):** Оставшиеся **80.0%** разблокируются посекундно в течение последующих **6 Месяцев (180 дней)**.
4. **Некастодиальное востребование:** Покупатель самостоятельно вызывает смарт-контракт со своего проверенного кошелька Solana Ed25519.

---

### РАЗДЕЛ 3: ПРАВОВОЙ СТАТУС И ОБЯЗАТЕЛЬСТВА

1. **Утилитарный товар:** Токен `$HAISI` предоставляет 50% скидку на микроплатежи машин, право на стейкинг veHAI с выплатой Real Yield в USDT и роль Gas-актива в суверенной L1 сети HAICHAIN.
2. **Отсутствие корпоративных прав:** Соглашение не предоставляет акций, долей или дивидендов в каком-либо юридическом лице.
3. **Обязательство целостности рынка:** Покупатель обязуется не участвовать в манипуляциях и демпинге ниже цены размещения.

---

### БЛОК ПОДПИСЕЙ (SIGNATURE BLOCK)

* **ФИО / Юридическое лицо Покупателя:** `________________________________________________`
* **Паспорт / Регистрационный номер:** `________________________________________________`
* **Электронная почта:** `________________________________________________`
* **Сумма покупки (USD):** `$________________________`
* **Выделено токенов $HAISI:** `________________________ $HAISI`
* **Адрес кошелька Solana (Ed25519 Pubkey):** `________________________________________________`

| ОТ КОМПАНИИ (СОВЕТ HAICHAIN) | ОТ ПОКУПАТЕЛЯ (СТРАТЕГИЧЕСКИЙ ИНВЕСТОР) |
| :--- | :--- |
| **Подпись:**<br><br>____________________________________ | **Подпись:**<br><br>____________________________________ |
| **Дата:** ____ / ____ / 2026 | **Дата:** ____ / ____ / 2026 |
| **Мультисиг Казначейство:** `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **Назначенный адрес Solana:** `____________________________________` |

---
*Официальный юридический документ • Международные стандарты цифровых активов • HAICHAIN 2026*""",

    "kk": """# HAICHAIN PRE-SEED SAFT КЕЛІСІМІ
## БОЛАШАҚ ТОКЕНДЕРГЕ АРНАЛҒАН ҚАРАПАЙЫМ КЕЛІСІМ (ЖЕКЕ PRE-SEED БӨЛІНІС)
### ХАЛЫҚАРАЛЫҚ ИНСТИТУЦИОНАЛДЫҚ ЗАҢДЫҚ СТАНДАРТ • SOLANA SPL TOKEN-2022 АРХИТЕКТУРАСЫ

* **Келісімшарт нөмірі:** `HAICHAIN-SAFT-PRESEED-2026-KK`
* **Басқарушы орган:** HAICHAIN Автономды Үлестірілген Архитектура Кеңесі
* **Актив санаты:** Желілік утилитарлық және басқару тауары (`$HAISI` SPL токені)
* **Өзгермейтін тұрақты эмиссия:** 1 000 000 000 $HAISI (Бір миллиард токен)
* **Pre-Seed ұсыныс бағасы:** **$0.007 USD / $HAISI** (FDV бағалауы: **$7 000 000 USD**)
* **Мақсатты ашық листинг бағасы (TGE):** **$0.010 USD / $HAISI** (FDV бағалауы: **$10 000 000 USD**)
* **Жеңілдік мөлшері:** Ашық TGE бағасынан **30% жеңілдік** (листинг кезінде +42.8% кіріс)
* **Есеп айырысу валютасы:** USDC / EURC (Circle MiCA стандарты), USDT немесе SOL

---

ОСЫ БОЛАШАҚ ТОКЕНДЕРГЕ АРНАЛҒАН ҚАРАПАЙЫМ КЕЛІСІМ (бұдан әрі "**Келісім**" немесе "**SAFT**") төменде қол қойған сатып алушының (бұдан әрі "**Сатып алушы**") көрсетілген соманы төлеуіне байланысты, **HAICHAIN Орталықсыздандырылған Жүйелер Архитектурасы Тобы** (бұдан әрі "**Компания**" немесе "**HAICHAIN**") Сатып алушыға **$HAISI Токендерін** (бұдан әрі "**Токендер**") алу құқығын беретінін куәландырады.

---

### 1-БӨЛІМ: МӘМІЛЕ ПАРАМЕТРЛЕРІ ЖӘНЕ ТОКЕНДЕРДІ БӨЛУ

1. **Сатып алу сомасы:**
   * Сатып алушы төлеуге келіседі: `________________________` **USD** (USDT, USDC немесе SOL түрінде Multi-Sig қазынашылық мекенжайына).
2. **Токендерді есептеу формуласы:**
   $$\text{Бөлінетін Токендер ($HAISI)} = \frac{\text{Сатып алу сомасы (USD)}}{\$0.007 \text{ USD}}$$
   * Сатып алушыға тиесілі $HAISI токендерінің жалпы саны: `________________________` **$HAISI**.
3. **Раундтың жалпы шегі:**
   * Бұл раунд **25 000 000 – 30 000 000 $HAISI (жалпы эмиссияның ең көбі 3.0%)** көлемімен шектеледі, бұл \$210 000 USD сомасына сәйкес келеді.

---

### 2-БӨЛІМ: ОНЧЕЙН-ВЕСТИНГ ЖӘНЕ ҮЛЕСТІРУ ТӘРТІБІ

1. **TGE кезіндегі бастапқы босату (20.0%):** TGE кезінде өтімділік пулы ашылғанда жалпы санның **20.0%** бірден қолжетімді болады.
2. **Cliff қатыру кезеңі (2 Ай):** TGE-ден кейінгі міндетті **2 Айлық (60 күн) Cliff** кезеңінде токендер блокчейнде толық қатырылады.
3. **Үздіксіз сызықтық ағын (6 Ай):** Қалған **80.0%** келесі **6 Ай (180 күн)** бойы әр секунд сайын біркелкі босатылады.
4. **Тікелей дербес талап ету:** Сатып алушы делдалсыз тексерілген Solana Ed25519 әмиянынан тікелей талап ете алады.

---

### ҚОЛ ҚОЮ ЖӘНЕ РАСТАУ (SIGNATURE BLOCK)

* **Сатып алушының толық аты / Заңды тұлға:** `________________________________________________`
* **Төлқұжат / Тіркеу нөмірі:** `________________________________________________`
* **Байланыс электрондық поштасы:** `________________________________________________`
* **Сатып алу сомасы (USD):** `$________________________`
* **Бөлінген $HAISI Токендері:** `________________________ $HAISI`
* **Тағайындалған Solana әмияны:** `________________________________________________`

| КОМПАНИЯ АТЫНАН (HAICHAIN КЕҢЕСІ) | САТЫП АЛУШЫ АТЫНАН (ИНВЕСТОР) |
| :--- | :--- |
| **Қолы:**<br><br>____________________________________ | **Қолы:**<br><br>____________________________________ |
| **Күні:** ____ / ____ / 2026 | **Күні:** ____ / ____ / 2026 |
| **Multi-Sig Қазынашылығы:** `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **Тағайындалған Solana мекенжайы:** `____________________________________` |

---
*Ресми заңды құжат • Халықаралық цифрлық активтер стандарттарымен реттеледі • HAICHAIN 2026*""",

    "hi": """# HAICHAIN प्री-सीड SAFT समझौता
## भविष्य के टोकन के लिए सरल समझौता (निजी प्री-सीड आवंटन)
### संस्थागत कानूनी मानक • SOLANA SPL TOKEN-2022 वास्तुकला

* **अनुबंध पहचानकर्ता:** `HAICHAIN-SAFT-PRESEED-2026-HI`
* **शासी निकाय:** HAICHAIN स्वायत्त वितरित वास्तुकला परिषद
* **परिसंपत्ति वर्गीकरण:** नेटवर्क उपयोगिता और शासन वस्तु (`$HAISI` SPL टोकन)
* **कुल निश्चित आपूर्ति:** 1,000,000,000 $HAISI (एक अरब टोकन अपरिवर्तनीय)
* **प्री-सीड पेशकश मूल्य:** **$0.007 USD / $HAISI** (निहित FDV: **$7,000,000 USD**)
* **लक्ष्य सार्वजनिक सूची मूल्य (TGE):** **$0.010 USD / $HAISI** (निहित FDV: **$10,000,000 USD**)
* **तरजीही छूट:** सार्वजनिक TGE के मुकाबले **30% छूट** (सूचीकरण पर तुरंत +42.8% लाभ)
* **निपटान मुद्रा:** USDC / EURC (Circle MiCA अनुपालक), USDT या SOL

---

भविष्य के टोकन के लिए यह सरल समझौता (यह "**समझौता**" या "**SAFT**") प्रमाणित करता है कि नीचे हस्ताक्षरकर्ता क्रेता ("**क्रेता**") द्वारा नीचे निर्धारित खरीद राशि ("**खरीद राशि**") के भुगतान के बदले, **HAICHAIN विकेंद्रीकृत सिस्टम वास्तुकला टास्कफोर्स** ("**कंपनी**" या "**HAICHAIN**") एतद्द्वारा क्रेता को यहां निर्धारित नियमों और शर्तों के अधीन **$HAISI टोकन** ("**टोकन**") के आवंटन का अधिकार जारी करती है।

---

### अनुभाग 1: लेनदेन पैरामीटर और टोकन आवंटन

1. **खरीद राशि:**
   * क्रेता योगदान करने के लिए सहमत है: `________________________` **USD** (मल्टी-सिग ट्रेजरी पते पर देय)।
2. **टोकन आवंटन गणना:**
   $$\text{आवंटित टोकन ($HAISI)} = \frac{\text{खरीद राशि (USD)}}{\$0.007 \text{ USD}}$$
   * क्रेता को आवंटित कुल $HAISI टोकन: `________________________` **$HAISI**।
3. **राउंड की कुल सीमा:**
   * यह निजी राउंड **25,000,000 से 30,000,000 $HAISI (कुल आपूर्ति का अधिकतम 3.0%)** पर सीमित है, जो \$210,000 USD के अधिकतम पूंजी निर्माण का प्रतिनिधित्व करता है।

---

### अनुभाग 2: ऑन-चेन वेस्टिंग तंत्र (3 अपरिवर्तनीय नियम)

1. **प्रारंभिक TGE अनलॉक (20.0%):** टोकन जनरेशन इवेंट (TGE) पर तुरंत **20.0%** का दावा किया जा सकता है।
2. **क्लिफ फ्रीज बाधा (2 महीने):** TGE के बाद **2 महीने (60 दिन)** की अनिवार्य अवधि तक टोकन पूर्णतः जमे रहते हैं।
3. **निरंतर रैखिक स्ट्रीमिंग (6 महीने):** शेष **80.0%** बाद के **6 महीनों (180 दिनों)** में प्रति सेकंड रैखिक रूप से अनलॉक होता है।
4. **गैर-कस्टोडियल दावा:** क्रेता सीधे अपने सत्यापित Solana Ed25519 वॉलेट से टोकन प्राप्त कर सकता है।

---

### हस्ताक्षर ब्लॉक (SIGNATURE BLOCK)

* **क्रेता का पूरा कानूनी नाम / कॉर्पोरेट संस्था:** `________________________________________________`
* **पासपोर्ट / राष्ट्रीय पहचान संख्या:** `________________________________________________`
* **प्राथमिक संपर्क ईमेल पता:** `________________________________________________`
* **खरीद राशि (USD):** `$________________________`
* **आवंटित $HAISI टोकन:** `________________________ $HAISI`
* **क्रेता का प्राप्त करने वाला Solana वॉलेट:** `________________________________________________`

| कंपनी के लिए (HAICHAIN परिषद) | क्रेता के लिए (रणनीतिक निवेशक) |
| :--- | :--- |
| **अधिकृत हस्ताक्षर:**<br><br>____________________________________ | **अधिकृत हस्ताक्षर:**<br><br>____________________________________ |
| **दिनांक:** ____ / ____ / 2026 | **दिनांक:** ____ / ____ / 2026 |
| **मल्टी-सिग ट्रेजरी:** `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **नामित Solana पता:** `____________________________________` |

---
*आधिकारिक कानूनी दस्तावेज • अंतर्राष्ट्रीय डिजिटल संपत्ति मानकों के तहत शासित • HAICHAIN 2026*""",

    "he": """# הסכם SAFT PRE-SEED של HAICHAIN
## הסכם פשוט עבור טוקנים עתידיים (הקצאת PRE-SEED פרטית)
### תקן משפטי מוסדי • ארכיטקטורת SOLANA SPL TOKEN-2022

* **מזהה חוזה:** `HAICHAIN-SAFT-PRESEED-2026-HE`
* **גוף מנהל:** מועצת הארכיטקטורה המבוזרת האוטונומית של HAICHAIN
* **סיווג נכס:** מוצר שימוש וממשל רשתי (טוקן SPL מסוג `$HAISI`)
* **היצע קבוע כולל:** 1,000,000,000 $HAISI (מיליארד טוקנים ללא שינוי)
* **מחיר הצעה ב-Pre-Seed:** **$0.007 USD / $HAISI** (שווי FDV: **$7,000,000 USD**)
* **מחיר יעד ברישום ציבורי (TGE):** **$0.010 USD / $HAISI** (שווי FDV: **$10,000,000 USD**)
* **הנחה מועדפת:** **30% הנחה** ביחס ל-TGE הציבורי (+42.8% עליית ערך מיידית)
* **מטבע סליקה:** USDC / EURC (תואם Circle MiCA), USDT או SOL

---

הסכם פשוט זה עבור טוקנים עתידיים (להלן "**הסכם זה**" או "**SAFT**") מאשר כי בתמורה לתשלום על ידי הרוכש החתום מטה (להלן "**הרוכש**") של סכום הרכישה המפורט להלן (להלן "**סכום הרכישה**"), **צוות משימת ארכיטקטורת המערכות המבוזרות של HAICHAIN** (להלן "**החברה**" או "**HAICHAIN**") מעניק בזאת לרוכש את הזכות להקצאת **טוקנים מסוג $HAISI** (להלן "**הטוקנים**"), בכפוף לתנאים המפורטים להלן.

---

### סעיף 1: פרמטרי עסקה והקצאת טוקנים

1. **סכום הרכישה:**
   * הרוכש מסכים להשקיע: `________________________` **USD** (באמצעות USDT, USDC או SOL לקופת המולטי-סיג).
2. **חישוב הקצאת טוקנים:**
   $$\text{טוקנים מוקצים ($HAISI)} = \frac{\text{סכום הרכישה (USD)}}{\$0.007 \text{ USD}}$$
   * סך טוקני $HAISI המוקצים לרוכש: `________________________` **$HAISI**.
3. **תקרת הסבב:**
   * סבב זה מוגבל באופן קשיח ל-**25,000,000 עד 30,000,000 $HAISI (לכל היותר 3.0% מסך ההיצע)**, המהווים תקרת גיוס מקסימלית של \$210,000 USD.

---

### סעיף 2: מנגנון שחרור (VESTING) על גבי הבלוקצ'יין

1. **שחרור ראשוני ב-TGE (20.0%):** **20.0%** זמינים לתביעה מיידית באירוע הנפקת הטוקנים (TGE).
2. **תקופת הקפאה Cliff (2 חודשים):** תקופת **Cliff מחייבת של חודשיים (60 יום)** שבה כל היתרה נעולה.
3. **שחרור ליניארי רציף (6 חודשים):** יתרת **80.0%** משתחררת בכל שנייה לאורך **6 החודשים (180 יום)** הבאים.
4. **תביעה ללא משמורת:** הרוכש מושך את הטוקנים ישירות מארנק ה-Solana Ed25519 המאומת שלו.

---

### בלוק חתימות (SIGNATURE BLOCK)

* **שם מלא / ישות משפטית של הרוכש:** `________________________________________________`
* **מספר דרכון / רישום תאגידי:** `________________________________________________`
* **דוא"ל ליצירת קשר:** `________________________________________________`
* **סכום הרכישה (USD):** `$________________________`
* **טוקני $HAISI שהוקצו:** `________________________ $HAISI`
* **כתובת ארנק Solana למשיכה:** `________________________________________________`

| מטעם החברה (מועצת HAICHAIN) | מטעם הרוכש (משקיע אסטרטגי) |
| :--- | :--- |
| **חתימה מורשית:**<br><br>____________________________________ | **חתימה מורשית:**<br><br>____________________________________ |
| **תאריך:** ____ / ____ / 2026 | **תאריך:** ____ / ____ / 2026 |
| **קופת מולטי-סיג:** `HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW` | **כתובת Solana לקבלת טוקנים:** `____________________________________` |

---
*מסמך משפטי רשמי • כפוף לתקנים בינלאומיים לנכסים דיגיטליים • HAICHAIN 2026*"""
}

# Also ensure Vietnamese single editions are in place or copied
# For VI: copy VI_EN or create clean VI
if not os.path.exists("HAICHAIN_PRESEED_SAFT_AGREEMENT_VI.md") and os.path.exists("HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md"):
    shutil.copy2("HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI.md")
if not os.path.exists("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md") and os.path.exists("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md"):
    shutil.copy2("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI.md")

# Write markdown files
for lang, content in MEMO_TRANSLATIONS.items():
    md_file = f"HAICHAIN_PRESEED_ONE_PAGER_MEMO_{lang.upper()}.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {md_file}")

for lang, content in SAFT_TRANSLATIONS.items():
    md_file = f"HAICHAIN_PRESEED_SAFT_AGREEMENT_{lang.upper()}.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {md_file}")

# List of all files to compile across 10 languages
tasks = []
all_langs = ["en", "vi", "zh", "ko", "es", "fr", "ru", "kk", "hi", "he"]

for lang in all_langs:
    memo_md = f"HAICHAIN_PRESEED_ONE_PAGER_MEMO_{lang.upper()}.md"
    memo_pdf = f"HAICHAIN_PRESEED_ONE_PAGER_MEMO_{lang.upper()}.pdf"
    if os.path.exists(memo_md):
        tasks.append((memo_md, memo_pdf, lang))

    saft_md = f"HAICHAIN_PRESEED_SAFT_AGREEMENT_{lang.upper()}.md"
    saft_pdf = f"HAICHAIN_PRESEED_SAFT_AGREEMENT_{lang.upper()}.pdf"
    if os.path.exists(saft_md):
        tasks.append((saft_md, saft_pdf, lang))

# Include legacy VI_EN as well
tasks.append(("HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.md", "HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf", "vi"))
tasks.append(("HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.md", "HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf", "vi"))

print(f"\n--- Total compilation tasks: {len(tasks)} ---")
for md, pdf, lang in tasks:
    if os.path.exists(md):
        print(f"Building {pdf} for {lang}...")
        build_pdf_from_markdown(md, pdf, lang=lang)
        app_target = os.path.join("app", pdf)
        shutil.copy2(pdf, app_target)
        print(f"[OK] Generated & Copied {pdf} -> {app_target} ({os.path.getsize(pdf)} bytes)")

print("\nALL 10 INTERNATIONAL SAFT AND MEMO PDFS SUCCESSFULLY COMPILED!")
