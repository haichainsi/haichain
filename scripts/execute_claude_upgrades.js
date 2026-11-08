const fs = require('fs');
const path = require('path');

console.log('=== HAICHAIN INSTITUTIONAL UPGRADE SCRIPT ===');

// 1. UPDATE sale-controller.js
function updateSaleController(filePath) {
  if (!fs.existsSync(filePath)) {
    console.warn(`File ${filePath} not found, skipping.`);
    return;
  }
  let code = fs.readFileSync(filePath, 'utf8');

  // Replace i18n dictionary entries
  const dictReplacements = [
    // en
    { from: "l1ValueTitle: 'L1 Sovereign ($1.00)',", to: "l1ValueTitle: 'Micro-Tx Capacity'," },
    { from: "projectedMultiple: '142x Projected Multiple',", to: "projectedMultiple: '~200 Ticks / $HAISI Gas Capacity'," },
    // vi
    { from: "l1ValueTitle: 'Định Giá L1 Sovereign ($1.00)',", to: "l1ValueTitle: 'Hạn Ngạch Giao Dịch Agent'," },
    { from: "projectedMultiple: 'Kỳ Vọng x142 Lần',", to: "projectedMultiple: '~200 Giao Dịch Vi Mô / $HAISI'," },
    // zh
    { from: "l1ValueTitle: '主链 Sovereign 预期 ($1.00)',", to: "l1ValueTitle: '智能体执行配额'," },
    { from: "projectedMultiple: '预期 142 倍',", to: "projectedMultiple: '约 200 次微交易 / $HAISI 算力'," },
    // ko
    { from: "l1ValueTitle: 'Sovereign L1 목표 ($1.00)',", to: "l1ValueTitle: '에이전트 실행 한도'," },
    { from: "projectedMultiple: '142배 예상 수익',", to: "projectedMultiple: '$HAISI당 약 200회 마이크로 결제'," },
    // fr
    { from: "l1ValueTitle: 'Objectif L1 Souverain (1,00 $)',", to: "l1ValueTitle: 'Capacité de Micro-Tx'," },
    { from: "projectedMultiple: 'Multiplicateur 142x',", to: "projectedMultiple: '~200 Ticks / Puissance Gas $HAISI'," },
    // es
    { from: "l1ValueTitle: 'Proyección L1 Soberano ($1.00)',", to: "l1ValueTitle: 'Capacidad de Micro-Tx'," },
    { from: "projectedMultiple: 'Múltiplo Proyectado 142x',", to: "projectedMultiple: '~200 Ticks / Potencia Gas $HAISI'," },
    // ru
    { from: "l1ValueTitle: 'Цель L1 Sovereign ($1.00)',", to: "l1ValueTitle: 'Квота Микро-Транзакций'," },
    { from: "projectedMultiple: 'Ожидаемый Мультипликатор 142x',", to: "projectedMultiple: '~200 Тиков / Газ $HAISI'," },
    // hi
    { from: "l1ValueTitle: 'L1 सोवरेन लक्ष्य ($1.00)',", to: "l1ValueTitle: 'माइक्रो-लेनदेन क्षमता'," },
    { from: "projectedMultiple: '142x अनुमानित रिटर्न',", to: "projectedMultiple: '~200 टिक्स / $HAISI गैस क्षमता'," },
    // he
    { from: "l1ValueTitle: 'יעד L1 ריבוני (1.00$)',", to: "l1ValueTitle: 'מכסת מיקרו-עסקאות'," },
    { from: "projectedMultiple: 'מכפיל חזוי פי 142',", to: "projectedMultiple: '~200 עסקאות / כוח גז $HAISI'," },
    // kk
    { from: "l1ValueTitle: 'Sovereign L1 Мақсаты ($1.00)',", to: "l1ValueTitle: 'Микро-Транзакция Сыйымдылығы'," },
    { from: "projectedMultiple: 'Болжамды Мультипликатор 142x',", to: "projectedMultiple: '~200 Тик / $HAISI Газ Қуаты'," }
  ];

  dictReplacements.forEach(({ from, to }) => {
    if (code.includes(from)) {
      code = code.replace(from, to);
    }
  });

  // Replace Card 3 HTML template
  const oldCard3Html = `<div class="col-span-2 sm:col-span-1 p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">\${getI18nText('l1ValueTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-l1-value">$142,857</div>
                <span class="text-[9px] text-neutral-500 font-medium block">142x Multiple</span>
              </div>`;

  const newCard3Html = `<div class="col-span-2 sm:col-span-1 p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">\${getI18nText('l1ValueTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-l1-value">28.5M Ticks</div>
                <span class="text-[9px] text-neutral-500 font-medium block" id="calc-l1-subtext">\${getI18nText('projectedMultiple')}</span>
              </div>`;

  if (code.includes(oldCard3Html)) {
    code = code.replace(oldCard3Html, newCard3Html);
    console.log(`[${filePath}] Updated Card 3 HTML.`);
  }

  // Replace Calculator updateCalculations logic
  const oldCalcLogic = `      const tgeValue = (totalTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
      const l1Value = (totalTokens * 1.00).toLocaleString('en-US', { style: 'currency', currency: 'USD' });

      totalHaiEl.textContent = totalTokens.toLocaleString('en-US');
      tgeValEl.textContent = tgeValue;
      l1ValEl.textContent = l1Value;`;

  const newCalcLogic = `      const tgeValue = (totalTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
      const executionCapacity = Math.round(totalTokens * 200);
      const executionText = executionCapacity >= 1000000 
        ? (executionCapacity / 1000000).toFixed(1) + 'M Ticks' 
        : executionCapacity.toLocaleString('en-US') + ' Ticks';

      totalHaiEl.textContent = totalTokens.toLocaleString('en-US');
      tgeValEl.textContent = tgeValue;
      l1ValEl.textContent = executionText;
      const l1SubEl = container.querySelector('#calc-l1-subtext');
      if (l1SubEl) l1SubEl.textContent = getI18nText('projectedMultiple');`;

  if (code.includes(oldCalcLogic)) {
    code = code.replace(oldCalcLogic, newCalcLogic);
    console.log(`[${filePath}] Updated Calculator logic.`);
  }

  fs.writeFileSync(filePath, code, 'utf8');
  console.log(`Successfully updated ${filePath}`);
}

updateSaleController('sale-controller.js');
updateSaleController('app/sale-controller.js');
