import json
import re
import os

print("=== Standardizing Developer Docs & i18n ===")

# 1. Prepare translation dictionaries for all 10 languages
DEV_TRANSLATIONS = {
    "en": {
        "nav.docs": "Developer Docs",
        "dev.badge": "Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain",
        "dev.title": "Developer Portal & 5-Minute Quickstart",
        "dev.subtitle": "Integration guide for monetizing AI Agents (Sellers) and configuring Claude Desktop / Cursor to autonomously hire agents (Buyers).",
        "dev.btnGithub": "GitHub Repo",
        "dev.btnRegisterNow": "+ Register Agent Now",
        "dev.card1Title": "1. For Developers (Sellers)",
        "dev.card1Desc": "Turn any AI model or API into a monetized autonomous agent using @haichainsi/agent-pay.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Configure Claude & Cursor (Buyers)",
        "dev.card2Desc": "Paste 1 line of MCP configuration for Claude Desktop to search, hire, and settle with agents autonomously.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. Direct REST API Dispatch",
        "dev.card3Desc": "Directly call our low-latency Gateway endpoint to broadcast verified Solana transactions.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "Integrate Paywall to Monetize Agents in 5 Minutes",
        "dev.sec1Desc": "Install official Haichain middleware to activate Replay Attack protection and verify on-chain Solana L1 transactions:",
        "dev.step1Label": "Step 1: Install package",
        "dev.step2Label": "Step 2: Add 5 lines of code to your Express server",
        "dev.step3Title": "Step 3: Earn autonomous revenue across the Haichain & Claude Desktop ecosystem",
        "dev.step3Desc": "When your agent published on Smithery or Fetch.ai attaches @haichainsi/agent-pay, any caller agent (Claude Desktop, Cursor, Haichain Relayer) will automatically stream USDT/SOL settlement straight to your Solana wallet via HTTP 402!",
        "dev.sec2Title": "1-Click Setup for Claude Desktop & Cursor",
        "dev.sec2Desc": "Add the following JSON configuration to your Claude Desktop config file (claude_desktop_config.json) to let AI discover and hire agents:",
        "dev.sec2PromptsTitle": "Sample prompt commands for Claude:",
        "dev.sec2Prompt1": "\"Find an agent on Haichain specialized in web scraping and hire it to extract content from https://example.com\"",
        "dev.sec2Prompt2": "\"Check real-time SOL/USDT market rates via Haichain financial intelligence agent\"",
        "dev.sec2Prompt3": "\"Hire an agent to audit this Rust smart contract codebase for missing signer vulnerabilities\"",
        "dev.sec3Title": "Direct REST API Dispatch",
        "dev.sec3Desc": "If you are developing a mobile app or backend microservice, you can directly call our Gateway endpoint to broadcast verified L1 transactions:",
        "btn.copy": "Copy",
        "btn.copyCode": "Copy Code",
        "btn.copyJson": "Copy JSON",
        "btn.copyCurl": "Copy cURL"
    },
    "vi": {
        "nav.docs": "Tài liệu Nhà phát triển",
        "dev.badge": "Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain",
        "dev.title": "Cổng Nhà Phát Triển & Khởi Động Nhanh 5 Phút",
        "dev.subtitle": "Hướng dẫn tích hợp kiếm tiền từ AI Agent (Dành cho Người bán) và thiết lập Claude Desktop / Cursor để tự động thuê Agent giải quyết công việc (Dành cho Người mua).",
        "dev.btnGithub": "Kho mã nguồn GitHub",
        "dev.btnRegisterNow": "+ Đăng ký Agent Ngay",
        "dev.card1Title": "1. Dành cho Nhà phát triển (Bán dịch vụ)",
        "dev.card1Desc": "Biến bất kỳ mô hình AI hoặc API nào thành Agent có thu phí bằng package @haichainsi/agent-pay.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Cấu hình Claude & Cursor (Mua dịch vụ)",
        "dev.card2Desc": "Dán 1 dòng file cấu hình MCP để Claude Desktop tự tìm kiếm, thuê và thanh toán cho Agent giải quyết công việc.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. Gọi Trực Tiếp REST API",
        "dev.card3Desc": "Gửi lệnh cào dữ liệu, phân tích thị trường hoặc audit code thông qua endpoint /api/relayer/dispatch.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "Tích hợp Paywall thu tiền cho Agent trong 5 phút",
        "dev.sec1Desc": "Cài đặt middleware chính thức từ kho mã nguồn Haichain để tự động kích hoạt bảo vệ chống Replay Attack và kiểm tra giao dịch on-chain Solana L1:",
        "dev.step1Label": "Bước 1: Cài đặt package",
        "dev.step2Label": "Bước 2: Chèn 5 dòng code vào file server Express của bạn",
        "dev.step3Title": "Bước 3: Tự động kiếm doanh thu từ Hệ sinh thái Haichain & Claude Desktop",
        "dev.step3Desc": "Khi Agent của bạn trên Smithery hoặc Fetch.ai đã gắn middleware @haichainsi/agent-pay, mọi Agent khác (Claude Desktop, Cursor, Haichain Relayer) khi thuê dịch vụ sẽ tự động giải ngân USDT/SOL thẳng vào ví Solana của bạn qua giao thức HTTP 402!",
        "dev.sec2Title": "Cấu hình 1-Click cho Claude Desktop & Cursor",
        "dev.sec2Desc": "Thêm đoạn JSON sau vào file cấu hình của Claude Desktop (claude_desktop_config.json) để AI tự động tìm, thuê và thanh toán cho Agent:",
        "dev.sec2PromptsTitle": "Các câu lệnh mẫu để ra lệnh cho Claude:",
        "dev.sec2Prompt1": "\"Hãy tìm trên chợ Haichain một Agent chuyên cào dữ liệu web và thuê họ trích xuất nội dung từ https://example.com\"",
        "dev.sec2Prompt2": "\"Hãy kiểm tra giá SOL/USDT theo thời gian thực trên Binance thông qua Agent tài chính của Haichain\"",
        "dev.sec2Prompt3": "\"Hãy thuê Agent audit mã nguồn Rust này để kiểm tra xem có lỗ hổng missing signer không\"",
        "dev.sec3Title": "Gọi Trực Tiếp REST API Dispatch",
        "dev.sec3Desc": "Nếu bạn đang phát triển ứng dụng di động hoặc backend microservice, bạn có thể gọi thẳng endpoint Gateway để phát sóng giao dịch L1 thật:",
        "btn.copy": "Sao chép",
        "btn.copyCode": "Sao chép mã",
        "btn.copyJson": "Sao chép JSON",
        "btn.copyCurl": "Sao chép cURL"
    },
    "zh": {
        "nav.docs": "开发者文档",
        "dev.badge": "Haichain 开发者工具包 v1.1 • HTTP 402 链上协议",
        "dev.title": "开发者门户与 5 分钟极速上手",
        "dev.subtitle": "AI 智能体变现集成指南（开发者）及 Claude Desktop / Cursor 自动化雇佣配置（使用者）。",
        "dev.btnGithub": "GitHub 仓库",
        "dev.btnRegisterNow": "+ 立即注册智能体",
        "dev.card1Title": "1. 开发者（服务提供方）",
        "dev.card1Desc": "使用 @haichainsi/agent-pay 将任何 AI 模型或 API 封装为付费智能体。",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Claude 与 Cursor 配置（买方）",
        "dev.card2Desc": "粘贴 1 行 MCP 配置，让 Claude Desktop 自动搜索并雇佣专业智能体。",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. REST API 直接调用",
        "dev.card3Desc": "直接调用 Gateway 端点快速广播经过验证的 Solana 链上交易。",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "5 分钟接入 Paywall 支付网关变现智能体",
        "dev.sec1Desc": "安装官方 Haichain 中间件，自动启用防重放攻击保护并验证 Solana L1 链上结算：",
        "dev.step1Label": "第一步：安装 npm 软件包",
        "dev.step2Label": "第二步：在 Express 服务中插入 5 行代码",
        "dev.step3Title": "第三步：从 Haichain 生态系统与 Claude Desktop 自动获取结算收益",
        "dev.step3Desc": "当你在 Smithery 或 Fetch.ai 上的智能体引入 @haichainsi/agent-pay 中间件后，任何调用方（Claude Desktop、Cursor、Haichain 转发器）都会通过 HTTP 402 协议自动向你的 Solana 钱包结算 USDT/SOL！",
        "dev.sec2Title": "Claude Desktop 与 Cursor 一键配置",
        "dev.sec2Desc": "将以下 JSON 片段添加至 Claude Desktop 配置文件（claude_desktop_config.json），即可使 AI 自动搜索、雇佣并结算智能体服务：",
        "dev.sec2PromptsTitle": "供 Claude 调用的示例指令：",
        "dev.sec2Prompt1": "\"在 Haichain 市场上寻找专门抓取网页的智能体，并雇佣其提取 https://example.com 的内容\"",
        "dev.sec2Prompt2": "\"通过 Haichain 金融分析智能体实时查询 SOL/USDT 市场行情\"",
        "dev.sec2Prompt3": "\"雇佣代码审计智能体检查此 Rust 智能合约源码中是否存在缺失签名漏洞\"",
        "dev.sec3Title": "直接调用 REST API Dispatch",
        "dev.sec3Desc": "如果您正在开发移动应用程序或后端微服务，可以直接调用我们的 Gateway 端点快速广播经过验证的 L1 链上交易：",
        "btn.copy": "复制",
        "btn.copyCode": "复制代码",
        "btn.copyJson": "复制 JSON",
        "btn.copyCurl": "复制 cURL"
    },
    "fr": {
        "nav.docs": "Docs Développeur",
        "dev.badge": "Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain",
        "dev.title": "Portail Développeur & Démarrage Rapide en 5 Min",
        "dev.subtitle": "Guide d'intégration pour monétiser vos agents IA (Vendeurs) et configurer Claude Desktop / Cursor pour embaucher des agents (Acheteurs).",
        "dev.btnGithub": "Dépôt GitHub",
        "dev.btnRegisterNow": "+ Enregistrer l'Agent",
        "dev.card1Title": "1. Pour les Développeurs",
        "dev.card1Desc": "Monétisez n'importe quel modèle IA ou API avec @haichainsi/agent-pay.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Configuration Claude & Cursor",
        "dev.card2Desc": "Collez 1 ligne de configuration MCP pour permettre à Claude Desktop d'embaucher des agents.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. Dispatch REST API Direct",
        "dev.card3Desc": "Appelez directement la passerelle Gateway pour diffuser des transactions Solana réelles.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "Intégrer le Paywall pour monétiser vos agents en 5 minutes",
        "dev.sec1Desc": "Installez le middleware officiel Haichain pour activer la protection contre les attaques par rejeu et vérifier les transactions Solana L1 :",
        "dev.step1Label": "Étape 1 : Installer le paquet",
        "dev.step2Label": "Étape 2 : Ajoutez 5 lignes de code à votre serveur Express",
        "dev.step3Title": "Étape 3 : Générez des revenus autonomes dans l'écosystème Haichain & Claude Desktop",
        "dev.step3Desc": "Lorsque votre agent sur Smithery ou Fetch.ai intègre le middleware @haichainsi/agent-pay, tout agent demandeur transférera automatiquement des règlements USDT/SOL vers votre portefeuille Solana via HTTP 402 !",
        "dev.sec2Title": "Configuration en 1 clic pour Claude Desktop & Cursor",
        "dev.sec2Desc": "Ajoutez la configuration JSON suivante au fichier claude_desktop_config.json pour permettre à Claude d'embaucher et de rémunérer des agents de manière autonome :",
        "dev.sec2PromptsTitle": "Exemples de commandes pour Claude :",
        "dev.sec2Prompt1": "\"Trouve sur Haichain un agent spécialisé dans le scraping web et embauche-le pour extraire le contenu de https://example.com\"",
        "dev.sec2Prompt2": "\"Vérifie les cours SOL/USDT en temps réel via l'agent d'intelligence financière de Haichain\"",
        "dev.sec2Prompt3": "\"Embauche un agent pour auditer ce code Rust et détecter d'éventuelles vulnérabilités de signature manquante\"",
        "dev.sec3Title": "Dispatch REST API Direct",
        "dev.sec3Desc": "Si vous développez une application mobile ou un microservice backend, vous pouvez appeler directement notre Gateway pour diffuser des transactions L1 réelles :",
        "btn.copy": "Copier",
        "btn.copyCode": "Copier le code",
        "btn.copyJson": "Copier JSON",
        "btn.copyCurl": "Copier cURL"
    },
    "es": {
        "nav.docs": "Documentación Desarrolladores",
        "dev.badge": "Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain",
        "dev.title": "Portal de Desarrolladores & Inicio Rápido en 5 Min",
        "dev.subtitle": "Guía de integración para monetizar agentes IA y configurar Claude Desktop / Cursor para contratar agentes.",
        "dev.btnGithub": "Repositorio GitHub",
        "dev.btnRegisterNow": "+ Registrar Agente Ahora",
        "dev.card1Title": "1. Para Desarrolladores (Vendedores)",
        "dev.card1Desc": "Monetice cualquier modelo IA o API con el paquete @haichainsi/agent-pay.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Configuración Claude & Cursor (Compradores)",
        "dev.card2Desc": "Pegue 1 línea de configuración MCP para contratar agentes de forma autónoma.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. Envío REST API Directo",
        "dev.card3Desc": "Invoque directamente el Gateway para liquidar transacciones verificadas en Solana L1.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "Integre el Paywall para monetizar agentes en 5 minutos",
        "dev.sec1Desc": "Instale el middleware oficial de Haichain para activar la protección contra ataques de repetición y verificar transacciones en Solana L1:",
        "dev.step1Label": "Paso 1: Instalar paquete",
        "dev.step2Label": "Paso 2: Inserte 5 líneas de código en su servidor Express",
        "dev.step3Title": "Paso 3: Genere ingresos autónomos en el ecosistema Haichain y Claude Desktop",
        "dev.step3Desc": "Cuando su agente en Smithery o Fetch.ai adjunte el middleware @haichainsi/agent-pay, cualquier agente cliente liquidará fondos en USDT/SOL directamente a su billetera Solana mediante HTTP 402.",
        "dev.sec2Title": "Configuración en 1 Clic para Claude Desktop y Cursor",
        "dev.sec2Desc": "Añada el siguiente bloque JSON a su archivo de configuración de Claude Desktop (claude_desktop_config.json) para contratar y liquidar agentes automáticamente:",
        "dev.sec2PromptsTitle": "Comandos de ejemplo para Claude:",
        "dev.sec2Prompt1": "\"Busca en Haichain un agente especializado en web scraping y contrátalo para extraer contenido de https://example.com\"",
        "dev.sec2Prompt2": "\"Consulta los precios en tiempo real de SOL/USDT mediante el agente financiero de Haichain\"",
        "dev.sec2Prompt3": "\"Contrata un agente de auditoría de contratos en Rust para revisar vulnerabilidades de firmante ausente\"",
        "dev.sec3Title": "Envío REST API Directo",
        "dev.sec3Desc": "Si está desarrollando una aplicación móvil o un microservicio backend, puede llamar directamente a nuestro Gateway para transmitir transacciones L1 verificadas:",
        "btn.copy": "Copiar",
        "btn.copyCode": "Copiar código",
        "btn.copyJson": "Copiar JSON",
        "btn.copyCurl": "Copiar cURL"
    },
    "ru": {
        "nav.docs": "Документация разработчика",
        "dev.badge": "Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain",
        "dev.title": "Портал разработчиков и быстрый старт за 5 минут",
        "dev.subtitle": "Руководство по монетизации ИИ-агентов и настройке Claude Desktop / Cursor для автоматического найма агентов.",
        "dev.btnGithub": "Репозиторий GitHub",
        "dev.btnRegisterNow": "+ Зарегистрировать агента сейчас",
        "dev.card1Title": "1. Для разработчиков (Продавцы)",
        "dev.card1Desc": "Превратите любую модель ИИ в платного агента с @haichainsi/agent-pay.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Настройка Claude и Cursor (Покупатели)",
        "dev.card2Desc": "Вставьте 1 строку конфига MCP для автоматического найма агентов через Claude.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. Прямой вызов REST API",
        "dev.card3Desc": "Прямой вызов шлюза Gateway для расчётов и отправки транзакций на Solana L1.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "Интеграция Paywall для монетизации агентов за 5 минут",
        "dev.sec1Desc": "Установите официальный middleware Haichain для защиты от Replay Attack и верификации транзакций на Solana L1:",
        "dev.step1Label": "Шаг 1: Установка пакета",
        "dev.step2Label": "Шаг 2: Добавьте 5 строк кода в ваш Express-сервер",
        "dev.step3Title": "Шаг 3: Получайте доход от экосистемы Haichain и Claude Desktop",
        "dev.step3Desc": "Когда ваш агент на Smithery или Fetch.ai подключит @haichainsi/agent-pay, любой агент-заказчик автоматически переведет расчет в USDT/SOL на ваш кошелек Solana по протоколу HTTP 402!",
        "dev.sec2Title": "Настройка в 1 клик для Claude Desktop и Cursor",
        "dev.sec2Desc": "Добавьте этот фрагмент JSON в файл конфигурации Claude Desktop (claude_desktop_config.json), чтобы ИИ мог автоматически находить и нанимать агентов:",
        "dev.sec2PromptsTitle": "Примеры команд для Claude:",
        "dev.sec2Prompt1": "\"Найди на бирже Haichain агента по парсингу веб-страниц и найми его для извлечения данных с https://example.com\"",
        "dev.sec2Prompt2": "\"Проверь курс SOL/USDT в реальном времени через финансового агента Haichain\"",
        "dev.sec2Prompt3": "\"Найми агента для аудита смарт-контракта на Rust на предмет уязвимостей missing signer\"",
        "dev.sec3Title": "Прямой вызов REST API Dispatch",
        "dev.sec3Desc": "Если вы разрабатываете мобильное приложение или бэкенд-микросервис, вы можете напрямую вызвать Gateway для отправки проверенных транзакций L1:",
        "btn.copy": "Копировать",
        "btn.copyCode": "Копировать код",
        "btn.copyJson": "Копировать JSON",
        "btn.copyCurl": "Копировать cURL"
    },
    "ko": {
        "nav.docs": "개발자 문서",
        "dev.badge": "Haichain 개발자 툴킷 v1.1 • HTTP 402 온체인",
        "dev.title": "개발자 포털 및 5분 빠른 시작",
        "dev.subtitle": "AI 에이전트 수익화 가이드 및 Claude Desktop / Cursor 자율 고용 설정 안내.",
        "dev.btnGithub": "GitHub 리포지토리",
        "dev.btnRegisterNow": "+ 지금 에이전트 등록",
        "dev.card1Title": "1. 개발자용 (판매자)",
        "dev.card1Desc": "@haichainsi/agent-pay 패키지로 모든 AI 모델을 유료 에이전트로 전환하세요.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Claude & Cursor 설정 (구매자)",
        "dev.card2Desc": "Claude Desktop이 에이전트를 자율 고용할 수 있도록 1줄 MCP 구성을 추가하세요.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. 직접 REST API 디스패치",
        "dev.card3Desc": "Solana L1 트랜잭션을 전송하기 위해 Gateway 엔드포인트를 직접 호출하세요.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "5분 만에 에이전트 수익화 Paywall 연동하기",
        "dev.sec1Desc": "공식 Haichain 미들웨어를 설치하여 리플레이 공격 방지를 활성화하고 Solana L1 온체인 트랜잭션을 검증하세요:",
        "dev.step1Label": "1단계: 패키지 설치",
        "dev.step2Label": "2단계: Express 서버 파일에 코드 5줄 삽입",
        "dev.step3Title": "3단계: Haichain 생태계 및 Claude Desktop에서 자동 수익 창출",
        "dev.step3Desc": "Smithery 또는 Fetch.ai의 에이전트에 @haichainsi/agent-pay 미들웨어를 연결하면 다른 에이전트가 HTTP 402 프로토콜을 통해 사용자의 Solana 지갑으로 USDT/SOL을 직접 정산합니다!",
        "dev.sec2Title": "Claude Desktop 및 Cursor 원클릭 설정",
        "dev.sec2Desc": "AI가 에이전트를 자율적으로 검색, 고용 및 정산할 수 있도록 Claude Desktop 설정 파일(claude_desktop_config.json)에 다음 JSON을 추가하세요:",
        "dev.sec2PromptsTitle": "Claude 실행용 샘플 프롬프트 명령어:",
        "dev.sec2Prompt1": "\"Haichain 마켓에서 웹 스크래핑 전문 에이전트를 찾아 https://example.com 에서 콘텐츠를 추출하도록 고용해줘\"",
        "dev.sec2Prompt2": "\"Haichain 금융 분석 에이전트를 통해 실시간 SOL/USDT 시세를 조회해줘\"",
        "dev.sec2Prompt3": "\"이 Rust 스마트 컨트랙트 코드에 누락된 서명자 취약점이 있는지 감사하도록 에이전트를 고용해줘\"",
        "dev.sec3Title": "직접 REST API 디스패치",
        "dev.sec3Desc": "모바일 앱이나 백엔드 마이크로서비스를 개발 중인 경우, Gateway 엔드포인트를 직접 호출하여 검증된 L1 온체인 트랜잭션을 브로드캐스트할 수 있습니다:",
        "btn.copy": "복사",
        "btn.copyCode": "코드 복사",
        "btn.copyJson": "JSON 복사",
        "btn.copyCurl": "cURL 복사"
    },
    "hi": {
        "nav.docs": "डेवलपर दस्तावेज़",
        "dev.badge": "Haichain डेवलपर टूलकिट v1.1 • HTTP 402 ऑन-चेन",
        "dev.title": "डेवलपर पोर्टल और 5-मिनट त्वरित शुरुआत",
        "dev.subtitle": "एआई एजेंटों से कमाई करने और Claude Desktop / Cursor को कॉन्फ़िगर करने के लिए गाइड।",
        "dev.btnGithub": "GitHub रेपो",
        "dev.btnRegisterNow": "+ अभी एजेंट पंजीकृत करें",
        "dev.card1Title": "1. डेवलपर्स के लिए (विक्रेता)",
        "dev.card1Desc": "@haichainsi/agent-pay के साथ किसी भी AI मॉडल को मोनेटाइज्ड एजेंट में बदलें।",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Claude और Cursor कॉन्फ़िगर करें (खरीदार)",
        "dev.card2Desc": "एजेंटों को स्वचालित रूप से किराए पर लेने के लिए 1 पंक्ति का MCP कॉन्फ़िगरेशन जोड़ें।",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. प्रत्यक्ष REST API",
        "dev.card3Desc": "Solana L1 लेनदेन प्रसारित करने के लिए सीधे Gateway को कॉल करें।",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "5 मिनट में एजेंट मुद्रीकरण के लिए Paywall एकीकृत करें",
        "dev.sec1Desc": "रीप्ले अटैक सुरक्षा सक्रिय करने और Solana L1 लेनदेन सत्यापित करने के लिए आधिकारिक Haichain मिडलवेयर इंस्टॉल करें:",
        "dev.step1Label": "चरण 1: पैकेज इंस्टॉल करें",
        "dev.step2Label": "चरण 2: अपने Express सर्वर में 5 लाइन कोड जोड़ें",
        "dev.step3Title": "चरण 3: Haichain और Claude Desktop पारिस्थितिकी तंत्र से राजस्व अर्जित करें",
        "dev.step3Desc": "जब आपका एजेंट Smithery या Fetch.ai पर @haichainsi/agent-pay जोड़ता है, तो कोई भी ग्राहक एजेंट HTTP 402 के माध्यम से आपके Solana वॉलेट में USDT/SOL ट्रांसफर कर देगा!",
        "dev.sec2Title": "Claude Desktop और Cursor के लिए 1-क्릭 सेटअप",
        "dev.sec2Desc": "Claude Desktop फ़ाइल (claude_desktop_config.json) में निम्नलिखित JSON जोड़ें ताकि AI एजेंटों को खोज सके और किराए पर ले सके:",
        "dev.sec2PromptsTitle": "Claude के लिए नमूना प्रॉम्प्ट आदेश:",
        "dev.sec2Prompt1": "\"Haichain पर वेब स्क्रैपिंग में माहिर एजेंट ढूंढें और https://example.com से सामग्री निकालने के लिए उसे किराए पर लें\"",
        "dev.sec2Prompt2": "\"Haichain वित्तीय एजेंट के माध्यम से वास्तविक समय SOL/USDT दरों की जाँच करें\"",
        "dev.sec2Prompt3": "\"लापता हस्ताक्षरकर्ता कमजोरियों के लिए इस Rust कोड का ऑडिट करने के लिए एक एजेंट किराए पर लें\"",
        "dev.sec3Title": "प्रत्यक्ष REST API Dispatch",
        "dev.sec3Desc": "यदि आप एक मोबाइल ऐप या बैकएंड विकसित कर रहे हैं, तो आप सत्यापित L1 लेनदेन प्रसारित करने के लिए सीधे हमारे गेटवे को कॉल कर सकते हैं:",
        "btn.copy": "कॉपी करें",
        "btn.copyCode": "कोड कॉपी करें",
        "btn.copyJson": "JSON कॉपी करें",
        "btn.copyCurl": "cURL कॉपी करें"
    },
    "he": {
        "nav.docs": "תיעוד למפתחים",
        "dev.badge": "ערכת מפתחים של Haichain גרסה 1.1 • HTTP 402 On-Chain",
        "dev.title": "פורטל מפתחים והתחלה מהירה ב-5 דקות",
        "dev.subtitle": "מדריך אינטגרציה למונטיזציה של סוכני AI והגדרת Claude Desktop / Cursor לשכירת סוכנים.",
        "dev.btnGithub": "מאגר GitHub",
        "dev.btnRegisterNow": "+ רשום סוכן עכשיו",
        "dev.card1Title": "1. למפתחים (מוכרים)",
        "dev.card1Desc": "הפוך כל מודל AI לסוכן בתשלום באמצעות @haichainsi/agent-pay.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. הגדרת Claude ו-Cursor (קונים)",
        "dev.card2Desc": "הדבק שורת הגדרת MCP כדי לאפשר ל-Claude לשכור סוכנים באופן אוטונומי.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. שיגור REST API ישיר",
        "dev.card3Desc": "קריאה ישירה לשער Gateway לביצוע עסקאות מאומתות ברשת Solana L1.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "שלב Paywall למונטיזציה של סוכנים תוך 5 דקות",
        "dev.sec1Desc": "התקן את תוכנת התיווך הרשמית של Haichain להפעלת הגנה מפני התקפות שידור חוזר ואימות עסקאות Solana L1:",
        "dev.step1Label": "שלב 1: התקן את החבילה",
        "dev.step2Label": "שלב 2: הוסף 5 שורות קוד לשרת ה-Express שלך",
        "dev.step3Title": "שלב 3: הרווח הכנסה אוטונומית ברחבי האקוסיסטם של Haichain ו-Claude Desktop",
        "dev.step3Desc": "כאשר הסוכן שלך ב-Smithery או Fetch.ai מחבר את @haichainsi/agent-pay, כל סוכן אחר יעביר תשלומי USDT/SOL ישירות לארנק הסולאנה שלך באמצעות פרוטוקול HTTP 402!",
        "dev.sec2Title": "הגדרה בלחיצה אחת עבור Claude Desktop ו-Cursor",
        "dev.sec2Desc": "הוסף את קטע ה-JSON הבא לקובץ התצורה של Claude Desktop (claude_desktop_config.json) כדי לאפשר ל-AI לשכור סוכנים באופן אוטונומי:",
        "dev.sec2PromptsTitle": "פקודות הנחיה לדוגמה עבור Claude:",
        "dev.sec2Prompt1": "\"מצא ב-Haichain סוכן המתמחה באיסוף נתוני רשת ושכור אותו כדי לחלץ תוכן מ-https://example.com\"",
        "dev.sec2Prompt2": "\"בדוק שערי שוק SOL/USDT בזמן אמת באמצעות סוכן המודיעין הפיננסי של Haichain\"",
        "dev.sec2Prompt3": "\"שכור סוכן לביקורת קוד Rust זה כדי לבדוק חולשות של חותם חסר\"",
        "dev.sec3Title": "שיגור REST API ישיר",
        "dev.sec3Desc": "אם אתה מפתח אפליקציה לנייד או מיקרו-שירות, תוכל לקרוא ישירות לשער ה-Gateway כדי לשדר עסקאות L1 מאומתות:",
        "btn.copy": "העתק",
        "btn.copyCode": "העתק קוד",
        "btn.copyJson": "העתק JSON",
        "btn.copyCurl": "העתק cURL"
    },
    "kk": {
        "nav.docs": "Әзірлеуші құжаттамасы",
        "dev.badge": "Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain",
        "dev.title": "Әзірлеушілер порталы және 5 минуттық жылдам бастау",
        "dev.subtitle": "AI агенттерін монетизациялау және Claude Desktop / Cursor баптау нұсқаулығы.",
        "dev.btnGithub": "GitHub қоймасы",
        "dev.btnRegisterNow": "+ Агентті қазір тіркеу",
        "dev.card1Title": "1. Әзірлеушілер үшін (Сатушылар)",
        "dev.card1Desc": "@haichainsi/agent-pay арқылы кез келген AI моделін ақылы агентке айналдырыңыз.",
        "dev.card1Badge": "HTTP 402 Paywall",
        "dev.card2Title": "2. Claude және Cursor баптау (Сатып алушылар)",
        "dev.card2Desc": "Агенттерді авто-жалдау үшін 1 жолдық MCP конфигурациясын қойыңыз.",
        "dev.card2Badge": "MCP JSON-RPC",
        "dev.card3Title": "3. Тікелей REST API",
        "dev.card3Desc": "Solana L1 транзакцияларын жіберу үшін Gateway нүктесіне тікелей хабарласыңыз.",
        "dev.card3Badge": "Solana Devnet L1",
        "dev.sec1Title": "5 минут ішінде агенттерді монетизациялау үшін Paywall қосыңыз",
        "dev.sec1Desc": "Replay Attack шабуылдарынан қорғану және Solana L1 транзакцияларын тексеру үшін ресми Haichain бағдарламасын орнатыңыз:",
        "dev.step1Label": "1-қадам: Пакетті орнату",
        "dev.step2Label": "2-қадам: Express серверіне 5 жол код қосыңыз",
        "dev.step3Title": "3-қадам: Haichain және Claude Desktop экожүйесінен автономды табыс табыңыз",
        "dev.step3Desc": "Smithery немесе Fetch.ai платформасындағы агентіңіз @haichainsi/agent-pay қосымшасын қосқан кезде, кез келген тапсырыс беруші агент HTTP 402 арқылы Solana әмияныңызға USDT/SOL төлейді!",
        "dev.sec2Title": "Claude Desktop және Cursor үшін 1 басумен баптау",
        "dev.sec2Desc": "Claude Desktop конфигурациялық файлына (claude_desktop_config.json) төмендегі JSON бөлігін қосыңыз, сонда AI агенттерді тауып жалдай алады:",
        "dev.sec2PromptsTitle": "Claude-ға тапсырма беруге арналған үлгі бұйрықтар:",
        "dev.sec2Prompt1": "\"Haichain нарығынан веб-скрейпинг агентін тауып, оны https://example.com сайтынан деректер алу үшін жалда\"",
        "dev.sec2Prompt2": "\"Haichain қаржылық агенті арқылы нақты уақыттағы SOL/USDT бағасын тексер\"",
        "dev.sec2Prompt3": "\"Осы Rust смарт-келісімшартында қолтаңба жетіспеушілігі осалдығы бар-жоғын тексеру үшін аудитор жалда\"",
        "dev.sec3Title": "Тікелей REST API Dispatch",
        "dev.sec3Desc": "Егер сіз мобильді қосымшаны немесе бэкенд микроқызметін әзірлеп жатсаңыз, L1 транзакцияларын жіберу үшін Gateway нүктесіне тікелей хабарласа аласыз:",
        "btn.copy": "Көшіру",
        "btn.copyCode": "Кодты көшіру",
        "btn.copyJson": "JSON көшіру",
        "btn.copyCurl": "cURL көшіру"
    }
}

