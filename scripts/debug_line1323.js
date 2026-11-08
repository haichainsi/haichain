const fs = require('fs');
const katex = require('katex');

function sanitizeFormula(formula) {
  let clean = formula.trim()
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"');
  
  clean = clean.replace(/\\text\{([^}]+)\}/g, (m, content) => {
    return '\\text{' + content.replace(/(?<!\\)_/g, '\\_') + '}';
  });

  return clean;
}

const l = '* **Bất biến $I_8$ (Thanh toán Đơn điệu & Duy nhất):** $\\text{paid}_{\\text{new}} \\le \\min(\\text{voucher.cumulative}, \\text{channel.reserved}) \\;\\land\\; \\text{paid}_{\\text{new}} \\ge \\text{paid}_{\\text{old}}$. Chống lặp và chống double-spending voucher.';

let res = l.replace(/(?<!\\)\$([^\$\n\r<]+?)\$/g, (m, formula) => {
  console.log('Found formula:', formula);
  const clean = sanitizeFormula(formula);
  return katex.renderToString(clean, { displayMode: false, throwOnError: false });
});

console.log('Result contains katex:', res.includes('class="katex"'));
console.log('Result length:', res.length);
