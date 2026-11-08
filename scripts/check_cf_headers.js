async function check() {
  const res = await fetch('https://haichain.si/dashboard?nocache=' + Date.now(), {
    headers: { 'User-Agent': 'Mozilla/5.0' }
  });
  console.log('CF-Ray:', res.headers.get('cf-ray'));
  console.log('CF-Cache-Status:', res.headers.get('cf-cache-status'));
  console.log('Age:', res.headers.get('age'));
  console.log('Last-Modified:', res.headers.get('last-modified'));
  console.log('Date:', res.headers.get('date'));
  
  const text = await res.text();
  const scriptMatch = text.match(/<script src="\/app\/i18n\.js\?v=([^"]*)">/);
  console.log('Script tag in live HTML:', scriptMatch ? scriptMatch[0] : 'NOT FOUND');

  const tabDesktop = text.match(/data-i18n="aiHub\.tabDesktop">([^<]*)</);
  console.log('tabDesktop in HTML:', tabDesktop ? tabDesktop[1] : 'NOT FOUND');
}
check();
