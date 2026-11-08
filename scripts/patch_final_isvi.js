const fs = require('fs');

const MM_KEYS = {
  kk: {
    metaMaskNotDetected: "Браузеріңізде MetaMask кеңейтімі табылмады.",
    checkingMetaMaskBalance: "MetaMask балансы тексерілуде...",
    approveInMetaMaskPopup: "MetaMask терезесінде растаңыз...",
    metaMaskDepositSuccess: "MetaMask Салымы Сәтті Расталды",
    depositCanceledMetaMask: "Салым тоқтатылды: MetaMask-та қол қоюдан бас тарттыңыз.",
    metaMaskError: "MetaMask қатесі:"
  },
  en: {
    metaMaskNotDetected: "MetaMask extension not detected in your browser.",
    checkingMetaMaskBalance: "Checking MetaMask balance...",
    approveInMetaMaskPopup: "Approve in MetaMask popup...",
    metaMaskDepositSuccess: "MetaMask Deposit Confirmed",
    depositCanceledMetaMask: "Deposit Canceled: You rejected the signature in MetaMask.",
    metaMaskError: "MetaMask error:"
  },
  zh: {
    metaMaskNotDetected: "未在您的浏览器中检测到 MetaMask 插件。",
    checkingMetaMaskBalance: "正在检查 MetaMask 余额...",
    approveInMetaMaskPopup: "请在 MetaMask 弹窗中完成授权...",
    metaMaskDepositSuccess: "MetaMask 充值确认成功",
    depositCanceledMetaMask: "充值已取消：您在 MetaMask 中拒绝了交易签名。",
    metaMaskError: "MetaMask 错误："
  },
  vi: {
    metaMaskNotDetected: "Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn.",
    checkingMetaMaskBalance: "Đang kiểm tra số dư ví MetaMask...",
    approveInMetaMaskPopup: "Chờ bạn duyệt trên MetaMask...",
    metaMaskDepositSuccess: "Nạp MetaMask Thành Công",
    depositCanceledMetaMask: "Giao dịch đã hủy: Bạn đã từ chối duyệt giao dịch trên ví MetaMask.",
    metaMaskError: "Lỗi giao dịch MetaMask:"
  },
  ko: {
    metaMaskNotDetected: "브라우저에서 MetaMask 확장 프로그램이 감지되지 않았습니다.",
    checkingMetaMaskBalance: "MetaMask 잔액 확인 중...",
    approveInMetaMaskPopup: "MetaMask 팝업에서 승인하세요...",
    metaMaskDepositSuccess: "MetaMask 입금 확인 완료",
    depositCanceledMetaMask: "입금 취소: MetaMask 서명을 거부했습니다.",
    metaMaskError: "MetaMask 오류:"
  },
  fr: {
    metaMaskNotDetected: "Extension MetaMask non détectée dans votre navigateur.",
    checkingMetaMaskBalance: "Vérification du solde MetaMask...",
    approveInMetaMaskPopup: "Approuvez dans la fenêtre MetaMask...",
    metaMaskDepositSuccess: "Dépôt MetaMask Confirmé",
    depositCanceledMetaMask: "Dépôt annulé : signature MetaMask rejetée.",
    metaMaskError: "Erreur MetaMask :"
  },
  es: {
    metaMaskNotDetected: "No se detectó la extensión de MetaMask en su navegador.",
    checkingMetaMaskBalance: "Comprobando saldo de MetaMask...",
    approveInMetaMaskPopup: "Apruebe en la ventana de MetaMask...",
    metaMaskDepositSuccess: "Depósito de MetaMask Confirmado",
    depositCanceledMetaMask: "Depósito cancelado: Rechazó la firma en MetaMask.",
    metaMaskError: "Error de MetaMask:"
  },
  ru: {
    metaMaskNotDetected: "Расширение MetaMask не обнаружено в вашем браузере.",
    checkingMetaMaskBalance: "Проверка баланса MetaMask...",
    approveInMetaMaskPopup: "Подтвердите во всплывающем окне MetaMask...",
    metaMaskDepositSuccess: "Пополнение через MetaMask Подтверждено",
    depositCanceledMetaMask: "Пополнение отменено: Вы отклонили подпись в MetaMask.",
    metaMaskError: "Ошибка MetaMask:"
  },
  hi: {
    metaMaskNotDetected: "आपके ब्राउज़र में MetaMask एक्सटेंशन नहीं मिला।",
    checkingMetaMaskBalance: "MetaMask शेष की जांच की जा रही है...",
    approveInMetaMaskPopup: "MetaMask पॉपअप में स्वीकृत करें...",
    metaMaskDepositSuccess: "MetaMask जमा की पुष्टि हुई",
    depositCanceledMetaMask: "जमा रद्द: आपने MetaMask में हस्ताक्षर अस्वीकार कर दिया।",
    metaMaskError: "MetaMask त्रुटि:"
  },
  he: {
    metaMaskNotDetected: "תוסף MetaMask לא זוהה בדפדפן שלך.",
    checkingMetaMaskBalance: "בודק יתרת MetaMask...",
    approveInMetaMaskPopup: "אשר בחלון הקופץ של MetaMask...",
    metaMaskDepositSuccess: "הפקדת MetaMask אושרה",
    depositCanceledMetaMask: "ההפקדה בוטלה: דחית את החתימה ב-MetaMask.",
    metaMaskError: "שגיאת MetaMask:"
  }
};

