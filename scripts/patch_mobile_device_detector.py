import re

print("Starting desktop web3 auto-connect fix...")

# 1. Update isMobileDevice in dashboard.html, app/dashboard.html, index.html, app/index.html
old_mobile_fn = '''    function isMobileDevice() {
      const ua = navigator.userAgent || '';
      const isTouch = (navigator.maxTouchPoints && navigator.maxTouchPoints > 0) || ('ontouchstart' in window);
      const isMobileUA = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile/i.test(ua);
      const isTablet = /(iPad|Tablet|(Android(?!.*Mobile))|(Silk(?!.*Mobile)))/i.test(ua);
      const isMacTouch = /Macintosh/i.test(ua) && isTouch; // iPadOS 13+ desktop agent
      const isNarrow = window.innerWidth <= 1024;
      return isMobileUA || isTablet || isMacTouch || (isTouch && isNarrow);
    }'''

new_mobile_fn = '''    function isMobileDevice() {
      const ua = navigator.userAgent || '';
      // Windows, Mac, and Linux desktop PCs (including Surface, touchscreen laptops) must NEVER be treated as mobile app platforms!
      if (/Windows NT|Macintosh|Linux/i.test(ua) && !/Android/i.test(ua)) {
        return false;
      }
      const isTouch = (navigator.maxTouchPoints && navigator.maxTouchPoints > 0) || ('ontouchstart' in window);
      const isMobileUA = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile/i.test(ua);
      const isTablet = /(iPad|Tablet|(Android(?!.*Mobile))|(Silk(?!.*Mobile)))/i.test(ua);
      const isMacTouch = /Macintosh/i.test(ua) && isTouch && !window.MSStream; // iPadOS 13+
      return isMobileUA || isTablet || isMacTouch;
    }'''

for html_file in ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html']:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize CRLF/LF
    content_norm = content.replace('\r\n', '\n')
    old_fn_norm = old_mobile_fn.replace('\r\n', '\n')
    new_fn_norm = new_mobile_fn.replace('\r\n', '\n')

    # Also handle index.html slight indentation differences if any
    if old_fn_norm in content_norm:
        content_norm = content_norm.replace(old_fn_norm, new_fn_norm)
        print(f"Updated isMobileDevice in {html_file}")
    else:
        # Regex replace for isMobileDevice
        pattern = r'function isMobileDevice\(\)\s*\{[\s\S]*?return isMobileUA \|\| isTablet \|\| isMacTouch \|\| \(isTouch && isNarrow\);[\s\S]*?\}'
        if re.search(pattern, content_norm):
            content_norm = re.sub(pattern, new_fn_norm.strip(), content_norm, count=1)
            print(f"Regex updated isMobileDevice in {html_file}")
        else:
            print(f"WARNING: isMobileDevice pattern not matched in {html_file}")

    if '\r\n' in content:
        content = content_norm.replace('\n', '\r\n')
    else:
        content = content_norm

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating isMobileDevice.")
