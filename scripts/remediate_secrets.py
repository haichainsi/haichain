import os
import re

def clean_secrets():
    # 1. _worker.js and app/_worker.js
    for fpath in ['_worker.js', 'app/_worker.js']:
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Replace global constants
            content = re.sub(
                r"const RESEND_API_KEY = ['\"][^'\"]+['\"];\r?\n",
                "",
                content
            )
            content = re.sub(
                r"const TELEGRAM_BOT_TOKEN = ['\"][^'\"]+['\"];\r?\n",
                "",
                content
            )
            content = re.sub(
                r"const resendKey = \(env && env\.RESEND_API_KEY\) \|\| RESEND_API_KEY;",
                "const resendKey = (env && env.RESEND_API_KEY) || (typeof process !== 'undefined' && process.env && process.env.RESEND_API_KEY) || '';",
                content
            )
            # Update telegram dispatch to use env
            old_tg = "const tgRes = await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,"
            new_tg = "const tgToken = (env && env.TELEGRAM_BOT_TOKEN) || (typeof process !== 'undefined' && process.env && process.env.TELEGRAM_BOT_TOKEN) || '';\n      if (!tgToken) { console.log('[Telegram Bot]: TELEGRAM_BOT_TOKEN not configured in env, skipping notification.'); return; }\n      const tgRes = await fetch(`https://api.telegram.org/bot${tgToken}/sendMessage`,"
            content = content.replace(old_tg, new_tg)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Patched {fpath}")

    # 2. server/cloud-mcp-functions/api/saft-submit.js
    fpath = 'server/cloud-mcp-functions/api/saft-submit.js'
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r"const RESEND_API_KEY = ['\"][^'\"]+['\"];\r?\n", "", content)
        content = re.sub(r"const TELEGRAM_BOT_TOKEN = ['\"][^'\"]+['\"];\r?\n", "", content)
        content = re.sub(
            r"const resendKey = \(env && env\.RESEND_API_KEY\) \|\| RESEND_API_KEY;",
            "const resendKey = (env && env.RESEND_API_KEY) || (typeof process !== 'undefined' && process.env && process.env.RESEND_API_KEY) || '';",
            content
        )
        old_tg = "const tgRes = await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,"
        new_tg = "const tgToken = (env && env.TELEGRAM_BOT_TOKEN) || (typeof process !== 'undefined' && process.env && process.env.TELEGRAM_BOT_TOKEN) || '';\n      if (!tgToken) { console.log('[Telegram Bot]: TELEGRAM_BOT_TOKEN not configured in env, skipping.'); return; }\n      const tgRes = await fetch(`https://api.telegram.org/bot${tgToken}/sendMessage`,"
        content = content.replace(old_tg, new_tg)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Patched {fpath}")

    # 3. server/haichain-mcp-worker.js
    fpath = 'server/haichain-mcp-worker.js'
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r"const RESEND_API_KEY = ['\"][^'\"]+['\"];\r?\n", "", content)
        content = re.sub(r"const TELEGRAM_BOT_TOKEN = ['\"][^'\"]+['\"];\r?\n", "", content)
        content = re.sub(
            r"const resendKey = \(env && env\.RESEND_API_KEY\) \|\| RESEND_API_KEY;",
            "const resendKey = (env && env.RESEND_API_KEY) || (typeof process !== 'undefined' && process.env && process.env.RESEND_API_KEY) || '';",
            content
        )
        old_tg = "const tgRes = await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,"
        new_tg = "const tgToken = (env && env.TELEGRAM_BOT_TOKEN) || (typeof process !== 'undefined' && process.env && process.env.TELEGRAM_BOT_TOKEN) || '';\n      if (!tgToken) { console.log('[Telegram Bot]: TELEGRAM_BOT_TOKEN not configured in env, skipping.'); return; }\n      const tgRes = await fetch(`https://api.telegram.org/bot${tgToken}/sendMessage`,"
        content = content.replace(old_tg, new_tg)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Patched {fpath}")

    # 4. server/production-agent-relayer.js
    fpath = 'server/production-agent-relayer.js'
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(
            r"const RESEND_API_KEY = ['\"][^'\"]+['\"];",
            "const RESEND_API_KEY = process.env.RESEND_API_KEY || '';",
            content
        )
        content = re.sub(
            r"const tgToken = ['\"]9066296959:[^'\"]+['\"];",
            "const tgToken = process.env.TELEGRAM_BOT_TOKEN || '';\n            if (!tgToken) { console.log('[Relayer Telegram]: No TELEGRAM_BOT_TOKEN, skipping.'); } else {",
            content
        )
        # Ensure we close the bracket or handle the Telegram block cleanly
        old_tg_end = "telegramSent = true;\n            } catch (tgErr) {"
        new_tg_end = "telegramSent = true;\n            }\n            } catch (tgErr) {"
        content = content.replace(old_tg_end, new_tg_end)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Patched {fpath}")

    # 5. pdf-modal.js and app/pdf-modal.js: remove client-side direct telegram fetch
    for fpath in ['pdf-modal.js', 'app/pdf-modal.js']:
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Find the client-side direct telegram block
            tg_pattern = re.compile(
                r"// 1\. Instant Real-Time Telegram Bot Notification.*?"
                r"fetch\('https://api\.telegram\.org/bot'\s*\+\s*tgToken\s*\+\s*'/sendMessage'.*?\n\s*\}\)\.catch\(.*?\);\n\s*\} catch \(_\) \{\}",
                re.DOTALL
            )
            new_content = tg_pattern.sub(
                "// 1. Telegram notification dispatched securely via backend worker /api/saft/submit (no client-side tokens)",
                content
            )
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] Patched {fpath}")

    # 6. scripts/*.py
    for fname in ['apply_luxury_email_and_sig_fix.py', 'patch_pdf_modal.py', 'test_luxury_email_template.py']:
        fpath = os.path.join('scripts', fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('re_Hqp1tNKV_6w8Ur4v3B91Jv6yusD4CK5pN', "os.environ.get('RESEND_API_KEY', '')")
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Patched {fpath}")

if __name__ == '__main__':
    clean_secrets()