function patchFinal(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Inject mm keys into DASH_NOTICES_I18N
  for (const [lang, map] of Object.entries(MM_KEYS)) {
    const langToken = `"${lang}": {`;
    const idx = html.indexOf(langToken);
    if (idx !== -1) {
      let inject = '\n';
      for (const [k, v] of Object.entries(map)) {
        inject += `      "${k}": ${JSON.stringify(v)},\n`;
      }
      const insertPoint = idx + langToken.length;
      html = html.substring(0, insertPoint) + inject + html.substring(insertPoint);
    }
  }

  // Replace remaining 8 lines
  html = html.replace(/message: isVi \? 'Vui lòng kết nối ví Passkey hoặc Phantom trước khi nạp tiền\.' : 'Please connect a wallet before depositing\.',/g,
    `message: getDashNotice('connectWalletBeforeDeposit'),`);

  html = html.replace(/alert\(isVi \? "Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn\." : "MetaMask extension not detected in your browser\."\);/g,
    `alert(getDashNotice('metaMaskNotDetected'));`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi \? "Đang kiểm tra số dư ví MetaMask\.\.\." : "Checking MetaMask balance\.\.\.";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('checkingMetaMaskBalance');`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi \? "Chờ bạn duyệt trên MetaMask\.\.\." : "Approve in MetaMask popup\.\.\.";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('approveInMetaMaskPopup');`);

  html = html.replace(/title: isVi \? 'Nạp MetaMask Thành Công' : 'MetaMask Deposit Confirmed',/g,
    `title: getDashNotice('metaMaskDepositSuccess'),`);

  html = html.replace(/alert\(isVi \? "Giao dịch đã hủy: Bạn đã từ chối duyệt giao dịch trên ví MetaMask\." : "Deposit Canceled: You rejected the signature in MetaMask\."\);/g,
    `alert(getDashNotice('depositCanceledMetaMask'));`);

  html = html.replace(/alert\(isVi \? `Lỗi giao dịch MetaMask: \$\{mmErr\.message \|\| mmErr\}` : `MetaMask error: \$\{mmErr\.message \|\| mmErr\}`\);/g,
    `alert(getDashNotice('metaMaskError') + ' ' + (mmErr.message || mmErr));`);

  html = html.replace(/title: isVi \? 'Yêu cầu kết nối ví' : 'Wallet Required',/g,
    `title: getDashNotice('walletNotConnected'),`);

  fs.writeFileSync(filePath, html, 'utf8');
  console.log('Final patch applied to:', filePath);
}

patchFinal('dashboard.html');
patchFinal('app/dashboard.html');
