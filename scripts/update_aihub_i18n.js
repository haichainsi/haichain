const fs = require('fs');

const TRANSLATIONS = {
  vi: {
    tabOnline: "2. Claude Mobile (Đám Mây)",
    onlineTitle: "Cloud MCP Gateway (Claude Mobile)",
    onlineBadge: "Đang Triển Khai",
    onlineDesc: "Kết nối Claude từ xa trên điện thoại yêu cầu máy chủ Cloud Gateway 24/7. Để trải nghiệm ngay, vui lòng chọn một trong hai phương án đã hoạt động 100% bên dưới:",
    onlineNoticeTitle: "Hạ tầng Cloud Gateway 24/7 đang được cấu hình",
    onlineNoticeText: "Trang web hiện là Static CDN nên địa chỉ từ xa trả về mã 404 khi Claude ping tới. Hãy dùng AI Playground ngay trên điện thoại hoặc Claude Desktop trên máy tính.",
    onlinePlaygroundBtn: "⚡ Mở AI Playground (Cho Điện Thoại)",
    onlineDesktopBtn: "💻 Claude Desktop (Cho Máy Tính)",
    onlineReadyToolsTitle: "4 Công cụ On-Chain đã sẵn sàng trên Kernel:"
  },
  en: {
    tabOnline: "2. Claude Mobile (Cloud)",
    onlineTitle: "Cloud MCP Gateway (Claude Mobile)",
    onlineBadge: "Under Deployment",
    onlineDesc: "Direct remote integration for Claude Mobile requires a dedicated 24/7 Cloud Gateway server. For immediate verified testing, choose one of the two active options below:",
    onlineNoticeTitle: "24/7 Cloud Gateway Server Under Deployment",
    onlineNoticeText: "The site is currently hosted on a Static CDN, so remote requests return 404. We recommend using AI Playground directly on mobile or Claude Desktop on PC.",
    onlinePlaygroundBtn: "⚡ Open AI Playground (Mobile)",
    onlineDesktopBtn: "💻 Claude Desktop (PC/Mac)",
    onlineReadyToolsTitle: "4 On-Chain MCP Tools Ready on Kernel:"
  },
  zh: {
    tabOnline: "2. Claude 移动端 (云端网关)",
    onlineTitle: "云端 MCP 网关 (Claude 移动端)",
    onlineBadge: "基础设施部署中",
    onlineDesc: "Claude 移动端远程连接需要专用的 24/7 云端网关服务器。如需立即体验，请选择以下已完全就绪的方案：",
    onlineNoticeTitle: "24/7 云端网关基础设施正在部署中",
    onlineNoticeText: "当前网站部署在静态 CDN 上，远程连接将返回 404。建议在手机端直接使用网页版 AI Playground，或在电脑上使用 Claude Desktop。",
    onlinePlaygroundBtn: "⚡ 打开 AI Playground (手机即开即用)",
    onlineDesktopBtn: "💻 Claude Desktop (电脑推荐)",
    onlineReadyToolsTitle: "4 项链上 MCP 工具已在内核就绪："
  },
  kk: {
    tabOnline: "2. Claude Mobile (Бұлтты)",
    onlineTitle: "Бұлтты MCP Gateway (Claude Mobile)",
    onlineBadge: "Орнатылуда",
    onlineDesc: "Claude Mobile қашықтағы интеграциясы тәулік бойы жұмыс істейтін арнайы Cloud Gateway серверін қажет етеді. Дереу сынап көру үшін төмендегі дайын нұсқаларды таңдаңыз:",
    onlineNoticeTitle: "24/7 Cloud Gateway инфрақұрылымы бапталуда",
    onlineNoticeText: "Қазіргі сайт статикалық CDN желісінде, сондықтан қашықтан қосылғанда 404 қатесі қайтарылады. Телефонда AI Playground немесе компьютерде Claude Desktop қолданыңыз.",
    onlinePlaygroundBtn: "⚡ AI Playground ашу (Мобильді)",
    onlineDesktopBtn: "💻 Claude Desktop (ДК/Mac)",
    onlineReadyToolsTitle: "Кернелде дайын 4 On-Chain MCP құралы:"
  },
  ko: {
    tabOnline: "2. Claude 모바일 (클라우드)",
    onlineTitle: "클라우드 MCP 게이트웨이 (Claude 모바일)",
    onlineBadge: "인프라 구축 중",
    onlineDesc: "Claude 모바일 원격 연결에는 24시간 전용 클라우드 게이트웨이 서버가 필요합니다. 즉시 검증을 위해 아래 준비된 두 가지 옵션을 이용해 주세요:",
    onlineNoticeTitle: "24/7 클라우드 게이트웨이 인프라 설정 중",
    onlineNoticeText: "현재 사이트는 정적 CDN으로 호스팅되어 원격 요청 시 404가 반환됩니다. 모바일에서는 AI Playground를, PC에서는 Claude Desktop을 권장합니다.",
    onlinePlaygroundBtn: "⚡ AI Playground 열기 (모바일 즉시 실행)",
    onlineDesktopBtn: "💻 Claude Desktop (PC/Mac 권장)",
    onlineReadyToolsTitle: "커널에 탑재된 4개 온체인 MCP 도구:"
  },
  fr: {
    tabOnline: "2. Claude Mobile (Cloud)",
    onlineTitle: "Passerelle MCP Cloud (Claude Mobile)",
    onlineBadge: "Déploiement en cours",
    onlineDesc: "L'intégration directe pour Claude Mobile requiert un serveur Cloud Gateway dédié 24/7. Pour tester immédiatement, choisissez l'une des deux options actives ci-dessous :",
    onlineNoticeTitle: "Serveur Cloud Gateway 24/7 en cours de configuration",
    onlineNoticeText: "Le site étant actuellement hébergé sur un CDN statique, les requêtes distantes renvoient une erreur 404. Utilisez l'AI Playground sur mobile ou Claude Desktop sur PC.",
    onlinePlaygroundBtn: "⚡ Ouvrir AI Playground (Mobile)",
    onlineDesktopBtn: "💻 Claude Desktop (PC/Mac)",
    onlineReadyToolsTitle: "4 outils MCP On-Chain prêts sur le Kernel :"
  },
  es: {
    tabOnline: "2. Claude Móvil (Nube)",
    onlineTitle: "Pasarela MCP en la Nube (Claude Móvil)",
    onlineBadge: "En Despliegue",
    onlineDesc: "La integración remota para Claude Móvil requiere un servidor Cloud Gateway dedicado 24/7. Para probar de inmediato, elija una de las dos opciones activas:",
    onlineNoticeTitle: "Infraestructura Cloud Gateway 24/7 en configuración",
    onlineNoticeText: "El sitio está alojado en un CDN estático, por lo que las solicitudes remotas devuelven 404. Recomendamos usar AI Playground en móvil o Claude Desktop en PC.",
    onlinePlaygroundBtn: "⚡ Abrir AI Playground (Móvil)",
    onlineDesktopBtn: "💻 Claude Desktop (PC/Mac)",
    onlineReadyToolsTitle: "4 herramientas MCP On-Chain listas en el Kernel:"
  },
  ru: {
    tabOnline: "2. Claude Mobile (Облако)",
    onlineTitle: "Облачный MCP-шлюз (Claude Mobile)",
    onlineBadge: "В процессе развертывания",
    onlineDesc: "Удаленная интеграция для Claude Mobile требует выделенного облачного сервера 24/7. Для немедленного тестирования выберите один из двух готовых вариантов:",
    onlineNoticeTitle: "Инфраструктура облачного шлюза 24/7 настраивается",
    onlineNoticeText: "Сайт размещен на статическом CDN, поэтому удаленные запросы возвращают 404. Рекомендуем использовать AI Playground на телефоне или Claude Desktop на ПК.",
    onlinePlaygroundBtn: "⚡ Открыть AI Playground (Для телефонов)",
    onlineDesktopBtn: "💻 Claude Desktop (Для ПК/Mac)",
    onlineReadyToolsTitle: "4 инструмента On-Chain MCP готовы в ядре:"
  },
  hi: {
    tabOnline: "2. Claude मोबाइल (क्लाउड)",
    onlineTitle: "क्लाउड MCP गेटवे (Claude मोबाइल)",
    onlineBadge: "तैनाती जारी",
    onlineDesc: "Claude मोबाइल के लिए रिमोट एकीकरण को समर्पित 24/7 क्लाउड गेटवे सर्वर की आवश्यकता होती है। तत्काल परीक्षण के लिए नीचे दिए गए विकल्पों में से चुनें:",
    onlineNoticeTitle: "24/7 क्लाउड गेटवे इंफ्रास्ट्रक्चर कॉन्फ़िगर हो रहा है",
    onlineNoticeText: "साइट वर्तमान में एक स्टेटिक CDN पर होस्ट की गई है, इसलिए रिमोट अनुरोध 404 लौटाते हैं। मोबाइल पर सीधे AI Playground या PC पर Claude Desktop का उपयोग करें।",
    onlinePlaygroundBtn: "⚡ AI Playground खोलें (मोबाइल)",
    onlineDesktopBtn: "💻 Claude Desktop (PC/Mac)",
    onlineReadyToolsTitle: "कर्नेल पर 4 ऑन-चेन MCP टूल्स तैयार:"
  },
  he: {
    tabOnline: "2. Claude Mobile (ענן)",
    onlineTitle: "שער MCP ענן (Claude Mobile)",
    onlineBadge: "בפריסה",
    onlineDesc: "שילוב מרוחק עבור Claude Mobile דורש שרת Cloud Gateway ייעודי הפועל 24/7. לבדיקה מיידית, בחר באחת משתי האפשרויות הפעילות להלן:",
    onlineNoticeTitle: "תשתית שרת Cloud Gateway 24/7 בתהליך הגדרה",
    onlineNoticeText: "האתר מתארח כעת ב-CDN סטטי, ולכן בקשות מרוחקות מחזירות 404. אנו ממליצים להשתמש ב-AI Playground ישירות בנייד או ב-Claude Desktop במחשב.",
    onlinePlaygroundBtn: "⚡ פתח את AI Playground (נייד)",
    onlineDesktopBtn: "💻 Claude Desktop (מחשב)",
    onlineReadyToolsTitle: "4 כלי On-Chain MCP מוכנים בקרנל:"
  }
};

