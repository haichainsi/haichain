import re

# 1. Update index.html and app/index.html
for path in ['index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Enhance openMobileMenu and closeMobileMenu and expose to window
    target_menu_funcs = """    function openMobileMenu() {
      if (!mobileMenu) return;
      mobileMenu.classList.remove('menu-closed');
      mobileMenu.classList.add('menu-open');
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.add('hidden');
      if (cIcon) {
        cIcon.classList.remove('hidden');
        cIcon.classList.add('inline-flex');
      }
      if (mobileMenuBtn) {
        mobileMenuBtn.setAttribute('aria-expanded', 'true');
      }
    }

    function closeMobileMenu() {
      if (!mobileMenu) return;
      mobileMenu.classList.remove('menu-open');
      mobileMenu.classList.add('menu-closed');
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.remove('hidden');
      if (cIcon) {
        cIcon.classList.add('hidden');
        cIcon.classList.remove('inline-flex');
      }
      if (mobileMenuBtn) {
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
      }
    }

    function toggleMobileMenu(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      if (!mobileMenu) return;
      if (mobileMenu.classList.contains('menu-open')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    }"""

    replacement_menu_funcs = """    function openMobileMenu() {
      if (!mobileMenu) return;
      mobileMenu.classList.remove('menu-closed', 'hidden', 'opacity-0');
      mobileMenu.classList.add('menu-open');
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.add('hidden');
      if (cIcon) {
        cIcon.classList.remove('hidden');
        cIcon.classList.add('inline-flex');
      }
      if (mobileMenuBtn) {
        mobileMenuBtn.setAttribute('aria-expanded', 'true');
      }
    }

    function closeMobileMenu() {
      if (!mobileMenu) return;
      mobileMenu.classList.remove('menu-open', 'hidden', 'opacity-0', 'opacity-100');
      mobileMenu.classList.add('menu-closed');
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.remove('hidden');
      if (cIcon) {
        cIcon.classList.add('hidden');
        cIcon.classList.remove('inline-flex');
      }
      if (mobileMenuBtn) {
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
      }
    }

    function toggleMobileMenu(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      if (!mobileMenu) return;
      if (mobileMenu.classList.contains('menu-open')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    }

    // Expose globally so external modals can cleanly close & sync mobile menu
    window.openMobileMenu = openMobileMenu;
    window.closeMobileMenu = closeMobileMenu;
    window.toggleMobileMenu = toggleMobileMenu;"""

    if target_menu_funcs in content:
        content = content.replace(target_menu_funcs, replacement_menu_funcs)
    else:
        print(f"WARNING: target_menu_funcs not exact match in {path}")

    # Update mobile-nav-whitepaper-link onclick to use window.closeMobileMenu
    content = content.replace(
        "if (typeof closeMobileMenu === 'function') closeMobileMenu();",
        "if (typeof window.closeMobileMenu === 'function') { window.closeMobileMenu(); }"
    )
    content = content.replace(
        "if (typeof closeMobileMenu === \\'function\\') closeMobileMenu();",
        "if (typeof window.closeMobileMenu === \\'function\\') { window.closeMobileMenu(); }"
    )

    # Bump version
    content = content.replace('v17_inapp_modal_strict_interceptor', 'v18_inapp_modal_menu_sync')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

# 2. Update dashboard.html and app/dashboard.html
for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('v17_inapp_modal_strict_interceptor', 'v18_inapp_modal_menu_sync')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

# 3. Update pdf-modal.js and app/pdf-modal.js
for path in ['pdf-modal.js', 'app/pdf-modal.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update handleWhitepaperClick
    target_handle = """  // Universal In-App Whitepaper Click Handler (100% Prevents Opening in New Tab)
  function handleWhitepaperClick(e, trigger) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }

    // Close mobile nav menu if open
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    }
    const mobMenu = document.getElementById('mobile-menu');
    if (mobMenu) {
      mobMenu.classList.remove('menu-open', 'opacity-100');
      mobMenu.classList.add('hidden', 'opacity-0');
    }"""

    replacement_handle = """  // Universal In-App Whitepaper Click Handler (100% Prevents Opening in New Tab)
  function handleWhitepaperClick(e, trigger) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }

    // Properly close mobile nav menu and restore hamburger icon
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    } else {
      const mobMenu = document.getElementById('mobile-menu');
      if (mobMenu) {
        mobMenu.classList.remove('menu-open', 'hidden', 'opacity-0', 'opacity-100');
        mobMenu.classList.add('menu-closed');
      }
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.remove('hidden');
      if (cIcon) {
        cIcon.classList.add('hidden');
        cIcon.classList.remove('inline-flex');
      }
      const mobileMenuBtn = document.getElementById('mobile-menu-btn');
      if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }"""

    if target_handle in content:
        content = content.replace(target_handle, replacement_handle)
    else:
        print(f"WARNING: target_handle not exact match in {path}")

    # In closePdfViewerModal, also ensure mobile menu state is cleanly restored
    target_close = """  window.closePdfViewerModal = function () {
    const modal = document.getElementById('pdf-viewer-modal');
    if (modal) {
      modal.classList.add('hidden');
    }
    document.body.style.overflow = '';

    // Stop observer & cancel rendering"""

    replacement_close = """  window.closePdfViewerModal = function () {
    const modal = document.getElementById('pdf-viewer-modal');
    if (modal) {
      modal.classList.add('hidden');
    }
    document.body.style.overflow = '';

    // Guarantee mobile menu state is fully clean and responsive
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    } else {
      const mobMenu = document.getElementById('mobile-menu');
      if (mobMenu) {
        mobMenu.classList.remove('menu-open', 'hidden', 'opacity-0', 'opacity-100');
        mobMenu.classList.add('menu-closed');
      }
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.remove('hidden');
      if (cIcon) {
        cIcon.classList.add('hidden');
        cIcon.classList.remove('inline-flex');
      }
      const mobileMenuBtn = document.getElementById('mobile-menu-btn');
      if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }

    // Stop observer & cancel rendering"""

    if target_close in content:
        content = content.replace(target_close, replacement_close)
    else:
        print(f"WARNING: target_close not exact match in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")
