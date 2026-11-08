import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    code = f.read()

target = """    const btnShareX = container.querySelector('#btn-share-ref-x');
    if (btnShareX) {
      btnShareX.addEventListener('click', () => {
        const refInput = container.querySelector('#ref-share-url-input');
        const url = refInput ? refInput.value : window.location.origin;
        const text = encodeURIComponent(`🚀 Join the HAICHAIN Pre-Seed Round! Get +5% Bonus $HAISI allocation on your SAFT deposit:\\n\\n${url}\\n\\n#HAICHAIN #Solana #AI #Token2022`);
        window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
      });
    }

    const btnShareTg = container.querySelector('#btn-share-ref-tg');
    if (btnShareTg) {
      btnShareTg.addEventListener('click', () => {
        const refInput = container.querySelector('#ref-share-url-input');
        const url = refInput ? refInput.value : window.location.origin;
        const text = encodeURIComponent(`Join HAICHAIN Pre-Seed Round with +5% $HAISI Token Bonus!`);
        window.open(`https://t.me/share/url?url=${encodeURIComponent(url)}&text=${text}`, '_blank');
      });
    }"""

replacement = """    const btnShareX = container.querySelector('#btn-share-ref-x');
    if (btnShareX) {
      btnShareX.addEventListener('click', () => {
        const refInput = container.querySelector('#ref-share-url-input');
        let url = refInput ? refInput.value : window.location.origin;
        if (!url.includes('utm_source')) {
          url += (url.includes('?') ? '&' : '?') + 'utm_source=twitter';
        }
        const text = encodeURIComponent(`🚀 Join the HAICHAIN Pre-Seed Round! Get +5% Bonus $HAISI allocation on your SAFT deposit:\\n\\n${url}\\n\\n#HAICHAIN #Solana #AI #Token2022`);
        window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
      });
    }

    const btnShareTg = container.querySelector('#btn-share-ref-tg');
    if (btnShareTg) {
      btnShareTg.addEventListener('click', () => {
        const refInput = container.querySelector('#ref-share-url-input');
        let url = refInput ? refInput.value : window.location.origin;
        if (!url.includes('utm_source')) {
          url += (url.includes('?') ? '&' : '?') + 'utm_source=telegram';
        }
        const text = encodeURIComponent(`Join HAICHAIN Pre-Seed Round with +5% $HAISI Token Bonus!`);
        window.open(`https://t.me/share/url?url=${encodeURIComponent(url)}&text=${text}`, '_blank');
      });
    }"""

if target in code:
    code = code.replace(target, replacement, 1)
    with open('sale-controller.js', 'w', encoding='utf-8') as f:
        f.write(code)
    with open('app/sale-controller.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Successfully patched share handlers with automated UTM tagging in sale-controller.js and app/sale-controller.js!")
else:
    print("Target not found in sale-controller.js!")
    sys.exit(1)