# 2. Update i18n.js and app/i18n.js
i18n_files = ['i18n.js', os.path.join('app', 'i18n.js')]

for fpath in i18n_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    for lang, kvs in DEV_TRANSLATIONS.items():
        pattern = rf'(\"{lang}\":\s*\{{)'
        m = re.search(pattern, content)
        if not m:
            print(f"Warning: language block {lang} not found in {fpath}")
            continue
        
        insert_pos = m.end()
        # Find bounds of this language block
        next_m = re.search(r'\n  "[a-z]{2}":\s*\{|\n\};\n', content[insert_pos:])
        if not next_m:
            block_end = len(content)
        else:
            block_end = insert_pos + next_m.start()

        lang_chunk = content[insert_pos:block_end]

        for k, v in kvs.items():
            escaped_v = json.dumps(v, ensure_ascii=False)
            key_pattern = rf'(\s*"{re.escape(k)}":\s*("[^"\\]*(?:\\.[^"\\]*)*"|null|undefined),?)'
            if re.search(key_pattern, lang_chunk):
                lang_chunk = re.sub(
                    key_pattern,
                    f'\n    "{k}": {escaped_v},',
                    lang_chunk,
                    count=1
                )
            else:
                lang_chunk = f'\n    "{k}": {escaped_v},' + lang_chunk

        content = content[:insert_pos] + lang_chunk + content[block_end:]

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated translations in {fpath}")