['i18n.js', 'app/i18n.js'].forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');
  
  for (const [lang, trans] of Object.entries(TRANSLATIONS)) {
    // Replace tabOnline
    const tabRegex = new RegExp(`("${lang}"\\s*:\\s*{[\\s\\S]*?"aiHub\\.tabOnline"\\s*:\\s*")[^"]*(")`);
    content = content.replace(tabRegex, `$1${trans.tabOnline}$2`);

    // Replace onlineTitle
    const titleRegex = new RegExp(`("${lang}"\\s*:\\s*{[\\s\\S]*?"aiHub\\.onlineTitle"\\s*:\\s*")[^"]*(")`);
    content = content.replace(titleRegex, `$1${trans.onlineTitle}$2`);

    // Replace onlineBadge
    const badgeRegex = new RegExp(`("${lang}"\\s*:\\s*{[\\s\\S]*?"aiHub\\.onlineBadge"\\s*:\\s*")[^"]*(")`);
    content = content.replace(badgeRegex, `$1${trans.onlineBadge}$2`);

    // Replace onlineDesc
    const descRegex = new RegExp(`("${lang}"\\s*:\\s*{[\\s\\S]*?"aiHub\\.onlineDesc"\\s*:\\s*")[^"]*(")`);
    content = content.replace(descRegex, `$1${trans.onlineDesc}$2`);

    // Inject extra keys if missing
    const targetAnchor = `"aiHub.onlineDesc": "${trans.onlineDesc}",`;
    const extraBlock = `
    "aiHub.onlineNoticeTitle": "${trans.onlineNoticeTitle}",
    "aiHub.onlineNoticeText": "${trans.onlineNoticeText}",
    "aiHub.onlinePlaygroundBtn": "${trans.onlinePlaygroundBtn}",
    "aiHub.onlineDesktopBtn": "${trans.onlineDesktopBtn}",
    "aiHub.onlineReadyToolsTitle": "${trans.onlineReadyToolsTitle}",`;

    if (!content.includes(`"aiHub.onlineNoticeTitle": "${trans.onlineNoticeTitle}"`)) {
      content = content.replace(targetAnchor, targetAnchor + extraBlock);
    }
  }

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Successfully updated', filePath);
});
