import os
import re

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the Document Icon container (was bg-black dark:bg-white text-white dark:text-black with <i data-lucide="file-text">)
    old_doc_icon = re.compile(
        r'<div class="w-6 h-6 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">\s*<i data-lucide="file-text" class="w-3\.5 h-3\.5 sm:w-4 sm:h-4"></i>\s*</div>',
        re.DOTALL
    )
    new_doc_icon = '''<div class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl bg-neutral-200 dark:bg-neutral-800 border border-neutral-300 dark:border-neutral-700 text-neutral-800 dark:text-neutral-200 flex items-center justify-center shrink-0 shadow-xs">
              <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>'''
    content, count_doc = old_doc_icon.subn(new_doc_icon, content)

    # 2. Replace Zoom Out icon
    old_zoom_out = re.compile(
        r'(<button id="pdf-modal-zoom-out"[^>]*>)\s*<i data-lucide="zoom-out" class="w-3\.5 h-3\.5 sm:w-4 sm:h-4"></i>\s*(</button>)',
        re.DOTALL
    )
    new_zoom_out = r'\1<svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>\2'
    content, count_zo = old_zoom_out.subn(new_zoom_out, content)

    # 3. Replace Zoom In icon
    old_zoom_in = re.compile(
        r'(<button id="pdf-modal-zoom-in"[^>]*>)\s*<i data-lucide="zoom-in" class="w-3\.5 h-3\.5 sm:w-4 sm:h-4"></i>\s*(</button>)',
        re.DOTALL
    )
    new_zoom_in = r'\1<svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>\2'
    content, count_zi = old_zoom_in.subn(new_zoom_in, content)

    # 4. Replace Close icon
    old_close = re.compile(
        r'(<button id="pdf-modal-close-btn"[^>]*>)\s*<i data-lucide="x" class="w-4 h-4 sm:w-4\.5 sm:h-4\.5"></i>\s*(</button>)',
        re.DOTALL
    )
    new_close = r'\1<svg class="w-4 h-4 sm:w-4.5 sm:h-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>\2'
    content, count_cl = old_close.subn(new_close, content)

    # 5. Replace Drawer Close button icon (ensure crisp SVG cross)
    old_drawer_close = re.compile(
        r'<button id="saft-drawer-close-btn"[^>]*>.*?</button>',
        re.DOTALL
    )
    new_drawer_close = '''<button id="saft-drawer-close-btn" type="button" class="w-8 h-8 rounded-xl flex items-center justify-center text-neutral-400 hover:text-white hover:bg-neutral-800 transition-colors cursor-pointer" title="Close" style="color: #d4d4d8 !important;">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>'''
    content, count_dcl = old_drawer_close.subn(new_drawer_close, content)

    # 6. Replace Chevrons in floating bottom pill
    old_prev = re.compile(
        r'(<button id="pdf-modal-prev-page"[^>]*>)\s*<i data-lucide="chevron-up" class="w-3\.5 h-3\.5 sm:w-4 sm:h-4"></i>\s*(</button>)',
        re.DOTALL
    )
    new_prev = r'\1<svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>\2'
    content, count_prev = old_prev.subn(new_prev, content)

    old_next = re.compile(
        r'(<button id="pdf-modal-next-page"[^>]*>)\s*<i data-lucide="chevron-down" class="w-3\.5 h-3\.5 sm:w-4 sm:h-4"></i>\s*(</button>)',
        re.DOTALL
    )
    new_next = r'\1<svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>\2'
    content, count_next = old_next.subn(new_next, content)

    # 7. Upgrade subtitle contrast in drawer
    content = content.replace('style="color: #a1a1aa !important;">Online legal verification', 'style="color: #d4d4d8 !important;">Online legal verification')
    content = content.replace('style="color: #a1a1aa !important;">Ticket limit:', 'style="color: #d4d4d8 !important;">Ticket limit:')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filepath}: doc_icon={count_doc}, zoom_out={count_zo}, zoom_in={count_zi}, close={count_cl}, drawer_close={count_dcl}, prev={count_prev}, next={count_next}")

update_file('app/pdf-modal.js')
update_file('pdf-modal.js')

# Update dashboard.html & app/dashboard.html cachebusters
for html_path in ['dashboard.html', 'app/dashboard.html']:
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'pdf-modal\.js\?v=v3[0-9]_[^"]+', 'pdf-modal.js?v=v36_svg_icons_1793638000000', html)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated cachebuster in {html_path}")
