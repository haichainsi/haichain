const fs = require('fs');

['sale-controller.js', 'app/sale-controller.js'].forEach(filePath => {
  if (!fs.existsSync(filePath)) return;
  let code = fs.readFileSync(filePath, 'utf8');

  // 1. Replace the Card 3 HTML template
  const targetCard3 = `<div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-l1-value">$142,857</div>
                <span class="text-[9px] text-neutral-500 font-medium block">142x Multiple</span>`;
  const replaceCard3 = `<div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-l1-value">28.5M Ticks</div>
                <span class="text-[9px] text-neutral-500 font-medium block" id="calc-l1-subtext">\${getI18nText('projectedMultiple')}</span>`;
  
  if (code.includes(targetCard3)) {
    code = code.replace(targetCard3, replaceCard3);
    console.log(`[${filePath}] Updated Card 3 HTML.`);
  } else {
    console.warn(`[${filePath}] targetCard3 not found.`);
  }

  // 2. Replace the calculation in updateCalculations
  const targetCalc = `      const tgeValue = (totalTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
      const l1Value = (totalTokens * 1.00).toLocaleString('en-US', { style: 'currency', currency: 'USD' });

      totalHaiEl.textContent = totalTokens.toLocaleString('en-US');
      tgeValEl.textContent = tgeValue;
      l1ValEl.textContent = l1Value;`;

  const replaceCalc = `      const tgeValue = (totalTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
      const executionCapacity = Math.round(totalTokens * 200);
      const executionText = executionCapacity >= 1000000 
        ? (executionCapacity / 1000000).toFixed(1) + 'M Ticks' 
        : executionCapacity.toLocaleString('en-US') + ' Ticks';

      totalHaiEl.textContent = totalTokens.toLocaleString('en-US');
      tgeValEl.textContent = tgeValue;
      l1ValEl.textContent = executionText;
      const l1SubEl = container.querySelector('#calc-l1-subtext');
      if (l1SubEl) l1SubEl.textContent = getI18nText('projectedMultiple');`;

  if (code.includes(targetCalc)) {
    code = code.replace(targetCalc, replaceCalc);
    console.log(`[${filePath}] Updated Calculation logic.`);
  } else {
    console.warn(`[${filePath}] targetCalc not found.`);
  }

  fs.writeFileSync(filePath, code, 'utf8');
});
