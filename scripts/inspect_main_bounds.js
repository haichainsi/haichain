const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const pMain = content.indexOf('<main class="max-w-7xl mx-auto px-4 sm:px-6 py-12">');
console.log('pMain:', pMain);
const pEndMain = content.indexOf('</main>', pMain);
console.log('pEndMain:', pEndMain);
console.log('After </main>:\n', content.substring(pEndMain, pEndMain + 400));
