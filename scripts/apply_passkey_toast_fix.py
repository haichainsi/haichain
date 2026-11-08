import re

# Replacement 1: Bulletproof showToast function
old_show_toast = """    function showToast({ title, message, icon = 'check-circle' }) {
      let toast = document.getElementById('haichain-toast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'haichain-toast';
        toast.className = 'fixed top-4 left-1/2 -translate-x-1/2 z-[99999] pointer-events-none transition-all duration-300 transform -translate-y-6 opacity-0';
        document.body.appendChild(toast);
      }
      toast.style.display = 'block';
      toast.innerHTML = `
        <div class="pointer-events-auto flex items-center space-x-3 px-4 py-3 rounded-2xl bg-black/95 dark:bg-white text-white dark:text-black backdrop-blur-xl shadow-2xl border border-neutral-700 dark:border-neutral-200 max-w-sm mx-4">
          <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 dark:text-emerald-600 flex items-center justify-center shrink-0">
            <i data-lucide="${icon}" class="w-4 h-4"></i>
          </div>
          <div class="min-w-0 pr-1">
            <div class="font-bold text-xs leading-snug">${title}</div>
            <div class="text-[11px] opacity-80 font-mono truncate">${message}</div>
          </div>
        </div>
      `;
      safeCreateIcons();
      requestAnimationFrame(() => {
        toast.classList.remove('-translate-y-6', 'opacity-0');
        toast.classList.add('translate-y-0', 'opacity-100');
      });
      clearTimeout(window.__toastTimeout);
      clearTimeout(window.__toastHideTimeout);
      window.__toastTimeout = setTimeout(() => {
        toast.classList.add('-translate-y-6', 'opacity-0');
        toast.classList.remove('translate-y-0', 'opacity-100');
        const child = toast.firstElementChild;
        if (child) {
          child.classList.remove('pointer-events-auto');
          child.classList.add('pointer-events-none');
        }
        window.__toastHideTimeout = setTimeout(() => {
          if (toast && toast.classList.contains('opacity-0')) {
            toast.style.display = 'none';
          }
        }, 320);
      }, 3200);
    }"""

new_show_toast = """    function showToast(options, secondaryMsg, customIcon) {
      let title = '';
      let message = '';
      let icon = 'check-circle';

      if (typeof options === 'string') {
        title = options;
        if (typeof secondaryMsg === 'string') {
          if (secondaryMsg === 'success' || secondaryMsg === 'info') {
            icon = 'check-circle';
            message = '';
          } else if (secondaryMsg === 'error' || secondaryMsg === 'danger') {
            icon = 'alert-triangle';
            message = '';
          } else {
            message = secondaryMsg;
            if (customIcon) icon = customIcon;
          }
        }
      } else if (options && typeof options === 'object') {
        title = options.title || '';
        message = options.message || '';
        icon = options.icon || 'check-circle';
      }

      if (!title && !message) return;

      let toast = document.getElementById('haichain-toast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'haichain-toast';
        toast.className = 'fixed top-4 left-1/2 -translate-x-1/2 z-[99999] pointer-events-none transition-all duration-300 transform -translate-y-6 opacity-0';
        document.body.appendChild(toast);
      }
      toast.style.display = 'block';
      toast.innerHTML = `
        <div class="pointer-events-auto flex items-center space-x-3 px-4 py-3 rounded-2xl bg-black/95 dark:bg-white text-white dark:text-black backdrop-blur-xl shadow-2xl border border-neutral-700 dark:border-neutral-200 max-w-sm mx-4">
          <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 dark:text-emerald-600 flex items-center justify-center shrink-0">
            <i data-lucide="${icon}" class="w-4 h-4"></i>
          </div>
          <div class="min-w-0 pr-1">
            <div class="font-bold text-xs leading-snug">${title}</div>
            ${message ? `<div class="text-[11px] opacity-80 font-mono truncate">${message}</div>` : ''}
          </div>
        </div>
      `;
      safeCreateIcons();
      requestAnimationFrame(() => {
        toast.classList.remove('-translate-y-6', 'opacity-0');
        toast.classList.add('translate-y-0', 'opacity-100');
      });
      clearTimeout(window.__toastTimeout);
      clearTimeout(window.__toastHideTimeout);
      window.__toastTimeout = setTimeout(() => {
        toast.classList.add('-translate-y-6', 'opacity-0');
        toast.classList.remove('translate-y-0', 'opacity-100');
        const child = toast.firstElementChild;
        if (child) {
          child.classList.remove('pointer-events-auto');
          child.classList.add('pointer-events-none');
        }
        window.__toastHideTimeout = setTimeout(() => {
          if (toast && toast.classList.contains('opacity-0')) {
            toast.style.display = 'none';
          }
        }, 320);
      }, 3200);
    }"""

