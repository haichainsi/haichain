import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = """            if (ctaEl) ctaEl.href = '/dashboard?tab=preseed&ref=' + encodeURIComponent(activeRef);
            banner.classList.remove('hidden');"""

replacement = """            if (ctaEl) {
              var targetHref = '/dashboard?tab=preseed&ref=' + encodeURIComponent(activeRef);
              if (utmSource) targetHref += '&utm_source=' + encodeURIComponent(utmSource);
              ctaEl.href = targetHref;
            }
            banner.classList.remove('hidden');"""

if target in html:
    html = html.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('app/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully patched index.html and app/index.html!")
else:
    print("Target not found in index.html!")
    sys.exit(1)
