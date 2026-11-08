const fs = require('fs');
const path = require('path');

// Test that pdfjs files exist and are ready
const pdfMinPath = path.join(__dirname, '..', 'pdfjs', 'pdf.min.js');
const workerMinPath = path.join(__dirname, '..', 'pdfjs', 'pdf.worker.min.js');

console.log('pdf.min.js exists:', fs.existsSync(pdfMinPath), 'size:', fs.statSync(pdfMinPath).size);
console.log('pdf.worker.min.js exists:', fs.existsSync(workerMinPath), 'size:', fs.statSync(workerMinPath).size);
