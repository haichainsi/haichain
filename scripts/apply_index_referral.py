import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_script = """    <!-- HAICHAIN Genesis Referral Tracker & Dynamic Welcome Banner -->
  <script>
    (function() {
      try {
        var p = new URLSearchParams(window.location.search);
        var ref = p.get('ref') || p.get('referrer') || p.get('inviter');
        if (ref && ref.trim().length >= 4) {
          var cleanRef = ref.trim();
          localStorage.setItem('haichain_ref', cleanRef);
          localStorage.setItem('haichain_ref_captured_at', new Date().toISOString());
        }

        // Show welcome banner if referral exists
        document.addEventListener('DOMContentLoaded', function() {
          var activeRef = ref || localStorage.getItem('haichain_ref');
          var banner = document.getElementById('referral-welcome-banner');
          var textEl = document.getElementById('referral-welcome-text');
          var ctaEl = document.getElementById('referral-welcome-cta');
          var ctaText = document.getElementById('referral-welcome-cta-text');
          if (activeRef && banner && textEl) {
            var shortRef = activeRef.slice(0, 6) + '...' + activeRef.slice(-4);
            var isVi = (localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang') || '').toLowerCase() === 'vi';
            if (isVi) {
              textEl.textContent = '🎉 Bạn nhận được lời mời từ ' + shortRef + '! Nhận thêm +5% Bonus $HAISI khi nạp.';
              if (ctaText) ctaText.textContent = 'Nhận +5% Bonus Ngay →';
            } else {
              textEl.textContent = '🎉 Invited by Genesis Backer ' + shortRef + '! Claim +5% Bonus $HAISI on your deposit.';
              if (ctaText) ctaText.textContent = 'Claim +5% Bonus →';
            }
            if (ctaEl) ctaEl.href = '/dashboard?tab=preseed&ref=' + encodeURIComponent(activeRef);
            banner.classList.remove('hidden');
          }
        });
      } catch (_) {}
    })();
  </script>"""

new_script = """    <!-- HAICHAIN Genesis Referral Tracker, Telemetry & Dynamic Welcome Banner -->
  <script>
    (function() {
      try {
        var p = new URLSearchParams(window.location.search);
        var ref = p.get('ref') || p.get('referrer') || p.get('inviter');
        if (ref && ref.trim().length >= 4) {
          var cleanRef = ref.trim();
          localStorage.setItem('haichain_ref', cleanRef);
          localStorage.setItem('haichain_ref_captured_at', new Date().toISOString());

          // 1. Detect Traffic Source & Campaign
          var utmSource = (p.get('utm_source') || '').toLowerCase();
          var detectedSource = 'Direct / Private Chat';
          if (utmSource) {
            if (utmSource === 'twitter' || utmSource === 'x') detectedSource = 'X (Twitter)';
            else if (utmSource === 'telegram' || utmSource === 'tg') detectedSource = 'Telegram';
            else if (utmSource === 'facebook' || utmSource === 'fb') detectedSource = 'Facebook';
            else if (utmSource === 'linkedin') detectedSource = 'LinkedIn';
            else if (utmSource === 'youtube') detectedSource = 'YouTube';
            else if (utmSource === 'discord') detectedSource = 'Discord';
            else if (utmSource === 'tiktok') detectedSource = 'TikTok';
            else detectedSource = utmSource.charAt(0).toUpperCase() + utmSource.slice(1);
          } else if (document.referrer) {
            try {
              var refHost = new URL(document.referrer, window.location.href).hostname.toLowerCase();
              if (refHost.indexOf('t.co') !== -1 || refHost.indexOf('twitter.com') !== -1 || refHost.indexOf('x.com') !== -1) {
                detectedSource = 'X (Twitter)';
              } else if (refHost.indexOf('t.me') !== -1 || refHost.indexOf('telegram.org') !== -1) {
                detectedSource = 'Telegram';
              } else if (refHost.indexOf('facebook.com') !== -1 || refHost.indexOf('fb.com') !== -1) {
                detectedSource = 'Facebook';
              } else if (refHost.indexOf('linkedin.com') !== -1) {
                detectedSource = 'LinkedIn';
              } else if (refHost.indexOf('google.') !== -1 || refHost.indexOf('bing.') !== -1 || refHost.indexOf('duckduckgo.') !== -1) {
                detectedSource = 'Search Engine';
              } else if (refHost.indexOf('haichain.si') === -1 && refHost !== window.location.hostname) {
                detectedSource = refHost.replace(/^www\\./, '');
              }
            } catch (_) {}
          }

          // 2. Device Detection
          var isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
          var device = isMobile ? 'Mobile' : 'Desktop';

          // 3. Uniqueness Check per Session
          var sessionKey = 'haichain_ref_hit_' + cleanRef.toLowerCase();
          var isUnique = !sessionStorage.getItem(sessionKey);
          sessionStorage.setItem(sessionKey, '1');

          var clickPayload = {
            ref: cleanRef,
            source: detectedSource,
            device: device,
            medium: p.get('utm_medium') || '',
            campaign: p.get('utm_campaign') || '',
            isUnique: isUnique,
            path: window.location.pathname,
            timestamp: Date.now()
          };

          // 4. Client-side local cache sync
          try {
            var localClicks = JSON.parse(localStorage.getItem('haichain_referral_clicks') || '[]');
            localClicks.unshift(clickPayload);
            if (localClicks.length > 50) localClicks.pop();
            localStorage.setItem('haichain_referral_clicks', JSON.stringify(localClicks));
          } catch (_) {}

          // 5. Send Telemetry to Edge Worker
          try {
            var beaconBody = JSON.stringify(clickPayload);
            if (navigator.sendBeacon) {
              navigator.sendBeacon('/api/referral/click', new Blob([beaconBody], { type: 'application/json' }));
            } else {
              fetch('/api/referral/click', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: beaconBody,
                keepalive: true
              }).catch(function() {});
            }
          } catch (_) {}
        }

        // Show welcome banner if referral exists
        document.addEventListener('DOMContentLoaded', function() {
          var activeRef = ref || localStorage.getItem('haichain_ref');
          var banner = document.getElementById('referral-welcome-banner');
          var textEl = document.getElementById('referral-welcome-text');
          var ctaEl = document.getElementById('referral-welcome-cta');
          var ctaText = document.getElementById('referral-welcome-cta-text');
          if (activeRef && banner && textEl) {
            var shortRef = activeRef.slice(0, 6) + '...' + activeRef.slice(-4);
            var isVi = (localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang') || '').toLowerCase() === 'vi';
            if (isVi) {
              textEl.textContent = '🎉 Bạn nhận được lời mời từ ' + shortRef + '! Nhận thêm +5% Bonus $HAISI khi nạp.';
              if (ctaText) ctaText.textContent = 'Nhận +5% Bonus Ngay →';
            } else {
              textEl.textContent = '🎉 Invited by Genesis Backer ' + shortRef + '! Claim +5% Bonus $HAISI on your deposit.';
              if (ctaText) ctaText.textContent = 'Claim +5% Bonus →';
            }
            if (ctaEl) ctaEl.href = '/dashboard?tab=preseed&ref=' + encodeURIComponent(activeRef);
            banner.classList.remove('hidden');
          }
        });
      } catch (_) {}
    })();
  </script>"""

if old_script in html:
    html = html.replace(old_script, new_script, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('app/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully patched index.html and app/index.html!")
else:
    print("Target old_script not found in index.html!")
