def patch_pdf_modal(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    target = """        // Save to localStorage
        try {
          const prev = JSON.parse(localStorage.getItem('HAICHAIN_SIGNED_SAFT_RECORDS') || '[]');
          prev.unshift(signedRecord);
          localStorage.setItem('HAICHAIN_SIGNED_SAFT_RECORDS', JSON.stringify(prev));
          localStorage.setItem('HAICHAIN_ACTIVE_SAFT', JSON.stringify(signedRecord));
        } catch (e) {
          console.warn('Could not save SAFT to storage:', e);
        }"""

    replacement = """        // Save to localStorage
        try {
          const prev = JSON.parse(localStorage.getItem('HAICHAIN_SIGNED_SAFT_RECORDS') || '[]');
          prev.unshift(signedRecord);
          localStorage.setItem('HAICHAIN_SIGNED_SAFT_RECORDS', JSON.stringify(prev));
          localStorage.setItem('HAICHAIN_ACTIVE_SAFT', JSON.stringify(signedRecord));
        } catch (e) {
          console.warn('Could not save SAFT to storage:', e);
        }

        // Asynchronously broadcast to Edge API (Telegram Bot + Google Sheets + Email Engine)
        try {
          fetch('/api/saft/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(signedRecord)
          }).catch(err => console.warn('Edge SAFT sync non-blocking error:', err));
        } catch (err) {
          console.warn('Edge SAFT dispatch error:', err);
        }"""

    if target in txt:
        txt = txt.replace(target, replacement, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(txt)
        print("Patched", path)
    else:
        print("Target not found in", path)

patch_pdf_modal('app/pdf-modal.js')
patch_pdf_modal('pdf-modal.js')
