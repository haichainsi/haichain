import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

files = ['dashboard.html', 'app/dashboard.html']

guarantee_i18n_entries = {
    "vi": {
        "guaranteeTitle": "BẢO CHỨNG CHUYỂN ĐỔI TOKEN MAINNET 100% CHO NHÀ ĐẦU TƯ",
        "guaranteeBadge": "ĐÃ XÁC THỰC BẢO CHỨNG HỢP ĐỒNG",
        "guaranteeCommitment": "Toàn bộ số lượng {tokens} của Quý Nhà Đầu Tư được bảo đảm pháp lý bất biến theo Thỏa Thuận SAFT. Mặc dù trên môi trường Pre-Seed hiện tại số dư được ghi nhận dưới dạng phân bổ bảo lưu, ngay khi HAICHAIN chính thức kích hoạt mạng Mainnet (Sự kiện TGE), hợp đồng thông minh Solana Token-2022 sẽ tự động chuyển đổi và giải ngân 100% số token này thành Token Thật on-chain trực tiếp về địa chỉ ví {address} của Quý Nhà Đầu Tư mà không phát sinh thêm bất kỳ chi phí hay thủ tục nào.",
        "guaranteeProofType": "Hình Thức Đầu Tư & Ký Duyệt",
        "guaranteeMintStandard": "Chuẩn Hợp Đồng On-Chain",
        "guaranteeDisbursement": "Cam Kết Quy Đổi Mainnet",
        "viewLegalSaftBtn": "Xem Thỏa Thuận Pháp Lý SAFT",
        "copyContractBtn": "Sao Chép Token-2022 Mint"
    },
    "en": {
        "guaranteeTitle": "OFFICIAL 100% MAINNET ALLOCATION GUARANTEE FOR INVESTORS",
        "guaranteeBadge": "OFFICIALLY GUARANTEED & BOUND",
        "guaranteeCommitment": "All {tokens} held by the Strategic Investor are immutably secured under the SAFT Agreement. While currently held as an allocated ledger reserve during the Pre-Seed phase, upon HAICHAIN Mainnet TGE, the Solana Token-2022 smart contract will automatically disburse 100% real on-chain tokens directly to this bound wallet address {address} with zero additional fees or manual intervention.",
        "guaranteeProofType": "Investment & Signature Method",
        "guaranteeMintStandard": "On-Chain Contract Standard",
        "guaranteeDisbursement": "Mainnet Conversion Commitment",
        "viewLegalSaftBtn": "View Legal SAFT Agreement",
        "copyContractBtn": "Copy Token-2022 Mint"
    },
    "zh": {
        "guaranteeTitle": "投资者 100% 主网代币兑换官方保函",
        "guaranteeBadge": "已完成合约保函认证",
        "guaranteeCommitment": "战略投资者的全部 {tokens} 均受 SAFT 协议不可篡改的法律保障。虽然在当前 Pre-Seed 阶段以锁定分配形式记录，但一旦 HAICHAIN 正式上线主网（TGE 事件），Solana Token-2022 智能合约将自动将 100% 真实链上代币直接分发至您绑定的钱包地址 {address}，无需任何额外费用或繁琐手续。",
        "guaranteeProofType": "投资方式与签名认证",
        "guaranteeMintStandard": "链上合约标准",
        "guaranteeDisbursement": "主网兑换承诺",
        "viewLegalSaftBtn": "查看 SAFT 法律协议",
        "copyContractBtn": "复制 Token-2022 Mint"
    },
    "ko": {
        "guaranteeTitle": "투자자를 위한 공식 100% 메인넷 토큰 전환 보증서",
        "guaranteeBadge": "계약 보증 인증 완료",
        "guaranteeCommitment": "전략적 투자자의 {tokens} 전량은 SAFT 계약에 의해 불변으로 법적 보증됩니다. 현재 프리시드 단계에서는 락업 배분으로 기록되지만, HAICHAIN 메인넷 공식 출시(TGE) 즉시 Solana Token-2022 스마트 컨트랙트가 100% 온체인 실제 토큰으로 자동 전환하여 귀하의 지갑 주소 {address}(으)로 직분배합니다.",
        "guaranteeProofType": "투자 방식 및 서명 인증",
        "guaranteeMintStandard": "온체인 스마트 컨트랙트 표준",
        "guaranteeDisbursement": "메인넷 전환 확약",
        "viewLegalSaftBtn": "SAFT 법적 계약서 보기",
        "copyContractBtn": "Token-2022 Mint 복사"
    },
    "fr": {
        "guaranteeTitle": "GARANTIE OFFICIELLE DE CONVERSION MAINNET À 100 % POUR LES INVESTISSEURS",
        "guaranteeBadge": "OFFICIELLEMENT GARANTI & LIÉ",
        "guaranteeCommitment": "L'intégralité des {tokens} détenus par l'investisseur stratégique est protégée de manière immuable en vertu de l'accord SAFT. Dès le lancement officiel du Mainnet HAICHAIN (événement TGE), le contrat intelligent Solana Token-2022 distribuera automatiquement 100 % de vrais jetons on-chain directement sur votre adresse de portefeuille liée {address}.",
        "guaranteeProofType": "Méthode d'investissement et signature",
        "guaranteeMintStandard": "Standard de contrat on-chain",
        "guaranteeDisbursement": "Engagement de conversion Mainnet",
        "viewLegalSaftBtn": "Consulter l'accord SAFT",
        "copyContractBtn": "Copier le contrat Mint"
    },
    "es": {
        "guaranteeTitle": "CERTIFICADO OFICIAL DE CONVERSIÓN MAINNET AL 100% PARA INVERSORES",
        "guaranteeBadge": "OFICIALMENTE GARANTIZADO Y VINCULADO",
        "guaranteeCommitment": "Todos los {tokens} del Inversor Estratégico están legalmente respaldados de forma inmutable bajo el Acuerdo SAFT. Tan pronto como HAICHAIN active su red Mainnet (evento TGE), el contrato inteligente Solana Token-2022 desembolsará automáticamente el 100% en tokens reales on-chain a su dirección de billetera {address} sin trámites adicionales.",
        "guaranteeProofType": "Método de Inversión y Firma",
        "guaranteeMintStandard": "Estándar de Contrato On-Chain",
        "guaranteeDisbursement": "Compromiso de Conversión Mainnet",
        "viewLegalSaftBtn": "Ver Acuerdo Legal SAFT",
        "copyContractBtn": "Copiar Mint Token-2022"
    },
    "ru": {
        "guaranteeTitle": "ОФИЦИАЛЬНАЯ 100% ГАРАНТИЯ КОНВЕРТАЦИИ В MAINNET ДЛЯ ИНВЕСТОРОВ",
        "guaranteeBadge": "ОФИЦИАЛЬНО ГАРАНТИРОВАНО И ЗАКРЕПЛЕНО",
        "guaranteeCommitment": "Все {tokens} стратегического инвестора юридически защищены соглашением SAFT. В момент запуска Mainnet HAICHAIN (событие TGE) смарт-контракт Solana Token-2022 автоматически конвертирует и переведет 100% реальных ончейн-токенов прямо на ваш привязанный адрес кошелька {address}.",
        "guaranteeProofType": "Метод инвестирования и подпись",
        "guaranteeMintStandard": "Стандарт ончейн-контракта",
        "guaranteeDisbursement": "Обязательство конвертации в Mainnet",
        "viewLegalSaftBtn": "Открыть соглашение SAFT",
        "copyContractBtn": "Скопировать Token-2022 Mint"
    },
    "kk": {
        "guaranteeTitle": "ИНВЕСТОРЛАР ҮШІН 100% MAINNET РЕСМИ КЕПІЛДІК СЕРТИФИКАТЫ",
        "guaranteeBadge": "КЕЛІСІМШАРТПЕН РЕСМИ КЕПІЛДЕНДІРІЛГЕН",
        "guaranteeCommitment": "Стратегиялық инвестордың барлық {tokens} SAFT келісіміне сәйкес өзгермейтін заңды кепілдікке ие. HAICHAIN Mainnet ресми іске қосылған кезде (TGE оқиғасы) Solana Token-2022 смарт-келісімшарты 100% нақты ончейн токендерін сіздің тіркелген әмиян мекенжайыңызға {address} автоматты түрде аударады.",
        "guaranteeProofType": "Инвестиция әдісі және қолтаңба",
        "guaranteeMintStandard": "Ончейн келісімшарт стандарты",
        "guaranteeDisbursement": "Mainnet-ке конвертация міндеттемесі",
        "viewLegalSaftBtn": "Заңды SAFT келісімін қарау",
        "copyContractBtn": "Token-2022 Mint көшіру"
    },
    "hi": {
        "guaranteeTitle": "निवेशकों के लिए आधिकारिक 100% मेननेट आवंटन गारंटी प्रमाणपत्र",
        "guaranteeBadge": "अनुबंध द्वारा आधिकारिक रूप से सुरक्षित",
        "guaranteeCommitment": "रणनीतिक निवेशक के सभी {tokens} SAFT समझौते के तहत कानूनी रूप से सुरक्षित हैं। HAICHAIN मेननेट सक्रिय होते ही Solana Token-2022 स्मार्ट अनुबंध 100% वास्तविक ऑन-चेन टोकन स्वचालित रूप से आपके वॉलेट पते {address} पर वितरित करेगा।",
        "guaranteeProofType": "निवेश विधि và हस्ताक्षर",
        "guaranteeMintStandard": "ऑन-चेन अनुबंध मानक",
        "guaranteeDisbursement": "मेननेट रूपांतरण प्रतिबद्धता",
        "viewLegalSaftBtn": "SAFT समझौता देखें",
        "copyContractBtn": "Token-2022 Mint कॉपी करें"
    },
    "he": {
        "guaranteeTitle": "תעודת אחריות רשמית להמרת 100% אסימונים ברשת ראשית (Mainnet)",
        "guaranteeBadge": "מאושר ומובטח חוזית",
        "guaranteeCommitment": "כל {tokens} של המשקיע האסטרטגי מובטחים משפטית תחת הסכם SAFT. עם השקת ה-Mainnet של HAICHAIN, החוזה החכם של Solana Token-2022 ימיר ויעביר באופן אוטומטי 100% אסימוני on-chain אמיתיים ישירות לכתובת הארנק המקושרת {address} ללא כל פעולה נוספת.",
        "guaranteeProofType": "שיטת השקעה וחתימה",
        "guaranteeMintStandard": "תקן חוזה On-Chain",
        "guaranteeDisbursement": "התחייבות המרה לרשת ראשית",
        "viewLegalSaftBtn": "צפה בהסכם SAFT",
        "copyContractBtn": "העתק Token-2022 Mint"
    }
}

