const fs = require('fs');
const katex = require('katex');

const inputFile = process.argv[2] || 'temp_math_items.json';
const outputFile = process.argv[3] || 'temp_math_rendered.json';

const items = JSON.parse(fs.readFileSync(inputFile, 'utf-8'));
const rendered = [];

let errors = 0;
for (let i = 0; i < items.length; i++) {
  const [type, formula] = items[i];
  
  // Clean whitespace and auto-escape any unescaped underscore inside \text{...}
  let clean = formula.trim()
    .replace(/[\u00a0\u1680\u2000-\u200b\u202f\u205f\u3000]/g, ' ')
    .replace(/ {2,}/g, ' ')
    .replace(/\\text\{([^}]+)\}/g, (m, content) => {
      return '\\text{' + content.replace(/(?<!\\)_/g, '\\_') + '}';
    });

  try {
    const isDisplay = type === 'display';
    const html = katex.renderToString(clean, {
      displayMode: isDisplay,
      throwOnError: true
    });
    if (isDisplay) {
      rendered.push(`<div class="math-display-block">${html}</div>`);
    } else {
      rendered.push(html);
    }
  } catch (e) {
    errors++;
    console.error(`Item #${i} (${type}) ERROR: ${e.message} in formula: ${formula}`);
    const isDisplay = type === 'display';
    const fallback = katex.renderToString(clean, {
      displayMode: isDisplay,
      throwOnError: false
    });
    rendered.push(isDisplay ? `<div class="math-display-block">${fallback}</div>` : fallback);
  }
}

if (errors > 0) {
  console.warn(`Rendered ${rendered.length} formulas with KaTeX (${errors} fallback).`);
}
fs.writeFileSync(outputFile, JSON.stringify(rendered), 'utf-8');
