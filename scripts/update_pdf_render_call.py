for p in ['pdf-modal.js', 'app/pdf-modal.js']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    target = 'successView.classList.remove(\'hidden\');'
    replacement = '''successView.classList.remove('hidden');
        try {
          if (typeof window.renderVestingVaultPage === 'function') {
            window.renderVestingVaultPage();
          }
        } catch (_) {}'''

    if target in c:
        c = c.replace(target, replacement, 1)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {p}")
    else:
        print(f"Target not found in {p}")
