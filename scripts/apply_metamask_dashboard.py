import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def patch_dashboard(filepath):
    print(f"--- Patching {filepath} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add MetaMask Card into Modal
    # Locate solflare card end
    solflare_card_end = '<!-- 2. Solflare Card with Nested Mobile Action Tray -->'
    if 'data-provider="metamask"' in content:
        print(f"[{filepath}] MetaMask card already present in modal markup.")
    else:
        metamask_html = '''        <!-- 3. MetaMask Card with Nested Mobile Action Tray -->
        <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 overflow-hidden transition-all duration-200">
          <button class="wallet-provider-btn w-full p-2.5 sm:p-3 flex items-center justify-between text-left cursor-pointer active:opacity-75" data-provider="metamask">
            <div class="flex items-center space-x-3 min-w-0">
              <div class="w-8 h-8 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 flex items-center justify-center text-lg shrink-0">
                🦊
              </div>
              <div class="min-w-0">
                <div class="font-semibold text-xs sm:text-sm text-black dark:text-white truncate" data-i18n="modal.walletMetamask">MetaMask Wallet</div>
                <div class="text-[11px] text-neutral-500 truncate" id="metamask-status-desc" data-i18n="modal.walletMetamaskDesc">EVM Multi-Chain & Solana Snap (Ethereum, BSC, Arbitrum)</div>
              </div>
            </div>
            <span id="metamask-arrow" class="text-xs font-mono text-neutral-400 transition-transform duration-200 shrink-0">&rarr;</span>
          </button>
          
          <!-- Inline MetaMask Mobile Action Tray -->
          <div id="metamask-mobile-tray" class="hidden px-2.5 pb-2.5 pt-1 space-y-1.5 border-t border-neutral-200 dark:border-neutral-800/80 bg-neutral-100/60 dark:bg-neutral-900/80">
            <button type="button" id="btn-tray-metamask-app" class="w-full py-2 px-3 rounded-xl bg-black text-white dark:bg-white dark:text-black font-semibold text-[11px] flex items-center justify-between transition-opacity active:opacity-75 cursor-pointer">
              <span class="flex items-center space-x-1.5 truncate">
                <span>🦊</span>
                <span>Open in MetaMask App (Mobile Browser)</span>
              </span>
              <span class="font-mono text-xs">&rarr;</span>
            </button>
            <div class="grid grid-cols-2 gap-1.5">
              <button type="button" id="btn-tray-metamask-connect" class="py-1.5 px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-800 text-black dark:text-white text-[10px] font-medium flex items-center justify-center space-x-1 transition-opacity active:opacity-75 cursor-pointer truncate">
                <span>⚡</span>
                <span>Connect Browser</span>
              </button>
              <a href="https://metamask.io/download/" target="_blank" rel="noopener" class="py-1.5 px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-800 text-black dark:text-white text-[10px] font-medium flex items-center justify-center space-x-1 transition-opacity active:opacity-75 cursor-pointer truncate">
                <span>📥</span>
                <span>Get MetaMask</span>
              </a>
            </div>
          </div>
        </div>

'''
        # Find where Solflare card ends (before "<!-- 3. Custom Solana Address" or "<!-- Custom Solana Address")
        pattern = r'(<!--\s*2\.\s*Solflare Card[\s\S]*?</div>\s*</div>\s*\n)'
        m = re.search(pattern, content)
        if m:
            content = content[:m.end()] + metamask_html + content[m.end():]
            print(f"[{filepath}] Successfully inserted MetaMask HTML card.")
        else:
            print(f"[{filepath}] ERROR: Could not find Solflare card end in HTML.")

    # 2. Add getMetaMaskProvider helper function
    if 'function getMetaMaskProvider()' not in content:
        helper_code = '''    // Helper: Detect MetaMask provider safely across desktop extensions & mobile
    function getMetaMaskProvider() {
      if (typeof window === 'undefined') return null;
      if (window.ethereum?.providers && Array.isArray(window.ethereum.providers)) {
        return window.ethereum.providers.find(p => p.isMetaMask && !p.isPhantom) || window.ethereum.providers.find(p => p.isMetaMask) || window.ethereum;
      }
      if (window.ethereum?.isMetaMask) {
        return window.ethereum;
      }
      if (window.ethereum) {
        return window.ethereum;
      }
      return null;
    }

'''
        # Insert before function updateWalletBtnUI
        target = 'function updateWalletBtnUI()'
        if target in content:
            content = content.replace(target, helper_code + '    ' + target, 1)
            print(f"[{filepath}] Inserted getMetaMaskProvider() helper.")
        else:
            print(f"[{filepath}] ERROR: Could not find updateWalletBtnUI() target.")

    # 3. Update normalizeProviderName
    old_norm = '''function normalizeProviderName(name) {
      if (!name) return 'Phantom';
      const lower = String(name).toLowerCase();
      if (lower.includes('solflare')) return 'Solflare';
      if (lower.includes('passkey') || lower.includes('faceid')) return 'FaceID / Windows Hello Passkey';
      if (lower.includes('custom')) return 'Custom Address';
      if (lower.includes('phantom')) return 'Phantom';
      return name;
    }'''

    new_norm = '''function normalizeProviderName(name) {
      if (!name) return 'Phantom';
      const lower = String(name).toLowerCase();
      if (lower.includes('metamask')) return 'MetaMask';
      if (lower.includes('solflare')) return 'Solflare';
      if (lower.includes('passkey') || lower.includes('faceid')) return 'FaceID / Windows Hello Passkey';
      if (lower.includes('custom')) return 'Custom Address';
      if (lower.includes('phantom')) return 'Phantom';
      return name;
    }'''

    if old_norm in content:
        content = content.replace(old_norm, new_norm, 1)
        print(f"[{filepath}] Updated normalizeProviderName().")

    # 4. Update updateWalletBtnUI to render MetaMask badge & balance
    old_btn_ui = '''        if (isBiometric) {
          wBtnText.innerHTML = `
            <span class="flex items-center space-x-1 sm:space-x-1.5">
              <i data-lucide="fingerprint" class="w-3 h-3 text-emerald-500 shrink-0"></i>
              <span class="font-mono text-[10px] sm:text-xs font-semibold text-emerald-600 dark:text-emerald-400 whitespace-nowrap"><span class="hidden md:inline text-neutral-400">Passkey: </span>${displayAddr}</span>
            </span>
          `;
        } else {
          wBtnText.innerHTML = `
            <span class="flex items-center space-x-1 sm:space-x-1.5">
              <span class="font-mono text-[10px] sm:text-xs font-semibold whitespace-nowrap">${displayAddr}</span>
              <span class="hidden sm:inline font-mono opacity-70 text-[10px]"> (${userWallet.solBalance || '0.00'} SOL)</span>
            </span>
          `;
        }'''

    new_btn_ui = '''        if (isBiometric) {
          wBtnText.innerHTML = `
            <span class="flex items-center space-x-1 sm:space-x-1.5">
              <i data-lucide="fingerprint" class="w-3 h-3 text-emerald-500 shrink-0"></i>
              <span class="font-mono text-[10px] sm:text-xs font-semibold text-emerald-600 dark:text-emerald-400 whitespace-nowrap"><span class="hidden md:inline text-neutral-400">Passkey: </span>${displayAddr}</span>
            </span>
          `;
        } else if (userWallet.isEVM || (userWallet.provider && userWallet.provider.toLowerCase().includes('metamask'))) {
          const balText = userWallet.evmBalance !== null && userWallet.evmBalance !== undefined ? userWallet.evmBalance + ' ETH' : (userWallet.solBalance || 'EVM');
          wBtnText.innerHTML = `
            <span class="flex items-center space-x-1 sm:space-x-1.5">
              <span class="text-xs shrink-0">🦊</span>
              <span class="font-mono text-[10px] sm:text-xs font-semibold whitespace-nowrap">${displayAddr}</span>
              <span class="hidden sm:inline font-mono opacity-70 text-[10px]"> (${balText})</span>
            </span>
          `;
        } else {
          wBtnText.innerHTML = `
            <span class="flex items-center space-x-1 sm:space-x-1.5">
              <span class="font-mono text-[10px] sm:text-xs font-semibold whitespace-nowrap">${displayAddr}</span>
              <span class="hidden sm:inline font-mono opacity-70 text-[10px]"> (${userWallet.solBalance || '0.00'} SOL)</span>
            </span>
          `;
        }'''

    if old_btn_ui in content:
        content = content.replace(old_btn_ui, new_btn_ui, 1)
        print(f"[{filepath}] Updated updateWalletBtnUI() display.")

    # 5. Update openAccountModal() badge and explorer
    old_account_badge = '''        const prov = (userWallet.provider || 'Phantom').toLowerCase();
        if (badgeIcon) {
          if (prov.includes('phantom')) {
            badgeIcon.className = "w-10 h-10 rounded-2xl bg-[#AB9FF2]/20 border border-[#AB9FF2]/40 flex items-center justify-center shrink-0 shadow-sm p-1.5";
            badgeIcon.innerHTML = '<svg class="w-full h-full" viewBox="0 0 128 128" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="128" height="128" rx="28" fill="#AB9FF2"/><path d="M106.5 64h-10.8c0-19.8-16.1-35.9-35.9-35.9S23.9 44.2 23.9 64c0 19.8 16.1 35.9 35.9 35.9 5 0 9.8-1 14.2-2.9l-4.1-13.6c-3.1 1.3-6.5 2-10.1 2-13.4 0-24.3-10.9-24.3-24.3 0-13.4 10.9-24.3 24.3-24.3 12.7 0 23.1 9.8 24.2 22.3H72c-1.4 0-2.5 1.1-2.5 2.5s1.1 2.5 2.5 2.5h34.5c1.4 0 2.5-1.1 2.5-2.5s-1.1-1.6-2.5-1.6z" fill="#FFFFFF"/><ellipse cx="49" cy="56" rx="5" ry="7" fill="#222222"/><ellipse cx="73" cy="56" rx="5" ry="7" fill="#222222"/></svg>';
          } else if (prov.includes('solflare')) {
            badgeIcon.className = "w-10 h-10 rounded-2xl bg-amber-500/15 border border-amber-500/30 flex items-center justify-center shrink-0 shadow-sm text-xl";
            badgeIcon.innerHTML = '<span>🔥</span>';
          } else {
            badgeIcon.className = "w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 border border-neutral-300 dark:border-neutral-700 flex items-center justify-center shrink-0 shadow-sm";
            badgeIcon.innerHTML = '<i data-lucide="wallet" class="w-5 h-5 text-neutral-800 dark:text-neutral-200"></i>';
          }
        }'''

    new_account_badge = '''        const prov = (userWallet.provider || 'Phantom').toLowerCase();
        if (badgeIcon) {
          if (prov.includes('metamask')) {
            badgeIcon.className = "w-10 h-10 rounded-2xl bg-amber-500/15 border border-amber-500/30 flex items-center justify-center shrink-0 shadow-sm text-xl";
            badgeIcon.innerHTML = '<span>🦊</span>';
          } else if (prov.includes('phantom')) {
            badgeIcon.className = "w-10 h-10 rounded-2xl bg-[#AB9FF2]/20 border border-[#AB9FF2]/40 flex items-center justify-center shrink-0 shadow-sm p-1.5";
            badgeIcon.innerHTML = '<svg class="w-full h-full" viewBox="0 0 128 128" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="128" height="128" rx="28" fill="#AB9FF2"/><path d="M106.5 64h-10.8c0-19.8-16.1-35.9-35.9-35.9S23.9 44.2 23.9 64c0 19.8 16.1 35.9 35.9 35.9 5 0 9.8-1 14.2-2.9l-4.1-13.6c-3.1 1.3-6.5 2-10.1 2-13.4 0-24.3-10.9-24.3-24.3 0-13.4 10.9-24.3 24.3-24.3 12.7 0 23.1 9.8 24.2 22.3H72c-1.4 0-2.5 1.1-2.5 2.5s1.1 2.5 2.5 2.5h34.5c1.4 0 2.5-1.1 2.5-2.5s-1.1-1.6-2.5-1.6z" fill="#FFFFFF"/><ellipse cx="49" cy="56" rx="5" ry="7" fill="#222222"/><ellipse cx="73" cy="56" rx="5" ry="7" fill="#222222"/></svg>';
          } else if (prov.includes('solflare')) {
            badgeIcon.className = "w-10 h-10 rounded-2xl bg-amber-500/15 border border-amber-500/30 flex items-center justify-center shrink-0 shadow-sm text-xl";
            badgeIcon.innerHTML = '<span>🔥</span>';
          } else {
            badgeIcon.className = "w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 border border-neutral-300 dark:border-neutral-700 flex items-center justify-center shrink-0 shadow-sm";
            badgeIcon.innerHTML = '<i data-lucide="wallet" class="w-5 h-5 text-neutral-800 dark:text-neutral-200"></i>';
          }
        }'''

    if old_account_badge in content:
        content = content.replace(old_account_badge, new_account_badge, 1)
        print(f"[{filepath}] Updated openAccountModal() badge icon.")

    # Update explorer link in openAccountModal()
    old_exp = '''      const expLink = document.getElementById('account-explorer-link');
      if (expLink) {
        expLink.href = `https://explorer.solana.com/address/${userWallet.address}?cluster=devnet`;
      }'''

    new_exp = '''      const expLink = document.getElementById('account-explorer-link');
      if (expLink) {
        if (userWallet.isEVM || (userWallet.provider && userWallet.provider.toLowerCase().includes('metamask'))) {
          expLink.href = `https://etherscan.io/address/${userWallet.address}`;
        } else {
          expLink.href = `https://explorer.solana.com/address/${userWallet.address}?cluster=devnet`;
        }
      }'''

    if old_exp in content:
        content = content.replace(old_exp, new_exp, 1)
        print(f"[{filepath}] Updated account-explorer-link.")

    # 6. Add MetaMask Tray Button Event Listeners
    if 'btnTrayMetaMaskApp' not in content:
        tray_listeners = '''    // Wire Up MetaMask Mobile Action Tray
    const btnTrayMetaMaskApp = document.getElementById('btn-tray-metamask-app');
    if (btnTrayMetaMaskApp) {
      btnTrayMetaMaskApp.addEventListener('click', () => {
        const cleanHost = window.location.host;
        const cleanPath = window.location.pathname;
        window.location.href = `https://metamask.app.link/dapp/${cleanHost}${cleanPath}`;
      });
    }

    const btnTrayMetaMaskConnect = document.getElementById('btn-tray-metamask-connect');
    if (btnTrayMetaMaskConnect) {
      btnTrayMetaMaskConnect.addEventListener('click', async () => {
        const mm = getMetaMaskProvider();
        if (mm) {
          try {
            const accounts = await mm.request({ method: 'eth_requestAccounts' });
            if (accounts && accounts[0]) {
              await setConnectedWallet(accounts[0], 'MetaMask');
              walletConnectModal.classList.add('hidden');
              openAccountModal();
            }
          } catch (e) {
            console.warn('MetaMask connect tray error:', e);
          }
        } else {
          const cleanHost = window.location.host;
          const cleanPath = window.location.pathname;
          window.location.href = `https://metamask.app.link/dapp/${cleanHost}${cleanPath}`;
        }
      });
    }

'''
        # Insert before btnTrayPhantomApp
        target = "const btnTrayPhantomApp = document.getElementById('btn-tray-phantom-app');"
        if target in content:
            content = content.replace(target, tray_listeners + '    ' + target, 1)
            print(f"[{filepath}] Inserted MetaMask mobile tray event listeners.")

    # 7. Update setConnectedWallet() to handle EVM
    old_set_wallet = '''    async function setConnectedWallet(pubkeyStr, providerName) {
      providerName = normalizeProviderName(providerName);
      let solBalStr = "0.000";
      if (solanaConnection && window.solanaWeb3) {
        try {
          const pk = new solanaWeb3.PublicKey(pubkeyStr);
          const rawLamports = await solanaConnection.getBalance(pk);
          solBalStr = (Number(rawLamports) / Number(solanaWeb3.LAMPORTS_PER_SOL)).toFixed(3);
        } catch (e) {
          console.warn("Could not fetch balance for:", pubkeyStr, e);
        }
      }

      userWallet = {
        address: pubkeyStr,
        provider: providerName,
        solBalance: solBalStr,
        biometric: providerName.toLowerCase().includes('passkey') || providerName.toLowerCase().includes('faceid')
      };'''

    new_set_wallet = '''    async function setConnectedWallet(pubkeyStr, providerName) {
      providerName = normalizeProviderName(providerName);
      let solBalStr = "0.000";
      let evmBalStr = null;
      const isEVM = pubkeyStr.startsWith('0x') || providerName.toLowerCase().includes('metamask');

      if (isEVM) {
        const mm = getMetaMaskProvider() || window.ethereum;
        if (mm && mm.request) {
          try {
            const rawHex = await mm.request({ method: 'eth_getBalance', params: [pubkeyStr, 'latest'] });
            if (rawHex) {
              const wei = BigInt(rawHex);
              const eth = Number(wei) / 1e18;
              evmBalStr = eth.toFixed(4);
            }
          } catch (e) {
            console.warn("Could not fetch EVM balance:", e);
          }
        }
      } else if (solanaConnection && window.solanaWeb3) {
        try {
          const pk = new solanaWeb3.PublicKey(pubkeyStr);
          const rawLamports = await solanaConnection.getBalance(pk);
          solBalStr = (Number(rawLamports) / Number(solanaWeb3.LAMPORTS_PER_SOL)).toFixed(3);
        } catch (e) {
          console.warn("Could not fetch balance for:", pubkeyStr, e);
        }
      }

      userWallet = {
        address: pubkeyStr,
        provider: providerName,
        solBalance: isEVM ? (evmBalStr !== null ? evmBalStr + ' ETH' : '0.000 ETH') : solBalStr,
        evmBalance: evmBalStr,
        isEVM: isEVM,
        biometric: providerName.toLowerCase().includes('passkey') || providerName.toLowerCase().includes('faceid')
      };'''

    if old_set_wallet in content:
        content = content.replace(old_set_wallet, new_set_wallet, 1)
        print(f"[{filepath}] Updated setConnectedWallet() for EVM support.")

    # 8. Add provider === 'metamask' in wallet-provider-btn click handler
    if "if (provider === 'metamask')" not in content:
        metamask_click_handler = '''        // METAMASK WALLET (EVM & Solana Snap Support)
        if (provider === 'metamask') {
          const mm = getMetaMaskProvider();
          if (mm) {
            try {
              walletBtnText.textContent = isVi ? "Đang kết nối MetaMask..." : "Connecting MetaMask...";
              const accounts = await mm.request({ method: 'eth_requestAccounts' });
              if (!accounts || accounts.length === 0) {
                throw new Error("No accounts authorized in MetaMask");
              }
              const account = accounts[0];
              let chainId = null;
              try {
                chainId = await mm.request({ method: 'eth_chainId' });
              } catch (_) {}

              await setConnectedWallet(account, 'MetaMask');
              walletConnectModal.classList.add('hidden');
              const shortAddr = account.slice(0, 6) + '...' + account.slice(-4);
              showToast({
                title: 'MetaMask Connected',
                message: shortAddr + (chainId ? ` (Chain ${parseInt(chainId, 16)})` : ''),
                icon: 'check-circle'
              });
              openAccountModal();

              if (mm.on && !mm._haichainListenersBound) {
                mm._haichainListenersBound = true;
                mm.on('accountsChanged', (newAccounts) => {
                  if (!newAccounts || newAccounts.length === 0) {
                    userWallet = null;
                    localStorage.removeItem('haichain-connected-wallet');
                    updateWalletBtnUI();
                  } else {
                    setConnectedWallet(newAccounts[0], 'MetaMask');
                  }
                });
                mm.on('chainChanged', () => {
                  if (userWallet && userWallet.provider === 'MetaMask') {
                    setConnectedWallet(userWallet.address, 'MetaMask');
                  }
                });
              }
            } catch (err) {
              console.error("MetaMask connection error:", err);
              updateWalletBtnUI();
              if (err.code === 4001) {
                showToast({
                  title: 'MetaMask',
                  message: isVi ? 'Người dùng đã hủy kết nối' : 'Connection rejected',
                  icon: 'alert-triangle'
                });
              } else {
                walletNoticeText.innerHTML = '<strong>MetaMask Error:</strong> ' + (err.message || err);
                walletNoticeBox.classList.remove('hidden');
                safeCreateIcons();
              }
            }
          } else if (isMobileDevice()) {
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
            }
          } else {
            walletNoticeText.innerHTML = isVi
              ? "<strong>Chưa phát hiện tiện ích MetaMask</strong> trên trình duyệt của bạn. Hãy cài đặt extension MetaMask hoặc mở trang web trên ứng dụng MetaMask Mobile."
              : "<strong>MetaMask extension not detected</strong>. Please install the MetaMask extension or open this URL inside MetaMask Mobile App.";
            walletInstallLink.href = "https://metamask.io/download/";
            walletInstallLink.parentElement.classList.remove('hidden');
            walletNoticeBox.classList.remove('hidden');
            safeCreateIcons();
          }
          return;
        }

'''
        # Insert before // 4. MANUAL ADDRESS or before // 3. SOLFLARE WALLET
        target = "// 3. SOLFLARE WALLET"
        if target in content:
            content = content.replace(target, metamask_click_handler + '        ' + target, 1)
            print(f"[{filepath}] Inserted MetaMask provider click handler.")
        else:
            print(f"[{filepath}] ERROR: Could not find target // 3. SOLFLARE WALLET.")

    # 9. Also update getActiveWeb3Wallet() to recognize MetaMask
    old_active_web3 = '''    function getActiveWeb3Wallet() {
      const phantom = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
      const solflare = window.solflare?.isSolflare ? window.solflare : null;

      // 1. Direct window provider presence with active public key
      if (phantom && phantom.publicKey) {
        return {
          instance: phantom,
          provider: 'Phantom',
          address: phantom.publicKey.toString()
        };
      }
      if (solflare && solflare.publicKey) {
        return {
          instance: solflare,
          provider: 'Solflare',
          address: solflare.publicKey.toString()
        };
      }

      // 2. User wallet state in memory / localStorage
      if (userWallet && userWallet.address) {
        const provLower = (userWallet.provider || '').toLowerCase();
        if (provLower.includes('phantom')) {
          return {
            instance: phantom || (window.solana && window.solana.isPhantom ? window.solana : null),
            provider: 'Phantom',
            address: userWallet.address
          };
        }
        if (provLower.includes('solflare')) {
          return {
            instance: solflare || null,
            provider: 'Solflare',
            address: userWallet.address
          };
        }
      }
      return null;
    }'''

    new_active_web3 = '''    function getActiveWeb3Wallet() {
      const phantom = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
      const solflare = window.solflare?.isSolflare ? window.solflare : null;
      const mm = getMetaMaskProvider();

      // 1. Direct window provider presence with active public key
      if (phantom && phantom.publicKey) {
        return {
          instance: phantom,
          provider: 'Phantom',
          address: phantom.publicKey.toString()
        };
      }
      if (solflare && solflare.publicKey) {
        return {
          instance: solflare,
          provider: 'Solflare',
          address: solflare.publicKey.toString()
        };
      }
      if (mm && mm.selectedAddress) {
        return {
          instance: mm,
          provider: 'MetaMask',
          address: mm.selectedAddress
        };
      }

      // 2. User wallet state in memory / localStorage
      if (userWallet && userWallet.address) {
        const provLower = (userWallet.provider || '').toLowerCase();
        if (provLower.includes('metamask')) {
          return {
            instance: mm || window.ethereum,
            provider: 'MetaMask',
            address: userWallet.address
          };
        }
        if (provLower.includes('phantom')) {
          return {
            instance: phantom || (window.solana && window.solana.isPhantom ? window.solana : null),
            provider: 'Phantom',
            address: userWallet.address
          };
        }
        if (provLower.includes('solflare')) {
          return {
            instance: solflare || null,
            provider: 'Solflare',
            address: userWallet.address
          };
        }
      }
      return null;
    }'''

    if old_active_web3 in content:
        content = content.replace(old_active_web3, new_active_web3, 1)
        print(f"[{filepath}] Updated getActiveWeb3Wallet() for MetaMask.")

    # 10. Update withdrawal authorization for MetaMask
    old_withdraw_auth = '''      // Require Cryptographic Authorization from connected wallet
      if (userWallet.provider === 'Phantom' || userWallet.provider === 'Solflare') {
        try {
          const web3Provider = userWallet.provider === 'Phantom' ? (window.phantom?.solana || window.solana) : window.solflare;
          if (web3Provider && typeof web3Provider.signMessage === 'function') {
            const msg = `HAICHAIN Master Vault Settlement Withdrawal:\\n\\nAmount: ${amount.toFixed(4)} USDT\\nRecipient: ${dest}\\nVault Owner: ${userWallet.address}\\nTimestamp: ${new Date().toISOString()}`;
            await web3Provider.signMessage(new TextEncoder().encode(msg), "utf8");
          }
        } catch (sigErr) {
          console.warn("Withdrawal authorization rejected:", sigErr);
          alert(isVi ? "Rút tiền đã hủy: Bạn đã từ chối ký xác thực giao dịch trên ví." : "Withdrawal Canceled: You rejected the cryptographic authorization signature.");
          return;
        }
      }'''

    new_withdraw_auth = '''      // Require Cryptographic Authorization from connected wallet
      if (userWallet.provider === 'MetaMask' || userWallet.isEVM) {
        const mm = getMetaMaskProvider() || window.ethereum;
        if (mm && mm.request) {
          try {
            const msg = `HAICHAIN Master Vault Settlement Withdrawal:\\n\\nAmount: ${amount.toFixed(4)} USDT\\nRecipient: ${dest}\\nVault Owner: ${userWallet.address}\\nTimestamp: ${new Date().toISOString()}`;
            await mm.request({
              method: 'personal_sign',
              params: [msg, userWallet.address]
            });
          } catch (sigErr) {
            console.warn("Withdrawal authorization rejected:", sigErr);
            alert(isVi ? "Rút tiền đã hủy: Bạn đã từ chối ký xác thực giao dịch trên ví MetaMask." : "Withdrawal Canceled: You rejected the MetaMask authorization signature.");
            return;
          }
        }
      } else if (userWallet.provider === 'Phantom' || userWallet.provider === 'Solflare') {
        try {
          const web3Provider = userWallet.provider === 'Phantom' ? (window.phantom?.solana || window.solana) : window.solflare;
          if (web3Provider && typeof web3Provider.signMessage === 'function') {
            const msg = `HAICHAIN Master Vault Settlement Withdrawal:\\n\\nAmount: ${amount.toFixed(4)} USDT\\nRecipient: ${dest}\\nVault Owner: ${userWallet.address}\\nTimestamp: ${new Date().toISOString()}`;
            await web3Provider.signMessage(new TextEncoder().encode(msg), "utf8");
          }
        } catch (sigErr) {
          console.warn("Withdrawal authorization rejected:", sigErr);
          alert(isVi ? "Rút tiền đã hủy: Bạn đã từ chối ký xác thực giao dịch trên ví." : "Withdrawal Canceled: You rejected the cryptographic authorization signature.");
          return;
        }
      }'''

    if old_withdraw_auth in content:
        content = content.replace(old_withdraw_auth, new_withdraw_auth, 1)
        print(f"[{filepath}] Updated withdrawal signature authorization for MetaMask.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{filepath}] Successfully updated and saved.\n")

patch_dashboard('dashboard.html')
patch_dashboard('app/dashboard.html')
