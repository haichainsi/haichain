def patch_switch_tab(filepath):
    print(f"Adding switch tab and lang listener in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    old_target = """      } else if (tabName === 'online') {
        if (hubTabDesktop) hubTabDesktop.className = inactiveTabClass;
        if (hubTabOnline) hubTabOnline.className = activeTabClass;
        if (hubTabWeb) hubTabWeb.className = inactiveTabClass;
        if (hubSectionDesktop) hubSectionDesktop.classList.add('hidden');
        if (hubSectionOnline) hubSectionOnline.classList.remove('hidden');
        if (hubSectionWeb) hubSectionWeb.classList.add('hidden');"""

    new_target = """      } else if (tabName === 'online') {
        if (hubTabDesktop) hubTabDesktop.className = inactiveTabClass;
        if (hubTabOnline) hubTabOnline.className = activeTabClass;
        if (hubTabWeb) hubTabWeb.className = inactiveTabClass;
        if (hubSectionDesktop) hubSectionDesktop.classList.add('hidden');
        if (hubSectionOnline) hubSectionOnline.classList.remove('hidden');
        if (hubSectionWeb) hubSectionWeb.classList.add('hidden');
        if (typeof updateAiHubUrls === 'function') updateAiHubUrls();"""

    if old_target in html:
        html = html.replace(old_target, new_target)
        print("Patched switchAiHubTab successfully.")
    else:
        print("WARNING: old_target not found in switchAiHubTab!")

    # Add language change listener and initial call
    old_init = "window.updateAiHubUrls = updateAiHubUrls;"
    new_init = """window.updateAiHubUrls = updateAiHubUrls;
    window.addEventListener('haichain:languageChanged', () => {
      if (typeof updateAiHubUrls === 'function') updateAiHubUrls();
    });
    // Initial sync
    setTimeout(() => { if (typeof updateAiHubUrls === 'function') updateAiHubUrls(); }, 150);"""

    if old_init in html:
        html = html.replace(old_init, new_init)
        print("Added lang listener and initial sync.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Done {filepath}.")

patch_switch_tab('dashboard.html')
patch_switch_tab('app/dashboard.html')
