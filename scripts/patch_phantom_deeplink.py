import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update assets/phantom-deeplink.js and app/assets/phantom-deeplink.js
for path in ['assets/phantom-deeplink.js', 'app/assets/phantom-deeplink.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add connectMetaMask and update openInAppBrowser
    old_open = """    openInAppBrowser: function(provider, targetUrl) {
      provider = (provider || 'phantom').toLowerCase();
      var appOrigin = window.location.origin;
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        appOrigin = 'https://haichain.pages.dev';
      }
      var dest = targetUrl || (appOrigin + window.location.pathname);
      if (dest.indexOf('autoConnect=') === -1) {
        dest += (dest.indexOf('?') === -1 ? '?' : '&') + 'autoConnect=' + encodeURIComponent(provider);
      }
      var link = provider === 'solflare'
        ? 'https://solflare.com/ul/v1/browse/' + encodeURIComponent(dest) + '?ref=' + encodeURIComponent(appOrigin)
        : 'https://phantom.com/ul/browse/' + encodeURIComponent(dest) + '?ref=' + encodeURIComponent(appOrigin);
      window.location.href = link;
    },"""

    new_open = """    connectMetaMask: function(targetRedirectUrl) {
      var appOrigin = window.location.origin;
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        appOrigin = 'https://haichain.pages.dev';
      }
      var appPath = window.location.pathname || '/';
      var redirectUrl = targetRedirectUrl || (appOrigin + appPath);
      var sep = redirectUrl.indexOf('?') === -1 ? '?' : '&';
      var returnUrl = encodeURIComponent(window.location.href);
      var targetUrlWithParams = redirectUrl + sep + 'auto_connect=metamask&return_url=' + returnUrl;
      var cleanDest = targetUrlWithParams.replace(/^https?:\\/\\//, '');
      var link = 'https://metamask.app.link/dapp/' + cleanDest;
      console.log('[HaichainMobileWallet] Launching official MetaMask Deeplink:', link);
      window.location.href = link;
    },

    openInAppBrowser: function(provider, targetUrl) {
      provider = (provider || 'phantom').toLowerCase();
      var appOrigin = window.location.origin;
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        appOrigin = 'https://haichain.pages.dev';
      }
      var dest = targetUrl || (appOrigin + window.location.pathname);
      if (provider === 'metamask') {
        this.connectMetaMask(dest);
        return;
      }
      if (dest.indexOf('autoConnect=') === -1 && dest.indexOf('auto_connect=') === -1) {
        dest += (dest.indexOf('?') === -1 ? '?' : '&') + 'autoConnect=' + encodeURIComponent(provider);
      }
      var link = provider === 'solflare'
        ? 'https://solflare.com/ul/v1/browse/' + encodeURIComponent(dest) + '?ref=' + encodeURIComponent(appOrigin)
        : 'https://phantom.com/ul/browse/' + encodeURIComponent(dest) + '?ref=' + encodeURIComponent(appOrigin);
      window.location.href = link;
    },"""

    if old_open in content:
        content = content.replace(old_open, new_open)
        print(f"Patched openInAppBrowser in {path}")
    else:
        print(f"WARNING: old_open not found in {path}")

    # Update handoffWallet validation to support EVM addresses (0x...) as well as Solana base58
    old_handoff = """        // 1. Direct Connected Wallet Handoff (from in-app browser or cross-browser share)
        var handoffWallet = params['connectedWallet'];
        var handoffProvider = params['provider'] || 'Phantom';
        if (handoffWallet && /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(handoffWallet)) {
          this.stripParamsAndCleanUrl(['connectedWallet', 'provider']);
          var handoffResult = {
            publicKey: handoffWallet,
            provider: handoffProvider,
            source: 'handoff'
          };
          this.broadcastConnection(handoffResult);
          if (typeof onSuccess === 'function') {
            onSuccess(handoffResult);
          }
          return true;
        }"""

    new_handoff = """        // 1. Direct Connected Wallet Handoff (from in-app browser or cross-browser share - supports both Solana and MetaMask EVM)
        var handoffWallet = params['connectedWallet'];
        var handoffProvider = params['provider'] || 'Phantom';
        var isSolanaAddr = /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(handoffWallet);
        var isEvmAddr = /^0x[a-fA-F0-9]{40}$/i.test(handoffWallet);
        if (handoffWallet && (isSolanaAddr || isEvmAddr)) {
          this.stripParamsAndCleanUrl(['connectedWallet', 'provider']);
          var finalProvider = isEvmAddr ? (handoffProvider || 'MetaMask') : handoffProvider;
          var handoffResult = {
            publicKey: handoffWallet,
            provider: finalProvider,
            isEVM: isEvmAddr,
            source: 'handoff'
          };
          this.broadcastConnection(handoffResult);
          if (typeof onSuccess === 'function') {
            onSuccess(handoffResult);
          }
          return true;
        }"""

    if old_handoff in content:
        content = content.replace(old_handoff, new_handoff)
        print(f"Patched handoffWallet in {path}")
    else:
        print(f"WARNING: old_handoff not found in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating phantom-deeplink.js files.")
