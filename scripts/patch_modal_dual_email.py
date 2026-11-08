def update_modal_resend(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    target = """          fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer ' + resendKey,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              from: 'HAICHAIN SAFT <onboarding@resend.dev>',
              to: ['haichain.si@gmail.com'],
              subject: emailSubject,
              html: emailBodyHtml
            })
          }).catch(e => console.warn('Resend direct non-blocking:', e));"""

    replacement = """          // (A) Send to Admin
          fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer ' + resendKey,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              from: 'HAICHAIN Official <no-reply@mail.haichain.si>',
              to: ['haichain.si@gmail.com'],
              subject: emailSubject,
              html: emailBodyHtml
            })
          }).catch(e => console.warn('Resend direct admin non-blocking:', e));

          // (B) Send to Investor (Confirmation & Receipt)
          if (email && email.includes('@')) {
            const investorSubject = 'HAICHAIN Official SAFT Agreement - Signed Confirmation (' + contractId + ')';
            const investorHtml = '<div style="font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;max-width:600px;margin:0 auto;padding:24px;background:#0c0c0e;color:#fff;border-radius:16px;border:1px solid #27272a;">' +
              '<h2 style="color:#ffffff;margin-top:0;border-bottom:1px solid #27272a;padding-bottom:12px;">HAICHAIN PRE-SEED SAFT EXECUTION CONFIRMATION</h2>' +
              '<p style="color:#e4e4e7;line-height:1.6;">Dear <strong>' + name + '</strong>,</p>' +
              '<p style="color:#d4d4d8;line-height:1.6;">Thank you for participating in the <strong>HAICHAIN Pre-Seed Strategic Round</strong>. Your Simple Agreement for Future Tokens (SAFT) has been cryptographically signed and officially recorded pursuant to the US ESIGN Act &amp; UETA standards.</p>' +
              '<div style="background:#18181b;border:1px solid #27272a;border-radius:12px;padding:16px;margin:20px 0;">' +
                '<table style="width:100%;border-collapse:collapse;color:#d4d4d8;font-size:13px;line-height:1.6;">' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;width:40%;">Contract ID:</td><td style="font-weight:bold;color:#fff;font-family:monospace;">' + contractId + '</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">Signatory Entity:</td><td style="font-weight:bold;color:#fff;">' + name + '</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">Subscription Investment:</td><td style="color:#4ade80;font-weight:bold;">$' + amount.toLocaleString('en-US') + ' USD (USDT)</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">Token Entitlement:</td><td style="font-weight:bold;color:#fff;">' + tokens.toLocaleString('en-US') + ' $HAISI (@ $0.007)</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">Projected TGE Value:</td><td style="color:#a1a1aa;">$' + Math.round(tokens * 0.01).toLocaleString('en-US') + ' USD (+42.8%)</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">Beneficiary Solana Wallet:</td><td style="font-family:monospace;font-size:11px;color:#fff;word-break:break-all;">' + wallet + '</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">Multi-Sig Treasury Vault:</td><td style="font-family:monospace;font-size:11px;color:#a1a1aa;word-break:break-all;">' + treasury + '</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">SHA-256 Audit Proof:</td><td style="font-family:monospace;font-size:10px;color:#71717a;word-break:break-all;">' + hashHex + '</td></tr>' +
                  '<tr><td style="padding:6px 0;color:#a1a1aa;">Timestamp (UTC):</td><td>' + timestamp + '</td></tr>' +
                '</table>' +
              '</div>' +
              '<p style="color:#a1a1aa;font-size:13px;line-height:1.6;">Your investment funds are secured in the Squads Multi-Sig Treasury on Solana Mainnet, and your $HAISI tokens will be minted and transferred directly to your beneficiary wallet at Token Generation Event (TGE).</p>' +
              '<div style="margin-top:24px;padding-top:16px;border-top:1px solid #27272a;text-align:center;">' +
                '<a href="https://haichain.si/dashboard" style="display:inline-block;background:#fff;color:#000;font-weight:bold;font-size:13px;padding:10px 24px;border-radius:9999px;text-decoration:none;">Access HAICHAIN Dashboard</a>' +
              '</div>' +
              '</div>';

            fetch('https://api.resend.com/emails', {
              method: 'POST',
              headers: {
                'Authorization': 'Bearer ' + resendKey,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                from: 'HAICHAIN Official <no-reply@mail.haichain.si>',
                to: [email],
                subject: investorSubject,
                html: investorHtml
              })
            }).catch(e => console.warn('Resend direct investor non-blocking:', e));
          }"""

    if target in txt:
        txt = txt.replace(target, replacement, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(txt)
        print("Updated modal resend in", path)
    else:
        print("Target not found in", path)

update_modal_resend('app/pdf-modal.js')
update_modal_resend('pdf-modal.js')