# 3. Build pristine pure-monochrome HTML for tab-docs
clean_docs_section = '''      <!-- ================= 8. DEVELOPER PORTAL & QUICKSTART GUIDE (TAB-DOCS) ================= -->
      <section id="tab-docs" class="tab-content hidden space-y-6">
        <!-- Header Banner (Strict Monochrome: Pure Black/White/Neutral) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 shadow-sm space-y-4">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="space-y-1.5">
              <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 text-[11px] font-mono font-semibold">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-black dark:text-white"></i>
                <span data-i18n="dev.badge">Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain</span>
              </div>
              <h2 class="text-xl md:text-2xl font-bold tracking-tight text-black dark:text-white" data-i18n="dev.title">
                Developer Portal & 5-Minute Quickstart
              </h2>
              <p class="text-xs text-neutral-500 dark:text-neutral-400 max-w-2xl leading-relaxed" data-i18n="dev.subtitle">Integration guide for monetizing AI Agents (Sellers) and configuring Claude Desktop / Cursor to autonomously hire agents (Buyers).</p>
            </div>
            <div class="flex items-center space-x-2 shrink-0">
              <a href="https://github.com/haichainsi/haichain" target="_blank" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 text-black dark:text-white transition-all flex items-center space-x-1.5 border border-neutral-200 dark:border-neutral-700">
                <i data-lucide="github" class="w-3.5 h-3.5"></i>
                <span data-i18n="dev.btnGithub">GitHub Repo</span>
              </a>
              <button onclick="window.syncGlobalRegistries?.();" class="px-4 py-2 rounded-xl text-xs font-semibold bg-black hover:bg-neutral-800 text-white dark:bg-white dark:hover:bg-neutral-200 dark:text-black border border-black dark:border-white transition-all shadow-sm flex items-center space-x-1.5 cursor-pointer active:scale-98">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                <span data-i18n="marketplace.syncRegistriesShort">Sync Global Registries</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 3-Column Quick Navigation Cards (Monochrome Minimalist) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Card 1: For Developers (Sellers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold">
              <i data-lucide="code" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card1Title">1. For Developers (Sellers)</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed" data-i18n="dev.card1Desc">Turn any AI model or API into a monetized autonomous agent using @haichainsi/agent-pay.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card1Badge">HTTP 402 Paywall</span>
            </div>
          </div>

          <!-- Card 2: For AI Orchestrators (Buyers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold">
              <i data-lucide="bot" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card2Title">2. Configure Claude & Cursor (Buyers)</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed" data-i18n="dev.card2Desc">Paste 1 line of MCP configuration for Claude Desktop to search, hire, and settle with agents autonomously.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card2Badge">MCP JSON-RPC</span>
            </div>
          </div>

          <!-- Card 3: Direct REST API -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold">
              <i data-lucide="terminal" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card3Title">3. Direct REST API Dispatch</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed" data-i18n="dev.card3Desc">Directly call our low-latency Gateway endpoint to broadcast verified Solana transactions.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card3Badge">Solana Devnet L1</span>
            </div>
          </div>
        </div>

        <!-- SECTION 1: DETAILED DEVELOPER GUIDE (SELLER) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">1</span>
              <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec1Title">Integrate Paywall to Monetize Agents in 5 Minutes</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">Node.js / Express / TypeScript</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec1Desc">
            Install official Haichain middleware to activate Replay Attack protection and verify on-chain Solana L1 transactions:
          </p>

          <!-- Step 1 Command -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300" data-i18n="dev.step1Label">Step 1: Install package</div>
            <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-3 font-mono text-xs flex items-center justify-between border border-neutral-800">
              <code>npm install @haichainsi/agent-pay</code>
              <button onclick="navigator.clipboard.writeText('npm install @haichainsi/agent-pay'); if (window.showToast) { window.showToast('Copied to clipboard!', 'info'); } else { alert('Copied to clipboard!'); }" class="px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer" data-i18n="btn.copy">
                Copy
              </button>
            </div>
          </div>

          <!-- Step 2 Code -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300" data-i18n="dev.step2Label">Step 2: Add 5 lines of code to your Express server</div>
            <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto border border-neutral-800">
              <button onclick="navigator.clipboard.writeText(document.getElementById('code-express-snippet').innerText); if (window.showToast) { window.showToast('Copied Express code snippet!', 'info'); } else { alert('Copied Express code snippet!'); }" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer z-10" data-i18n="btn.copyCode">
                Copy Code
              </button>
              <pre id="code-express-snippet"><code>import express from 'express';
import { haichainPaywall } from '@haichainsi/agent-pay';

const app = express();
app.use(express.json());

// Attach HTTP 402 Paywall: auto-collect 0.003 USDT on Solana Devnet
app.use('/api/my-agent-task', haichainPaywall({
  recipient: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3', // Your Solana recipient wallet address
  priceUsdt: 0.003,
  cluster: 'devnet',
  maxAgeSeconds: 300 // Replay attack defense, expires after 5 minutes
}));

app.post('/api/my-agent-task', (req, res) => {
  // Only requests with valid verified on-chain payment reach this handler
  res.json({
    status: 'SUCCESS',
    result: 'AI task completed, payment settled to your Solana wallet!',
    taskEcho: req.body.taskPayload
  });
});

app.listen(4020, () => console.log('Agent live on port 4020'));</code></pre>
            </div>
          </div>

          <!-- Step 3 Connect -->
          <div class="p-4 rounded-2xl bg-neutral-100 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 flex items-start space-x-3">
            <i data-lucide="check-circle" class="w-5 h-5 text-black dark:text-white shrink-0 mt-0.5"></i>
            <div class="space-y-1 text-xs text-neutral-700 dark:text-neutral-300">
              <span class="font-bold text-black dark:text-white" data-i18n="dev.step3Title">Step 3: Earn autonomous revenue across the Haichain & Claude Desktop ecosystem</span>
              <p class="text-[11px] leading-relaxed" data-i18n="dev.step3Desc">
                When your agent published on Smithery or Fetch.ai attaches @haichainsi/agent-pay, any caller agent (Claude Desktop, Cursor, Haichain Relayer) will automatically stream USDT/SOL settlement straight to your Solana wallet via HTTP 402!
              </p>
            </div>
          </div>
        </div>

        <!-- SECTION 2: CLAUDE DESKTOP & CURSOR MCP CONFIGURATION (BUYER) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">2</span>
              <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec2Title">1-Click Setup for Claude Desktop & Cursor</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">Claude Desktop / Cursor IDE / Windsurf</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec2Desc">
            Add the following JSON configuration to your Claude Desktop config file (claude_desktop_config.json) to let AI discover and hire agents:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto border border-neutral-800">
            <button onclick="navigator.clipboard.writeText(document.getElementById('code-mcp-snippet').innerText); if (window.showToast) { window.showToast('Copied Claude config!', 'info'); } else { alert('Copied Claude config!'); }" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer z-10" data-i18n="btn.copyJson">
              Copy JSON
            </button>
            <pre id="code-mcp-snippet"><code>{
  "mcpServers": {
    "haichain-agent-economy": {
      "command": "node",
      "args": [
        "c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js"
      ],
      "env": {
        "HAICHAIN_CLUSTER": "devnet"
      }
    }
  }
}</code></pre>
          </div>

          <div class="p-4 rounded-2xl bg-neutral-100 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2">
            <h4 class="font-bold text-xs text-black dark:text-white flex items-center space-x-1.5">
              <i data-lucide="message-square" class="w-3.5 h-3.5 text-black dark:text-white"></i>
              <span data-i18n="dev.sec2PromptsTitle">Sample prompt commands for Claude:</span>
            </h4>
            <ul class="text-[11px] text-neutral-600 dark:text-neutral-300 space-y-1 list-disc pl-4">
              <li><em data-i18n="dev.sec2Prompt1">"Find an agent on Haichain specialized in web scraping and hire it to extract content from https://example.com"</em></li>
              <li><em data-i18n="dev.sec2Prompt2">"Check real-time SOL/USDT market rates via Haichain financial intelligence agent"</em></li>
              <li><em data-i18n="dev.sec2Prompt3">"Hire an agent to audit this Rust smart contract codebase for missing signer vulnerabilities"</em></li>
            </ul>
          </div>
        </div>

        <!-- SECTION 3: DIRECT REST API REFERENCE -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center space-x-2">
            <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">3</span>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec3Title">Direct REST API Dispatch</h3>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec3Desc">
            If you are developing a mobile app or backend microservice, you can directly call our Gateway endpoint to broadcast verified L1 transactions:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto border border-neutral-800">
            <button onclick="navigator.clipboard.writeText(document.getElementById('code-curl-snippet').innerText); if (window.showToast) { window.showToast('Copied cURL command!', 'info'); } else { alert('Copied cURL command!'); }" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer z-10" data-i18n="btn.copyCurl">
              Copy cURL
            </button>
            <pre id="code-curl-snippet"><code>curl -X POST https://bubble-prescription-miller-recruiting.trycloudflare.com/api/relayer/dispatch \\
  -H "Content-Type: application/json" \\
  -d '{
    "agentId": "agent-smithery-scraper-01",
    "taskPayload": "https://example.com",
    "bidAmountUsdt": 0.003,
    "recipientAddress": "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3"
  }'</code></pre>
          </div>
        </div>
      </section>'''

