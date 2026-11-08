const fs = require('fs');

function patchDialog(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  if (content.includes('DEFAULT_EMPTY_NOTICE')) {
    console.log(filePath, 'already has DEFAULT_EMPTY_NOTICE');
    return;
  }

  const oldCode = `    const lower = (title + ' ' + body).toLowerCase();`;
  
  const newCode = `    const DEFAULT_EMPTY_NOTICE = {
      vi: "Chưa phát hiện tiện ích ví Web3 (Phantom, Solflare, MetaMask) trên trình duyệt này.\\n\\nVui lòng mở trang web trong trình duyệt nội bộ của ứng dụng ví, hoặc chuyển sang tab 'Faucet (+$10)' để nhận 10 USDT thử nghiệm miễn phí!",
      en: "Web3 wallet extension (Phantom, Solflare, MetaMask) not detected in this browser.\\n\\nPlease open the website inside your wallet app's in-app browser, or switch to the 'Faucet (+$10)' tab to claim 10 USDT free test funds!",
      zh: "未在此浏览器中检测到 Web3 钱包扩展 (Phantom、Solflare、MetaMask)。\\n\\n请在钱包 App 内置浏览器中打开，或切换到“Faucet (+$10)”标签免费领取 10 USDT 测试资金！",
      kk: "Бұл браузерде Web3 әмиян кеңейтімі (Phantom, Solflare, MetaMask) табылмады.\\n\\nӘмиян қолданбасының ішкі браузерінде ашыңыз немесе тегін 10 USDT алу үшін 'Faucet (+$10)' қойындысына өтіңіз!",
      ko: "이 브라우저에서 Web3 지갑 확장 프로그램(Phantom, Solflare, MetaMask)을 감지할 수 없습니다.\\n\\n지갑 앱의 인앱 브라우저에서 열거나 'Faucet (+$10)' 탭으로 전환하여 무료 10 USDT 테스트 자금을 받으세요!",
      fr: "Extension de portefeuille Web3 (Phantom, Solflare, MetaMask) non détectée dans ce navigateur.\\n\\nVeuillez ouvrir dans le navigateur de votre portefeuille ou passer à l'onglet 'Faucet (+$10)' pour réclamer 10 USDT de test gratuits !",
      es: "No se detectó la extensión de billetera Web3 (Phantom, Solflare, MetaMask) en este navegador.\\n\\nÁbralo en el navegador de su billetera o cambie a la pestaña 'Faucet (+$10)' para reclamar 10 USDT de fondos de prueba gratuitos.",
      ru: "Расширение Web3-кошелька (Phantom, Solflare, MetaMask) не обнаружено в браузере.\\n\\nОткройте сайт во встроенном браузере приложения кошелька или перейдите на вкладку 'Faucet (+$10)', чтобы получить бесплатные 10 USDT!",
      hi: "इस ब्राउज़र में Web3 वॉलेट एक्सटेंशन (Phantom, Solflare, MetaMask) नहीं मिला।\\n\\nकृपया अपने वॉलेट ऐप के ब्राउज़र में खोलें या 10 USDT मुफ़्त टेस्ट फंड के लिए 'Faucet (+$10)' टैब पर जाएँ!",
      he: "תוסף ארנק Web3 (Phantom, Solflare, MetaMask) לא זוהה בדפדפן זה.\\n\\nאנא פתח בדפדפן של אפליקציית הארנק או עבור ללשונית 'Faucet (+$10)' לקבלת 10 USDT כספי בדיקה בחינם!"
    };

    if (!body || !body.trim()) {
      const curLang = (window.haichainI18n && typeof window.haichainI18n.current === 'function')
        ? window.haichainI18n.current()
        : (window.haichainI18n?.currentLang || 'en');
      body = DEFAULT_EMPTY_NOTICE[curLang] || DEFAULT_EMPTY_NOTICE['en'];
      if (!title) {
        title = curLang === 'vi' ? 'Thông Báo Hệ Thống' : 'HAICHAIN System';
      }
    }

    const lower = (title + ' ' + body).toLowerCase();`;

  if (content.includes(oldCode)) {
    content = content.replace(oldCode, newCode);
    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Successfully patched', filePath);
  } else {
    console.error('Target oldCode not found in', filePath);
  }
}

patchDialog('dialog.js');
patchDialog('app/dialog.js');
