const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
console.log('Includes playground.quickDemos:', content.includes('data-i18n="playground.quickDemos"'));
console.log('Search quickDemos:', content.indexOf('quickDemos'));
if (content.indexOf('quickDemos') !== -1) {
  console.log(content.substring(content.indexOf('quickDemos') - 30, content.indexOf('quickDemos') + 60));
}
