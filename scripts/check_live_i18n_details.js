async function checkI18n() {
  const url = 'https://haichain.si/app/i18n.js?v=v37_clean_tabs_1793637655564';
  const res = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
  console.log('CF-Cache-Status for i18n:', res.headers.get('cf-cache-status'));
  const text = await res.text();
  console.log('File length:', text.length);
  
  // Find "vi": { ... "aiHub.tabDesktop": ... }
  // Let's find index of "aiHub.tabDesktop"
  let idx = 0;
  let count = 0;
  while ((idx = text.indexOf('"aiHub.tabDesktop"', idx)) !== -1) {
    count++;
    console.log(`Match ${count} at ${idx}:`, text.substring(idx, idx + 80).replace(/\n/g, ' '));
    idx += 18;
  }
}
checkI18n();
