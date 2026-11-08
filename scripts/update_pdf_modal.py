# -*- coding: utf-8 -*-
with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove fallback iframe HTML
old_iframe = '<iframe id="pdf-modal-fallback-iframe" class="w-full h-full flex-1 border-0 hidden"></iframe>'
new_comment = '<!-- Pure Canvas Architecture: 100% In-App Canvas, Zero Iframe Fallbacks -->'
if old_iframe in text:
    text = text.replace(old_iframe, new_comment)
    print("Replaced old_iframe")

# 2. Replace catch block
old_catch = """    } catch (err) {
      console.error('Canvas PDF rendering error, switching to secure fallback:', err);
      // Fallback: load iframe if canvas engine encounters an unexpected network block
      if (loader) loader.classList.add('hidden');
      if (fallbackIframe) {
        fallbackIframe.classList.remove('hidden');
        fallbackIframe.src = pdfUrl.split('#')[0] + '#toolbar=0&navpanes=0&view=FitH';
      }
    }"""

new_catch = """    } catch (err) {
      console.error('Canvas PDF rendering error:', err);
      if (loader) {
        loader.classList.remove('opacity-0', 'hidden');
        loader.innerHTML = `
          <div class="text-center p-6 max-w-xs">
            <p class="text-sm font-medium text-neutral-800 dark:text-neutral-200 mb-3">Không thể tải tài liệu / Failed to load document</p>
            <button type="button" onclick="window.openPdfViewerModal('${pdfUrl}')" class="px-4 py-2 rounded-xl bg-black dark:bg-white text-white dark:text-black text-xs font-mono font-bold cursor-pointer active:scale-95 shadow-md">
              Thử lại / Retry
            </button>
          </div>
        `;
      }
    }"""

if old_catch in text:
    text = text.replace(old_catch, new_catch)
    print("Replaced old_catch")

# 3. Ensure scroll is at top after Page 1 render
old_page1 = """      // Fast-render Page 1 immediately (<80ms)
      await renderPageSlot(1);

      // Dismiss loader immediately after Page 1 is ready (<100ms)"""

new_page1 = """      // Fast-render Page 1 immediately (<80ms)
      await renderPageSlot(1);
      if (scrollContainer) scrollContainer.scrollTop = 0;

      // Dismiss loader immediately after Page 1 is ready (<100ms)"""

if old_page1 in text:
    text = text.replace(old_page1, new_page1)
    print("Replaced old_page1")

with open('pdf-modal.js', 'w', encoding='utf-8') as f:
    f.write(text)

with open('app/pdf-modal.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Both pdf-modal.js and app/pdf-modal.js updated!")
