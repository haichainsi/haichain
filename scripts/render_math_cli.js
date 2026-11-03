const fs = require('fs');
const path = require('path');
const katex = require('katex');

const inputFile = process.argv[2];
const outputFile = process.argv[3];

if (!inputFile || !outputFile) {
  console.error("Usage: node render_math_cli.js <input.html> <output.html>");
  process.exit(1);
}

let html = fs.readFileSync(inputFile, 'utf-8');

function sanitizeFormula(formula) {
  let clean = formula.trim()
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/<\/?em>/g, '_')
    .replace(/<\/?strong>/g, '__');
  
  // Auto-escape any unescaped underscore inside \text{...}
  clean = clean.replace(/\\text\{([^}]+)\}/g, (m, content) => {
    return '\\text{' + content.replace(/(?<!\\)_/g, '\\_') + '}';
  });

  return clean;
}

function isValidMath(raw) {
  let f = raw.trim()
    .replace(/<\/?em>/g, '_')
    .replace(/<\/?strong>/g, '__');
    
  if (!f) return false;
  
  // Never allow block HTML tags inside inline math
  if (/<(p|div|li|ol|ul|table|tr|td|pre|blockquote)\b/i.test(f)) {
    return false;
  }
  
  // Check if currency amount
  if (/^\d[\d,.]*(?:\s*(?:million|billion|trillion|[kKmMbB]))?\+?$/.test(f)) {
    return false;
  }
  if (/^(?:HAISI|SOL|USDT|BTC|ETH|USD)\b/.test(f)) {
    return false;
  }

  // Must contain math indicators
  if (f.includes('\\')) return true;
  if (f.includes('_') || f.includes('^') || f.includes('{') || f.includes('}')) return true;
  if (/\b[a-zA-Z]\b\s*(=|&lt;|&gt;|<|>|\\le|\\ge|\+|-|\*|\/)\s*/.test(f)) return true;
  if (/^[a-zA-Z](?:_[a-zA-Z0-9]+)?$/.test(f)) return true;
  if (/^[a-zA-Z]\s*,\s*[a-zA-Z]$/.test(f)) return true;
  if (/^I_[1-9]$/.test(f) || /^T_[1-4]$/.test(f)) return true;

  return false;
}

// 1. Split by <pre> blocks so we NEVER touch ASCII diagrams or code!
const parts = html.split(/(<pre[\s\S]*?<\/pre>)/gi);

for (let i = 0; i < parts.length; i += 2) {
  let text = parts[i];

  // Protect all explicit currency patterns
  text = text.replace(/(?<!\\)\$(\d[\d,.]*(?:\s*(?:million|billion|trillion|[kKmMbB]))?(?:\+)?)/g, '&#36;$1');
  text = text.replace(/(?<!\\)\$(HAISI|SOL|USDT|BTC|ETH)\b/g, '&#36;$1');

  // Replace display math: <p>$$...$$</p> or $$...$$
  text = text.replace(/<p>\s*\$\$([\s\S]*?)\$\$\s*<\/p>/g, (m, formula) => {
    try {
      const clean = sanitizeFormula(formula);
      return '<div class="math-display-block">' + 
             katex.renderToString(clean, { displayMode: true, throwOnError: false, strict: "ignore" }) + 
             '</div>';
    } catch (e) {
      return m;
    }
  });

  text = text.replace(/\$\$([\s\S]*?)\$\$/g, (m, formula) => {
    try {
      const clean = sanitizeFormula(formula);
      return '<div class="math-display-block">' + 
             katex.renderToString(clean, { displayMode: true, throwOnError: false, strict: "ignore" }) + 
             '</div>';
    } catch (e) {
      return m;
    }
  });

  // Replace inline math: $...$
  text = text.replace(/(?<!\\)\$([^\$\n\r]+?)\$/g, (m, formula) => {
    if (!isValidMath(formula)) {
      return m;
    }

    try {
      const clean = sanitizeFormula(formula);
      return katex.renderToString(clean, { displayMode: false, throwOnError: false, strict: "ignore" });
    } catch (e) {
      return m;
    }
  });

  parts[i] = text;
}

fs.writeFileSync(outputFile, parts.join(''), 'utf-8');
