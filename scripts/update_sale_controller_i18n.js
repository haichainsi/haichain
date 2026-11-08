const fs = require('fs');

const extraKeys = {
  en: {
    vestingCliffCard: '2. Cliff (2 Months)',
    vestingCliffDesc: '0% Unlock (Anti-dump)',
    vestingLinearCard: '3. Linear (6 Months)',
    autofillPhantom: 'Auto-fill Phantom',
    saftDocTitle: 'HAICHAIN Pre-Seed SAFT Agreement (Standard English Edition)',
    memoDocTitle: 'HAICHAIN Pre-Seed 1-Pager Memo',
    saftAlertTitle: 'SAFT SUBSCRIPTION & TOKEN-2022 ALLOCATION RECORDED!',
    saftAlertInvestor: 'Investor',
    saftAlertAlloc: 'Allocation',
    saftAlertAmount: 'Amount',
    saftAlertWallet: 'Solana Wallet',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Active for your Phantom wallet',
    saftAlertSchedule: '✓ Vesting Schedule: 20% TGE, 2-Mo Cliff, 6-Mo Linear Stream',
    saftAlertTransferPrompt: 'Please transfer funds to the Multi-Sig Treasury:',
    saftAlertRedirect: 'Redirecting to your dedicated Vesting Vault tab.'
  },
  vi: {
    vestingCliffCard: '2. Cliff (2 Tháng)',
    vestingCliffDesc: 'Khóa 0% (Anti-dump)',
    vestingLinearCard: '3. Tuyến Tính (6 Tháng)',
    autofillPhantom: 'Lấy ví Phantom',
    saftDocTitle: 'Hợp Đồng SAFT Pre-Seed HAICHAIN (Standard English Edition)',
    memoDocTitle: 'Bản Tóm Tắt 1 Trang Pre-Seed HAICHAIN',
    saftAlertTitle: 'ĐÃ GHI NHẬN ĐĂNG KÝ SAFT VÀ PHÂN BỔ TOKEN-2022!',
    saftAlertInvestor: 'Nhà đầu tư',
    saftAlertAlloc: 'Phân bổ',
    saftAlertAmount: 'Giá trị',
    saftAlertWallet: 'Ví thụ hưởng',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Đã kích hoạt cho ví Phantom của bạn',
    saftAlertSchedule: '✓ Lịch Vesting: 20% TGE, Cliff 2 tháng, Linear Stream 6 tháng',
    saftAlertTransferPrompt: 'Vui lòng chuyển USDT/SOL vào Ví Kho Bạc Multi-Sig:',
    saftAlertRedirect: 'Hệ thống sẽ tự động chuyển bạn đến Két Vesting để kiểm tra số dư.'
  },
  zh: {
    vestingCliffCard: '2. 锁仓期 (2个月)',
    vestingCliffDesc: '0% 解锁 (防止抛售)',
    vestingLinearCard: '3. 线性释放 (6个月)',
    autofillPhantom: '自动填充 Phantom 钱包',
    saftDocTitle: 'HAICHAIN 种子轮 SAFT 协议 (标准英文版)',
    memoDocTitle: 'HAICHAIN 种子轮单页备忘录',
    saftAlertTitle: 'SAFT 认购与 Token-2022 份额已成功记录！',
    saftAlertInvestor: '投资者',
    saftAlertAlloc: '分配份额',
    saftAlertAmount: '金额',
    saftAlertWallet: '接收钱包',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: 已为您的 Phantom 钱包激活',
    saftAlertSchedule: '✓ 释放计划: 20% TGE, 2个月锁仓, 6个月线性流式释放',
    saftAlertTransferPrompt: '请将款项转入多签国库金库地址：',
    saftAlertRedirect: '正在自动跳转至您的专属 Vesting 金库页面。'
  },
  ko: {
    vestingCliffCard: '2. 클리프 (2개월)',
    vestingCliffDesc: '0% 락업 (덤핑 방지)',
    vestingLinearCard: '3. 선형 스트리밍 (6개월)',
    autofillPhantom: 'Phantom 지갑 자동 입력',
    saftDocTitle: 'HAICHAIN 프리시드 SAFT 계약서 (표준 영문판)',
    memoDocTitle: 'HAICHAIN 프리시드 1페이지 요약',
    saftAlertTitle: 'SAFT 청약 및 Token-2022 배분이 등록되었습니다!',
    saftAlertInvestor: '투자자',
    saftAlertAlloc: '배분 수량',
    saftAlertAmount: '청약 금액',
    saftAlertWallet: '수령 지갑',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Phantom 지갑에 활성화됨',
    saftAlertSchedule: '✓ 베스팅 일정: TGE 20%, 2개월 클리프, 6개월 선형 스트리밍',
    saftAlertTransferPrompt: '멀티시그 금고 주소로 자금을 전송해 주세요:',
    saftAlertRedirect: '전용 베스팅 볼트 탭으로 이동합니다.'
  },
  fr: {
    vestingCliffCard: '2. Cliff (2 Mois)',
    vestingCliffDesc: '0% Déblocage (Anti-dump)',
    vestingLinearCard: '3. Linéaire (6 Mois)',
    autofillPhantom: 'Remplissage auto Phantom',
    saftDocTitle: 'Accord SAFT Pre-Seed HAICHAIN (Édition Anglaise Standard)',
    memoDocTitle: 'Mémo 1 Page Pre-Seed HAICHAIN',
    saftAlertTitle: 'SOUSCRIPTION SAFT ET ALLOCATION TOKEN-2022 ENREGISTRÉES !',
    saftAlertInvestor: 'Investisseur',
    saftAlertAlloc: 'Allocation',
    saftAlertAmount: 'Montant',
    saftAlertWallet: 'Portefeuille Solana',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook : Actif pour votre portefeuille Phantom',
    saftAlertSchedule: '✓ Calendrier de vesting : 20% TGE, Cliff 2 mois, Flux linéaire 6 mois',
    saftAlertTransferPrompt: 'Veuillez transférer les fonds vers la Trésorerie Multi-Sig :',
    saftAlertRedirect: 'Redirection vers votre coffre-fort de vesting.'
  },
  es: {
    vestingCliffCard: '2. Cliff (2 Meses)',
    vestingCliffDesc: '0% Desbloqueo (Anti-dump)',
    vestingLinearCard: '3. Lineal (6 Meses)',
    autofillPhantom: 'Autocompletar Phantom',
    saftDocTitle: 'Acuerdo SAFT Pre-Seed HAICHAIN (Edición Estándar en Inglés)',
    memoDocTitle: 'Memorando de 1 Página Pre-Seed HAICHAIN',
    saftAlertTitle: '¡SUSCRIPCIÓN SAFT Y ASIGNACIÓN TOKEN-2022 REGISTRADAS!',
    saftAlertInvestor: 'Inversionista',
    saftAlertAlloc: 'Asignación',
    saftAlertAmount: 'Monto',
    saftAlertWallet: 'Billetera Solana',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Activo para su billetera Phantom',
    saftAlertSchedule: '✓ Calendario de vesting: 20% TGE, Cliff 2 meses, Transmisión lineal 6 meses',
    saftAlertTransferPrompt: 'Por favor transfiera los fondos a la Tesorería Multi-Sig:',
    saftAlertRedirect: 'Redirigiendo a su bóveda de vesting dedicada.'
  },
  ru: {
    vestingCliffCard: '2. Клифф (2 Месяца)',
    vestingCliffDesc: '0% Разблокировки (Анти-дамп)',
    vestingLinearCard: '3. Линейный (6 Месяцев)',
    autofillPhantom: 'Автозаполнение Phantom',
    saftDocTitle: 'Соглашение SAFT Pre-Seed HAICHAIN (Стандартная англ. версия)',
    memoDocTitle: '1-страничный меморандум Pre-Seed HAICHAIN',
    saftAlertTitle: 'ПОДПИСКА SAFT И АЛЛОКАЦИЯ TOKEN-2022 УСПЕШНО ЗАРЕГИСТРИРОВАНЫ!',
    saftAlertInvestor: 'Инвестор',
    saftAlertAlloc: 'Аллокация',
    saftAlertAmount: 'Сумма',
    saftAlertWallet: 'Solana Кошелек',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Активен для вашего Phantom кошелька',
    saftAlertSchedule: '✓ График вестинга: 20% TGE, 2 мес. клифф, 6 мес. линейный стриминг',
    saftAlertTransferPrompt: 'Пожалуйста, переведите средства в Мультисиг Казначейство:',
    saftAlertRedirect: 'Перенаправление в ваш персональный сейф вестинга.'
  },
  hi: {
    vestingCliffCard: '2. क्लिफ (2 महीने)',
    vestingCliffDesc: '0% अनलॉक (डंप सुरक्षा)',
    vestingLinearCard: '3. लीनियर (6 महीने)',
    autofillPhantom: 'Phantom वॉलेट ऑटो-फिल',
    saftDocTitle: 'HAICHAIN प्री-सीड SAFT समझौता (मानक अंग्रेजी संस्करण)',
    memoDocTitle: 'HAICHAIN प्री-सीड 1-पेज मेमो',
    saftAlertTitle: 'SAFT सदस्यता और Token-2022 आवंटन दर्ज किया गया!',
    saftAlertInvestor: 'निवेशक',
    saftAlertAlloc: 'आवंटन',
    saftAlertAmount: 'राशि',
    saftAlertWallet: 'Solana वॉलेट',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: आपके Phantom वॉलेट के लिए सक्रिय',
    saftAlertSchedule: '✓ वेस्टिंग शेड्यूल: 20% TGE, 2 महीने क्लिफ, 6 महीने लीनियर स्ट्रीम',
    saftAlertTransferPrompt: 'कृपया मल्टी-सिग ट्रेजरी में धनराशि ट्रांसफर करें:',
    saftAlertRedirect: 'आपके वेस्टिंग वॉल्ट टैब पर पुनर्निर्देशित किया जा रहा है।'
  },
  he: {
    vestingCliffCard: '2. תקופת נעילה (חודשיים)',
    vestingCliffDesc: '0% שחרור (הגנה ממכירה)',
    vestingLinearCard: '3. שחרור ליניארי (6 חודשים)',
    autofillPhantom: 'מילוי אוטומטי Phantom',
    saftDocTitle: 'הסכם SAFT Pre-Seed של HAICHAIN (מהדורה רשמית באנגלית)',
    memoDocTitle: 'תזכיר עמוד אחד Pre-Seed של HAICHAIN',
    saftAlertTitle: 'הרשמת SAFT והקצאת Token-2022 נרשמו בהצלחה!',
    saftAlertInvestor: 'משקיע',
    saftAlertAlloc: 'הקצאה',
    saftAlertAmount: 'סכום',
    saftAlertWallet: 'ארנק Solana',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: פעיל עבור ארנק Phantom שלך',
    saftAlertSchedule: '✓ לוח זמנים: 20% TGE, נעילה של חודשיים, הזרמה ליניארית של 6 חודשים',
    saftAlertTransferPrompt: 'אנא העבר את הכספים לקופת האוצר:',
    saftAlertRedirect: 'מעביר אותך לכרטיסיית כספת הווסטינג שלך.'
  },
  kk: {
    vestingCliffCard: '2. Клифф (2 Ай)',
    vestingCliffDesc: '0% Ашу (Анти-дамп)',
    vestingLinearCard: '3. Сызықты (6 Ай)',
    autofillPhantom: 'Phantom әмиянын автотолтыру',
    saftDocTitle: 'HAICHAIN Pre-Seed SAFT Келісімі (Стандартты ағылшын басылымы)',
    memoDocTitle: 'HAICHAIN Pre-Seed 1-Беттік Мемосы',
    saftAlertTitle: 'SAFT ЖАЗЫЛУЫ ЖӘНЕ TOKEN-2022 БӨЛІНІСІ СӘТТІ ТІРКЕЛДІ!',
    saftAlertInvestor: 'Инвестор',
    saftAlertAlloc: 'Бөлініс',
    saftAlertAmount: 'Сомасы',
    saftAlertWallet: 'Solana Әмияны',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Phantom әмияныңыз үшін белсенді',
    saftAlertSchedule: '✓ Вестинг кестесі: 20% TGE, 2 айлық клифф, 6 айлық сызықты стриминг',
    saftAlertTransferPrompt: 'Қаражатты Multi-Sig Қазынашылығына аударыңыз:',
    saftAlertRedirect: 'Жеке вестинг сейфі қойындысына бағытталуда.'
  }
};

