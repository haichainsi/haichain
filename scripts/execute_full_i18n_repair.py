import re
import json

# 1. Dictionaries to inject
from i18n_patch_dictionaries import i18n_keys, vesting_breakdown, dash_new_keys

def patch_i18n_file(file_path):
    print(f"\n--- Patching {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    patched = content
    for lang, keys in i18n_keys.items():
        # Find block for lang: "<lang>": {
        pattern = rf'("{lang}":\s*\{{\s*\n)'
        m = re.search(pattern, patched)
        if m:
            injection = ""
            for k, val in keys.items():
                if f'"{k}"' not in patched:
                    val_escaped = val.replace('\\', '\\\\').replace('"', '\\"')
                    injection += f'    "{k}": "{val_escaped}",\n'
            if injection:
                patched = patched[:m.end()] + injection + patched[m.end():]
                print(f"  Added i18n keys for {lang}")
        else:
            print(f"  [WARN] Block for {lang} not found in {file_path}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(patched)
    print(f"Saved {file_path}")

def patch_dashboard_file(file_path):
    print(f"\n--- Patching {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update VESTING_VAULT_I18N
    for lang, val in vesting_breakdown.items():
        pattern = rf'(VESTING_VAULT_I18N\s*=\s*\{{[\s\S]*?["\']{lang}["\']:\s*\{{\s*\n)'
        m = re.search(pattern, content)
        if m:
            key_check = f'"guaranteeVestingBreakdown"'
            if key_check not in content:
                val_escaped = val.replace('\\', '\\\\').replace('"', '\\"')
                injection = f'    "guaranteeVestingBreakdown": "{val_escaped}",\n'
                content = content[:m.end()] + injection + content[m.end():]
                print(f"  Added guaranteeVestingBreakdown for {lang}")

    # 2. Update DASH_NOTICES_I18N
    for lang, keys in dash_new_keys.items():
        pattern = rf'(DASH_NOTICES_I18N\s*=\s*\{{[\s\S]*?["\']{lang}["\']:\s*\{{\s*\n)'
        m = re.search(pattern, content)
        if m:
            injection = ""
            for k, val in keys.items():
                if f'"{k}"' not in content:
                    val_escaped = val.replace('\\', '\\\\').replace('"', '\\"')
                    injection += f'    "{k}": "{val_escaped}",\n'
            if injection:
                content = content[:m.end()] + injection + content[m.end():]
                print(f"  Added DASH_NOTICES_I18N keys for {lang}")

    # 3. Patch HTML markup
    # Line 1439 close button
    content = re.sub(
        r'<button id="close-ai-hub-modal" type="button" class="([^"]*)" title="Đóng">',
        r'<button id="close-ai-hub-modal" type="button" class="\1" title="Close" data-i18n-title="aiHub.close">',
        content
    )

    # Line 1471 Desktop desc
    content = re.sub(
        r'<p class="text-\[11px\] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">\s*Dành cho máy tính đã cài <strong>Claude Desktop</strong> hoặc <strong>Cursor IDE</strong>\. Tự động cấu hình MCP server và kết nối két chi tiêu on-chain\.\s*</p>',
        r'<p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.desktopDesc">For computers with Claude Desktop or Cursor IDE installed. Automatically configures MCP server and binds to on-chain spending vault.</p>',
        content
    )

    # Line 1480 Terminal run
    content = re.sub(
        r'<span>Mở Terminal / PowerShell và chạy:</span>',
        r'<span data-i18n="aiHub.desktopCmdLabel">Run in Terminal / PowerShell / Command Prompt:</span>',
        content
    )

    # Line 1537 Online desc
    content = re.sub(
        r'<p class="text-\[11px\] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">\s*Dành cho người dùng chat trên web <strong>claude\.ai</strong> trên trình duyệt \(Chrome, Safari, Brave, Edge\)\. Kết nối trực tiếp qua giao thức đám mây\.\s*</p>',
        r'<p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.onlineDesc">For users chatting on claude.ai in browser (Chrome, Safari, Brave, Edge). Connects directly via cloud protocol.</p>',
        content
    )

    # Line 2072 Account sync
    content = re.sub(
        r'<span id="account-sync-browser-text">Đồng bộ sang trình duyệt Chrome</span>',
        r'<span id="account-sync-browser-text" data-i18n="account.syncBrowser">Sync to Chrome Browser</span>',
        content
    )

    # Line 5323 Guarantee breakdown in certificate
    content = re.sub(
        r'<div class="text-\[10px\] text-neutral-400 font-sans">20% TGE \+ 80% Tuyến Tính 6T</div>',
        r'<div class="text-[10px] text-neutral-400 font-sans">${getVestingText(\'guaranteeVestingBreakdown\', lang)}</div>',
        content
    )

    # 4. Patch JS Strings & Alerts
    # Line 5819 MetaMask toast message
    content = re.sub(
        r'message:\s*`\+\$\{added\.toFixed\(2\)\} USDT • Ký xác thực: \$\{signature\.slice\(0, 6\)\}\.\.\.`',
        r'message: `+${added.toFixed(2)} USDT • ${getDashNotice(\'signedAuthPrefix\')} ${signature.slice(0, 6)}...`',
        content
    )

    # Line 3272 Biometric decryption error
    content = re.sub(
        r'throw new Error\(window\.haichainI18n\?\.currentLang === [\'"]vi[\'"]\s*\?\s*"Không thể giải mã Vault sinh trắc học hiện tại[\s\S]*?original device\."\);',
        r'throw new Error(getDashNotice(\'biometricDecryptError\'));',
        content
    )

    # Line 3421 Mobile wallet callback error
    content = re.sub(
        r'message:\s*err\s*\|\|\s*[\'"]Không thể kết nối ví[\'"]',
        r'message: err || getDashNotice(\'connectWalletFailed\')',
        content
    )

    # Line 2972-2974 Disconnect toast
    content = re.sub(
        r'title:\s*window\.haichainI18n\?\.currentLang === [\'"]vi[\'"]\s*\?\s*[\'"]Đã Ngắt Kết Nối[\'"]\s*:\s*[\'"]Wallet Disconnected[\'"],\s*message:\s*window\.haichainI18n\?\.currentLang === [\'"]vi[\'"]\s*\?\s*[\'"]Đã thoát phiên làm việc an toàn[\'"]\s*:\s*[\'"]Session terminated successfully[\'"]',
        r'title: getDashNotice(\'walletDisconnectedTitle\'),\n          message: getDashNotice(\'sessionTerminatedMsg\')',
        content
    )

    # Line 3125 Custom wallet connect toast
    content = re.sub(
        r'title:\s*window\.haichainI18n\?\.currentLang === [\'"]vi[\'"]\s*\?\s*[\'"]Đã Kết Nối Ví Custom[\'"]\s*:\s*[\'"]Custom Wallet Connected[\'"]',
        r'title: getDashNotice(\'customWalletConnectedTitle\')',
        content
    )

    # Line 6205-6228 Copy button toasts
    old_copy_block = """        if (copyDesktopInstallText) copyDesktopInstallText.textContent = "✓ Đã sao chép lệnh!";
        showToast({ title: "Đã sao chép!", message: "Dán vào Terminal/PowerShell để cài đặt tự động", icon: "check" });
        setTimeout(() => {
          if (copyDesktopInstallText) copyDesktopInstallText.textContent = "Sao chép lệnh cài đặt 1-Click";
        }, 3000);
      } else {
        showToast({ title: "Lệnh cài đặt:", message: cmd, icon: "terminal" });
      }
    });
  }

  const copyOnlineMcpBtn = document.getElementById("copy-online-mcp-btn");
  const copyOnlineMcpText = document.getElementById("copy-online-mcp-text");
  if (copyOnlineMcpBtn) {
    copyOnlineMcpBtn.addEventListener("click", () => {
      const url = "https://mcp.haichain.si/sse";
      if (navigator.clipboard) {
        navigator.clipboard.writeText(url);
        if (copyOnlineMcpText) copyOnlineMcpText.textContent = "✓ Đã sao chép link!";
        showToast({ title: "Đã sao chép!", message: "Dán vào Settings -> Connectors trên claude.ai", icon: "check" });
        setTimeout(() => {
          if (copyOnlineMcpText) copyOnlineMcpText.textContent = "Sao chép đường dẫn Remote MCP";
        }, 3000);
      } else {
        showToast({ title: "Remote MCP URL:", message: url, icon: "link" });
      }
    });
  }

  // Web Direct Launch button -> Switch to Playground Tab
  const launchWebDirectBtn = document.getElementById("launch-web-direct-btn");
  if (launchWebDirectBtn) {
    launchWebDirectBtn.addEventListener("click", () => {
      if (aiHubModal) aiHubModal.classList.add("hidden");
      if (typeof window.switchTab === "function") {
        window.switchTab("tab-playground");
      }
      showToast({ title: "AI Playground", message: "Trải nghiệm suy luận AI trực tiếp qua Web3", icon: "zap" });
    });
  }"""

    new_copy_block = """        if (copyDesktopInstallText) copyDesktopInstallText.textContent = getDashNotice('cmdCopied');
        showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('cmdCopyToastMsg'), icon: "check" });
        setTimeout(() => {
          if (copyDesktopInstallText) copyDesktopInstallText.textContent = getDashNotice('cmdCopyBtn');
        }, 3000);
      } else {
        showToast({ title: getDashNotice('installCmdToastTitle'), message: cmd, icon: "terminal" });
      }
    });
  }

  const copyOnlineMcpBtn = document.getElementById("copy-online-mcp-btn");
  const copyOnlineMcpText = document.getElementById("copy-online-mcp-text");
  if (copyOnlineMcpBtn) {
    copyOnlineMcpBtn.addEventListener("click", () => {
      const url = "https://mcp.haichain.si/sse";
      if (navigator.clipboard) {
        navigator.clipboard.writeText(url);
        if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopied');
        showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('linkCopyToastMsg'), icon: "check" });
        setTimeout(() => {
          if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopyBtn');
        }, 3000);
      } else {
        showToast({ title: "Remote MCP URL:", message: url, icon: "link" });
      }
    });
  }

  // Web Direct Launch button -> Switch to Playground Tab
  const launchWebDirectBtn = document.getElementById("launch-web-direct-btn");
  if (launchWebDirectBtn) {
    launchWebDirectBtn.addEventListener("click", () => {
      if (aiHubModal) aiHubModal.classList.add("hidden");
      if (typeof window.switchTab === "function") {
        window.switchTab("tab-playground");
      }
      showToast({ title: "AI Playground", message: getDashNotice('aiPlaygroundToast'), icon: "zap" });
    });
  }"""

    # Normalize CRLF
    content_norm = content.replace('\r\n', '\n')
    old_copy_block_norm = old_copy_block.replace('\r\n', '\n')
    new_copy_block_norm = new_copy_block.replace('\r\n', '\n')
    if old_copy_block_norm in content_norm:
        content_norm = content_norm.replace(old_copy_block_norm, new_copy_block_norm)
        print("  Replaced copy toasts block successfully.")
    else:
        print("  [WARN] old_copy_block_norm not found in content!")

    content = content_norm

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

# Run updates
patch_i18n_file('i18n.js')
patch_i18n_file('app/i18n.js')
patch_dashboard_file('dashboard.html')
patch_dashboard_file('app/dashboard.html')

print("\nAll files patched successfully!")
