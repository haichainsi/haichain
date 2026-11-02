# -*- coding: utf-8 -*-
import sys, os, json

sys.stdout.reconfigure(encoding='utf-8')

# Translations for all 10 languages
ALL_TRANSLATIONS = {
    "vi": {
        "agenticShift.badge": "LÀN SÓNG TOÀN CẦU • KỶ NGUYÊN AI AGENT (2026+)",
        "agenticShift.title": "Cả thế giới công nghệ đều nhận ra: \"AI Agent bắt buộc phải có tiền!\"",
        "agenticShift.subtitle": "Cả thế giới công nghệ (từ OpenAI, Google, Stripe cho đến Coinbase) đều đã nhận ra một sự thật: \"Năm 2023 - 2024 là kỷ nguyên AI biết trò chuyện (Chatbot). Nhưng từ năm 2026 trở đi là kỷ nguyên AI biết tự hành động (AI Agent). Và một khi AI hành động, nó BẮT BUỘC phải có tiền!\"",
        "agenticShift.card1Title": "Gã khổng lồ thanh toán Stripe (Mỹ)",
        "agenticShift.card1Desc": "Vừa thành lập một bộ phận riêng nghiên cứu \"Agentic Commerce\" (Thương mại cho AI).",
        "agenticShift.card2Title": "Sàn tiền mã hóa Coinbase (Mỹ)",
        "agenticShift.card2Desc": "CEO Brian Armstrong vừa tuyên bố: \"Các nhà phát triển hãy cấp ví tiền cho AI đi, tương lai là máy móc tự thanh toán với nhau\".",
        "agenticShift.card3Title": "Các Startup gọi vốn khủng",
        "agenticShift.card3Desc": "Các công ty như Skyfire Systems hay Nevermined vừa huy động hàng chục triệu USD từ các quỹ lớn chỉ để giải quyết bài toán: Làm sao để AI có thể tự quẹt tiền?",

        "advantages.badge": "LỢI THẾ CỐT LÕI • 4 ĐỘT PHÁ SỐNG CÒN",
        "advantages.title": "Vậy HAICHAIN có gì KHÁC BIỆT để vượt trội?",
        "advantages.subtitle": "Hầu hết các dự án trên thế giới hiện nay chỉ mới là ý tưởng trên giấy hoặc làm theo lối mòn cũ. HAICHAIN tạo ra 4 sự khác biệt mang tính sống còn:",
        "advantages.item1Title": "1. Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí",
        "advantages.item1Rival": "<strong>Các đối thủ trên thế giới:</strong> Họ cố dùng thẻ tín dụng hoặc cổng thanh toán truyền thống. Nhưng thẻ Visa/Mastercard có phí tối thiểu là <strong>$0.30 + 2.9%</strong> cho mỗi giao dịch. Nếu con AI của bạn chỉ đọc 1 đoạn văn tốn <strong>$0.002</strong>, bạn không thể trả $0.30 tiền phí cho một việc giá $0.002 được (phí đắt gấp 150 lần giá trị công việc)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Thiết kế riêng công nghệ Kênh thanh toán vi mô (State Channel) trên nền tảng Solana. Cho phép AI chi trả các khoản <strong>$0.001, $0.002</strong> với <strong>0% phí trung gian</strong> và độ trễ chỉ <strong>160 mili-giây</strong> (nhanh hơn cái chớp mắt)!",
        "advantages.item2Title": "2. Cầu dao an toàn 380ms (Chống mất tiền do AI bị hack)",
        "advantages.item2Rival": "<strong>Các đối thủ:</strong> Họ chỉ mải mê nghĩ cách \"Làm sao cho AI tiêu tiền thật nhanh\", mà quên mất bài toán an toàn: Lỡ con AI bị kẻ xấu lừa (Prompt Injection) hoặc bị lỗi lặp tiêu sạch tiền thì sao?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Đặt \"Quyền kiểm soát của con người\" lên số 1:<br>&bull; <strong>Hạn mức vận tốc (Velocity Cap):</strong> Khóa cứng tốc độ tiêu tiền (ví dụ không quá $0.50/phút).<br>&bull; <strong>Cầu dao ngắt khẩn cấp (Emergency Kill-Switch):</strong> Nếu thấy AI có dấu hiệu bất thường, bạn chỉ cần bấm 1 nút hoặc nhắn 1 tin, Hợp đồng thông minh sẽ đóng băng toàn bộ quỹ và rút tiền về túi bạn trong đúng <strong>380 mili-giây</strong>, không một ai có thể lấy cắp tiền của bạn.",
        "advantages.item3Title": "3. Cực kỳ đơn giản cho người dùng cuối (Chuẩn MCP của Claude)",
        "advantages.item3Rival": "<strong>Các đối thủ:</strong> Bắt người dùng phải là lập trình viên giỏi, phải tự viết mã code, cấu hình máy chủ, tạo API phức tạp thì mới dùng được.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Tiên phong đón đầu chuẩn giao thức MCP (Model Context Protocol) mới nhất của công ty Anthropic (nhà sáng lập Claude).<br>👉 <strong>Người dùng bình thường không biết code chỉ cần copy 1 đường link dán vào app Claude trên điện thoại là xong trong 30 giây!</strong>",
        "advantages.item4Title": "4. Minh bạch tuyệt đối trên Blockchain (Không ai gian lận được)",
        "advantages.item4Desc": "Mọi khoản chi dù chỉ 1 phần nghìn cent đều có chứng thực mật mã độc lập (Merkle Proof) gắn liền với mạng lưới Solana. Doanh nghiệp khi kiểm toán cuối năm có thể mở sổ cái ra đối chiếu từng giao dịch một, minh bạch 100%, không bao giờ lo nhân viên hay AI gian lận báo khống chi phí."
    },
    "en": {
        "agenticShift.badge": "GLOBAL SHIFT • THE AGENTIC ERA (2026+)",
        "agenticShift.title": "The Tech World Realizes: \"AI Agents Must Have Money!\"",
        "agenticShift.subtitle": "From OpenAI, Google, Stripe to Coinbase, the entire tech landscape has recognized an inescapable truth: \"2023 - 2024 was the era of conversational AI (Chatbots). But from 2026 onward is the era of autonomous action (AI Agents). And once AI acts, it MUST have money!\"",
        "agenticShift.card1Title": "Payment Giant Stripe (USA)",
        "agenticShift.card1Desc": "Recently established a dedicated division researching \"Agentic Commerce\" (Commerce for Autonomous AI).",
        "agenticShift.card2Title": "Crypto Exchange Coinbase (USA)",
        "agenticShift.card2Desc": "CEO Brian Armstrong declared: \"Developers, give your AI agents crypto wallets — the future is machines transacting directly with machines.\"",
        "agenticShift.card3Title": "Mega-Funded AI Startups",
        "agenticShift.card3Desc": "Pioneers like Skyfire Systems and Nevermined raised tens of millions from tier-1 VCs just to solve one question: How can AI autonomously pay for resources?",

        "advantages.badge": "CORE ADVANTAGE • 4 VITAL DIFFERENTIATORS",
        "advantages.title": "What Makes HAICHAIN Unrivaled & Far Superior?",
        "advantages.subtitle": "Most initiatives today are merely whitepapers or legacy re-wrappers. HAICHAIN delivers 4 mission-critical breakthroughs:",
        "advantages.item1Title": "1. Sub-Cent Micro-Payments (< $0.01) with 0% Fees",
        "advantages.item1Rival": "<strong>Global Competitors:</strong> Try to force credit cards or legacy payment gateways. But Visa/Mastercard mandates a minimum fee of <strong>$0.30 + 2.9%</strong> per transaction. If your AI reads a paragraph costing <strong>$0.002</strong>, you cannot pay a $0.30 fee for a $0.002 task (the fee is 150x the value of the work)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Proprietary State Channel micro-escrow engine on Solana. Enables AI to disburse <strong>$0.001, $0.002</strong> micro-payments with <strong>0% intermediary fees</strong> and only <strong>160ms latency</strong> (faster than a human eye blink)!",
        "advantages.item2Title": "2. 380ms Emergency Circuit Breaker (Anti-Drain & Exploit Defense)",
        "advantages.item2Rival": "<strong>Competitors:</strong> Only obsess over \"how to let AI spend money fast\", ignoring core safety: What if the AI falls for a Prompt Injection attack or loops uncontrollably and drains your entire wallet?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Places \"Human Sovereign Control\" at #1:<br>&bull; <strong>Velocity Cap:</strong> Hard-caps spending speed (e.g., max $0.50/minute).<br>&bull; <strong>Emergency Kill-Switch:</strong> At any anomaly, 1 tap or 1 message triggers smart contracts to freeze all vaults and refund balance to your cold wallet in exactly <strong>380ms</strong>. No adversary can drain your capital.",
        "advantages.item3Title": "3. Ultra-Simple for End-Users (Claude's Official MCP Standard)",
        "advantages.item3Rival": "<strong>Competitors:</strong> Require users to be advanced software engineers, forcing manual code writing, server configs, and complex API credential wrangling.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Pioneers Anthropic's universal Model Context Protocol (MCP) standard.<br>👉 <strong>Non-technical users simply paste 1 link into the Claude mobile app and start in 30 seconds — zero code required!</strong>",
        "advantages.item4Title": "4. Absolute Blockchain Transparency (100% Tamper-Proof & Auditable)",
        "advantages.item4Desc": "Every micro-disbursement down to 1/1,000th of a cent carries an independent cryptographic Merkle Proof anchored to Solana L1. Enterprises undergoing year-end audits can reconcile every single execution on-chain with 100% mathematical integrity — eliminating fraudulent expense claims from either employees or rogue AI."
    },
    "zh": {
        "agenticShift.badge": "全球浪潮 • AI AGENT 智能体时代 (2026+)",
        "agenticShift.title": "全球科技巨头达成共识：\"AI Agent 智能体必须拥有资金！\"",
        "agenticShift.subtitle": "从 OpenAI、Google、Stripe 到 Coinbase，巨头们都深刻认识到一个事实：\"2023 - 2024 年是对话式 AI（聊天机器人）时代。但从 2026 年起，正式进入自主行动的 AI 智能体时代。而一旦 AI 开始行动，它就必须拥有可自主支配的资金！\"",
        "agenticShift.card1Title": "全球支付巨头 Stripe（美国）",
        "agenticShift.card1Desc": "刚刚成立了专门的独立部门，重磅押注并研发 \"Agentic Commerce\"（AI 智能体自主商业）。",
        "agenticShift.card2Title": "加密资产交易巨头 Coinbase（美国）",
        "agenticShift.card2Desc": "CEO Brian Armstrong 明确呼吁：\"开发者们，请尽快为 AI 配备加密钱包，未来的商业形态属于机器与机器之间的自主结算。\"",
        "agenticShift.card3Title": "狂揽巨资的顶级初创企业",
        "agenticShift.card3Desc": "像 Skyfire Systems 和 Nevermined 这样的初创公司刚刚从顶级风投基金募集了数千万美元，只为解决一个核心痛点：AI 如何才能自主支付费用？",

        "advantages.badge": "核心壁垒 • 4 大生死攸关的技术差异",
        "advantages.title": "HAICHAIN 究竟拥有什么核心差异以实现全面超越？",
        "advantages.subtitle": "目前全球绝大多数同类项目仍停留在白皮书概念或传统老路。HAICHAIN 从底层构建了 4 项生死攸关的革命性差异：",
        "advantages.item1Title": "1. 亚美分级微支付（单笔低于 1 美分）且 0% 中介费",
        "advantages.item1Rival": "<strong>行业竞品：</strong> 试图强行套用信用卡或传统支付网关。但 Visa/Mastercard 每笔交易最低收取 <strong>$0.30 + 2.9%</strong> 的固定底费。如果您的 AI 调用一次推理仅需 <strong>$0.002</strong>，您绝不可能为一个价值 $0.002 的任务支付 $0.30 的手续费（中介费高达工作价值的 150 倍）！",
        "advantages.item1Hai": "<strong>HAICHAIN：</strong> 在 Solana 上深度构建专属状态通道微支付网络。允许 AI 极速结算 <strong>$0.001、$0.002</strong> 的微额账单，享受 <strong>0% 中介手续费</strong>，结算延迟仅 <strong>160 毫秒</strong>（比眨眼还要快）！",
        "advantages.item2Title": "2. 380 毫秒紧急熔断断路器（彻底防御 AI 提示词注入盗币）",
        "advantages.item2Rival": "<strong>同类竞品：</strong> 只顾着研究 \"如何让 AI 快速花钱\"，却完全忽略了底层资金安全：如果 AI 遭遇提示词注入攻击（Prompt Injection）被诱导转移资金，或者代码死循环刷爆钱包怎么办？",
        "advantages.item2Hai": "<strong>HAICHAIN：</strong> 始终将 \"人类最高主权控制\" 置于第一位：<br>&bull; <strong>速度上限（Velocity Cap）：</strong> 智能合约硬锁定资金消耗速率（如每分钟不超 $0.50）。<br>&bull; <strong>紧急熔断断路器（Emergency Kill-Switch）：</strong> 一旦检测到异常行为，只需一键或发送一条指令，智能合约将在 <strong>380 毫秒</strong> 内瞬间冻结并全额召回资金至安全钱包，任何人休想盗走一分钱。",
        "advantages.item3Title": "3. 极致极简的终端体验（原生支持 Anthropic Claude MCP 协议）",
        "advantages.item3Rival": "<strong>同类竞品：</strong> 门槛极高，要求用户必须是资深工程师，必须自己手写代码、配置专用服务器、管理复杂的 API 鉴权才能勉强跑通。",
        "advantages.item3Hai": "<strong>HAICHAIN：</strong> 率先深度集成 Anthropic（Claude 缔造者）官方的 MCP（Model Context Protocol）协议。<br>👉 <strong>毫无编程基础的普通用户，仅需复制一个链接粘贴到手机 Claude App，30 秒内立即可用！</strong>",
        "advantages.item4Title": "4. 区块链链上绝对透明（零造假可能，财务 100% 可审计）",
        "advantages.item4Desc": "每一笔哪怕仅千分之一美分的微额支出，都附带锚定在 Solana L1 上的独立密码学默克尔证明（Merkle Proof）。企业年终审计时，可直接打开链上账本逐笔核对，100% 真实透明，彻底杜绝员工或失控 AI 虚报发票与冒领费用的风险。"
    },
    "ko": {
        "agenticShift.badge": "글로벌 대전환 • AI 에이전트 시대 (2026+)",
        "agenticShift.title": "글로벌 테크 업계의 만장일치 결론: \"AI 에이전트는 반드시 돈을 가져야 한다!\"",
        "agenticShift.subtitle": "OpenAI, Google, Stripe부터 Coinbase에 이르기까지 모두가 하나의 진실을 깨달았습니다: \"2023-2024년은 대화하는 AI(챗봇)의 시대였습니다. 그러나 2026년부터는 스스로 행동하는 AI(에이전트)의 시대입니다. 그리고 AI가 행동하는 순간, 반드시 돈이 필요합니다!\"",
        "agenticShift.card1Title": "글로벌 결제 공룡 Stripe (미국)",
        "agenticShift.card1Desc": "\"Agentic Commerce(AI 전용 자율 상거래)\"를 연구하는 전담 부서를 공식 신설했습니다.",
        "agenticShift.card2Title": "가상자산 거래소 Coinbase (미국)",
        "agenticShift.card2Desc": "CEO Brian Armstrong 선언: \"개발자 여러분, AI에게 지갑을 발급하십시오. 미래는 기계가 서로 직접 결제하는 세상입니다.\"",
        "agenticShift.card3Title": "거액 투자를 유치한 스타트업들",
        "agenticShift.card3Desc": "Skyfire Systems나 Nevermined 같은 혁신 기업들이 AI가 스스로 결제하는 방법을 해결하기 위해 톱 티어 VC로부터 수천만 달러를 유치했습니다.",

        "advantages.badge": "핵심 우위 • 4대 결정적 차별점",
        "advantages.title": "그렇다면 HAICHAIN은 어떤 차별성으로 경쟁자를 압도하는가?",
        "advantages.subtitle": "현재 전 세계 대부분의 프로젝트는 백서 단계에 머물러 있거나 낡은 방식을 답습합니다. HAICHAIN은 생존을 결정짓는 4가지 혁신을 제공합니다:",
        "advantages.item1Title": "1. 1센트 미만 초미세 결제 (0% 수수료)",
        "advantages.item1Rival": "<strong>기존 경쟁사:</strong> 신용카드나 레거시 결제망을 억지로 연결하려 합니다. 그러나 Visa/Mastercard는 거래당 최소 <strong>$0.30 + 2.9%</strong>의 수수료를 부과합니다. AI가 문단 하나를 읽는 데 <strong>$0.002</strong>가 든다면, $0.002짜리 작업에 $0.30 수수료를 낼 수는 없습니다 (수수료가 작업 가치의 150배)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Solana 기반 자체 상태 채널(State Channel) 기술 설계. AI가 <strong>$0.001, $0.002</strong>를 <strong>0% 중개 수수료</strong> 및 눈 깜빡임보다 빠른 <strong>160ms 지연 시간</strong>으로 실시간 정산합니다!",
        "advantages.item2Title": "2. 380ms 긴급 서킷 브레이커 (AI 해킹 및 자금 탈취 방지)",
        "advantages.item2Rival": "<strong>경쟁사:</strong> 오직 \"AI가 돈을 얼마나 빨리 쓰게 할 것인가\"에만 몰두하며 보안을 망각합니다: 만약 AI가 악의적인 프롬프트 인젝션(Prompt Injection)에 속거나 무한 루프로 잔고를 탕진하면 어떻게 합니까?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> \"인간의 절대적 주권 통제\"를 1순위에 둡니다:<br>&bull; <strong>유속 한도 (Velocity Cap):</strong> 지출 속도를 스마트 계약으로 엄격히 제한합니다 (예: 분당 $0.50 이하).<br>&bull; <strong>긴급 킬스위치 (Kill-Switch):</strong> 이상 징후 발생 시 클릭 한 번으로 스마트 계약이 모든 자금을 동결하고 정확히 <strong>380ms</strong> 만에 안전 지갑으로 회수합니다.",
        "advantages.item3Title": "3. 엔드유저를 위한 초간편 연동 (Claude 공식 MCP 표준)",
        "advantages.item3Rival": "<strong>경쟁사:</strong> 사용자가 숙련된 개발자여야 하며, 직접 코드를 짜고 서버를 구축하며 복잡한 API 키를 설정하도록 강요합니다.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Anthropic(Claude 창립사)의 최신 MCP(Model Context Protocol) 표준을 전격 도입.<br>👉 <strong>코딩을 모르는 일반인도 링크 하나만 복사해 모바일 Claude 앱에 붙여넣으면 30초 만에 완료!</strong>",
        "advantages.item4Title": "4. 블록체인 기반 절대적 투명성 (위변조 불가 및 감사 용이)",
        "advantages.item4Desc": "1센트의 1/1,000에 불과한 지출이라도 Solana L1에 앵커링된 독립적인 머클 증명(Merkle Proof)을 보유합니다. 기업 연말 감사 시 온체인 원장을 통해 모든 거래를 100% 투명하게 대조할 수 있어 직원이나 AI의 허위 비용 청구가 원천 차단됩니다."
    },
    "fr": {
        "agenticShift.badge": "RÉVOLUTION GLOBALE • L'ÈRE DES AGENTS IA (2026+)",
        "agenticShift.title": "Le Monde de la Tech Réalise : « Les Agents IA Doivent Avoir de l'Argent ! »",
        "agenticShift.subtitle": "D'OpenAI, Google, Stripe à Coinbase, tous reconnaissent une vérité : « 2023 - 2024 était l'ère des chatbots. Mais à partir de 2026 s'ouvre l'ère des Agents IA autonomes. Et dès qu'une IA agit, elle DOIT avoir de l'argent ! »",
        "agenticShift.card1Title": "Le Géant des Paiements Stripe (USA)",
        "agenticShift.card1Desc": "Vient de créer une division dédiée à la recherche sur le « Commerce Agentique » (Commerce pour l'IA).",
        "agenticShift.card2Title": "Plateforme Crypto Coinbase (USA)",
        "agenticShift.card2Desc": "Le PDG Brian Armstrong déclare : « Développeurs, donnez des portefeuilles cryptos à vos IA — l'avenir appartient aux machines payant d'autres machines. »",
        "agenticShift.card3Title": "Startups aux Levées de Fonds Record",
        "agenticShift.card3Desc": "Des pionniers comme Skyfire Systems ou Nevermined ont levé des dizaines de millions de dollars auprès des plus grands fonds pour répondre à une question : comment permettre à l'IA de payer ?",

        "advantages.badge": "AVANTAGES CLÉS • 4 DIFFÉRENCIATEURS VITAUX",
        "advantages.title": "En Quoi HAICHAIN est-il Radicalement Supérieur ?",
        "advantages.subtitle": "La plupart des projets actuels ne sont que des concepts théoriques ou de vieilles recettes. HAICHAIN apporte 4 ruptures vitales :",
        "advantages.item1Title": "1. Micropaiements Inférieurs au Centime avec 0% de Frais",
        "advantages.item1Rival": "<strong>Concurrents mondiaux :</strong> Tentent d'imposer cartes de crédit et passerelles classiques. Mais Visa/Mastercard impose des frais minimaux de <strong>0,30 $ + 2,9 %</strong> par transaction. Si votre IA lit un texte pour <strong>0,002 $</strong>, vous ne pouvez pas payer 0,30 $ de frais pour 0,002 $ de travail (les frais sont 150 fois supérieurs à la tâche) !",
        "advantages.item1Hai": "<strong>HAICHAIN :</strong> Technologie propriétaire de canaux d'état (State Channel) sur Solana. Permet à l'IA de régler <strong>0,001 $, 0,002 $</strong> avec <strong>0 % de frais</strong> et une latence de <strong>160 ms</strong> (plus rapide qu'un battement de cils) !",
        "advantages.item2Title": "2. Disjoncteur de Sécurité 380ms (Protection Anti-Drainage)",
        "advantages.item2Rival": "<strong>Concurrents :</strong> Cherchent uniquement à faire dépenser l'argent à l'IA, oubliant la sécurité vitale : que faire si l'IA subit une injection de prompt malveillante ou une boucle infinie qui vide vos fonds ?",
        "advantages.item2Hai": "<strong>HAICHAIN :</strong> Place le « Contrôle Souverain Humain » au premier plan :<br>&bull; <strong>Plafond de Vélocité :</strong> Verrouille la vitesse de dépense (ex. max 0,50 $/min).<br>&bull; <strong>Disjoncteur d'Urgence :</strong> En cas d'anomalie, 1 clic ou 1 commande gèle les fonds et les rapatrie en exactement <strong>380 ms</strong>. Zéro risque de vol.",
        "advantages.item3Title": "3. Simplicité Ultime pour l'Utilisateur (Standard MCP de Claude)",
        "advantages.item3Rival": "<strong>Concurrents :</strong> Exigent d'être un développeur chevronné, forçant à coder, configurer des serveurs et gérer des API complexes.",
        "advantages.item3Hai": "<strong>HAICHAIN :</strong> Intègre nativement le standard universel MCP (Model Context Protocol) d'Anthropic (créateur de Claude).<br>👉 <strong>Un utilisateur sans compétences techniques colle simplement un lien dans l'application Claude en 30 secondes !</strong>",
        "advantages.item4Title": "4. Transparence Absolue sur la Blockchain (Inviolable et Auditable)",
        "advantages.item4Desc": "Chaque dépense, même d'un millième de centime, comporte une preuve cryptographique de Merkle ancrée sur Solana. Les entreprises peuvent auditer chaque transaction sur le grand livre décentralisé avec 100% de transparence, sans craindre la moindre fraude comptable."
    },
    "es": {
        "agenticShift.badge": "CAMBIO GLOBAL • LA ERA DE LOS AGENTES IA (2026+)",
        "agenticShift.title": "Todo el Mundo Tecnológico lo Comprende: \"¡Los Agentes de IA Deben Tener Dinero!\"",
        "agenticShift.subtitle": "Desde OpenAI, Google, Stripe hasta Coinbase, todos han reconocido una verdad: \"2023 - 2024 fue la era de la IA conversacional (Chatbots). Pero a partir de 2026 comienza la era de la IA que actúa por sí misma (Agentes de IA). ¡Y una vez que la IA actúa, OBLIGATORIAMENTE debe tener dinero!\"",
        "agenticShift.card1Title": "El Gigante de Pagos Stripe (EE. UU.)",
        "agenticShift.card1Desc": "Acaba de crear una división exclusiva para investigar el \"Comercio Agéntico\" (Comercio para la IA).",
        "agenticShift.card2Title": "Plataforma Cripto Coinbase (EE. UU.)",
        "agenticShift.card2Desc": "El CEO Brian Armstrong declaró: \"Desarrolladores, proporcionen billeteras a sus IA: el futuro es de máquinas realizando pagos entre sí.\"",
        "agenticShift.card3Title": "Startups con Rondas Gigantescas",
        "agenticShift.card3Desc": "Compañías como Skyfire Systems o Nevermined recaudaron decenas de millones de fondos líderes solo para resolver un enigma: ¿Cómo puede la IA pagar por sí misma?",

        "advantages.badge": "VENTAJAS CLAVE • 4 DIFERENCIADORES VITALES",
        "advantages.title": "¿Qué Hace a HAICHAIN Drásticamente Superior?",
        "advantages.subtitle": "La mayoría de los proyectos en el mundo siguen siendo ideas en papel o métodos obsoletos. HAICHAIN aporta 4 diferencias vitales:",
        "advantages.item1Title": "1. Micropagos de Menos de 1 Centavo con 0% de Comisiones",
        "advantages.item1Rival": "<strong>Competidores globales:</strong> Intentan usar tarjetas de crédito o pasarelas obsoletas. Pero Visa/Mastercard cobra un mínimo de <strong>$0.30 + 2.9%</strong> por transacción. Si tu IA lee un párrafo que cuesta <strong>$0.002</strong>, ¡no puedes pagar $0.30 de comisión por un trabajo de $0.002 (la tarifa es 150 veces el valor del trabajo)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Tecnología propia de Canales de Estado en Solana. Permite a la IA desembolsar pagos de <strong>$0.001, $0.002</strong> con <strong>0% de comisiones</strong> y una latencia de solo <strong>160 ms</strong> (¡más rápido que un parpadeo)!",
        "advantages.item2Title": "2. Disyuntor de Emergencia de 380ms (Protección Anti-Robo)",
        "advantages.item2Rival": "<strong>Competidores:</strong> Solo se preocupan por \"cómo hacer que la IA gaste rápido\", ignorando la seguridad: ¿Qué pasa si la IA sufre una inyección de prompts o un bucle infinito que vacía tu billetera?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Pone el \"Control Soberano Humano\" en el puesto #1:<br>&bull; <strong>Límite de Velocidad (Velocity Cap):</strong> Bloquea el ritmo de gasto (ej. máx. $0.50/min).<br>&bull; <strong>Disyuntor de Emergencia:</strong> Ante cualquier anomalía, 1 clic congela los fondos y los devuelve a tu billetera en solo <strong>380 ms</strong>.",
        "advantages.item3Title": "3. Máxima Simplicidad para el Usuario (Estándar MCP de Claude)",
        "advantages.item3Rival": "<strong>Competidores:</strong> Exigen que seas programador experto, obligándote a codificar, configurar servidores y gestionar API complejas.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Pionero en adoptar el estándar universal MCP de Anthropic (creadores de Claude).<br>👉 <strong>¡Cualquier usuario sin conocimientos técnicos solo copia un enlace en su app Claude y listo en 30 segundos!</strong>",
        "advantages.item4Title": "4. Transparencia Absoluta en Blockchain (Incorruptible y Auditable)",
        "advantages.item4Desc": "Cada desembolso, incluso de 1/1,000 de centavo, cuenta con una Prueba de Merkle criptográfica anclada en Solana. Las empresas pueden auditar cada transacción en la cadena con un 100% de transparencia, eliminando cualquier reporte inflado de gastos."
    },
    "ru": {
        "agenticShift.badge": "ГЛОБАЛЬНЫЙ СДВИГ • ЭРА AI-АГЕНТОВ (2026+)",
        "agenticShift.title": "Весь технологический мир осознал: \"AI-агенты обязаны иметь деньги!\"",
        "agenticShift.subtitle": "От OpenAI, Google, Stripe до Coinbase все признали очевидный факт: \"2023–2024 годы были эпохой чат-ботов. Но с 2026 года наступает эра действующих AI-агентов. А как только AI начинает действовать, ему ОБЯЗАТЕЛЬНО нужны деньги!\"",
        "agenticShift.card1Title": "Платежный гигант Stripe (США)",
        "agenticShift.card1Desc": "Недавно создал специальное подразделение для исследований \"Agentic Commerce\" (Коммерция для автономного AI).",
        "agenticShift.card2Title": "Криптобиржа Coinbase (США)",
        "agenticShift.card2Desc": "CEO Брайан Армстронг заявил: \"Разработчики, дайте своим AI-агентам кошельки — будущее за прямыми расчетами машин с машинами\".",
        "agenticShift.card3Title": "Стартапы с рекордными раундами",
        "agenticShift.card3Desc": "Такие компании, как Skyfire Systems и Nevermined, привлекли десятки миллионов долларов от ведущих фондов ради одной задачи: как научить AI платить самому?",

        "advantages.badge": "КЛЮЧЕВЫЕ ПРЕИМУЩЕСТВА • 4 ЖИЗНЕННО ВАЖНЫХ ОТЛИЧИЯ",
        "advantages.title": "В чем кардинальное превосходство HAICHAIN?",
        "advantages.subtitle": "Большинство мировых проектов сегодня — лишь концепции на бумаге или повторение старых путей. HAICHAIN создал 4 жизненно важных отличия:",
        "advantages.item1Title": "1. Микроплатежи меньше цента (< $0.01) с комиссией 0%",
        "advantages.item1Rival": "<strong>Мировые конкуренты:</strong> Пытаются использовать кредитные карты или старые платежные шлюзы. Но Visa/Mastercard берут минимум <strong>$0.30 + 2.9%</strong> за транзакцию. Если ваш AI читает текст стоимостью <strong>$0.002</strong>, вы не можете платить комиссию $0.30 за задачу в $0.002 (комиссия в 150 раз выше стоимости работы)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Собственные микроканалы расчетов (State Channel) на базе Solana. Позволяет AI оплачивать счета по <strong>$0.001, $0.002</strong> с <strong>0% комиссии</strong> и задержкой всего <strong>160 мс</strong> (быстрее моргания глаза)!",
        "advantages.item2Title": "2. Аварийный рубильник 380мс (Защита от взлома и утечки средств)",
        "advantages.item2Rival": "<strong>Конкуренты:</strong> Думают только о том, как научить AI быстрее тратить деньги, игнорируя безопасность: что будет, если AI попадет под Prompt Injection или зависнет в бесконечном цикле, списав весь баланс?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Ставит «Суверенный контроль человека» на 1-е место:<br>&bull; <strong>Лимит скорости (Velocity Cap):</strong> Жестко ограничивает траты (например, не более $0.50/мин).<br>&bull; <strong>Аварийный рубильник:</strong> При любой аномалии 1 клик или сообщение мгновенно замораживает средства и возвращает их вам ровно за <strong>380 мс</strong>.",
        "advantages.item3Title": "3. Предельная простота для пользователя (Стандарт MCP от Claude)",
        "advantages.item3Rival": "<strong>Конкуренты:</strong> Требуют навыков программирования, заставляя вручную писать код, настраивать серверы и сложные API-ключи.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Первым внедрил новейший стандарт MCP (Model Context Protocol) от компании Anthropic (создатели Claude).<br>👉 <strong>Обычный пользователь без навыков кода просто вставляет одну ссылку в приложение Claude за 30 секунд!</strong>",
        "advantages.item4Title": "4. Абсолютная прозрачность на блокчейне (100% защита от махинаций)",
        "advantages.item4Desc": "Каждый платеж вплоть до 1/1000 цента сопровождается независимым криптографическим доказательством Меркла в сети Solana. При аудите компании могут сверить каждую транзакцию в ончейн-реестре со 100% прозрачностью, исключая любые приписки расходов."
    },
    "hi": {
        "agenticShift.badge": "वैश्विक बदलाव • AI एजेंट युग (2026+)",
        "agenticShift.title": "पूरी तकनीकी दुनिया समझ चुकी है: \"AI एजेंटों के पास पैसा होना ही चाहिए!\"",
        "agenticShift.subtitle": "OpenAI, Google, Stripe से लेकर Coinbase तक सभी ने एक सच्चाई स्वीकार कर ली है: \"2023 - 2024 चैटबॉट्स का युग था। लेकिन 2026 से स्वायत्त AI एजेंटों का युग शुरू हो रहा है। और जब AI काम करेगा, तो उसके पास पैसा होना अनिवार्य है!\"",
        "agenticShift.card1Title": "भुगतान दिग्गज Stripe (USA)",
        "agenticShift.card1Desc": "\"Agentic Commerce\" (स्वायत्त AI के लिए वाणिज्य) पर शोध के लिए एक विशेष विभाग की स्थापना की।",
        "agenticShift.card2Title": "क्रिप्टो एक्सचेंज Coinbase (USA)",
        "agenticShift.card2Desc": "सीईओ ब्रायन आर्मस्ट्रांग ने कहा: \"डेवलपर्स, AI को वॉलेट दें — भविष्य मशीनों के आपस में लेन-देन का है।\"",
        "agenticShift.card3Title": "भारी फंडिंग प्राप्त AI स्टार्टअप्स",
        "agenticShift.card3Desc": "Skyfire Systems और Nevermined जैसी कंपनियों ने केवल इस समस्या के समाधान के लिए शीर्ष फंडों से करोड़ों डॉलर जुटाए: AI खुद भुगतान कैसे करे?",

        "advantages.badge": "मुख्य लाभ • 4 महत्वपूर्ण निर्णायक अंतर",
        "advantages.title": "HAICHAIN को सबसे अलग और श्रेष्ठ क्या बनाता है?",
        "advantages.subtitle": "आज दुनिया की अधिकांश परियोजनाएं केवल कागजी विचार हैं या पुराने ढर्रे पर चल रही हैं। HAICHAIN 4 अत्यंत महत्वपूर्ण नवाचार प्रदान करता है:",
        "advantages.item1Title": "1. 1 सेंट से भी कम सूक्ष्म-भुगतान (0% शुल्क)",
        "advantages.item1Rival": "<strong>वैश्विक प्रतिस्पर्धी:</strong> क्रेडिट कार्ड या पुराने गेटवे का उपयोग करने की कोशिश करते हैं। लेकिन Visa/Mastercard का न्यूनतम शुल्क <strong>$0.30 + 2.9%</strong> प्रति लेनदेन है। यदि आपका AI <strong>$0.002</strong> का काम करता है, तो आप उस पर $0.30 शुल्क नहीं दे सकते (शुल्क काम के मूल्य से 150 गुना अधिक है)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Solana पर मालिकाना स्टेट चैनल तकनीक। AI को <strong>$0.001, $0.002</strong> के भुगतान <strong>0% शुल्क</strong> और केवल <strong>160ms विलंबता</strong> (पलक झपकने से भी तेज) के साथ करने में सक्षम बनाता है!",
        "advantages.item2Title": "2. 380ms आपातकालीन सर्किट ब्रेकर (AI हैक सुरक्षा)",
        "advantages.item2Rival": "<strong>प्रतिस्पर्धी:</strong> केवल \"AI से तेजी से पैसे कैसे खर्च करवाएं\" पर ध्यान देते हैं, सुरक्षा को भूल जाते हैं: क्या होगा यदि AI किसी प्रॉम्प्ट इंजेक्शन हमले का शिकार हो जाए या आपके पूरे पैसे खाली कर दे?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> \"मानव संप्रभु नियंत्रण\" को #1 पर रखता है:<br>&bull; <strong>वेलोसिटी कैप:</strong> खर्च की गति को लॉक करता है (उदा. अधिकतम $0.50/मिनट)।<br>&bull; <strong>आपातकालीन किल-स्विच:</strong> किसी भी असामान्यता पर, 1 क्लिक <strong>380ms</strong> में सभी फंड को फ्रीज कर वापस आपके सुरक्षित वॉलेट में भेज देता है।",
        "advantages.item3Title": "3. अंतिम उपयोगकर्ताओं के लिए बेहद आसान (Claude का MCP मानक)",
        "advantages.item3Rival": "<strong>प्रतिस्पर्धी:</strong> उपयोगकर्ताओं को कुशल प्रोग्रामर होने के लिए मजबूर करते हैं, जिन्हें कोड लिखना और जटिल API सेट करना पड़ता है।",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Anthropic (Claude के निर्माता) के नवीनतम MCP प्रोटोकॉल का समर्थन करता है।<br>👉 <strong>सामान्य उपयोगकर्ता बिना कोडिंग के सिर्फ 1 लिंक कॉपी करके मोबाइल Claude ऐप में 30 सेकंड में शुरू कर सकते हैं!</strong>",
        "advantages.item4Title": "4. ब्लॉकचेन पर पूर्ण पारदर्शिता (धोखाधड़ी असंभव)",
        "advantages.item4Desc": "1 सेंट के 1/1,000वें हिस्से तक का प्रत्येक खर्च Solana L1 से जुड़े स्वतंत्र मर्कल प्रूफ के साथ होता है। वर्ष के अंत में ऑडिट के दौरान कंपनियां 100% पारदर्शिता के साथ हर लेन-देन का मिलान कर सकती हैं।"
    },
    "he": {
        "agenticShift.badge": "מהפכה גלובלית • עידן סוכני ה-AI (2026+)",
        "agenticShift.title": "כל עולם הטכנולוגיה מבין: \"סוכני AI חייבים כסף!\"",
        "agenticShift.subtitle": "מ-OpenAI, גוגל, סטרייפ ועד קוינבייס, כולם מבינים עובדה אחת: \"2023 - 2024 היו עידן הצ'אטבוטים. אך משנת 2026 והלאה מתחיל עידן סוכני ה-AI האוטונומיים. וברגע ש-AI פועל, הוא חייב שיהיה לו כסף!\"",
        "agenticShift.card1Title": "ענקית התשלומים Stripe (ארה\"ב)",
        "agenticShift.card1Desc": "הקימה חטיבה ייעודית החוקרת את \"Agentic Commerce\" (מסחר אוטונומי עבור בינה מלאכותית).",
        "agenticShift.card2Title": "בורסת הקריפטו Coinbase (ארה\"ב)",
        "agenticShift.card2Desc": "המנכ\"ל בריאן ארמסטרונג הכריז: \"מפתחים, תנו ארנקים ל-AI שלכם — העתיד הוא מכונות שמשלמות ישירות למכונות.\"",
        "agenticShift.card3Title": "סטארט-אפים עם גיוסי ענק",
        "agenticShift.card3Desc": "חברות כמו Skyfire Systems או Nevermined גייסו עשרות מיליוני דולרים מקרנות מובילות רק כדי לפתור בעיה אחת: כיצד ה-AI ישלם בעצמו?",

        "advantages.badge": "יתרון מרכזי • 4 הבדלים קריטיים",
        "advantages.title": "במה HAICHAIN שונה לחלוטין ונעלה על כולם?",
        "advantages.subtitle": "רוב הפרויקטים בעולם כיום הם רק רעיונות על הנייר או מיחזור של פתרונות ישנים. HAICHAIN מציגה 4 יתרונות קריטיים:",
        "advantages.item1Title": "1. מיקרו-תשלומים מתחת לסנט עם 0% עמלות",
        "advantages.item1Rival": "<strong>מתחרים גלובליים:</strong> מנסים להשתמש בכרטיסי אשראי רגילים. אך ויזה ומאסטרקארד גובות עמלת מינימום של <strong>$0.30 + 2.9%</strong> לכל עסקה. אם ה-AI שלכם קורא פסקה בעלות של <strong>$0.002</strong>, אינכם יכולים לשלם עמלה של $0.30 עבור פעולה ששווה $0.002 (העמלה יקרה פי 150 משווי העבודה)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> טכנולוגיית ערוצי מצב (State Channel) ייעודית על גבי Solana. מאפשרת ל-AI לבצע תשלומים של <strong>$0.001, $0.002</strong> עם <strong>0% עמלות תיווך</strong> וזמן תגובה של <strong>160 מילי-שניות</strong> בלבד!",
        "advantages.item2Title": "2. מפסק ביטחון של 380 מילי-שניות (הגנה מפני גניבת כספים)",
        "advantages.item2Rival": "<strong>מתחרים:</strong> מתמקדים רק ב\"איך לתת ל-AI להוציא כסף מהר\", ומתעלמים מהבטיחות: מה אם ה-AI יפול קורבן למתקפת Prompt Injection או לולאה אינסופית שתרוקן את הארנק?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> שמה את \"השליטה האנושית הבלעדית\" במקום הראשון:<br>&bull; <strong>מגבלת מהירות (Velocity Cap):</strong> מגבילה הרמטית את קצב ההוצאה (למשל עד $0.50 לדקה).<br>&bull; <strong>מפסק חירום:</strong> בלחיצת כפתור אחת החוזה החכם מקפיא את הכספים ומחזיר אותם אליכם תוך <strong>380 מילי-שניות</strong> בלבד.",
        "advantages.item3Title": "3. פשטות מוחלטת למשתמש הקצה (תקן ה-MCP של Claude)",
        "advantages.item3Rival": "<strong>מתחרים:</strong> דורשים מהמשתמש להיות מתכנת מיומן, לכתוב קוד בעצמו, להגדיר שרתים ולנהל מפתחות API מורכבים.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> מובילה באימוץ תקן ה-MCP (Model Context Protocol) הרשמי של Anthropic (יוצרת Claude).<br>👉 <strong>משתמשים רגילים ללא ידע בקוד פשוט מעתיקים קישור אחד לאפליקציית Claude בנייד ומוכנים תוך 30 שניות!</strong>",
        "advantages.item4Title": "4. שקיפות מוחלטת בבלוקצ'יין (ללא אפשרות להונאות)",
        "advantages.item4Desc": "כל הוצאה של אפילו אלפית הסנט מגובה בהוכחת מרקל קריפטוגרפית עצמאית ב-Solana. חברות יכולות לבצע ביקורת סוף שנה מול ספר החשבונות המבוזר בשקיפות של 100%, ללא חשש מחיובים כוזבים."
    },
    "kk": {
        "agenticShift.badge": "ЖАҺАНДЫҚ БҰРЫЛЫС • AI АГЕНТТЕР ДӘУІРІ (2026+)",
        "agenticShift.title": "Бүкіл технология әлемі түсінді: \"AI агенттеріне міндетті түрде ақша керек!\"",
        "agenticShift.subtitle": "OpenAI, Google, Stripe-тан Coinbase-ке дейін барлығы бір шындықты мойындады: \"2023 - 2024 жылдар сөйлесетін AI (чат-боттар) дәуірі болды. Ал 2026 жылдан бастап дербес әрекет ететін AI (AI агенттер) дәуірі басталды. AI әрекет еткен кезде оған МІНДЕТТІ ТҮРДЕ ақша қажет!\"",
        "agenticShift.card1Title": "Төлем алыбы Stripe (АҚШ)",
        "agenticShift.card1Desc": "\"Agentic Commerce\" (AI үшін дербес сауда) бағытын зерттейтін арнайы бөлім ашты.",
        "agenticShift.card2Title": "Coinbase криптобиржасы (АҚШ)",
        "agenticShift.card2Desc": "Бас директор Брайан Армстронг: \"Әзірлеушілер, AI-ға крипто әмиян беріңіздер — болашақ машиналардың өзара дербес есеп айырысуында.\"",
        "agenticShift.card3Title": "Ірі инвестиция тартқан стартаптар",
        "agenticShift.card3Desc": "Skyfire Systems және Nevermined сияқты компаниялар ірі қорлардан тек бір мәселені шешу үшін миллиондаған доллар тартты: AI қалай өздігінен төлей алады?",

        "advantages.badge": "НЕГІЗГІ АРТЫҚШЫЛЫҚ • 4 МАҢЫЗДЫ АЙЫРМАШЫЛЫҚ",
        "advantages.title": "HAICHAIN-нің озық болуының басты айырмашылығы неде?",
        "advantages.subtitle": "Бүгінде әлемдегі көптеген жобалар әлі де тек қағаз жүзінде немесе ескі жолмен келеді. HAICHAIN 4 өмірлік маңызы бар айырмашылықты ұсынады:",
        "advantages.item1Title": "1. 1 центтен төмен микро-төлемдер (0% комиссия)",
        "advantages.item1Rival": "<strong>Бәсекелестер:</strong> Несие карталарын немесе ескі төлем шлюздерін пайдалануға тырысады. Бірақ Visa/Mastercard әр транзакция үшін кемінде <strong>$0.30 + 2.9%</strong> алады. Егер сіздің AI құны <strong>$0.002</strong> болатын мәтінді оқыса, сіз $0.002 тұратын жұмыс үшін $0.30 комиссия төлей алмайсыз (комиссия жұмыс құнынан 150 есе қымбат)!",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Solana базасындағы арнайы микро-төлем арналары (State Channel). AI-ға <strong>$0.001, $0.002</strong> төлемдерін <strong>0% комиссиямен</strong> және небәрі <strong>160 миллисекундтық</strong> кідіріспен жүргізуге мүмкіндік береді!",
        "advantages.item2Title": "2. 380мс қауіпсіздік ажыратқышы (AI бұзылуынан қорғау)",
        "advantages.item2Rival": "<strong>Бәсекелестер:</strong> Тек \"AI қалай тезірек ақша жұмсайды\" деп ойлайды, қауіпсіздікті ұмытады: егер AI шабуылға (Prompt Injection) ұшыраса немесе қателікпен барлық ақшаны тауысса не болады?",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> \"Адамның егеменді бақылауын\" 1-орынға қояды:<br>&bull; <strong>Жылдамдық шегі (Velocity Cap):</strong> Жұмсау жылдамдығын бұғаттайды (мысалы, минутына $0.50-ден аспайды).<br>&bull; <strong>Шұғыл ажыратқыш:</strong> Аномалия байқалса, 1 батырма арқылы қаражатты <strong>380 мс</strong> ішінде толық қайтарады.",
        "advantages.item3Title": "3. Қолданушыға арналған қарапайымдылық (Claude-тың MCP стандарты)",
        "advantages.item3Rival": "<strong>Бәсекелестер:</strong> Қолданушыдан тәжірибелі бағдарламашы болуды, код жазуды, серверлерді баптауды талап етеді.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Anthropic (Claude құрушысы) компаниясының ресми MCP хаттамасын қолдайды.<br>👉 <strong>Бағдарламалауды білмейтін қарапайым қолданушы бар болғаны 1 сілтемені көшіріп, Claude қолданбасына 30 секундта қоса алады!</strong>",
        "advantages.item4Title": "4. Блокчейндегі абсолютті ашықтық (ешкім алдай алмайды)",
        "advantages.item4Desc": "Тіпті 1 центтің 1/1000 бөлігіне дейінгі әрбір шығын Solana желісіндегі тәуелсіз криптографиялық Merkle дәлелдемесімен бекітіледі. Кәсіпорындар әрбір транзакцияны 100% ашықтықпен тексере алады."
    }
}