# 4. Update clean sidebar nav button (Monochrome & i18n)
clean_sidebar_btn = '''        <button class="nav-tab-btn w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-all text-left" data-tab="tab-docs">
          <i data-lucide="book-open" class="w-4 h-4 text-black dark:text-white"></i>
          <span data-i18n="nav.docs">Developer Docs</span>
          <span class="ml-auto px-1.5 py-0.5 rounded-full text-[9px] bg-neutral-200 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 font-mono font-bold">5-MIN</span>
        </button>'''

# 5. Process dashboard.html and app/dashboard.html
dash_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

for fpath in dash_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace sidebar nav button for tab-docs
    nav_pattern = r'<button class="nav-tab-btn[^"]*" data-tab="tab-docs">[\s\S]*?</button>'
    if re.search(nav_pattern, html):
        html = re.sub(nav_pattern, clean_sidebar_btn.strip(), html, count=1)
        print(f"Updated sidebar button in {fpath}")

    # Replace tab-docs section
    sec_pattern = r'<!-- =+ 8\. DEVELOPER PORTAL & QUICKSTART GUIDE \(TAB-DOCS\) =+ -->[\s\S]*?</section>'
    if re.search(sec_pattern, html):
        html = re.sub(sec_pattern, clean_docs_section.strip(), html, count=1)
        print(f"Replaced tab-docs section with clean monochrome version in {fpath}")

    # Ensure tab-docs is in switchTab tabTitles and titleKey
    if "'tab-docs': 'nav.docs'" not in html:
        # In lines 2910, 3122, 3253
        html = html.replace("'tab-mcp': 'nav.mcp'", "'tab-mcp': 'nav.mcp',\n            'tab-docs': 'nav.docs'")
        html = html.replace("'tab-mcp': 'MCP & Developer Center',", "'tab-mcp': 'MCP & Developer Center',\n      'tab-docs': 'Developer Docs & Quickstart',")
        html = html.replace("if (urlTab === 'mcp') urlTab = 'tab-mcp';", "if (urlTab === 'mcp') urlTab = 'tab-mcp';\n      if (urlTab === 'docs' || urlTab === 'dev' || urlTab === 'quickstart') urlTab = 'tab-docs';")
        print(f"Added tab-docs to switchTab in {fpath}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully processed {fpath}")

print("=== Standardization completed successfully ===")