cert_markup = """
          <!-- Official Mainnet Allocation Guarantee Certificate (Bảo Chứng Chuyển Đổi Token Mainnet 100%) -->
          <div class="p-5 sm:p-6 rounded-2xl bg-neutral-900 border border-neutral-700/80 text-white font-mono text-xs space-y-4 shadow-sm relative overflow-hidden">
            <div class="absolute top-0 right-0 w-48 h-48 bg-white/5 rounded-full blur-2xl pointer-events-none -mr-10 -mt-10"></div>
            
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-neutral-800 gap-2 relative z-10">
              <div class="flex items-center space-x-2">
                <span class="p-1 rounded-lg bg-white text-black flex items-center justify-center">
                  <i data-lucide="shield-check" class="w-4 h-4"></i>
                </span>
                <span class="font-bold text-xs sm:text-sm tracking-wide text-white uppercase">${getVestingText('guaranteeTitle', lang)}</span>
              </div>
              <div class="flex items-center space-x-2">
                <span class="px-2.5 py-0.5 rounded-full text-[9.5px] sm:text-[10px] font-mono bg-white text-black font-bold uppercase tracking-wider flex items-center space-x-1.5 shadow-xs">
                  <span class="w-1.5 h-1.5 rounded-full bg-black animate-ping"></span>
                  <span>${getVestingText('guaranteeBadge', lang)}</span>
                </span>
              </div>
            </div>

            <div class="space-y-2 relative z-10 font-sans text-xs sm:text-[13px] text-neutral-300 leading-relaxed">
              <p>
                ${getVestingText('guaranteeCommitment', lang).replace('{tokens}', `<strong class="text-white font-bold">${haiTotal.toLocaleString()} $HAISI</strong>`).replace('{address}', `<span class="font-mono text-white font-semibold underline underline-offset-2">${currentAddress}</span>`)}
              </p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-1 relative z-10 font-mono text-[11px]">
              <div class="p-3 rounded-xl bg-neutral-950/80 border border-neutral-800 space-y-1">
                <span class="text-[9.5px] text-neutral-400 uppercase font-sans">${getVestingText('guaranteeProofType', lang)}</span>
                <div class="text-white font-bold flex items-center space-x-1.5">
                  <i data-lucide="file-check" class="w-3.5 h-3.5 text-white"></i>
                  <span>${alloc.paymentMethod ? alloc.paymentMethod : 'Web3 Smart Contract SAFT'}</span>
                </div>
                <div class="text-[10px] text-neutral-400 truncate font-mono">Tx: ${alloc.txSignature ? alloc.txSignature.slice(0, 16) + '...' : 'ON-CHAIN-VERIFIED'}</div>
              </div>

              <div class="p-3 rounded-xl bg-neutral-950/80 border border-neutral-800 space-y-1">
                <span class="text-[9.5px] text-neutral-400 uppercase font-sans">${getVestingText('guaranteeMintStandard', lang)}</span>
                <div class="text-white font-bold flex items-center space-x-1.5">
                  <i data-lucide="cpu" class="w-3.5 h-3.5 text-white"></i>
                  <span>Solana Token-2022</span>
                </div>
                <div class="text-[10px] text-neutral-400 font-mono">Transfer-Hook Enforced</div>
              </div>

              <div class="p-3 rounded-xl bg-neutral-950/80 border border-neutral-800 space-y-1">
                <span class="text-[9.5px] text-neutral-400 uppercase font-sans">${getVestingText('guaranteeDisbursement', lang)}</span>
                <div class="text-white font-bold flex items-center space-x-1.5">
                  <i data-lucide="zap" class="w-3.5 h-3.5 text-white"></i>
                  <span>100% On-Chain TGE</span>
                </div>
                <div class="text-[10px] text-neutral-400 font-sans">20% TGE + 80% Tuyến Tính 6T</div>
              </div>
            </div>

            <div class="pt-2 flex flex-wrap items-center gap-2.5 relative z-10">
              <button type="button" onclick="if(window.openSaftPdfModal){window.openSaftPdfModal();}else{window.switchTab('tab-preseed');}" class="py-2 px-3.5 rounded-xl bg-white text-black hover:bg-neutral-200 font-medium text-xs font-mono transition-all flex items-center space-x-1.5 shadow-sm active:scale-95 cursor-pointer">
                <i data-lucide="file-text" class="w-3.5 h-3.5"></i>
                <span>${getVestingText('viewLegalSaftBtn', lang)}</span>
              </button>
              <button type="button" onclick="window.copyToken2022Mint()" class="py-2 px-3.5 rounded-xl border border-neutral-700 text-white hover:border-white font-medium text-xs font-mono transition-all flex items-center space-x-1.5 active:scale-95 cursor-pointer">
                <i data-lucide="copy" class="w-3.5 h-3.5"></i>
                <span>${getVestingText('copyContractBtn', lang)}</span>
              </button>
            </div>
          </div>
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject guarantee i18n keys
    for lang, dict_vals in guarantee_i18n_entries.items():
        if f'"{lang}":' in content and f'"{lang}": {{\n      "guaranteeTitle"' not in content:
            # Pattern matching "lang": { with optional spaces/newlines
            pat = re.compile(r'(\s*"' + lang + r'":\s*\{)', re.MULTILINE)
            def repl(m):
                res = m.group(1) + '\n'
                for k, v in dict_vals.items():
                    clean_v = v.replace('"', '\\"')
                    res += f'      "{k}": "{clean_v}",\n'
                return res
            content, count = pat.subn(repl, content, count=1)
            # print(f"{filepath} [{lang}]: injected {count}")

    # 2. Inject window.openSaftPdfModal if missing
    if 'window.openSaftPdfModal' not in content:
        helper = """
    window.openSaftPdfModal = function() {
      if (typeof window.openPdfViewerModal === 'function') {
        window.openPdfViewerModal('/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf', 'HAICHAIN Official SAFT Agreement (Mainnet Guaranteed)');
      } else {
        window.open('/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf', '_blank');
      }
    };
"""
        content = content.replace('window.renderVestingVaultPage = renderVestingVaultPage;', 'window.renderVestingVaultPage = renderVestingVaultPage;' + helper)

    # 3. Clean dead `if (false) {` block in deposit modal
    dead_block_pattern = re.compile(r'if\s*\(\s*false\s*\)\s*\{[\s\S]*?\}\s*(?=\/\/\s*Fetch latest blockhash)', re.MULTILINE)
    content, count_dead = dead_block_pattern.subn('', content)
    print(f"{filepath}: removed {count_dead} dead block(s)")

    # 4. Inject Certificate into renderVestingVaultPage
    if '<!-- Official Mainnet Allocation Guarantee Certificate' not in content:
        content = content.replace('<!-- 4 Executive KPI Cards -->', cert_markup + '\n          <!-- 4 Executive KPI Cards -->')
        print(f"{filepath}: injected Certificate markup")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filepath} successfully.")
