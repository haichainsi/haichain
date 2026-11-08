import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update initReferralTracking to send telemetry beacon on dashboard
old_init_ref = """  function initReferralTracking() {
    try {
      const params = new URLSearchParams(window.location.search);
      const ref = params.get('ref') || params.get('referrer') || params.get('inviter');
      if (ref && ref.trim().length >= 4) {
        const clean = ref.trim();
        localStorage.setItem('haichain_ref', clean);
        localStorage.setItem('haichain_ref_captured_at', new Date().toISOString());
        console.log('[HAICHAIN] Genesis Referral captured:', clean);
      }
    } catch (_) {}
  }"""

new_init_ref = """  function detectReferralTrafficSource(urlParams) {
    var utm = (urlParams.get('utm_source') || '').toLowerCase();
    if (utm) {
      if (utm === 'twitter' || utm === 'x') return 'X (Twitter)';
      if (utm === 'telegram' || utm === 'tg') return 'Telegram';
      if (utm === 'facebook' || utm === 'fb') return 'Facebook';
      if (utm === 'linkedin') return 'LinkedIn';
      if (utm === 'youtube') return 'YouTube';
      if (utm === 'discord') return 'Discord';
      if (utm === 'tiktok') return 'TikTok';
      return utm.charAt(0).toUpperCase() + utm.slice(1);
    }
    if (document.referrer) {
      try {
        var refHost = new URL(document.referrer, window.location.href).hostname.toLowerCase();
        if (refHost.indexOf('t.co') !== -1 || refHost.indexOf('twitter.com') !== -1 || refHost.indexOf('x.com') !== -1) return 'X (Twitter)';
        if (refHost.indexOf('t.me') !== -1 || refHost.indexOf('telegram.org') !== -1) return 'Telegram';
        if (refHost.indexOf('facebook.com') !== -1 || refHost.indexOf('fb.com') !== -1) return 'Facebook';
        if (refHost.indexOf('linkedin.com') !== -1) return 'LinkedIn';
        if (refHost.indexOf('google.') !== -1 || refHost.indexOf('bing.') !== -1 || refHost.indexOf('duckduckgo.') !== -1) return 'Search Engine';
        if (refHost.indexOf('haichain.si') === -1 && refHost !== window.location.hostname) return refHost.replace(/^www\\./, '');
      } catch (_) {}
    }
    return 'Direct / Private Chat';
  }

  function initReferralTracking() {
    try {
      const params = new URLSearchParams(window.location.search);
      const ref = params.get('ref') || params.get('referrer') || params.get('inviter');
      if (ref && ref.trim().length >= 4) {
        const clean = ref.trim();
        localStorage.setItem('haichain_ref', clean);
        localStorage.setItem('haichain_ref_captured_at', new Date().toISOString());
        console.log('[HAICHAIN] Genesis Referral captured:', clean);

        // Detect Source & Device
        const source = detectReferralTrafficSource(params);
        const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        const device = isMobile ? 'Mobile' : 'Desktop';

        // Check session uniqueness
        const sessionKey = 'haichain_ref_hit_' + clean.toLowerCase();
        const isUnique = !sessionStorage.getItem(sessionKey);
        sessionStorage.setItem(sessionKey, '1');

        const payload = {
          ref: clean,
          source: source,
          device: device,
          medium: params.get('utm_medium') || '',
          campaign: params.get('utm_campaign') || '',
          isUnique: isUnique,
          path: window.location.pathname,
          timestamp: Date.now()
        };

        // Local cache sync
        try {
          const clicks = JSON.parse(localStorage.getItem('haichain_referral_clicks') || '[]');
          clicks.unshift(payload);
          if (clicks.length > 50) clicks.pop();
          localStorage.setItem('haichain_referral_clicks', JSON.stringify(clicks));
        } catch (_) {}

        // Send Beacon to Edge
        try {
          const beaconBody = JSON.stringify(payload);
          if (navigator.sendBeacon) {
            navigator.sendBeacon('/api/referral/click', new Blob([beaconBody], { type: 'application/json' }));
          } else {
            fetch('/api/referral/click', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: beaconBody,
              keepalive: true
            }).catch(() => {});
          }
        } catch (_) {}
      }
    } catch (_) {}
  }"""

if old_init_ref in content:
    content = content.replace(old_init_ref, new_init_ref, 1)
    print("Replaced initReferralTracking successfully!")
else:
    print("Could not find old_init_ref!")

with open('sale-controller.js', 'w', encoding='utf-8') as f:
    f.write(content)
