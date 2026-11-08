import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def patch_tray_logic(filepath):
    print(f"Updating tray logic in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the helper and cleaner provider click logic
    helper_code = '''    function closeAllWalletTrays(exceptTrayId) {
      const trays = [
        { id: 'phantom-mobile-tray', arrow: 'phantom-arrow' },
        { id: 'solflare-mobile-tray', arrow: 'solflare-arrow' },
        { id: 'metamask-mobile-tray', arrow: 'metamask-arrow' },
        { id: 'manual-address-panel', arrow: 'manual-arrow' }
      ];
      trays.forEach(item => {
        if (item.id !== exceptTrayId) {
          const el = document.getElementById(item.id);
          const arr = document.getElementById(item.arrow);
          if (el) el.classList.add('hidden');
          if (arr) arr.classList.remove('rotate-90');
        }
      });
    }

'''

    if 'function closeAllWalletTrays' not in content:
        target = "document.querySelectorAll('.wallet-provider-btn').forEach(btn => {"
        if target in content:
            content = content.replace(target, helper_code + '    ' + target, 1)
            print(f"[{filepath}] Added closeAllWalletTrays helper.")

    # In Phantom mobile toggle
    phantom_old = '''          } else if (isMobileDevice()) {
            // Smoothly toggle inline Phantom mobile action tray
            const tray = document.getElementById('phantom-mobile-tray');
            const arrow = document.getElementById('phantom-arrow');
            const sTray = document.getElementById('solflare-mobile-tray');
            const sArrow = document.getElementById('solflare-arrow');
            const mPanel = document.getElementById('manual-address-panel');
            const mArrow = document.getElementById('manual-arrow');

            if (sTray) sTray.classList.add('hidden');
            if (sArrow) sArrow.classList.remove('rotate-90');
            if (mPanel) mPanel.classList.add('hidden');
            if (mArrow) mArrow.classList.remove('rotate-90');

            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }'''

    phantom_new = '''          } else if (isMobileDevice()) {
            closeAllWalletTrays('phantom-mobile-tray');
            const tray = document.getElementById('phantom-mobile-tray');
            const arrow = document.getElementById('phantom-arrow');
            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }'''

    if phantom_old in content:
        content = content.replace(phantom_old, phantom_new, 1)
        print(f"[{filepath}] Updated Phantom mobile tray toggle.")

    # In Solflare mobile toggle
    solflare_old = '''          } else if (isMobileDevice()) {
            // Smoothly toggle inline Solflare mobile action tray
            const tray = document.getElementById('solflare-mobile-tray');
            const arrow = document.getElementById('solflare-arrow');
            const pTray = document.getElementById('phantom-mobile-tray');
            const pArrow = document.getElementById('phantom-arrow');
            const mPanel = document.getElementById('manual-address-panel');
            const mArrow = document.getElementById('manual-arrow');

            if (pTray) pTray.classList.add('hidden');
            if (pArrow) pArrow.classList.remove('rotate-90');
            if (mPanel) mPanel.classList.add('hidden');
            if (mArrow) mArrow.classList.remove('rotate-90');

            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }'''

    solflare_new = '''          } else if (isMobileDevice()) {
            closeAllWalletTrays('solflare-mobile-tray');
            const tray = document.getElementById('solflare-mobile-tray');
            const arrow = document.getElementById('solflare-arrow');
            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }'''

    if solflare_old in content:
        content = content.replace(solflare_old, solflare_new, 1)
        print(f"[{filepath}] Updated Solflare mobile tray toggle.")

    # In MetaMask mobile toggle
    metamask_old = '''          } else if (isMobileDevice()) {
            // Smoothly toggle inline MetaMask mobile action tray
            const tray = document.getElementById('metamask-mobile-tray');
            const arrow = document.getElementById('metamask-arrow');
            const pTray = document.getElementById('phantom-mobile-tray');
            const pArrow = document.getElementById('phantom-arrow');
            const sTray = document.getElementById('solflare-mobile-tray');
            const sArrow = document.getElementById('solflare-arrow');
            const mPanel = document.getElementById('manual-address-panel');
            const mArrow = document.getElementById('manual-arrow');

            if (pTray) pTray.classList.add('hidden');
            if (pArrow) pArrow.classList.remove('rotate-90');
            if (sTray) sTray.classList.add('hidden');
            if (sArrow) sArrow.classList.remove('rotate-90');
            if (mPanel) mPanel.classList.add('hidden');
            if (mArrow) mArrow.classList.remove('rotate-90');

            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }'''

    metamask_new = '''          } else if (isMobileDevice()) {
            closeAllWalletTrays('metamask-mobile-tray');
            const tray = document.getElementById('metamask-mobile-tray');
            const arrow = document.getElementById('metamask-arrow');
            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }'''

    if metamask_old in content:
        content = content.replace(metamask_old, metamask_new, 1)
        print(f"[{filepath}] Updated MetaMask mobile tray toggle.")

    # In Manual provider toggle
    manual_old = '''        // 4. MANUAL ADDRESS (Show/Hide Input with Clipboard Paste)
        if (provider === 'manual') {
          const mPanel = document.getElementById('manual-address-panel');
          const mArrow = document.getElementById('manual-arrow');
          const pTray = document.getElementById('phantom-mobile-tray');
          const pArrow = document.getElementById('phantom-arrow');
          const sTray = document.getElementById('solflare-mobile-tray');
          const sArrow = document.getElementById('solflare-arrow');

          if (pTray) pTray.classList.add('hidden');
          if (pArrow) pArrow.classList.remove('rotate-90');
          if (sTray) sTray.classList.add('hidden');
          if (sArrow) sArrow.classList.remove('rotate-90');

          if (mPanel) {
            const isHidden = mPanel.classList.contains('hidden');
            if (isHidden) {
              mPanel.classList.remove('hidden');
              if (mArrow) mArrow.classList.add('rotate-90');
              manualWalletInput.focus();
            } else {
              mPanel.classList.add('hidden');
              if (mArrow) mArrow.classList.remove('rotate-90');
            }
          }
          return;
        }'''

    manual_new = '''        // 4. MANUAL ADDRESS (Show/Hide Input with Clipboard Paste)
        if (provider === 'manual') {
          closeAllWalletTrays('manual-address-panel');
          const mPanel = document.getElementById('manual-address-panel');
          const mArrow = document.getElementById('manual-arrow');
          if (mPanel) {
            const isHidden = mPanel.classList.contains('hidden');
            if (isHidden) {
              mPanel.classList.remove('hidden');
              if (mArrow) mArrow.classList.add('rotate-90');
              manualWalletInput.focus();
            } else {
              mPanel.classList.add('hidden');
              if (mArrow) mArrow.classList.remove('rotate-90');
            }
          }
          return;
        }'''

    if manual_old in content:
        content = content.replace(manual_old, manual_new, 1)
        print(f"[{filepath}] Updated Manual address panel toggle.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{filepath}] Done.\n")

patch_tray_logic('dashboard.html')
patch_tray_logic('app/dashboard.html')