HTML_SECTIONS = """
  <!-- ======================== SECTION: THE GLOBAL AGENTIC SHIFT ======================== -->
  <section id="agentic-shift" class="py-16 sm:py-20 border-b border-brand-lightBorder dark:border-brand-border bg-white dark:bg-black relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-4xl mx-auto mb-12">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
          <span data-i18n="agenticShift.badge">LÀN SÓNG TOÀN CẦU • KỶ NGUYÊN AI AGENT (2026+)</span>
        </div>
        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold tracking-tight text-black dark:text-white leading-tight" data-i18n="agenticShift.title">
          Cả thế giới công nghệ đều nhận ra: "AI Agent bắt buộc phải có tiền!"
        </h2>
        <div class="mt-5 p-5 sm:p-6 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-sm sm:text-base text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans shadow-xs">
          <p data-i18n="agenticShift.subtitle">
            Cả thế giới công nghệ (từ OpenAI, Google, Stripe cho đến Coinbase) đều đã nhận ra một sự thật: &ldquo;Năm 2023 - 2024 là kỷ nguyên AI biết trò chuyện (Chatbot). Nhưng từ năm 2026 trở đi là kỷ nguyên AI biết tự hành động (AI Agent). Và một khi AI hành động, nó BẮT BUỘC phải có tiền!&rdquo;
          </p>
        </div>
      </div>

      <!-- 3 Global Proof Pillars Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Stripe -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all flex flex-col justify-between">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center text-black dark:text-white">
              <i data-lucide="credit-card" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="agenticShift.card1Title">
              Gã khổng lồ thanh toán Stripe (Mỹ)
            </h3>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card1Desc">
              Vừa thành lập một bộ phận riêng nghiên cứu "Agentic Commerce" (Thương mại cho AI).
            </p>
          </div>
          <div class="pt-4 mt-4 border-t border-neutral-200/60 dark:border-neutral-800/60 flex items-center justify-between text-[11px] font-mono text-neutral-500">
            <span>Agentic Commerce</span>
            <span class="font-bold text-black dark:text-white">Silicon Valley, USA</span>
          </div>
        </div>

        <!-- Coinbase -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all flex flex-col justify-between">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center text-black dark:text-white">
              <i data-lucide="wallet" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="agenticShift.card2Title">
              Sàn tiền mã hóa Coinbase (Mỹ)
            </h3>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card2Desc">
              CEO Brian Armstrong vừa tuyên bố: "Các nhà phát triển hãy cấp ví tiền cho AI đi, tương lai là máy móc tự thanh toán với nhau".
            </p>
          </div>
          <div class="pt-4 mt-4 border-t border-neutral-200/60 dark:border-neutral-800/60 flex items-center justify-between text-[11px] font-mono text-neutral-500">
            <span>AI Crypto Wallets</span>
            <span class="font-bold text-black dark:text-white">Nasdaq: COIN</span>
          </div>
        </div>

        <!-- Mega Startups -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all flex flex-col justify-between">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center text-black dark:text-white">
              <i data-lucide="trending-up" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="agenticShift.card3Title">
              Các Startup gọi vốn khủng
            </h3>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card3Desc">
              Các công ty như Skyfire Systems hay Nevermined vừa huy động hàng chục triệu USD từ các quỹ lớn chỉ để giải quyết bài toán: Làm sao để AI có thể tự quẹt tiền?
            </p>
          </div>
          <div class="pt-4 mt-4 border-t border-neutral-200/60 dark:border-neutral-800/60 flex items-center justify-between text-[11px] font-mono text-neutral-500">
            <span>Tier-1 VC Funding</span>
            <span class="font-bold text-black dark:text-white">$10M+ Raised</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================== SECTION: 4 VITAL DIFFERENTIATORS ======================== -->
  <section id="haichain-advantages" class="py-16 sm:py-20 border-b border-brand-lightBorder dark:border-brand-border bg-neutral-50/70 dark:bg-neutral-950/70 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full border border-neutral-300 dark:border-neutral-800 bg-white dark:bg-neutral-900 text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
          <span data-i18n="advantages.badge">LỢI THẾ CỐT LÕI • 4 ĐỘT PHÁ SỐNG CÒN</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-black dark:text-white" data-i18n="advantages.title">
          Vậy HAICHAIN có gì KHÁC BIỆT để vượt trội?
        </h2>
        <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 mt-4 leading-relaxed font-light" data-i18n="advantages.subtitle">
          Hầu hết các dự án trên thế giới hiện nay chỉ mới là ý tưởng trên giấy hoặc làm theo lối mòn cũ. HAICHAIN tạo ra 4 sự khác biệt mang tính sống còn:
        </p>
      </div>

      <!-- 4 Pillars Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Pillar 1: Sub-Cent 0% Fee -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-11 h-11 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center text-black dark:text-white shrink-0">
              <i data-lucide="zap" class="w-5 h-5"></i>
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item1Title">
              1. Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí
            </h3>
          </div>
          <div class="p-4 rounded-2xl bg-rose-500/5 border border-rose-500/20 text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans" data-i18n="advantages.item1Rival">
            <strong>Các đối thủ trên thế giới:</strong> Họ cố dùng thẻ tín dụng hoặc cổng thanh toán truyền thống. Nhưng thẻ Visa/Mastercard có phí tối thiểu là <strong>$0.30 + 2.9%</strong> cho mỗi giao dịch. Nếu con AI của bạn chỉ đọc 1 đoạn văn tốn <strong>$0.002</strong>, bạn không thể trả $0.30 tiền phí cho một việc giá $0.002 được (phí đắt gấp 150 lần giá trị công việc)!
          </div>
          <div class="p-4 rounded-2xl bg-emerald-500/5 border border-emerald-500/20 text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans" data-i18n="advantages.item1Hai">
            <strong>HAICHAIN:</strong> Thiết kế riêng công nghệ Kênh thanh toán vi mô (State Channel) trên nền tảng Solana. Cho phép AI chi trả các khoản <strong>$0.001, $0.002</strong> với <strong>0% phí trung gian</strong> và độ trễ chỉ <strong>160 mili-giây</strong> (nhanh hơn cái chớp mắt)!
          </div>
        </div>

        <!-- Pillar 2: Emergency Circuit Breaker 380ms -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-11 h-11 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center text-black dark:text-white shrink-0">
              <i data-lucide="shield-alert" class="w-5 h-5"></i>
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item2Title">
              2. Cầu dao an toàn 380ms (Chống mất tiền do AI bị hack)
            </h3>
          </div>
          <div class="p-4 rounded-2xl bg-rose-500/5 border border-rose-500/20 text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans" data-i18n="advantages.item2Rival">
            <strong>Các đối thủ:</strong> Họ chỉ mải mê nghĩ cách "Làm sao cho AI tiêu tiền thật nhanh", mà quên mất bài toán an toàn: Lỡ con AI bị kẻ xấu lừa (Prompt Injection) hoặc bị lỗi lặp tiêu sạch tiền thì sao?
          </div>
          <div class="p-4 rounded-2xl bg-emerald-500/5 border border-emerald-500/20 text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans" data-i18n="advantages.item2Hai">
            <strong>HAICHAIN:</strong> Đặt "Quyền kiểm soát của con người" lên số 1:<br>&bull; <strong>Hạn mức vận tốc (Velocity Cap):</strong> Khóa cứng tốc độ tiêu tiền (ví dụ không quá $0.50/phút).<br>&bull; <strong>Cầu dao ngắt khẩn cấp (Emergency Kill-Switch):</strong> Nếu thấy AI có dấu hiệu bất thường, bạn chỉ cần bấm 1 nút hoặc nhắn 1 tin, Hợp đồng thông minh sẽ đóng băng toàn bộ quỹ và rút tiền về túi bạn trong đúng <strong>380 mili-giây</strong>, không một ai có thể lấy cắp tiền của bạn.
          </div>
        </div>

        <!-- Pillar 3: Ultra-Simple MCP Standard -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-11 h-11 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center text-black dark:text-white shrink-0">
              <i data-lucide="smartphone" class="w-5 h-5"></i>
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item3Title">
              3. Cực kỳ đơn giản cho người dùng cuối (Chuẩn MCP của Claude)
            </h3>
          </div>
          <div class="p-4 rounded-2xl bg-rose-500/5 border border-rose-500/20 text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans" data-i18n="advantages.item3Rival">
            <strong>Các đối thủ:</strong> Bắt người dùng phải là lập trình viên giỏi, phải tự viết mã code, cấu hình máy chủ, tạo API phức tạp thì mới dùng được.
          </div>
          <div class="p-4 rounded-2xl bg-emerald-500/5 border border-emerald-500/20 text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans" data-i18n="advantages.item3Hai">
            <strong>HAICHAIN:</strong> Tiên phong đón đầu chuẩn giao thức MCP (Model Context Protocol) mới nhất của công ty Anthropic (nhà sáng lập Claude).<br>👉 <strong>Người dùng bình thường không biết code chỉ cần copy 1 đường link dán vào app Claude trên điện thoại là xong trong 30 giây!</strong>
          </div>
        </div>

        <!-- Pillar 4: Blockchain Transparency & Merkle Proof -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-11 h-11 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center text-black dark:text-white shrink-0">
              <i data-lucide="file-check-2" class="w-5 h-5"></i>
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item4Title">
              4. Minh bạch tuyệt đối trên Blockchain (Không ai gian lận được)
            </h3>
          </div>
          <div class="p-5 rounded-2xl bg-neutral-100/60 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-xs sm:text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans" data-i18n="advantages.item4Desc">
            Mọi khoản chi dù chỉ 1 phần nghìn cent đều có chứng thực mật mã độc lập (Merkle Proof) gắn liền với mạng lưới Solana. Doanh nghiệp khi kiểm toán cuối năm có thể mở sổ cái ra đối chiếu từng giao dịch một, minh bạch 100%, không bao giờ lo nhân viên hay AI gian lận báo khống chi phí.
          </div>
          <div class="p-4 rounded-2xl bg-neutral-50 dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 flex items-center justify-between text-xs font-mono text-neutral-500">
            <span class="flex items-center space-x-2">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span>Solana Cryptographic Anchor</span>
            </span>
            <span class="font-bold text-black dark:text-white">Merkle Root Verified</span>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

def update_html(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    target = '  <!-- ======================== SECTION: MARKET PROOF & DATA ======================== -->'
    if target in content and 'id="agentic-shift"' not in content:
        content = content.replace(target, HTML_SECTIONS + "\n\n" + target, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Successfully injected 2 sections into {path}')
    elif 'id="agentic-shift"' in content:
        print(f'Sections already exist in {path}')
    else:
        print(f'Target not found in {path}')

def update_i18n_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject keys for each language
    for lang, kvs in ALL_TRANSLATIONS.items():
        search_str = f'"{lang}": {{\n'
        if search_str not in content:
            search_str = f"'{lang}': {{\n"
        if search_str in content:
            inject_str = ""
            for k, v in kvs.items():
                v_escaped = json.dumps(v, ensure_ascii=False)
                inject_str += f'    "{k}": {v_escaped},\n'
            if inject_str:
                content = content.replace(search_str, search_str + inject_str, 1)
                print(f'Injected keys for {lang} in {path}')
        else:
            print(f'Language block {lang} not found in {path}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Finished updating {path}')

# Execute updates
update_html('index.html')
update_html('app/index.html')

update_i18n_file('i18n.js')
update_i18n_file('app/i18n.js')

print('All landing sections and 10-language translations successfully processed.')
