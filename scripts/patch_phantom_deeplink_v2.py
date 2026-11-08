import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update assets/phantom-deeplink.js and app/assets/phantom-deeplink.js
for path in ['assets/phantom-deeplink.js', 'app/assets/phantom-deeplink.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update connectMetaMask to include session id and storage
    old_mm_func = """    connectMetaMask: function(targetRedirectUrl) {
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
    },"""

    new_mm_func = """    connectMetaMask: function(targetRedirectUrl) {
      var appOrigin = window.location.origin;
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        appOrigin = 'https://haichain.pages.dev';
      }
      var appPath = window.location.pathname || '/';
      var redirectUrl = targetRedirectUrl || (appOrigin + appPath);
      var sep = redirectUrl.indexOf('?') === -1 ? '?' : '&';
      
      var sessId = 'mm_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 8);
      window.__currentMetaMaskSessionId = sessId;
      try {
        localStorage.setItem('haichain_metamask_pending_session', sessId);
      } catch (_) {}

      var returnUrl = encodeURIComponent(window.location.href);
      var targetUrlWithParams = redirectUrl + sep + 'auto_connect=metamask&sess_id=' + sessId + '&return_url=' + returnUrl;
      var cleanDest = targetUrlWithParams.replace(/^https?:\\/\\//, '');
      var link = 'https://metamask.app.link/dapp/' + cleanDest;
      console.log('[HaichainMobileWallet] Launching official MetaMask Deeplink with Session Relay:', link);
      window.location.href = link;
    },"""

    if old_mm_func in content:
        content = content.replace(old_mm_func, new_mm_func)
        print(f"Patched connectMetaMask in {path}")
    else:
        print(f"WARNING: old_mm_func not found in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating phantom-deeplink.js files.")
