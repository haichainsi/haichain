/**
 * HAICHAIN Universal Mobile Wallet Bridge (Phantom & Solflare)
 * Standard E2EE X25519 Connect Handshake with Automatic Return Redirect & Cross-Browser/Cross-Tab Handoff
 */
(function(window) {
  'use strict';

  var STORAGE_SK_KEY = 'haichain_mobile_wallet_dapp_sk';
  var STORAGE_PROVIDER_KEY = 'haichain_mobile_wallet_provider';
  var STORAGE_SESSION_KEY = 'haichain_mobile_wallet_session';
  var STORAGE_TS_KEY = 'haichain_mobile_wallet_sk_ts';

  function getCookie(name) {
    try {
      var match = document.cookie.match(new RegExp('(?:^|;\\s*)' + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + '=([^;]*)'));
      return match ? decodeURIComponent(match[1]) : null;
    } catch (_) {
      return null;
    }
  }

  function setCookie(name, val, maxAgeSec) {
    try {
      document.cookie = name + '=' + encodeURIComponent(val) + '; Path=/; Max-Age=' + (maxAgeSec || 1800) + '; SameSite=Lax';
    } catch (_) {}
  }

  function clearCookie(name) {
    try {
      document.cookie = name + '=; Path=/; Max-Age=0; SameSite=Lax';
    } catch (_) {}
  }

  var HaichainMobileWallet = {
    isAvailable: function() {
      return typeof window.nacl !== 'undefined' && typeof window.bs58 !== 'undefined';
    },

    ensureCryptoReady: function(callback, maxWaitMs) {
      maxWaitMs = maxWaitMs || 2500;
      var startTime = Date.now();
      var check = function() {
        if (typeof window.nacl !== 'undefined' && typeof window.bs58 !== 'undefined') {
          callback(true);
          return;
        }
        if (Date.now() - startTime >= maxWaitMs) {
          callback(false);
          return;
        }
        setTimeout(check, 50);
      };
      check();
    },

    saveEphemeralKey: function(skB58, provider) {
      try {
        localStorage.setItem(STORAGE_SK_KEY, skB58);
        localStorage.setItem(STORAGE_PROVIDER_KEY, provider);
        localStorage.setItem(STORAGE_TS_KEY, Date.now().toString());
      } catch (_) {}
      try {
        sessionStorage.setItem(STORAGE_SK_KEY, skB58);
        sessionStorage.setItem(STORAGE_PROVIDER_KEY, provider);
      } catch (_) {}
      setCookie(STORAGE_SK_KEY, skB58, 1800);
      setCookie(STORAGE_PROVIDER_KEY, provider, 1800);
    },

    getEphemeralKey: function() {
      var skB58 = null;
      var provider = 'Phantom';
      try {
        skB58 = localStorage.getItem(STORAGE_SK_KEY) || sessionStorage.getItem(STORAGE_SK_KEY);
        provider = localStorage.getItem(STORAGE_PROVIDER_KEY) || sessionStorage.getItem(STORAGE_PROVIDER_KEY) || 'Phantom';
      } catch (_) {}
      if (!skB58) {
        skB58 = getCookie(STORAGE_SK_KEY);
        var cp = getCookie(STORAGE_PROVIDER_KEY);
        if (cp) provider = cp;
      }
      return { skB58: skB58, provider: provider };
    },

    clearEphemeralKey: function() {
      try {
        localStorage.removeItem(STORAGE_SK_KEY);
        localStorage.removeItem(STORAGE_PROVIDER_KEY);
        localStorage.removeItem(STORAGE_TS_KEY);
      } catch (_) {}
      try {
        sessionStorage.removeItem(STORAGE_SK_KEY);
        sessionStorage.removeItem(STORAGE_PROVIDER_KEY);
      } catch (_) {}
      clearCookie(STORAGE_SK_KEY);
      clearCookie(STORAGE_PROVIDER_KEY);
    },

    extractParams: function() {
      var params = {};
      try {
        // 1. Search Query Parameters (?key=value)
        if (window.location.search) {
          var searchParams = new URLSearchParams(window.location.search);
          searchParams.forEach(function(v, k) {
            params[k] = v;
          });
        }

        // 2. Hash Fragment Parameters (#key=value or #/route?key=value)
        if (window.location.hash) {
          var rawHash = window.location.hash.substring(1);
          var queryPart = rawHash.indexOf('?') !== -1 ? rawHash.substring(rawHash.indexOf('?') + 1) : rawHash;
          if (queryPart.indexOf('=') !== -1) {
            var hashParams = new URLSearchParams(queryPart);
            hashParams.forEach(function(v, k) {
              if (!params[k]) params[k] = v;
            });
          }
        }
      } catch (err) {
        console.warn('[HaichainMobileWallet] Error parsing URL params:', err);
      }
      return params;
    },

    stripParamsAndCleanUrl: function(keysToRemove) {
      try {
        var url = new URL(window.location.href);
        if (Array.isArray(keysToRemove)) {
          keysToRemove.forEach(function(k) { url.searchParams.delete(k); });
        }
        // Also clean hash if it had callback params
        if (url.hash && (url.hash.indexOf('phantom_encryption_public_key') !== -1 || url.hash.indexOf('data=') !== -1 || url.hash.indexOf('connectedWallet=') !== -1)) {
          url.hash = '';
        }
        var q = url.searchParams.toString();
        var cleanPath = url.origin + url.pathname + (q ? '?' + q : '') + url.hash;
        var docTitle = typeof document !== 'undefined' ? document.title : '';
        window.history.replaceState({}, docTitle, cleanPath);
      } catch (_) {}
    },

    isPhantomInAppBrowser: function() {
      try {
        var ua = (navigator.userAgent || '').toLowerCase();
        var hasPhantomObj = !!(window.phantom?.solana || window.solana?.isPhantom);
        var hasPhantomUa = ua.indexOf('phantom') !== -1;
        var isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
        return hasPhantomUa || (hasPhantomObj && isMobile);
      } catch (_) {
        return false;
      }
    },

    buildHandoffUrl: function(walletAddress, provider, targetUrl) {
      var appOrigin = window.location.origin;
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        appOrigin = 'https://haichain.pages.dev';
      }
      var dest = targetUrl || (appOrigin + window.location.pathname);
      var sep = dest.indexOf('?') === -1 ? '?' : '&';
      return dest + sep + 'connectedWallet=' + encodeURIComponent(walletAddress) + '&provider=' + encodeURIComponent(provider || 'Phantom');
    },

    openInAppBrowser: function(provider, targetUrl) {
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
        : 'https://phantom.app/ul/browse/' + encodeURIComponent(dest) + '?ref=' + encodeURIComponent(appOrigin);
      window.location.href = link;
    },

    connect: function(provider, targetRedirectUrl) {
      provider = (provider || 'phantom').toLowerCase();
      var appOrigin = window.location.origin;
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        appOrigin = 'https://haichain.pages.dev';
      }
      var appPath = window.location.pathname || '/';
      var redirectUrl = targetRedirectUrl || (appOrigin + appPath);

      if (!this.isAvailable()) {
        console.warn('Crypto libraries not loaded yet, falling back to in-app browse link.');
        this.openInAppBrowser(provider, redirectUrl);
        return;
      }

      try {
        var keyPair = window.nacl.box.keyPair();
        var skB58 = window.bs58.encode(keyPair.secretKey);
        var pkB58 = window.bs58.encode(keyPair.publicKey);

        // Save ephemeral key across all storage mechanisms (local, session, cookie)
        this.saveEphemeralKey(skB58, provider);

        // Official Universal Link with verified native app intent
        var baseUrl = provider === 'solflare'
          ? 'https://solflare.com/ul/v1/connect'
          : 'https://phantom.app/ul/v1/connect';

        var connectUrl = new URL(baseUrl);
        connectUrl.searchParams.set('app_url', appOrigin);
        connectUrl.searchParams.set('dapp_encryption_public_key', pkB58);
        connectUrl.searchParams.set('redirect_link', redirectUrl);
        // HAICHAIN program & vault operate on devnet
        connectUrl.searchParams.set('cluster', 'devnet');

        console.log('[HaichainMobileWallet] Launching official Connect Deeplink:', connectUrl.toString());
        window.location.href = connectUrl.toString();
      } catch (err) {
        console.error('[HaichainMobileWallet] Connect failed, falling back to browse:', err);
        this.openInAppBrowser(provider, redirectUrl);
      }
    },

    broadcastConnection: function(walletData) {
      try {
        if (typeof window.BroadcastChannel !== 'undefined') {
          var bc = new BroadcastChannel('haichain_mobile_wallet');
          bc.postMessage({ type: 'HAICHAIN_WALLET_SYNC', data: walletData });
          setTimeout(function() { try { bc.close(); } catch (_) {} }, 1000);
        }
      } catch (_) {}
      try {
        window.dispatchEvent(new CustomEvent('haichain_wallet_connected', { detail: walletData }));
      } catch (_) {}
    },

    onConnected: function(callback) {
      if (typeof callback !== 'function') return;

      // 1. Cross-tab BroadcastChannel
      try {
        if (typeof window.BroadcastChannel !== 'undefined') {
          var bc = new BroadcastChannel('haichain_mobile_wallet');
          bc.onmessage = function(ev) {
            if (ev && ev.data && ev.data.type === 'HAICHAIN_WALLET_SYNC' && ev.data.data) {
              callback(ev.data.data);
            }
          };
        }
      } catch (_) {}

      // 2. Custom DOM event within window
      try {
        window.addEventListener('haichain_wallet_connected', function(ev) {
          if (ev && ev.detail) callback(ev.detail);
        });
      } catch (_) {}

      // 3. Storage event for cross-tab localStorage update
      try {
        window.addEventListener('storage', function(ev) {
          if (ev.key === 'haichain-connected-wallet' && ev.newValue) {
            try {
              var parsed = JSON.parse(ev.newValue);
              if (parsed && parsed.address) {
                callback({
                  publicKey: parsed.address,
                  provider: parsed.provider || 'Phantom',
                  solBalance: parsed.solBalance,
                  source: 'storage_sync'
                });
              }
            } catch (_) {}
          }
        });
      } catch (_) {}
    },

    handleRedirectCallback: function(onSuccess, onError) {
      var self = this;
      try {
        var params = this.extractParams();

        // 1. Direct Connected Wallet Handoff (from in-app browser or cross-browser share)
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
        }

        // 2. Error returned from wallet app
        var errorCode = params['errorCode'];
        var errorMessage = params['errorMessage'];
        if (errorCode || errorMessage) {
          this.stripParamsAndCleanUrl(['errorCode', 'errorMessage']);
          if (typeof onError === 'function') {
            onError(errorMessage || ('Connection rejected (code ' + errorCode + ')'));
          }
          return false;
        }

        // 3. E2EE Encrypted Callback from Phantom / Solflare
        var peerEncryptionPubKey = params['phantom_encryption_public_key'] || params['solflare_encryption_public_key'];
        var nonceB58 = params['nonce'];
        var dataB58 = params['data'];

        if (peerEncryptionPubKey && nonceB58 && dataB58) {
          console.log('[HaichainMobileWallet] Encrypted callback payload received. Ensuring crypto is ready...');

          this.ensureCryptoReady(function(ready) {
            if (!ready) {
              console.error('[HaichainMobileWallet] Crypto libraries (nacl/bs58) not ready.');
              if (typeof onError === 'function') onError('Thư viện mã hóa tải chậm, vui lòng thử lại.');
              return;
            }

            var ephem = self.getEphemeralKey();
            var skB58 = ephem.skB58;
            var storedProvider = ephem.provider || 'Phantom';

            if (!skB58) {
              console.error('[HaichainMobileWallet] No stored dApp secret key found in localStorage/sessionStorage/cookies.');
              if (typeof onError === 'function') {
                onError('Khóa phiên bị mất do chuyển tab/trình duyệt. Vui lòng mở trang trong Phantom App hoặc dán địa chỉ ví.');
              }
              return;
            }

            try {
              var peerPubKey = window.bs58.decode(peerEncryptionPubKey);
              var dappSk = window.bs58.decode(skB58);
              var nonce = window.bs58.decode(nonceB58);
              var encryptedData = window.bs58.decode(dataB58);

              var sharedSecret = window.nacl.box.before(peerPubKey, dappSk);
              var decrypted = window.nacl.box.open.after(encryptedData, nonce, sharedSecret);

              if (!decrypted) {
                console.error('[HaichainMobileWallet] Decryption failed - invalid MAC or corrupted payload.');
                if (typeof onError === 'function') onError('Giải mã phản hồi từ ví thất bại.');
                return;
              }

              // Successfully decrypted: clean up temporary secret key and clean URL
              self.clearEphemeralKey();
              self.stripParamsAndCleanUrl(['phantom_encryption_public_key', 'solflare_encryption_public_key', 'nonce', 'data']);

              var jsonStr = new TextDecoder().decode(decrypted);
              var payload = JSON.parse(jsonStr);
              console.log('[HaichainMobileWallet] Handshake Success! Connected Wallet:', payload.public_key);

              if (payload.session) {
                try {
                  localStorage.setItem(STORAGE_SESSION_KEY, payload.session);
                } catch (_) {}
              }

              var providerName = storedProvider.charAt(0).toUpperCase() + storedProvider.slice(1);
              var resObj = {
                publicKey: payload.public_key,
                session: payload.session,
                provider: providerName,
                source: 'deeplink'
              };

              self.broadcastConnection(resObj);

              if (typeof onSuccess === 'function') {
                onSuccess(resObj);
              }
            } catch (decErr) {
              console.error('[HaichainMobileWallet] Decrypt exception:', decErr);
              if (typeof onError === 'function') onError('Lỗi giải mã: ' + (decErr.message || 'Không xác định'));
            }
          });

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