function patchFile(filePath) {
  let code = fs.readFileSync(filePath, 'utf8');

  // 1. Inject extra keys into SALE_I18N for each language
  for (const lang of Object.keys(extraKeys)) {
    const langToken = `  ${lang}: {`;
    const idx = code.indexOf(langToken);
    if (idx !== -1) {
      // Find insertion point right after `  ${lang}: {`
      const insertIdx = idx + langToken.length;
      let injectStr = '\n';
      for (const [k, v] of Object.entries(extraKeys[lang])) {
        // Only if key not already present in that block
        const escapedVal = v.replace(/'/g, "\\'");
        injectStr += `    ${k}: '${escapedVal}',\n`;
      }
      code = code.substring(0, insertIdx) + injectStr + code.substring(insertIdx);
    }
  }

  // 2. Replace hardcoded cards in renderPrivateSaleView
  const oldCliffBlock = `<div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                    <span class="text-neutral-400 text-[10px] block">2. Cliff (2 Tháng)</span>
                    <span class="text-neutral-500 font-medium">Khóa 0% (Anti-dump)</span>
                  </div>
                  <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                    <span class="text-neutral-400 text-[10px] block">3. Linear (6 Tháng)</span>
                    <strong class="text-black dark:text-white font-bold" id="calc-stream-tokens">114,286 $HAISI</strong>
                  </div>`;

  const newCliffBlock = `<div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                    <span class="text-neutral-400 text-[10px] block" id="calc-step2-title">${'${getI18nText(\'vestingCliffCard\')}'}</span>
                    <span class="text-neutral-500 font-medium" id="calc-step2-desc">${'${getI18nText(\'vestingCliffDesc\')}'}</span>
                  </div>
                  <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                    <span class="text-neutral-400 text-[10px] block" id="calc-step3-title">${'${getI18nText(\'vestingLinearCard\')}'}</span>
                    <strong class="text-black dark:text-white font-bold" id="calc-stream-tokens">114,286 $HAISI</strong>
                  </div>`;

  if (code.includes('2. Cliff (2 Tháng)')) {
    // Regex or string replace
    code = code.replace(/<span class="text-neutral-400 text-\[10px\] block">2\. Cliff \(2 Th[^<]*\)<\/span>\s*<span class="text-neutral-500 font-medium">Kh[^<]*\(Anti-dump\)<\/span>/g, 
      `<span class="text-neutral-400 text-[10px] block" id="calc-step2-title">\${getI18nText('vestingCliffCard')}</span>\n                    <span class="text-neutral-500 font-medium" id="calc-step2-desc">\${getI18nText('vestingCliffDesc')}</span>`);
    code = code.replace(/<span class="text-neutral-400 text-\[10px\] block">3\. Linear \(6 Th[^<]*\)<\/span>/g,
      `<span class="text-neutral-400 text-[10px] block" id="calc-step3-title">\${getI18nText('vestingLinearCard')}</span>`);
  }

  // 3. Replace autofill text
  code = code.replace(/<span>\$\{getActiveLang\(\) === 'vi' \? 'L[^']*' : 'Auto-fill Phantom'\}<\/span>/g,
    `<span id="calc-autofill-text">\${getI18nText('autofillPhantom')}</span>`);

  // 4. In updateLanguage(), dynamically update these elements
  const updateLangTarget = `const mobileTitleEl = document.getElementById('mobile-sale-title');
    if (mobileTitleEl) mobileTitleEl.textContent = getI18nText('mobileNav');`;
  
  const updateLangInject = `const mobileTitleEl = document.getElementById('mobile-sale-title');
    if (mobileTitleEl) mobileTitleEl.textContent = getI18nText('mobileNav');
    const s2Title = document.getElementById('calc-step2-title');
    if (s2Title) s2Title.textContent = getI18nText('vestingCliffCard');
    const s2Desc = document.getElementById('calc-step2-desc');
    if (s2Desc) s2Desc.textContent = getI18nText('vestingCliffDesc');
    const s3Title = document.getElementById('calc-step3-title');
    if (s3Title) s3Title.textContent = getI18nText('vestingLinearCard');
    const autoFillSpan = document.getElementById('calc-autofill-text');
    if (autoFillSpan) autoFillSpan.textContent = getI18nText('autofillPhantom');`;

  code = code.replace(updateLangTarget, updateLangInject);

  // 5. Replace PDF open titles
  code = code.replace(/const title = getActiveLang\(\) === 'vi'\s*\?[^;]+;/g, 
    `const title = getI18nText('saftDocTitle');`);
  
  // 6. Replace SAFT alert with localized version
  const oldAlertRegex = /const msg = getActiveLang\(\) === 'vi'[\s\S]*?alert\(msg\);/;
  const newAlertCode = `const msg = \`\${getI18nText('saftAlertTitle')}\\n\\n\${getI18nText('saftAlertInvestor')}: \${name}\\n\${getI18nText('saftAlertAlloc')}: \${totalHai} \\$HAISI\\n\${getI18nText('saftAlertAmount')}: \\$\${amount} USDT\\n\${getI18nText('saftAlertWallet')}: \${wallet}\\n\\n\${getI18nText('saftAlertHookActive')}\\n\${getI18nText('saftAlertSchedule')}\\n\\n\${getI18nText('saftAlertTransferPrompt')}\\n\${window.HAICHAIN_SALE_CONFIG.TREASURY_ADDRESS}\\n\\n\${getI18nText('saftAlertRedirect')}\`;
        alert(msg);`;
  code = code.replace(oldAlertRegex, newAlertCode);

  fs.writeFileSync(filePath, code, 'utf8');
  console.log('Successfully updated:', filePath);
}

patchFile('sale-controller.js');
patchFile('app/sale-controller.js');
