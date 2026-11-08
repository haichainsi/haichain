import re

for filepath in ['pdf-modal.js', 'app/pdf-modal.js']:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Add blocker element to innerHTML
    target_iframe = '<iframe id="pdf-modal-iframe" src="" class="w-full h-full flex-1 border-0" allow="fullscreen"></iframe>'
    replacement_iframe = '''<!-- Protective Corner Mask & Blocker: Completely hides and neutralizes any popout/new-tab button -->
          <div id="pdf-modal-popout-blocker" class="absolute top-0 right-0 w-[72px] h-[58px] z-20 pointer-events-auto bg-white dark:bg-[#0c0c0e] hidden" style="touch-action: none;"></div>
          <iframe id="pdf-modal-iframe" src="" class="w-full h-full flex-1 border-0" allow="fullscreen"></iframe>'''

    c = c.replace(target_iframe, replacement_iframe)

    # Attach event listeners in ensurePdfModal
    target_listeners = """    const iframe = modal.querySelector('#pdf-modal-iframe');
    const loader = modal.querySelector('#pdf-modal-loader');"""
    replacement_listeners = """    const blocker = modal.querySelector('#pdf-modal-popout-blocker');
    if (blocker) {
      blocker.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); });
      blocker.addEventListener('touchstart', (e) => { e.preventDefault(); e.stopPropagation(); }, { passive: false });
    }

    const iframe = modal.querySelector('#pdf-modal-iframe');
    const loader = modal.querySelector('#pdf-modal-loader');"""

    c = c.replace(target_listeners, replacement_listeners)

    # In openPdfViewerModal, toggle blocker visibility
    target_open = """      if (isAndroid) {
        // Android Chrome: Route via Google Docs Viewer for flawless CJK typography, touch scrolling, and zero crash
        const origin = window.location.origin || 'https://haichain.si';
        const absolutePdfUrl = cleanPath.startsWith('http') ? cleanPath : origin + cleanPath;
        iframe.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-forms');
        iframe.src = 'https://docs.google.com/viewer?embedded=true&url=' + encodeURIComponent(absolutePdfUrl);
      } else {
        // Desktop & iOS Safari: High-speed native vector rendering with hidden toolbars
        iframe.removeAttribute('sandbox');
        iframe.src = cleanPath + '#toolbar=0&navpanes=0&view=FitH';
      }"""

    replacement_open = """      const blocker = document.getElementById('pdf-modal-popout-blocker');
      if (isAndroid) {
        // Android Chrome: Route via Google Docs Viewer for flawless CJK typography, touch scrolling, and zero crash
        const origin = window.location.origin || 'https://haichain.si';
        const absolutePdfUrl = cleanPath.startsWith('http') ? cleanPath : origin + cleanPath;
        iframe.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-forms');
        if (blocker) blocker.classList.remove('hidden');
        iframe.src = 'https://docs.google.com/viewer?embedded=true&url=' + encodeURIComponent(absolutePdfUrl);
      } else {
        // Desktop & iOS Safari: High-speed native vector rendering with hidden toolbars
        iframe.removeAttribute('sandbox');
        if (blocker) blocker.classList.add('hidden');
        iframe.src = cleanPath + '#toolbar=0&navpanes=0&view=FitH';
      }"""

    c = c.replace(target_open, replacement_open)

    # In closePdfViewerModal, hide blocker
    target_close = """      const loader = document.getElementById('pdf-modal-loader');
      if (loader) {
        loader.classList.add('opacity-0', 'hidden');
      }"""
    replacement_close = """      const loader = document.getElementById('pdf-modal-loader');
      if (loader) {
        loader.classList.add('opacity-0', 'hidden');
      }
      const blocker = document.getElementById('pdf-modal-popout-blocker');
      if (blocker) {
        blocker.classList.add('hidden');
      }"""

    c = c.replace(target_close, replacement_close)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

print('Updated popout blocker in pdf-modal.js and app/pdf-modal.js')
