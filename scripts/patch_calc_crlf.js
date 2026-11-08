const fs = require('fs');

['sale-controller.js', 'app/sale-controller.js'].forEach(filePath => {
  if (!fs.existsSync(filePath)) return;
  let code = fs.readFileSync(filePath, 'utf8');

  // Replace with regex that handles \r?\n
  const regexCard3 = /(<div[^>]*id="calc-l1-value">)[^<]*(<\/div>\s*<span[^>]*>)142x Multiple(<\/span>)/;
  if (regexCard3.test(code)) {
    code = code.replace(regexCard3, '$128.5M Ticks$2${getI18nText(\'projectedMultiple\')}$3');
    console.log(`[${filePath}] Updated Card 3 HTML.`);
  } else {
    console.warn(`[${filePath}] regexCard3 did not match.`);
  }

  // Replace calculation logic
  const oldCalcStr = "const l1Value = (totalTokens * 1.00).toLocaleString('en-US', { style: 'currency', currency: 'USD' });";
  const newCalcStr = `const executionCapacity = Math.round(totalTokens * 200);
      const l1Value = executionCapacity >= 1000000 
        ? (executionCapacity / 1000000).toFixed(1) + 'M Ticks' 
        : executionCapacity.toLocaleString('en-US') + ' Ticks';`;

  if (code.includes(oldCalcStr)) {
    code = code.replace(oldCalcStr, newCalcStr);
    console.log(`[${filePath}] Replaced l1Value computation.`);
  } else {
    console.warn(`[${filePath}] oldCalcStr not found.`);
  }

  // Also update calc-l1-subtext update
  const oldSetVal = "l1ValEl.textContent = l1Value;";
  const newSetVal = `l1ValEl.textContent = l1Value;
      const l1SubEl = container.querySelector('#calc-l1-subtext');
      if (l1SubEl) l1SubEl.textContent = getI18nText('projectedMultiple');`;

  if (code.includes(oldSetVal) && !code.includes('#calc-l1-subtext')) {
    code = code.replace(oldSetVal, newSetVal);
    console.log(`[${filePath}] Added dynamic subtext update.`);
  }

  fs.writeFileSync(filePath, code, 'utf8');
});
