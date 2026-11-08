const katex = require('katex');

function renderMathInMarkdown(text) {
  // 1. First replace display math $$ ... $$
  text = text.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
    try {
      const clean = formula.trim()
        .replace(/[\t]/g, ' ')
        .replace(/\\text\s*\{/g, '\\text{');
      return '\n\n<div class="math-display-container">' + 
             katex.renderToString(clean, { displayMode: true, throwOnError: false }) + 
             '</div>\n\n';
    } catch (e) {
      return match;
    }
  });

  // 2. Next replace inline math $ ... $
  // Protect currency like $10.00, $0.000001, $30+, $821 million, $HAISI
  // A true inline math pattern has typical math symbols: \, ^, _, =, <, >, +, -, *, Greek, or single-variable like $B$, $K$, $I_1$
  text = text.replace(/(?<!\\)\$([^\$\n]+?)\$/g, (match, formula) => {
    const trimmed = formula.trim();
    // Skip if it looks like currency ($10, $0.50, $45B, $HAISI)
    if (/^[\d,.]+(\s*(million|billion|trillion|[kKmMbB]))?(\+)?$/.test(trimmed) || trimmed.startsWith('HAISI')) {
      return match;
    }
    // Only render if it contains math notation, LaTeX commands, or valid identifiers
    try {
      const clean = trimmed.replace(/[\t]/g, ' ');
      return katex.renderToString(clean, { displayMode: false, throwOnError: false });
    } catch (e) {
      return match;
    }
  });

  return text;
}

const sample = `
Here is an equation:
$$\\mathbf{Hai} = \\text{Human} + \\text{AI}$$
And here is inline: $AI^2$ and latency $\\tau \\le 12.0\\text{s}$.
Cost is $10.00 and token is $HAISI, while parameter is $K$.
`;

const res = renderMathInMarkdown(sample);
console.log('Result contains katex-display:', res.includes('katex-display'));
console.log('Result contains katex:', res.includes('class="katex"'));
console.log('Currency preserved ($10.00):', res.includes('$10.00'));
console.log('Token preserved ($HAISI):', res.includes('$HAISI'));
