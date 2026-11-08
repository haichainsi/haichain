const fs = require('fs');

const MOBILE_TRANSLATIONS = {
  vi: {
    tabOnline: "2. Claude Mobile",
    onlineTitle: "Claude Mobile MCP Gateway",
    onlineBadge: "SẴN SÀNG (24/7)",
    onlineDesc: "Kết nối trực tiếp 24/7 cho ứng dụng Claude trên iPhone/Android. Giao tiếp an toàn qua giao thức Streamable HTTP toàn cầu mà không cần cài đặt phần mềm nào trên máy tính.",
    onlineUrlLabel: "URL Máy Chủ MCP (Dành cho Claude Mobile):",
    onlineCopyBtn: "Sao Chép URL Máy Chủ",
    onlineCopiedBtn: "✓ Đã sao chép URL!",
    onlineStepsTitle: "3 Bước Kết Nối Trên App Claude Mobile:",
    onlineStep1: "Mở app Claude trên điện thoại -> Cài đặt (Settings) -> Trình kết nối (Connectors) -> Thêm trình kết nối tùy chỉnh.",
    onlineStep2: "Đặt Tên: 'HAICHAIN' và dán URL máy chủ https://mcp.haichain.si/api/mcp vào ô URL.",
    onlineStep3: "Bấm Kết nối -> Chọn 'Không đăng nhập' (hoặc bấm 'Vẫn tiếp tục') -> Hoàn tất!",
    onlineReadyToolsTitle: "4 Công Cụ On-Chain Đã Sẵn Sàng Trên Claude:"
  },
  en: {
    tabOnline: "2. Claude Mobile",
    onlineTitle: "Claude Mobile MCP Gateway",
    onlineBadge: "ONLINE (24/7)",
    onlineDesc: "Direct 24/7 cloud integration for the Claude app on iOS & Android. Connects directly to the global HAICHAIN Cloud MCP Gateway via Streamable HTTP with zero desktop software required.",
    onlineUrlLabel: "MCP Server URL (For Claude Mobile):",
    onlineCopyBtn: "Copy Server URL",
    onlineCopiedBtn: "✓ URL copied!",
    onlineStepsTitle: "3 Steps to Connect on Claude Mobile:",
    onlineStep1: "Open Claude app on phone -> Settings -> Connectors -> Add custom connector.",
    onlineStep2: "Set Name to 'HAICHAIN' and paste the Server URL https://mcp.haichain.si/api/mcp into the URL field.",
    onlineStep3: "Click Connect -> Select 'No authentication' (or click 'Continue anyway') -> Done!",
    onlineReadyToolsTitle: "4 On-Chain MCP Tools Ready on Claude:"
  },
  zh: {
    tabOnline: "2. Claude 移动端",
    onlineTitle: "Claude 移动端 MCP 网关",
    onlineBadge: "在线运行 (24/7)",
    onlineDesc: "适用于 iOS 和 Android 端 Claude 移动应用的 24/7 极速云端直连。基于全球 Streamable HTTP 协议，无需在电脑端安装任何本地软件。",
    onlineUrlLabel: "MCP 服务器 URL (Claude 移动端专享)：",
    onlineCopyBtn: "复制服务器 URL",
    onlineCopiedBtn: "✓ URL 已复制！",
    onlineStepsTitle: "Claude 移动端连接 3 步指南：",
    onlineStep1: "在手机上打开 Claude 应用 -> 设置 -> 连接器 -> 添加自定义连接器。",
    onlineStep2: "设置名称为“HAICHAIN”，将服务器 URL https://mcp.haichain.si/api/mcp 粘贴至输入框。",
    onlineStep3: "点击连接 -> 选择“无需登录”（或点击“仍要继续”） -> 即可完成！",
    onlineReadyToolsTitle: "Claude 已就绪 4 项链上工具："
  },
  kk: {
    tabOnline: "2. Claude Mobile",
    onlineTitle: "Claude Mobile MCP Gateway",
    onlineBadge: "ONLINE (24/7)",
    onlineDesc: "iOS және Android жүйелеріндегі Claude мобильді қолданбасы үшін 24/7 тікелей бұлтты интеграция. Компьютерге ешқандай бағдарлама орнатуды талап етпейді.",
    onlineUrlLabel: "MCP Сервер URL мекенжайы (Claude Mobile үшін):",
    onlineCopyBtn: "Сервер URL-ін көшіру",
    onlineCopiedBtn: "✓ URL көшірілді!",
    onlineStepsTitle: "Claude Mobile-де қосылудың 3 қадамы:",
    onlineStep1: "Телефонда Claude қолданбасын ашыңыз -> Баптаулар -> Қосқыштар -> Реттелетін қосқыш қосу.",
    onlineStep2: "Атауын 'HAICHAIN' деп қойып, жоғарыдағы https://mcp.haichain.si/api/mcp сервер URL-ін қойыңыз.",
    onlineStep3: "Қосылу түймесін басыңыз -> 'Кірусіз' таңдаңыз (немесе 'Жалғастыру') -> Дайын!",
    onlineReadyToolsTitle: "Кернелде дайын 4 On-Chain MCP құралы:"
  },
  ko: {
    tabOnline: "2. Claude 모바일",
    onlineTitle: "Claude 모바일 MCP 게이트웨이",
    onlineBadge: "ONLINE (24/7)",
    onlineDesc: "iOS 및 Android Claude 모바일 앱을 위한 24시간 연중무휴 클라우드 직결. PC에 별도 프로그램을 설치할 필요가 없습니다.",
    onlineUrlLabel: "MCP 서버 URL (Claude 모바일 전용):",
    onlineCopyBtn: "서버 URL 복사",
    onlineCopiedBtn: "✓ URL 복사 완료!",
    onlineStepsTitle: "Claude 모바일 연결 3단계:",
    onlineStep1: "스마트폰에서 Claude 앱 실행 -> 설정 -> 커넥터 -> 커스텀 커넥터 추가.",
    onlineStep2: "이름을 'HAICHAIN'으로 입력하고 서버 URL https://mcp.haichain.si/api/mcp 를 붙여넣습니다.",
    onlineStep3: "연결 클릭 -> '로그인 안 함' 선택 (또는 '계속 진행' 클릭) -> 완료!",
    onlineReadyToolsTitle: "커널에 탑재된 4개 온체인 MCP 도구:"
  },
  fr: {
    tabOnline: "2. Claude Mobile",
    onlineTitle: "Passerelle MCP Claude Mobile",
    onlineBadge: "EN LIGNE (24/7)",
    onlineDesc: "Intégration cloud 24/7 pour l'application Claude sur iOS et Android. Aucun logiciel de bureau requis.",
    onlineUrlLabel: "URL Serveur MCP (Claude Mobile) :",
    onlineCopyBtn: "Copier l'URL Serveur",
    onlineCopiedBtn: "✓ URL copiée !",
    onlineStepsTitle: "3 Étapes de Connexion sur Claude Mobile :",
    onlineStep1: "Ouvrez l'application Claude sur votre téléphone -> Paramètres -> Connecteurs -> Ajouter un connecteur personnalisé.",
    onlineStep2: "Nom : 'HAICHAIN' et collez l'URL https://mcp.haichain.si/api/mcp dans le champ URL.",
    onlineStep3: "Cliquez sur Connecter -> Sélectionnez 'Sans authentification' (ou 'Continuer quand même') -> Terminé !",
    onlineReadyToolsTitle: "4 outils MCP On-Chain prêts sur Claude :"
  },
  es: {
    tabOnline: "2. Claude Móvil",
    onlineTitle: "Pasarela MCP Claude Móvil",
    onlineBadge: "EN LÍNEA (24/7)",
    onlineDesc: "Integración en la nube 24/7 para la app de Claude en iOS y Android. No requiere software de escritorio.",
    onlineUrlLabel: "URL del Servidor MCP (Claude Móvil):",
    onlineCopyBtn: "Copiar URL del Servidor",
    onlineCopiedBtn: "✓ ¡URL copiada!",
    onlineStepsTitle: "3 Pasos para Conectar en Claude Móvil:",
    onlineStep1: "Abre la app de Claude en el teléfono -> Ajustes -> Conectores -> Añadir conector personalizado.",
    onlineStep2: "Pon Nombre: 'HAICHAIN' y pega la URL https://mcp.haichain.si/api/mcp en el campo de URL.",
    onlineStep3: "Haz clic en Conectar -> Selecciona 'Sin autenticación' (o 'Continuar de todos modos') -> ¡Listo!",
    onlineReadyToolsTitle: "4 herramientas MCP On-Chain listas en Claude:"
  },
  ru: {
    tabOnline: "2. Claude Mobile",
    onlineTitle: "Облачный MCP-шлюз Claude Mobile",
    onlineBadge: "ОНЛАЙН (24/7)",
    onlineDesc: "Круглосуточная интеграция 24/7 для приложения Claude на iOS и Android. Не требует установки программ на ПК.",
    onlineUrlLabel: "URL MCP-сервера (Для Claude Mobile):",
    onlineCopyBtn: "Скопировать URL сервера",
    onlineCopiedBtn: "✓ URL скопирован!",
    onlineStepsTitle: "3 шага для подключения в Claude Mobile:",
    onlineStep1: "Откройте приложение Claude на телефоне -> Настройки -> Коннекторы -> Добавить пользовательский коннектор.",
    onlineStep2: "Укажите имя: 'HAICHAIN' и вставьте URL https://mcp.haichain.si/api/mcp в поле адреса.",
    onlineStep3: "Нажмите Подключить -> Выберите 'Без входа' (или 'Все равно продолжить') -> Готово!",
    onlineReadyToolsTitle: "4 инструмента On-Chain MCP готовы в Claude:"
  },
  hi: {
    tabOnline: "2. Claude मोबाइल",
    onlineTitle: "Claude मोबाइल MCP गेटवे",
    onlineBadge: "सक्रिय (24/7)",
    onlineDesc: "iOS और Android पर Claude मोबाइल ऐप के लिए 24/7 क्लाउड एकीकरण। किसी डेस्कटॉप सॉफ़्टवेयर की आवश्यकता नहीं है।",
    onlineUrlLabel: "MCP सर्वर URL (Claude मोबाइल के लिए):",
    onlineCopyBtn: "सर्वर URL कॉपी करें",
    onlineCopiedBtn: "✓ URL कॉपी किया गया!",
    onlineStepsTitle: "Claude मोबाइल पर कनेक्ट करने के 3 चरण:",
    onlineStep1: "फोन पर Claude ऐप खोलें -> सेटिंग्स -> कनेक्टर्स -> कस्टम कनेक्टर जोड़ें।",
    onlineStep2: "नाम: 'HAICHAIN' रखें और सर्वर URL https://mcp.haichain.si/api/mcp पेस्ट करें।",
    onlineStep3: "कनेक्ट पर क्लिक करें -> 'कोई लॉगिन नहीं' चुनें -> पूरा हुआ!",
    onlineReadyToolsTitle: "Claude पर 4 ऑन-चेन टूल्स तैयार:"
  },
  he: {
    tabOnline: "2. Claude Mobile",
    onlineTitle: "שער MCP של Claude Mobile",
    onlineBadge: "מקוון (24/7)",
    onlineDesc: "שילוב ענן 24/7 עבור אפליקציית Claude ב-iOS ו-Android. אינו דורש תוכנת מחשב.",
    onlineUrlLabel: "כתובת שרת MCP (עבור Claude Mobile):",
    onlineCopyBtn: "העתק כתובת שרת",
    onlineCopiedBtn: "✓ הכתובת הועתקה!",
    onlineStepsTitle: "3 שלבים לחיבור ב-Claude Mobile:",
    onlineStep1: "פתח את אפליקציית Claude בנייד -> הגדרות -> מחברים -> הוסף מחבר מותאם אישית.",
    onlineStep2: "הגדר שם: 'HAICHAIN' והדבק את הכתובת https://mcp.haichain.si/api/mcp בשדה ה-URL.",
    onlineStep3: "לחץ על התחבר -> בחר 'ללא כניסה' (או 'המשך בכל מקרה') -> בוצע!",
    onlineReadyToolsTitle: "4 כלי On-Chain MCP מוכנים ב-Claude:"
  }
};

['i18n.js', 'app/i18n.js'].forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');

  for (const [lang, t] of Object.entries(MOBILE_TRANSLATIONS)) {
    const langStart = content.indexOf(`"${lang}": {`);
    if (langStart === -1) continue;
    const nextLangStart = content.indexOf(`"${lang === 'he' ? '}' : '",'}"`, langStart + 10);
    const langBlockEnd = nextLangStart !== -1 ? nextLangStart : content.indexOf('};\n', langStart);

    // Update keys
    for (const [k, v] of Object.entries(t)) {
      const fullKey = `aiHub.${k}`;
      const keyRegex = new RegExp(`("${fullKey}"\\s*:\\s*")[^"]*(")`);
      if (keyRegex.test(content)) {
        content = content.replace(keyRegex, `$1${v}$2`);
      }
    }
  }

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Successfully updated i18n in', filePath);
});
