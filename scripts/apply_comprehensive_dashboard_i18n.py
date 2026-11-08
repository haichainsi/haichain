import re
from i18n_patch_dictionaries import i18n_keys, vesting_breakdown, dash_new_keys

def patch_i18n(file_path):
    print(f"\n================ Patching {file_path} ================")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for lang in ['kk', 'en', 'zh', 'fr', 'ko', 'es', 'ru', 'vi', 'hi', 'he']:
        keys = i18n_keys.get(lang, {})
        # Find exact position for "<lang>": {
        m = re.search(rf'"{lang}":\s*\{{\s*\n', content)
        if not m:
            print(f"ERROR: Lang {lang} not found in {file_path}")
            continue
        
        pos = m.end()
        injection = ""
        for k, v in keys.items():
            v_esc = v.replace('\\', '\\\\').replace('"', '\\"')
            injection += f'    "{k}": "{v_esc}",\n'
        
        content = content[:pos] + injection + content[pos:]
        print(f"  Inserted {len(keys)} keys into '{lang}'")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

def patch_dashboard(file_path):
    print(f"\n================ Patching {file_path} ================")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize CRLF
    content = content.replace('\r\n', '\n')

    # 1. Patch VESTING_VAULT_I18N
    v_start = content.find('const VESTING_VAULT_I18N = {')
    v_end = content.find('const DASH_NOTICES_I18N = {')
    if v_start == -1 or v_end == -1:
        print("ERROR: VESTING_VAULT_I18N boundaries not found")
        return
    
    vesting_block = content[v_start:v_end]
    for lang in ['en', 'vi', 'zh', 'ko', 'fr', 'es', 'ru', 'kk', 'hi', 'he']:
        val = vesting_breakdown.get(lang, '')
        val_esc = val.replace('\\', '\\\\').replace('"', '\\"')
        # Find "<lang>": { inside vesting_block
        m = re.search(rf'"{lang}":\s*\{{\s*\n', vesting_block)
        if m:
            pos = m.end()
            line = f'    "guaranteeVestingBreakdown": "{val_esc}",\n'
            vesting_block = vesting_block[:pos] + line + vesting_block[pos:]
            print(f"  Added guaranteeVestingBreakdown to VESTING_VAULT_I18N['{lang}']")
        else:
            print(f"  [WARN] {lang} not found in VESTING_VAULT_I18N")

    content = content[:v_start] + vesting_block + content[v_end:]

    # 2. Patch DASH_NOTICES_I18N
    d_start = content.find('const DASH_NOTICES_I18N = {')
    d_end = content.find('function getDashNotice(key) {')
    if d_start == -1 or d_end == -1:
        print("ERROR: DASH_NOTICES_I18N boundaries not found")
        return

    dash_block = content[d_start:d_end]
    for lang in ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he']:
        keys = dash_new_keys.get(lang, {})
        m = re.search(rf'"{lang}":\s*\{{\s*\n', dash_block)
        if m:
            pos = m.end()
            injection = ""
            for k, v in keys.items():
                v_esc = v.replace('\\', '\\\\').replace('"', '\\"')
                injection += f'    "{k}": "{v_esc}",\n'
            dash_block = dash_block[:pos] + injection + dash_block[pos:]
            print(f"  Added {len(keys)} keys to DASH_NOTICES_I18N['{lang}']")
        else:
            print(f"  [WARN] {lang} not found in DASH_NOTICES_I18N")

    content = content[:d_start] + dash_block + content[d_end:]

    # 3. Patch DOM Markup
    # Close button title
    s_close = '<button id="close-ai-hub-modal" type="button" class="w-9 h-9 rounded-full flex items-center justify-center text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-colors cursor-pointer shrink-0" title="Đóng">'
    r_close = '<button id="close-ai-hub-modal" type="button" class="w-9 h-9 rounded-full flex items-center justify-center text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-colors cursor-pointer shrink-0" title="Close" data-i18n-title="aiHub.close">'
    if s_close in content:
        content = content.replace(s_close, r_close)
        print("  Patched close-ai-hub-modal")
    else:
        print("  [WARN] close-ai-hub-modal not found")

    # Desktop desc
    s_desk = """              <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
                Dành cho máy tính đã cài <strong>Claude Desktop</strong> hoặc <strong>Cursor IDE</strong>. Tự động cấu hình MCP server và kết nối két chi tiêu on-chain.
              </p>"""
    r_desk = """              <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.desktopDesc">
                For computers with Claude Desktop or Cursor IDE installed. Automatically configures MCP server and binds to on-chain spending vault.
              </p>"""
    if s_desk in content:
        content = content.replace(s_desk, r_desk)
        print("  Patched aiHub.desktopDesc")
    else:
        print("  [WARN] aiHub.desktopDesc not found")

    # Desktop cmd label
    s_cmd_label = '<span>Mở Terminal / PowerShell và chạy:</span>'
    r_cmd_label = '<span data-i18n="aiHub.desktopCmdLabel">Run in Terminal / PowerShell / Command Prompt:</span>'
    if s_cmd_label in content:
        content = content.replace(s_cmd_label, r_cmd_label)
        print("  Patched aiHub.desktopCmdLabel")
    else:
        print("  [WARN] aiHub.desktopCmdLabel not found")

    # Online desc
    s_online = """              <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
                Dành cho người dùng chat trên web <strong>claude.ai</strong> trên trình duyệt (Chrome, Safari, Brave, Edge). Kết nối trực tiếp qua giao thức đám mây.
              </p>"""
    r_online = """              <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.onlineDesc">
                For users chatting on claude.ai in browser (Chrome, Safari, Brave, Edge). Connects directly via cloud protocol.
              </p>"""
    if s_online in content:
        content = content.replace(s_online, r_online)
        print("  Patched aiHub.onlineDesc")
    else:
        print("  [WARN] aiHub.onlineDesc not found")

    # Account sync
    s_sync = '<span id="account-sync-browser-text">Đồng bộ sang trình duyệt Chrome</span>'
    r_sync = '<span id="account-sync-browser-text" data-i18n="account.syncBrowser">Sync to Chrome Browser</span>'
    if s_sync in content:
        content = content.replace(s_sync, r_sync)
        print("  Patched account-sync-browser-text")
    else:
        print("  [WARN] account-sync-browser-text not found")

    # Guarantee breakdown
    s_breakdown = '<div class="text-[10px] text-neutral-400 font-sans">20% TGE + 80% Tuyến Tính 6T</div>'
    r_breakdown = '<div class="text-[10px] text-neutral-400 font-sans">${getVestingText(\'guaranteeVestingBreakdown\', lang)}</div>'
    if s_breakdown in content:
        content = content.replace(s_breakdown, r_breakdown)
        print("  Patched guaranteeVestingBreakdown markup")
    else:
        print("  [WARN] guaranteeVestingBreakdown markup not found")

    # 4. Patch JS Strings & Notifications
    # MetaMask toast
    s_mm = 'message: `+$${added.toFixed(2)} USDT • Ký xác thực: ${signature.slice(0, 6)}...`,'
    r_mm = 'message: `+$${added.toFixed(2)} USDT • ${getDashNotice(\'signedAuthPrefix\')} ${signature.slice(0, 6)}...`,'
    if s_mm in content:
        content = content.replace(s_mm, r_mm)
        print("  Patched MetaMask toast")
    else:
        print("  [WARN] MetaMask toast not found")

    # Biometric decrypt error
    s_bio = """          throw new Error(window.haichainI18n?.currentLang === 'vi'
            ? "Không thể giải mã Vault sinh trắc học hiện tại. Hệ thống từ chối tạo khóa mới để bảo vệ an toàn số dư đang có trong Vault của bạn. Vui lòng quét lại FaceID trên đúng thiết bị ban đầu."
            : "Could not decrypt existing biometric vault. The system refused to overwrite your key to protect existing vault funds. Please re-authenticate on the original device.");"""
    r_bio = "          throw new Error(getDashNotice('biometricDecryptError'));"
    if s_bio in content:
        content = content.replace(s_bio, r_bio)
        print("  Patched biometricDecryptError")
    else:
        print("  [WARN] biometricDecryptError not found")

    # Mobile wallet err
    s_mw = "message: err || 'Không thể kết nối ví',"
    r_mw = "message: err || getDashNotice('connectWalletFailed'),"
    if s_mw in content:
        content = content.replace(s_mw, r_mw)
        print("  Patched mobile wallet err")
    else:
        print("  [WARN] mobile wallet err not found")

    # Disconnect toast
    s_dc = """        showToast({
          title: window.haichainI18n?.currentLang === 'vi' ? 'Đã Ngắt Kết Nối' : 'Wallet Disconnected',
          message: window.haichainI18n?.currentLang === 'vi' ? 'Đã thoát phiên làm việc an toàn' : 'Session terminated successfully',
          icon: 'log-out'
        });"""
    r_dc = """        showToast({
          title: getDashNotice('walletDisconnectedTitle'),
          message: getDashNotice('sessionTerminatedMsg'),
          icon: 'log-out'
        });"""
    if s_dc in content:
        content = content.replace(s_dc, r_dc)
        print("  Patched disconnect toast")
    else:
        print("  [WARN] disconnect toast not found")

    # Custom wallet toast
    s_cw = "title: window.haichainI18n?.currentLang === 'vi' ? 'Đã Kết Nối Ví Custom' : 'Custom Wallet Connected',"
    r_cw = "title: getDashNotice('customWalletConnectedTitle'),"
    if s_cw in content:
        content = content.replace(s_cw, r_cw)
        print("  Patched custom wallet toast")
    else:
        print("  [WARN] custom wallet toast not found")

    # Copy buttons in AI Hub
    s_cp1 = 'if (copyDesktopInstallText) copyDesktopInstallText.textContent = "✓ Đã sao chép lệnh!";\n          showToast({ title: "Đã sao chép!", message: "Dán vào Terminal/PowerShell để cài đặt tự động", icon: "check" });'
    r_cp1 = "if (copyDesktopInstallText) copyDesktopInstallText.textContent = getDashNotice('cmdCopied');\n          showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('cmdCopyToastMsg'), icon: 'check' });"
    if s_cp1 in content:
        content = content.replace(s_cp1, r_cp1)
        print("  Patched copyDesktopInstallText copied")
    else:
        print("  [WARN] s_cp1 not found")

    s_cp2 = 'if (copyDesktopInstallText) copyDesktopInstallText.textContent = "Sao chép lệnh cài đặt 1-Click";'
    r_cp2 = "if (copyDesktopInstallText) copyDesktopInstallText.textContent = getDashNotice('cmdCopyBtn');"
    if s_cp2 in content:
        content = content.replace(s_cp2, r_cp2)
        print("  Patched copyDesktopInstallText reset")
    else:
        print("  [WARN] s_cp2 not found")

    s_cp3 = 'showToast({ title: "Lệnh cài đặt:", message: cmd, icon: "terminal" });'
    r_cp3 = "showToast({ title: getDashNotice('installCmdToastTitle'), message: cmd, icon: 'terminal' });"
    if s_cp3 in content:
        content = content.replace(s_cp3, r_cp3)
        print("  Patched copyDesktopInstallText fallback")
    else:
        print("  [WARN] s_cp3 not found")

    s_cp4 = 'if (copyOnlineMcpText) copyOnlineMcpText.textContent = "✓ Đã sao chép link!";\n          showToast({ title: "Đã sao chép!", message: "Dán vào Settings -> Connectors trên claude.ai", icon: "check" });'
    r_cp4 = "if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopied');\n          showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('linkCopyToastMsg'), icon: 'check' });"
    if s_cp4 in content:
        content = content.replace(s_cp4, r_cp4)
        print("  Patched copyOnlineMcpText copied")
    else:
        print("  [WARN] s_cp4 not found")

    s_cp5 = 'if (copyOnlineMcpText) copyOnlineMcpText.textContent = "Sao chép đường dẫn Remote MCP";'
    r_cp5 = "if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopyBtn');"
    if s_cp5 in content:
        content = content.replace(s_cp5, r_cp5)
        print("  Patched copyOnlineMcpText reset")
    else:
        print("  [WARN] s_cp5 not found")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

patch_i18n('i18n.js')
patch_i18n('app/i18n.js')
patch_dashboard('dashboard.html')
patch_dashboard('app/dashboard.html')

print("\nSUCCESS: All files patched successfully!")
