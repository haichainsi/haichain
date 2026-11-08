def add_sheet_webhook_support(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    target = """        // 2. Asynchronously broadcast to Edge API & Webhook (Google Sheets + Email)
        try {
          fetch('/api/saft/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(signedRecord)
          }).catch(err => console.warn('Edge SAFT sync non-blocking error:', err));
        } catch (err) {
          console.warn('Edge SAFT dispatch error:', err);
        }"""

    replacement = """        // 2. Asynchronously broadcast to Edge API & Webhook (Google Sheets + Email)
        try {
          fetch('/api/saft/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(signedRecord)
          }).catch(err => console.warn('Edge SAFT sync non-blocking error:', err));
        } catch (err) {
          console.warn('Edge SAFT dispatch error:', err);
        }

        // 3. Direct Google Apps Script Webhook Dispatch (Google Sheets + Dual Email)
        try {
          const sheetWebhook = window.HAICHAIN_GOOGLE_SHEETS_WEBHOOK_URL || '';
          if (sheetWebhook) {
            fetch(sheetWebhook, {
              method: 'POST',
              mode: 'no-cors',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(signedRecord)
            }).catch(e => console.warn('Google Sheets Webhook non-blocking:', e));
          }
        } catch (_) {}"""

    if target in txt:
        txt = txt.replace(target, replacement, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(txt)
        print("Updated webhook in", path)
    else:
        print("Target not found in", path)

add_sheet_webhook_support('app/pdf-modal.js')
add_sheet_webhook_support('pdf-modal.js')
