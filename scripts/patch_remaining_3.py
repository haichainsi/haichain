def patch_remaining(file_path):
    print(f"Patching remaining in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # 1. Desktop desc
    s_desk = """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
            Dành cho máy tính đã cài <strong>Claude Desktop</strong> hoặc <strong>Cursor IDE</strong>. Tự động cấu hình MCP server và kết nối két chi tiêu on-chain.
          </p>"""
    r_desk = """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.desktopDesc">
            For computers with Claude Desktop or Cursor IDE installed. Automatically configures MCP server and binds to on-chain spending vault.
          </p>"""
    if s_desk in content:
        content = content.replace(s_desk, r_desk)
        print("  Patched desktop desc successfully")
    else:
        print("  ERROR: s_desk not found")

    # 2. Online desc
    s_online = """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
            Dành cho người dùng chat trên web <strong>claude.ai</strong> trên trình duyệt (Chrome, Safari, Brave, Edge). Kết nối trực tiếp qua giao thức đám mây.
          </p>"""
    r_online = """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.onlineDesc">
            For users chatting on claude.ai in browser (Chrome, Safari, Brave, Edge). Connects directly via cloud protocol.
          </p>"""
    if s_online in content:
        content = content.replace(s_online, r_online)
        print("  Patched online desc successfully")
    else:
        print("  ERROR: s_online not found")

    # 3. Disconnect toast
    s_dc = """      showToast({
        title: window.haichainI18n?.currentLang === 'vi' ? 'Đã Ngắt Kết Nối' : 'Wallet Disconnected',
        message: window.haichainI18n?.currentLang === 'vi' ? 'Đã thoát phiên làm việc an toàn' : 'Session terminated successfully',
        icon: 'log-out'
      });"""
    r_dc = """      showToast({
        title: getDashNotice('walletDisconnectedTitle'),
        message: getDashNotice('sessionTerminatedMsg'),
        icon: 'log-out'
      });"""
    if s_dc in content:
        content = content.replace(s_dc, r_dc)
        print("  Patched disconnect toast successfully")
    else:
        print("  ERROR: s_dc not found")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

patch_remaining('dashboard.html')
patch_remaining('app/dashboard.html')
