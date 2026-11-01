/**
 * HAICHAIN Universal Mobile Wallet Bridge (Phantom & Solflare)
 * Standard E2EE X25519 Connect Handshake with Automatic Return Redirect
 */
(function(window) {
  'use strict';

  var STORAGE_SK_KEY = 'haichain_mobile_wallet_dapp_sk';
  var STORAGE_PROVIDER_KEY = 'haichain_mobile_wallet_provider';
  var STORAGE_SESSION_KEY = 'haichain_mobile_wallet_session';

  var HaichainMobileWallet = {
    isAvailable: function() {
      return typeof window.nacl !== 'undefined' && typeof window.bs58 !== 'undefined';
    },

    connect: function(provider) {
      provider = (provider || 'phantom').toLowerCase();
      var appOrigin = window.location.origin;
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        appOrigin = 'https://haichain.pages.dev';
      }
      var appPath = window.location.pathname;
      var redirectUrl = appOrigin + appPath;

      if (!this.isAvailable()) {
        console.warn('Crypto libraries not loaded yet, falling back to in-app browse link.');
        var fallbackBrowse = provider === 'solflare'
          ? 'https://solflare.com/ul/v1/browse/' + encodeURIComponent(redirectUrl + '?autoConnect=solflare')
          : 'https://phantom.com/ul/browse/' + encodeURIComponent(redirectUrl + '?autoConnect=phantom');
        window.location.href = fallbackBrowse;
        return;
      }

      try {
        var keyPair = window.nacl.box.keyPair();
        var skB58 = window.bs58.encode(keyPair.secretKey);
        var pkB58 = window.bs58.encode(keyPair.publicKey);

        try {
          localStorage.setItem(STORAGE_SK_KEY, skB58);
          localStorage.setItem(STORAGE_PROVIDER_KEY, provider);
        } catch (_) {}

        var baseUrl = provider === 'solflare'
          ? 'https://solflare.com/ul/v1/connect'
          : 'https://phantom.app/ul/v1/connect';

        var connectUrl = new URL(baseUrl);
        connectUrl.searchParams.set('app_url', appOrigin);
        connectUrl.searchParams.set('dapp_encryption_public_key', pkB58);
        connectUrl.searchParams.set('redirect_link', redirectUrl);
        connectUrl.searchParams.set('cluster', 'devnet');

        console.log('[HaichainMobileWallet] Launching official Connect Deeplink:', connectUrl.toString());
        window.location.href = connectUrl.toString();
      } catch (err) {
        console.error('[HaichainMobileWallet] Connect failed, falling back to browse:', err);
        var fallbackBrowse = provider === 'solflare'
          ? 'https://solflare.com/ul/v1/browse/' + encodeURIComponent(redirectUrl + '?autoConnect=solflare')
          : 'https://phantom.com/ul/browse/' + encodeURIComponent(redirectUrl + '?autoConnect=phantom');
        window.location.href = fallbackBrowse;
      }
    },

    handleRedirectCallback: function(onSuccess, onError) {
      try {
        var urlParams = new URLSearchParams(window.location.search);

        // 1. Check for Direct Connected Wallet Handoff (from in-app browser or cross-browser share)
        var handoffWallet = urlParams.get('connectedWallet');
        var handoffProvider = urlParams.get('provider') || 'Phantom';
        if (handoffWallet && /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(handoffWallet)) {
          var cleanUrl = new URL(window.location.href);
          cleanUrl.searchParams.delete('connectedWallet');
          cleanUrl.searchParams.delete('provider');
          var docTitle = typeof document !== 'undefined' ? document.title : '';
          window.history.replaceState({}, docTitle, cleanUrl.toString());

          if (typeof onSuccess === 'function') {
            onSuccess({
              publicKey: handoffWallet,
              provider: handoffProvider,
              source: 'handoff'
            });
          }
          return true;
        }

        // 2. Check for Error return from wallet app
        var errorCode = urlParams.get('errorCode');
        var errorMessage = urlParams.get('errorMessage');
        if (errorCode || errorMessage) {
          var cleanUrl = new URL(window.location.href);
          cleanUrl.searchParams.delete('errorCode');
          cleanUrl.searchParams.delete('errorMessage');
          var docTitle = typeof document !== 'undefined' ? document.title : '';
          window.history.replaceState({}, docTitle, cleanUrl.toString());
          if (typeof onError === 'function') {
            onError(errorMessage || ('Connection rejected (code ' + errorCode + ')'));
          }
          return false;
        }

        // 3. Check for E2EE Encrypted Callback from Phantom / Solflare
        var peerEncryptionPubKey = urlParams.get('phantom_encryption_public_key') || urlParams.get('solflare_encryption_public_key');
        var nonceB58 = urlParams.get('nonce');
        var dataB58 = urlParams.get('data');

        if (peerEncryptionPubKey && nonceB58 && dataB58) {
          var cleanUrl = new URL(window.location.href);
          cleanUrl.searchParams.delete('phantom_encryption_public_key');
          cleanUrl.searchParams.delete('solflare_encryption_public_key');
          cleanUrl.searchParams.delete('nonce');
          cleanUrl.searchParams.delete('data');
          var docTitle = typeof document !== 'undefined' ? document.title : '';
          window.history.replaceState({}, docTitle, cleanUrl.toString());

          var skB58 = null;
          var storedProvider = 'Phantom';
          try {
            skB58 = localStorage.getItem(STORAGE_SK_KEY);
            storedProvider = localStorage.getItem(STORAGE_PROVIDER_KEY) || 'Phantom';
            localStorage.removeItem(STORAGE_SK_KEY);
          } catch (_) {}

          if (!skB58) {
            console.error('[HaichainMobileWallet] No stored dApp secret key found in localStorage to decrypt payload.');
            if (typeof onError === 'function') onError('No session key found to decrypt wallet response.');
            return false;
          }

          if (!this.isAvailable()) {
            console.error('[HaichainMobileWallet] Crypto libraries (nacl/bs58) not ready.');
            if (typeof onError === 'function') onError('Crypto libraries not loaded.');
            return false;
          }

          var peerPubKey = window.bs58.decode(peerEncryptionPubKey);
          var dappSk = window.bs58.decode(skB58);
          var nonce = window.bs58.decode(nonceB58);
          var encryptedData = window.bs58.decode(dataB58);

          var sharedSecret = window.nacl.box.before(peerPubKey, dappSk);
          var decrypted = window.nacl.box.open.after(encryptedData, nonce, sharedSecret);

          if (!decrypted) {
            console.error('[HaichainMobileWallet] Decryption failed - invalid MAC or corrupted payload.');
            if (typeof onError === 'function') onError('Failed to decrypt wallet payload.');
            return false;
          }

          var jsonStr = new TextDecoder().decode(decrypted);
          var payload = JSON.parse(jsonStr);
          console.log('[HaichainMobileWallet] Handshake Success! Connected Wallet:', payload.public_key);

          try {
            if (payload.session) {
              localStorage.setItem(STORAGE_SESSION_KEY, payload.session);
            }
          } catch (_) {}

          var providerName = storedProvider.charAt(0).toUpperCase() + storedProvider.slice(1);
          if (typeof onSuccess === 'function') {
            onSuccess({
              publicKey: payload.public_key,
              session: payload.session,
              provider: providerName,
              source: 'deeplink'
            });
          }
          return true;
        }
      } catch (e) {
        console.error('[HaichainMobileWallet] handleRedirectCallback exception:', e);
        if (typeof onError === 'function') onError(e.message || 'Callback handling failed');
      }
      return false;
    }
  };

  window.HaichainMobileWallet = HaichainMobileWallet;
})(typeof window !== 'undefined' ? window : this);
