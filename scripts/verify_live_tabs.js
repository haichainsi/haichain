async function test() {
  try {
    const res = await fetch('https://haichain.si/dashboard?t=' + Date.now(), {
      headers: { 'User-Agent': 'Mozilla/5.0' }
    });
    const html = await res.text();
    console.log('HTML status:', res.status);
    const m1 = html.match(/data-i18n="aiHub\.tabDesktop">([^<]*)</);
    const m2 = html.match(/data-i18n="aiHub\.tabOnline">([^<]*)</);
    const m3 = html.match(/data-i18n="aiHub\.tabWeb">([^<]*)</);
    console.log('DOM in HTML:');
    console.log('tabDesktop:', m1 ? m1[1] : 'null');
    console.log('tabOnline:', m2 ? m2[1] : 'null');
    console.log('tabWeb:', m3 ? m3[1] : 'null');

    const scriptMatch = html.match(/src="(\/app\/i18n\.js[^"]*)"/);
    console.log('i18n script src in HTML:', scriptMatch ? scriptMatch[1] : 'null');

    if (scriptMatch) {
      const resJs = await fetch('https://haichain.si' + scriptMatch[1], {
        headers: { 'User-Agent': 'Mozilla/5.0' }
      });
      const js = await resJs.text();
      const viMatch = js.match(/"aiHub\.tabDesktop":\s*"([^"]*)"/);
      const viMatchOnline = js.match(/"aiHub\.tabOnline":\s*"([^"]*)"/);
      const viMatchWeb = js.match(/"aiHub\.tabWeb":\s*"([^"]*)"/);
      console.log('In fetched i18n.js:');
      console.log('aiHub.tabDesktop:', viMatch ? viMatch[1] : 'null');
      console.log('aiHub.tabOnline:', viMatchOnline ? viMatchOnline[1] : 'null');
      console.log('aiHub.tabWeb:', viMatchWeb ? viMatchWeb[1] : 'null');
    }
  } catch (e) {
    console.error('Error:', e);
  }
}
test();