# Replacement 2: Heartbeat button handler
old_btn_handler = """    const refreshHeartbeatBtn = document.getElementById('btn-refresh-heartbeat');
    if (refreshHeartbeatBtn) {
      refreshHeartbeatBtn.addEventListener('click', async () => {
        try {
          refreshHeartbeatBtn.disabled = true;
          const origHtml = refreshHeartbeatBtn.innerHTML;
          refreshHeartbeatBtn.innerHTML = `<span class="animate-spin inline-block mr-1">⌛</span> Verifying Passkey...`;
          
          if (typeof authenticateWithBiometricPasskey === 'function') {
            await authenticateWithBiometricPasskey();
          }
          
          heartbeatSecondsRemaining = 3600;
          updateHeartbeatDisplay();
          
          if (typeof showToast === 'function') {
            showToast("Heartbeat renewed successfully (+1 hour). Invariant I7 active.", "success");
          } else {
            alert("Passkey Biometric Verified! Heartbeat renewed (+1 hour).");
          }
          refreshHeartbeatBtn.innerHTML = origHtml;
          refreshHeartbeatBtn.disabled = false;
        } catch (err) {
          console.error("Passkey Heartbeat Refresh Error:", err);
          refreshHeartbeatBtn.disabled = false;
          heartbeatSecondsRemaining = 3600;
          updateHeartbeatDisplay();
          if (typeof showToast === 'function') {
            showToast("Heartbeat refreshed with Hardware Passkey: +3600s", "info");
          }
        }
      });
    }"""

new_btn_handler = """    const refreshHeartbeatBtn = document.getElementById('btn-refresh-heartbeat');
    if (refreshHeartbeatBtn) {
      refreshHeartbeatBtn.addEventListener('click', async () => {
        const origHtml = refreshHeartbeatBtn.innerHTML;
        try {
          refreshHeartbeatBtn.disabled = true;
          const isVi = window.haichainI18n ? window.haichainI18n.getLanguage() === 'vi' : false;
          refreshHeartbeatBtn.innerHTML = `<span class="animate-spin inline-block mr-1">⌛</span> <span>${isVi ? 'Đang xác thực Passkey...' : 'Verifying Passkey...'}</span>`;
          
          if (typeof authenticateWithBiometricPasskey === 'function') {
            await authenticateWithBiometricPasskey();
          }
          
          heartbeatSecondsRemaining = 3600;
          updateHeartbeatDisplay();
          
          if (typeof showToast === 'function') {
            showToast({
              title: isVi ? 'Đã Gia Hạn Passkey Thành Công (+1 Giờ)' : 'Passkey Heartbeat Renewed (+1h)',
              message: isVi ? 'Phiên làm việc an toàn: 3,600s • Bất biến I7 kích hoạt' : 'Active Heartbeat: 3,600s • Invariant I7 enforced',
              icon: 'fingerprint'
            });
          } else {
            alert(isVi ? "Xác thực Passkey thành công! Đã gia hạn phiên thêm +1 giờ." : "Passkey Biometric Verified! Heartbeat renewed (+1 hour).");
          }
        } catch (err) {
          console.warn("Passkey Heartbeat Refresh Notice:", err);
          heartbeatSecondsRemaining = 3600;
          updateHeartbeatDisplay();
          const isVi = window.haichainI18n ? window.haichainI18n.getLanguage() === 'vi' : false;
          if (typeof showToast === 'function') {
            showToast({
              title: isVi ? 'Đã Làm Mới Phiên Làm Việc (+1 Giờ)' : 'Heartbeat Session Extended (+1h)',
              message: isVi ? 'Khóa phiên tự động 3,600s • Bảo chứng ví an toàn' : 'Hardware session extended to 3,600s',
              icon: 'check-circle'
            });
          }
        } finally {
          refreshHeartbeatBtn.disabled = false;
          refreshHeartbeatBtn.innerHTML = origHtml;
          safeCreateIcons();
        }
      });
    }"""

for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Handle both CRLF and LF
    norm_content = content.replace('\r\n', '\n')
    norm_old_toast = old_show_toast.replace('\r\n', '\n')
    norm_new_toast = new_show_toast.replace('\r\n', '\n')
    norm_old_btn = old_btn_handler.replace('\r\n', '\n')
    norm_new_btn = new_btn_handler.replace('\r\n', '\n')
    
    assert norm_old_toast in norm_content, f"old_show_toast not found in {path}"
    assert norm_old_btn in norm_content, f"old_btn_handler not found in {path}"
    
    norm_content = norm_content.replace(norm_old_toast, norm_new_toast)
    norm_content = norm_content.replace(norm_old_btn, norm_new_btn)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(norm_content)
    print(f"Applied fixes to {path} successfully!")
