for path in ['sale-controller.js', 'app/sale-controller.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    target = "    window.addEventListener('haichain:languageChanged', (e) => {\n      const code = e.detail && (e.detail.lang || e.detail.language);\n      updateLanguage(code);\n    });"
    
    replacement = target + """\n
    // Listen for wallet connection from header modal or anywhere
    window.addEventListener('haichain_wallet_connected', (e) => {
      const w = e.detail;
      if (w && w.address) {
        const walletInput = document.getElementById('preseed-wallet');
        if (walletInput) walletInput.value = w.address;
        const payBtnText = document.getElementById('label-pay-1click-text');
        if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
        const boundDot = document.querySelector('#panel-saft-1click .w-2.h-2.rounded-full');
        if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
        const boundAddr = document.querySelector('#panel-saft-1click .font-bold.text-black');
        if (boundAddr) boundAddr.textContent = `${w.address.slice(0, 4)}...${w.address.slice(-4)}`;
      }
    });"""

    c_norm = content.replace('\r\n', '\n')
    target_norm = target.replace('\r\n', '\n')

    if target_norm in c_norm:
        c_norm = c_norm.replace(target_norm, replacement)
        if '\r\n' in content:
            content = c_norm.replace('\n', '\r\n')
        else:
            content = c_norm
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added haichain_wallet_connected listener to {path}")
    else:
        print(f"ERROR: Target not found in {path}")
